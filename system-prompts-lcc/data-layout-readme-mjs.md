<!--
name: 'Data: layout-readme.mjs'
description: >-
  design-sync artifact-road lib/layout-readme.mjs rewriting generated README
  text, extracted with the skill for the model.
ccVersion: 2.1.330
-->
// Rewrites the text the build generated (README.md, the head of each usage
// note) to describe a Design System artifact's files in place of ds-bundle/.
// An agent that builds with the system loads the files README.md names, in the
// order it names them. Text a person wrote is never changed.

const RULE = '\\n\\n---\\n\\n';
const MAX_TRANSLATED = 10;
// When someone edits the system on the artifact's page, the page replaces
// everything from exactly this rule and heading on with a section of its own.
const CONSUMING_HEAD = '## Consuming this system (generated \\u2014 do not edit)';
// The React that a Design System artifact's page loads by itself. It must match
// the version and addresses that page uses, or README.md names files it does not load.
export const PAGE_REACT = {
  version: '18.3.1',
  urls: ['https://cdn.jsdelivr.net/npm/react@18.3.1/umd/react.production.min.js', 'https://cdn.jsdelivr.net/npm/react-dom@18.3.1/umd/react-dom.production.min.js'],
};

function list(items) {
  return items.length <= 1 ? items.join('') : items.slice(0, -1).join(', ') + ' and ' + items.at(-1);
}

function code(s) {
  return '\`' + s + '\`';
}

