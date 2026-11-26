<!--
name: 'Data: artifact-layout.mjs'
description: >-
  design-sync artifact-road script artifact-layout.mjs, rewriting a finished
  ds-bundle/ as Design System artifact files; extracted with the skill for the
  model to run and read.
ccVersion: 2.1.332
-->
#!/usr/bin/env node
// Rewrites a finished ds-bundle/ as the files of a Design System artifact on
// claude.ai, which shows only what sits at fixed paths under project/.
// Writes ds-bundle/.artifact/project/ (the files to publish) and
// ds-bundle/.artifact/layout.json (what was written). Nothing else in
// ds-bundle/ is touched. The same input gives the same bytes, so a later run
// can find what changed by comparing hashes: no clock, no machine path.

import { createHash } from 'node:crypto';
import { lstatSync, mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { layoutCard } from './lib/layout-cards.mjs';
import { inMib, joinStylesheets, quoted, Refusal } from './lib/layout-css.mjs';
import { contentTypeOf, isSection, LIMITS, preflight } from './lib/layout-preflight.mjs';
import { joinTypes, layoutReadme, layoutUsageNote, PAGE_REACT } from './lib/layout-readme.mjs';
import { tokensCss, tokensFromCss } from './lib/layout-tokens.mjs';
import { BuildFolder } from './lib/layout-tree.mjs';

const USAGE = 'usage: node artifact-layout.mjs <ds-bundle> [--title "<name>"]\\n' +
  'Exit codes: 0, layout written; 1, refused, one line per reason; 2, wrong arguments. Every run first deletes <ds-bundle>/.artifact/, whoever wrote it, and only exit 0 leaves a new one.';
const IDENT = /^(?!(?:__proto__|constructor|prototype)$)[A-Za-z_$][A-Za-z0-9_$]{0,63}$/;
// components/Cover/ is the artifact's cover page; lib/ and src/ hold its libraries and sources.
const RESERVED = /^(?:cover|lib|src)$/i;
// Written by the build for its own use. Never published, so not worth listing.
const BOOKKEEPING = /^(?:_ds_sync\\.json|_ds_needs_recompile|_vendor\\/react-dom\\.js|components\\/[^/]+\\/([^/]+)\\/\\1\\.jsx)$/;
const MAX_SAID = 10; // lines printed for one kind of message, and entries printed of one list

const errors = [];
const warnings = [];

function readBundle(tree) {
  if (!tree.has('_ds_bundle.js')) throw new Refusal('[NO_BUNDLE] the folder has no readable _ds_bundle.js.');
  const text = tree.text('_ds_bundle.js');
  const firstLine = text.slice(0, Math.max(0, text.indexOf('\\n')));
  let header = null;
  try { header = JSON.parse(/^\\/\\* @ds-bundle: (.*) \\*\\/$/.exec(firstLine)[1]); } catch { /* refused below */ }
  if (typeof header?.namespace !== 'string' || !IDENT.test(header.namespace) || !Array.isArray(header.components ?? [])) {
    throw new Refusal('[BUNDLE_HEADER] _ds_bundle.js does not start with a readable @ds-bundle header.');
  }
  return { namespace: header.namespace, listed: (header.components ?? []).map((c) => c?.name), body: text.slice(firstLine.length + 1) };
}

// Each component's name and its folder in ds-bundle/. The artifact has one folder
// per component and no group folders, so a name must be unique.
function findComponents(tree) {
  const found = new Map();
  for (const p of tree.paths) {
    const m = /^components\\/([^/]+)\\/([^/]+)\\/([^/]+)\\.html$/.exec(p);
    if (!m || m[2] !== m[3]) continue;
    const [, group, name] = m;
    if (found.has(name)) errors.push('[COMPONENT_TWICE] ' + quoted(name) + ' is in two groups (' + quoted(found.get(name)) + ' and ' + quoted('components/' + group + '/' + name) + '), and an artifact has one folder per component name.');
    else if (!IDENT.test(name)) errors.push('[COMPONENT_NAME] ' + quoted(name) + ' cannot name a component\\'s folder in an artifact. The name must be an ASCII identifier (letters, digits, _ and $, not starting with a digit) of at most 64 characters, and not constructor, prototype or __proto__.');
    else if (RESERVED.test(name)) errors.push('[COMPONENT_RESERVED] a component is called ' + quoted(name) + ', and an artifact keeps components/' + name + '/ for a use of its own.');
    else found.set(name, 'components/' + group + '/' + name);
  }
  return found;
}

// One line per different message, and at most MAX_SAID of a kind: a stylesheet
// with a thousand dead url()s is one problem, not a thousand.
function brief(lines) {
  const out = [];
  const count = new Map();
  for (const line of new Set(lines)) {
    const tag = line.slice(0, line.indexOf(']') + 1);
    count.set(tag, (count.get(tag) ?? 0) + 1);
    if (count.get(tag) <= MAX_SAID) out.push(line);
  }
  for (const [tag, n] of count) if (n > MAX_SAID) out.push(tag + ' and ' + (n - MAX_SAID) + ' more of this kind');
  return out;
}

// made.out: path under project/ to its bytes. made.from: that path to its file of ds-bundle/. made.consumed: files of ds-bundle/
// published, whole or inside another file. A path goes in NFC: the built-in tool stores no other form.
function put(made, path, content, from) {
  path = path.normalize('NFC');
  const bytes = Buffer.isBuffer(content) ? content : Buffer.from(content, 'utf8');
  // Stopped at once: the pre-flight would refuse it too, but only after everything had been read into memory.
  made.total += bytes.length;
  if (made.total > LIMITS.totalBytes || made.out.size >= LIMITS.files) throw new Refusal('[TOO_LARGE] the design system comes to more than ' + LIMITS.files + ' files or ' + inMib(LIMITS.totalBytes) + ', the most one design system may hold. The limit was passed at ' + quoted(path) + '.');
  if (made.out.has(path) && !made.out.get(path).equals(bytes)) errors.push('[PATH_CLASH] ' + quoted(made.from.get(path)) + ' and ' + quoted(from) + ' would both be published as ' + quoted(path) + '.');
  made.out.set(path, bytes);
  made.from.set(path, from);
  if (made.tree.has(from)) made.consumed.add(from);
}

function asMd(path) {
  return path.replace(/\\.mdx$/i, '.md').normalize('NFC');
}

function layout(SRC, givenTitle, OUT) {
  const tree = new BuildFolder(SRC, errors, warnings);
  const bundle = readBundle(tree);
  const NS = bundle.namespace;
  const title = givenTitle ?? NS;
  const made = { tree, out: new Map(), from: new Map(), consumed: new Set(), total: 0 };
  const { out, consumed } = made;

  const folders = findComponents(tree);
  // The bundle header has the build's order; a card it does not list goes last.
  const order = [...new Set([...bundle.listed.filter((n) => folders.has(n)), ...folders.keys()])];
  let floors = 0;
  const types = [];
  let notes = 0;
  for (const name of order) {
    const at = folders.get(name) + '/' + name;
    try {
      const card = layoutCard(tree.text(at + '.html'), { file: at + '.html', name, tree });
      put(made, 'components/' + name + '/preview.html', card.html, at + '.html');
      for (const u of card.used) consumed.add(u);
      if (card.floor) floors++;
    } catch (e) {
      if (!(e instanceof Refusal)) throw e;
      errors.push(e.message);
    }
    if (tree.has(at + '.prompt.md')) { put(made, 'components/' + name + '/README.md', layoutUsageNote(tree.text(at + '.prompt.md'), name), at + '.prompt.md'); notes++; }
    if (tree.has(at + '.d.ts')) { types.push([name, tree.text(at + '.d.ts')]); consumed.add(at + '.d.ts'); }
  }
  if (types.length) put(made, 'components/index.d.ts', joinTypes(types), 'the .d.ts files');

  // The build's header also holds a hash of every usage note and type file. This
  // one keeps only what the page reads, so editing a doc does not change bundle.js.
  put(made, 'components/bundle.js', '/* @ds-bundle: ' + JSON.stringify({ format: 4, namespace: NS, components: order.map((name) => ({ name })) }) + ' */\\n' + bundle.body, '_ds_bundle.js');

  // React 18 is listed in design-system.json's "libraries" with no file, so the
  // artifact's page loads its own production build of React 18 from a CDN and the
  // build's file (over a megabyte) is not published. The build's file is published
  // for any other version, for a test release, and when compiled code uses React's
  // internals, some of which only a development build has. It sets both
  // window.React and window.ReactDOM, so it is listed once; listed twice, it would run twice.
  let react = null;
  if (order.length && !tree.has('_vendor/react.js')) warnings.push('[REACT_MISSING] the build has components but no _vendor/react.js, so no preview will run.');
  else if (order.length) {
    const text = tree.text('_vendor/react.js');
    // Anything after the three numbers, as in 18.3.0-canary-1a2b, marks a test release, which may not work on the React the page loads.
    const [, version, rest, plain] = /\\bReactVersion\\s*=\\s*["'](\\d+\\.\\d+\\.\\d+)([-+.\\w]{0,40})(["'])?/.exec(text) ?? /\\bversion\\s*[:=]\\s*["'](\\d+\\.\\d+\\.\\d+)([-+.\\w]{0,40})(["'])?/.exec(text) ?? [];
    const major = PAGE_REACT.version.split('.')[0];
    const internals = [...out].some(([p, bytes]) => /(?:^|\\/)(?:bundle\\.js|preview\\.html)$/.test(p) && bytes.includes('__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED'));
    if (!version) errors.push('[REACT_VERSION] cannot find a React version in _vendor/react.js.');
    else if (version.startsWith(major + '.') && rest === '' && plain && !internals) react = { version, libraries: [{ name: 'react', version: major, global: 'React' }, { name: 'react-dom', version: major, global: 'ReactDOM' }] };
    else {
      const why = !version.startsWith(major + '.') ? undefined : rest !== '' || !plain ? 'it is a test release' : 'the compiled code uses React\\'s internals';
      react = { version: version + rest, why, file: 'components/lib/react.js', libraries: [{ name: 'react', version, global: 'React', file: 'components/lib/react.js' }] };
      put(made, react.file, tree.bytes('_vendor/react.js'), '_vendor/react.js');
    }
  }

  const sheet = joinStylesheets(tree);
  for (const w of sheet.warnings) warnings.push(w);
  for (const p of sheet.used) consumed.add(p);
  // The note the build leaves in place of a stylesheet when a library styles itself at run time.
  const onlyANote = tree.has('_ds_bundle.css') && tree.text('_ds_bundle.css').startsWith('/* @ds-css-runtime');
  if (sheet.css) put(made, 'components/bundle.css', sheet.css, 'styles.css');
  const fonts = sheet.fonts.map((f) => ({ ...f, file: 'fonts/' + f.file.split('/').pop() }));
  sheet.fonts.forEach((f, i) => put(made, fonts[i].file, tree.bytes(f.file), f.file));
  for (const p of tree.paths) {
    if (!/^fonts\\/[^/]+\\.(?:woff2?|ttf|otf)$/i.test(p) || consumed.has(p) || sheet.spare.has(p)) continue;
    put(made, p, tree.bytes(p), p);
    warnings.push('[FONT_UNLISTED] ' + quoted(p) + ' is named by no @font-face rule, so no page will load it');
  }
  const { tokens, report: tokenReport } = tokensFromCss(sheet.css, { title, fonts });
  if (tokens) {
    put(made, 'tokens.json', JSON.stringify(tokens, null, 2) + '\\n', 'the custom properties');
    put(made, 'tokens.css', tokensCss(tokens, title), 'the custom properties');
  }
  for (const why of tokenReport.skipped) warnings.push('[THEME_SKIPPED] ' + why);

  // The tool that publishes takes no .mdx, so such a file is published as .md, and
  // the build's own list of links follows the published names, .md and NFC.
  const guidelines = tree.paths.filter((p) => /^guidelines\\/.+\\.mdx?$/i.test(p));
  for (const p of guidelines) {
    if (p !== 'guidelines/index.md') { put(made, asMd(p), tree.bytes(p), p); continue; }
    const renamed = new Set(guidelines.filter((g) => asMd(g) !== g).map((g) => g.slice('guidelines/'.length)));
    put(made, p, tree.text(p).replace(/\\(\\.\\/([^()#?\\n]{1,300})(?=[)#?])/g, (link, to) => (renamed.has(to) ? '(./' + asMd(to) : link)), p);
  }

  const readme = layoutReadme(tree.has('README.md') ? tree.text('README.md') : '# ' + title + '\\n', {
    namespace: NS, components: order, hasCss: sheet.css !== '', hasTokens: tokens !== null, hasTypes: types.length > 0, hasNotes: notes > 0, react, fonts,
    guidelines: guidelines.filter((p) => p !== 'guidelines/index.md').length,
  });
  put(made, 'README.md', readme.text, 'README.md');
  const stale = readme.stale.slice(0, MAX_SAID).map((p) => quoted(p)).join(', ') + (readme.stale.length > MAX_SAID ? ' and ' + (readme.stale.length - MAX_SAID) + ' more' : '');
  if (!tree.has('README.md')) warnings.push('[README_MISSING] the build has no README.md that can be read, so the layout\\'s README.md holds only the "Consuming this system" section');
  else if (!readme.recognized) warnings.push('[README_UNRECOGNIZED] README.md is not the one the build writes, so it is kept whole, with the "Consuming this system" section added' + (stale ? '. It names ' + stale + ', which the artifact does not have' : ''));
  else if (stale) warnings.push('[README_STALE_PATH] README.md begins with text from .design-sync/conventions.md that names ' + stale + ', which the artifact does not have.');

  // createdOnFiles marks an artifact that keeps its content in files. Its time
  // here is a placeholder: that and the title are for whoever publishes to
  // settle, and an artifact that exists already keeps its own.
  put(made, 'design-system.json', JSON.stringify({
    v: 3,
    assetGroups: {},
    blobs: {},
    createdOnFiles: { at: '1970-01-01T00:00:00.000Z', v: 1 },
    docs: { readme: 'project/README.md', sections: [...out.keys()].filter(isSection).sort().map((p) => 'project/' + p) },
    groups: [],
    layout: 'files',
    libraries: react?.libraries ?? [],
    namespace: NS,
    sections: {},
    title,
  }, null, 2) + '\\n', 'the index');

  const checked = preflight(out);
  for (const e of checked.errors) errors.push(e);
  for (const w of checked.warnings) warnings.push(w);
  if (errors.length) return null;

  const notPublished = tree.paths.filter((p) => !consumed.has(p) && !BOOKKEEPING.test(p) && !(onlyANote && p === '_ds_bundle.css') && !(react && p === '_vendor/react.js'));
  const ownEntry = new Set(made.from.values());
  // design-system.json goes last: a reader that finds it may trust that the rest is there.
  const written = [...[...out.keys()].filter((p) => p !== 'design-system.json').sort(), 'design-system.json'];
  const report = JSON.stringify({
    version: 1,
    title,
    namespace: NS,
    sourceDigest: tree.digest(),
    files: written.map((p) => ({ path: 'project/' + p, sha256: createHash('sha256').update(out.get(p)).digest('hex'), size: out.get(p).length, contentType: contentTypeOf(p) })),
    // Files with no entry of their own above, because their content sits inside another file.
    carriedInside: [...consumed].filter((p) => !ownEntry.has(p) && (sheet.css || !sheet.used.has(p))).sort(),
    notPublished,
    // published: false means the artifact's page loads its own React in place of _vendor/react.js.
    react: react && { version: react.version, published: react.file !== undefined, why: react.why },
    components: order.length,
    floorCards: floors,
    tokens: { ...tokenReport, skipped: undefined },
    fonts: fonts.length,
    warnings: brief(warnings),
  }, null, 2) + '\\n';
  // .artifact/ was removed before the build was read. Folders are made one at a time and
  // files only where none exists, so a link found at one of these paths stops the run. A
  // folder swapped for a link after it was made here is still written through.
  const fresh = new Set();
  const makeFolder = (dir) => {
    if (fresh.has(dir)) return;
    if (dir !== OUT) makeFolder(dirname(dir));
    mkdirSync(dir);
    fresh.add(dir);
  };
  try {
    for (const p of written) {
      makeFolder(dirname(join(OUT, 'project', p)));
      writeFileSync(join(OUT, 'project', p), out.get(p), { flag: 'wx' });
    }
    writeFileSync(join(OUT, 'layout.json'), report, { flag: 'wx' });
  } catch (e) {
    if (e?.code !== 'EEXIST') throw e;
    throw new Refusal('[CHANGED_WHILE_WRITING] something else put ' + quoted(e.path ?? OUT, 300) + ' there while the layout was being made.');
  }

  const lines = [];
  for (const n of tokenReport.notes.slice(0, MAX_SAID)) lines.push('  tokens: ' + n);
  if (tokenReport.notes.length > MAX_SAID) lines.push('  tokens: and ' + (tokenReport.notes.length - MAX_SAID) + ' more notes (all in layout.json)');
  lines.push('  components: ' + order.length + (floors ? ' (' + floors + ' shown as a placeholder card)' : ''));
  lines.push('  tokens: ' + tokenReport.shown + ' of ' + tokenReport.declared + ' custom properties shown as tokens' + (tokens?.color ? ', theme(s): ' + tokenReport.themes.join(', ') : ''));
  if (react && !react.file) lines.push('  React: left to the artifact\\'s page, which loads React ' + PAGE_REACT.version + ' from jsDelivr. Previews need jsDelivr to be reachable.' + (react.version === PAGE_REACT.version ? '' : ' The build used ' + react.version + '.'));
  if (react?.why) lines.push('  React ' + react.version + ': published as ' + react.file + ' and not left to the artifact\\'s page, because ' + react.why + '.');
  if (fonts.length) lines.push('  fonts: ' + fonts.length + ' face(s) listed in tokens.json');
  if (notPublished.length) lines.push('  not published (an artifact has no place for them): ' + notPublished.slice(0, MAX_SAID).map((p) => quoted(p)).join(', ') + (notPublished.length > MAX_SAID ? ' and ' + (notPublished.length - MAX_SAID) + ' more (all in layout.json)' : ''));
  lines.push('\\u2713 wrote ' + join(OUT, 'project') + ': ' + written.length + ' files, ' + written.reduce((n, p) => n + out.get(p).length, 0) + ' bytes');
  return lines;
}

// What is at the path, looked at without following a link. Nothing, if it cannot be looked at.
function lookAt(path) {
  try { return lstatSync(path); } catch { return undefined; }
}

// Whether .artifact/ holds a report of the shape this script writes. It must be a real
// folder, not a link, and the report is read like any file of a build: through no link,
// and only up to the size one file may be.
function holdsOurReport(src) {
  if (!lookAt(join(src, '.artifact'))?.isDirectory()) return false;
  try {
    const report = JSON.parse(new BuildFolder(join(src, '.artifact'), [], []).text('layout.json'));
    return report?.version === 1 && typeof report.sourceDigest === 'string';
  } catch { return false; }
}

// Whatever goes wrong, no layout may be left for a later step to publish. Returns false if it could not be removed.
function removeLayout(OUT) {
  try { rmSync(OUT, { recursive: true, force: true }); return true; } catch (e) {
    console.error('\\u2717 [STALE_LAYOUT] ' + quoted(OUT, 300) + ' could not be removed (' + quoted(e?.code ?? e) + '), so it still holds a layout that is not this build\\'s.');
    return false;
  }
}

// Gives the exit code. It is set, not passed to process.exit(), which can cut off what was just printed.
function main() {
  const [first, flag, value, ...more] = process.argv.slice(2);
  const title = value?.replace(/\\s+/g, ' ').trim();
  const wrong = !first || first.startsWith('--') || more.length > 0 || (flag !== undefined && (flag !== '--title' || !title || title.startsWith('--')));
  const src = first && !first.startsWith('--') ? resolve(first) : null;
  const st = src === null ? undefined : lookAt(src);
  // Nothing is removed through a link, and nothing from a folder that is not a
  // build's: .artifact/ is this script's to delete only beside the build's
  // bundle, or where it holds a report that this script wrote.
  const ours = st?.isDirectory() && (lookAt(join(src, '_ds_bundle.js'))?.isFile() || holdsOurReport(src));
  const OUT = ours ? join(src, '.artifact') : null;
  if (OUT && !removeLayout(OUT)) return 1;
  if (wrong) { console.error(USAGE); return 2; }
  if (!OUT) {
    console.error('\\u2717 ' + quoted(src, 300) + (st?.isDirectory() ? ' has no _ds_bundle.js of its own (a link does not count), so it is not a build' : ' is not a folder' + (st?.isSymbolicLink() ? ' but a symbolic link, which is not followed' : '')) + '.');
    return 1;
  }
  let done = null;
  try { done = layout(src, title, OUT); } catch (e) {
    errors.push(e instanceof Refusal ? e.message
      : typeof e?.syscall === 'string' ? '[IO_FAILED] reading the build or writing the layout failed: ' + quoted(e.message, 300) + '.'
      : '[FAILED] the layout script stopped on an unexpected error, which is a bug in the script and not in the build: ' + quoted(e?.message ?? e, 300));
  }
  for (const w of brief(warnings)) console.error('! ' + w);
  if (done) { for (const l of done) console.error(l); return 0; }
  const isGone = removeLayout(OUT);
  for (const e of brief(errors)) console.error('\\u2717 ' + e);
  console.error('\\u2717 layout refused: ' + new Set(errors).size + ' problem(s)' + (isGone ? ', nothing written' : ''));
  return 1;
}

process.exitCode = main();