// info: { namespace, components: [name], hasCss, hasTokens, hasTypes, hasNotes,
//         react: { version, file: its path if the system holds a copy } | null,
//         fonts: [{ family, file, weight, style }], guidelines: number }
// Names only files the system has.
export function consumingSection(info) {
  const { namespace: ns, fonts } = info;
  const sheets = [...(info.hasTokens ? ['tokens.css'] : []), ...(info.hasCss ? ['components/bundle.css'] : [])];
  const toCopy = [...sheets.map(code), code('components/bundle.js'), ...(info.hasTypes ? [code('components/index.d.ts')] : []), ...fonts.map((f) => code(f.file))];
  const reactFiles = !info.react ? [] : info.react.file ? [info.react.file] : PAGE_REACT.urls;
  const more = [
    ...(info.hasTypes ? ['a component\\'s props: ' + code('<Comp>Props') + ' in ' + code('components/index.d.ts')] : []),
    ...(info.hasNotes ? ['how to use a component, with examples: ' + code('components/<Comp>/README.md')] : []),
    ...(info.hasTokens ? ['token values: ' + code('tokens.json')] : []),
    ...(info.guidelines ? ['the system\\'s own guidance: ' + code('guidelines/')] : []),
  ];
  const lines = [
    CONSUMING_HEAD, '',
    'Every path named in this file is under ' + code('project/') + ' in this design system' + (info.react && !info.react.file ? ' (the two jsDelivr addresses below are web addresses, not paths)' : '') + ': read ' + code('project/components/bundle.js') + ', not ' + code('components/bundle.js') + '.', '',
    ...staleNames(info.stale ?? [], info),
    code('components/bundle.js') + ' defines ' + code('window.' + ns) + ' (' + info.components.length + ' component' + (info.components.length === 1 ? '' : 's') + ').' +
      (info.hasCss ? ' ' + code('components/bundle.css') + ' is its stylesheet, with the library\\'s own custom properties in it.' : ' The library styles itself at run time, so it has no stylesheet.') +
      (info.hasTokens ? ' ' + code('tokens.css') + ' holds the tokens the pages of this system show' + (fonts.length ? ', and an ' + code('@font-face') + ' rule for each font file' : '') + '.' : '') +
      (!info.react ? '' : ' The bundle reads ' + code('window.React') + ' and ' + code('window.ReactDOM') + (info.react.file
        ? '; ' + code(info.react.file) + ' sets both (React ' + info.react.version + ', the version the library was built against).'
        : '. This system includes no copy of React: the artifact\\'s own page loads React ' + PAGE_REACT.version + ' from jsDelivr, and any other page needs React ' + PAGE_REACT.version.split('.')[0] + ' too, as below.' + (info.react.version === PAGE_REACT.version ? '' : ' The library was built against ' + info.react.version + '.'))),
    'Build any UI by mounting these components. Never hand-build a control the system provides.', '',
    '- **Any page:** load' + (sheets.length || info.react ? ', in this order, ' : ' ') + list([...sheets, ...reactFiles, 'components/bundle.js'].map(code)) + '. A script here is a classic script, not a module.' +
      (info.react && !info.react.file ? ' A page that already has React 18 as ' + code('window.React') + ' and ' + code('window.ReactDOM') + ' skips the two web addresses.' : ''),
    '- **Design canvas:** copy ' + list(toCopy) + ' in full' + (toCopy.length > 1 ? ', each' : '') + ' to the same path under the canvas\\'s ' + code('project/ds/<folder>/') + '.' +
      (sheets.length ? ' Link the stylesheet' + (sheets.length > 1 ? 's in that order,' : '') + ' before the script.' : '') +
      (!info.react ? '' : info.react.file ? ' Leave ' + code('components/lib/') + ' out: the artboard supplies React.' : ' The artboard supplies React.') +
      (info.hasTypes ? ' The editor\\'s Properties panel reads each component\\'s props from ' + code('components/index.d.ts') + '.' : '') +
      ' Mount a component with ' + code('<x-import component-from-global-scope="' + ns + '.<Comp>">') + '.',
    '- **Slides deck, or any surface that cannot run the bundle:** ' + (info.hasTokens ? 'take ' + code('tokens.json') + (fonts.length ? ' and the font files' : '') + '; a deck mounts no components.' : 'this system has no token file to take.'),
    ...(more.length ? ['', '**Where to read more:** ' + more.join('; ') + '.'] : []),
  ];
  if (fonts.length) {
    lines.push('', '| family | weight | style | file |', '| --- | --- | --- | --- |',
      ...fonts.map((f) => '| ' + f.family + ' | ' + f.weight + ' | ' + f.style + ' | ' + code(f.file) + ' |'));
  }
  return lines.join('\\n') + '\\n';
}

function whereThingsAre(info) {
  const ns = info.namespace;
  const perComponent = [
    ...(info.hasNotes ? [code('components/<Name>/README.md') + ' (usage, example JSX)'] : []),
    code('components/<Name>/preview.html') + ' (the live preview)',
    ...(info.hasTypes ? [code('components/index.d.ts') + ' (every ' + code('<Name>Props') + ')'] : []),
  ];
  return [
    '## Where things are', '',
    '- ' + code('components/bundle.js') + ' \\u2014 every component, as one script that sets ' + code('window.' + ns) + '.',
    ...(info.hasCss ? ['- ' + code('components/bundle.css') + ' \\u2014 the one stylesheet: the library\\'s tokens and component styles, joined.'] : []),
    '- ' + perComponent.join(', ') + '.',
    ...(info.hasTokens ? ['- ' + code('tokens.json') + ' \\u2014 the tokens this system\\'s pages show, read from the library\\'s custom properties; ' + code('tokens.css') + ' is the same as CSS.'] : []),
    ...(info.fonts.length ? ['- ' + code('fonts/') + ' \\u2014 the font files, listed in ' + code('tokens.json') + '.'] : []),
    ...(info.guidelines ? ['- ' + code('guidelines/') + ' \\u2014 the design system\\'s own usage guidance (' + info.guidelines + ' doc(s), see ' + code('guidelines/index.md') + '). Read these before composing larger layouts.'] : []),
    ...(info.hasNotes ? ['', 'For a specific component, read ' + code('components/<Name>/README.md') + '.'] : []),
    '', '',
  ].join('\\n');
}

// The paths in text that exist in the build folder and not in the artifact.
const BUILD_ONLY = /(?<![\\w-])(?<![\\w>*-]\\/)(?:_ds_bundle\\.(?:js|css)|styles\\.css|_vendor\\/[\\w.-]{0,100}|_preview\\/[\\w.-]{0,100}|tokens\\/[\\w*/-]{0,100}(?:\\.[\\w*/-]{1,100}){0,3}\\.css|fonts\\/fonts\\.css)(?![\\w-])/g;
export function buildOnlyPaths(text) {
  const found = new Map();
  for (const m of text.matchAll(BUILD_ONLY)) found.set(m.index, m[0].replace(/\\.$/, ''));
  // One file for each component in the build: the ending alone, or after a
  // component's name or a placeholder for one. "vite-env.d.ts" is no such file.
  for (const ending of ['.prompt.md', '.d.ts']) {
    for (let at = text.indexOf(ending); at >= 0; at = text.indexOf(ending, at + 1)) {
      let from = at;
      while (from > 0 && at - from < 100 && /[\\w<>]/.test(text[from - 1])) from--;
      if (/^(?:\\w|\\.\\w)/.test(text.slice(at + ending.length, at + ending.length + 2)) || /[\\w.<>-]/.test(text[from - 1] ?? '') || !/^(?:[A-Z<]|$)/.test(text.slice(from, at))) continue;
      found.set(from, text.slice(from, at) + ending);
    }
  }
  return [...new Set([...found].sort((a, b) => a[0] - b[0]).map(([, path]) => path))];
}

// Where a reader finds, in the artifact, what a path of the build folder held. Null: nowhere.
function publishedAs(path, info) {
  if (path.endsWith('.prompt.md')) return info.hasNotes ? 'components/<Name>/README.md' : null;
  if (path.endsWith('.d.ts')) return info.hasTypes ? 'components/index.d.ts' : null;
  if (path === '_ds_bundle.js') return 'components/bundle.js';
  if (path.startsWith('_preview/')) return 'components/<Name>/preview.html';
  if (/^_vendor\\/react(?:-dom)?\\.js$/.test(path)) return info.react?.file ?? null;
  if (!path.endsWith('.css')) return null;
  // The font faces are written out in tokens.css, and so are the tokens of a library with no stylesheet.
  if (info.hasTokens && (path === 'fonts/fonts.css' || !info.hasCss)) return 'tokens.css';
  return info.hasCss ? 'components/bundle.css' : null;
}

// Text a person wrote is kept as it is, so what it names and the artifact lacks is translated here.
function staleNames(stale, info) {
  if (!stale.length) return [];
  const byPlace = new Map();
  for (const path of stale.slice(0, MAX_TRANSLATED)) {
    const place = publishedAs(path, info);
    byPlace.set(place, [...(byPlace.get(place) ?? []), path]);
  }
  return ['The text above this section names files of the build that made this design system, which does not hold them under those names. ' +
    [...byPlace].map(([place, paths]) => (place === null ? list(paths.map(code)) + (paths.length > 1 ? ' have' : ' has') + ' no counterpart here' : 'Read ' + code(place) + ' in place of ' + list(paths.map(code)))).join('. ') + '.' +
    (stale.length > MAX_TRANSLATED ? ' It names ' + (stale.length - MAX_TRANSLATED) + ' more such file' + (stale.length - MAX_TRANSLATED > 1 ? 's' : '') + '.' : ''), ''];
}

// The first from in text replaced by to, which is taken as it stands: "$&" in it means nothing.
function swap(text, from, to) {
  return text.replace(from, () => to);
}

// stale: build-folder paths still named in text a person wrote.
// recognized: false when the generated part was not found, and so was left as it is.
export function layoutReadme(readme, info) {
  const head = '# ' + info.namespace + ' (';
  const title = readme.startsWith(head) ? 0 : readme.indexOf('\\n' + head) + 1 || -1;
  const from = title < 0 ? -1 : readme.indexOf('\\n## Where things are\\n', title);
  const loading = from < 0 ? -1 : readme.indexOf('\\n## Loading\\n', from);
  const authored = loading < 0 ? readme : readme.slice(0, title);
  const stale = buildOnlyPaths(authored);
  const tail = RULE + consumingSection({ ...info, stale });
  if (loading < 0) return { text: readme.trimEnd() + tail, stale, recognized: false };
  let rest = readme.slice(loading + 1);
  // From this sentence to the end of the code block under it.
  const lines = rest.indexOf('Add these two lines to your page once');
  const fence = lines < 0 ? -1 : rest.indexOf('\\n\`\`\`\\n', lines);
  if (fence >= 0) rest = rest.slice(0, lines) + 'What to load, and in what order, is under "Consuming this system" at the end of this file.\\n' + rest.slice(fence + '\\n\`\`\`\\n'.length);
  rest = swap(rest, '(bundled for the preview cards as \`_vendor/preview-decorators.js\`)', '(each preview card carries a copy)');
  rest = swap(rest, 'They are declared inside \`_ds_bundle.css\` (this DS ships one compiled stylesheet rather than separate token files).', 'They are declared inside \`components/bundle.css\`.');
  rest = swap(rest, 'See \`tokens/\` for the full list.', !info.hasCss ? '' : 'All of them are declared in \`components/bundle.css\`' + (info.hasTokens ? '; \`tokens.json\` lists the ones with a value a page can show.' : '.'));
  return { text: authored + readme.slice(title, from + 1) + whereThingsAre(info) + rest.trimEnd() + tail, stale, recognized: true };
}

// Only the first line and the "Variants" line name files of the build folder.
// The artifact's page takes a note's first sentence of prose for the component's
// summary, so those two lines, which the build writes, go below the first
// paragraph of the library's own doc, where that begins like a sentence and holds
// no code fence: a blank line inside the code would be taken for the paragraph's end.
export function layoutUsageNote(text, name) {
  const nl = text.indexOf('\\n');
  const head = swap(nl < 0 ? text : text.slice(0, nl), '(bundle loaded from the root \`_ds_bundle.js\`)', '(from \`components/bundle.js\`)');
  const rest = swap(nl < 0 ? '' : text.slice(nl), '\\nVariants (see \`' + name + '.html\`): ', '\\nVariants (see \`preview.html\`): ');
  const doc = /^((?:\\n+Variants \\([^\\n]*)?)\\n+(# [^\\n]*\\n\\n+(?=[\\p{L}"'(])[^\\n]+(?:\\n[^\\n]+)*)/u.exec(rest);
  return doc && !/^ {0,3}(?:\`\`\`|~~~)/m.test(doc[2]) ? doc[2] + '\\n\\n' + head + doc[1] + rest.slice(doc[0].length) : head + rest;
}

// files: [[name, text of <Name>.d.ts]]. The artifact's page and its readers look
// up <Name>Props in the one joined file.
export function joinTypes(files) {
  const IMPORT = /^import \\* as React from 'react';\\n+/;
  return "import * as React from 'react';\\n\\n" + files.map(([, text]) => text.replace(IMPORT, '').trim()).join('\\n\\n') + '\\n';
}
