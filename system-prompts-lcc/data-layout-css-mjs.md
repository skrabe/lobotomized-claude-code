<!--
name: 'Data: layout-css.mjs'
description: >-
  design-sync artifact-road lib/layout-css.mjs joining styles.css for a Design
  System artifact, extracted with the skill for the model.
ccVersion: 2.1.330
-->
// Joins styles.css and all it imports into the one stylesheet a Design System
// artifact loads. The artifact's page loads it sometimes through a <link> and
// sometimes pasted into a <style>, so nothing in it may depend on where the
// file sits: no local @import, no relative url().
// The CSS comes from the library being synced and may be huge or malformed, so
// every scan here is a single forward pass.

const FONT_RANK = ['woff2', 'woff', 'ttf', 'otf'];
const MIME = new Map(Object.entries({
  woff2: 'font/woff2', woff: 'font/woff', ttf: 'font/ttf', otf: 'font/otf',
  png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', gif: 'image/gif',
  webp: 'image/webp', avif: 'image/avif', svg: 'image/svg+xml', ico: 'image/x-icon',
}));
// A larger file stays a url(): as a data: URI it would be repeated at every
// url() that names it.
export const INLINE_MAX_BYTES = 1024 * 1024;
// All data: URIs together. A file is carried again at each mention.
export const INLINE_TOTAL_BYTES = 8 * 1024 * 1024;
// The most one file of an artifact may be. Joining stops here: a sheet imported
// under many conditions is written once for each.
export const SHEET_MAX_BYTES = 15 * 1024 * 1024;
const MAX_IMPORT_DEPTH = 8;

function extOf(path) {
  return path.slice(path.lastIndexOf('.') + 1).toLowerCase();
}

// Thrown when a build cannot be laid out as an artifact. Its message, "[TAG] " and
// a sentence, is for the person to read as it stands.
export class Refusal extends Error {}

// Characters that draw nothing, or that hide or reorder what is around them.
// Global, for replace() and search(): test() on it would remember where it stopped.
export const UNSEEN = /[\\p{Cc}\\p{Cf}\\p{Co}\\p{Cn}\\p{Zl}\\p{Zp}\\u034f\\u115f\\u1160\\u17b4\\u17b5\\u180b-\\u180f\\u2800\\u3164\\ufe00-\\ufe0f\\uffa0\\u{e0100}-\\u{e01ef}]/gu;

// Other people's text, for printing: one line, cut short, with characters that do not show (they can hide words from a
// person that a model still reads) written as their code. The codes are written first and the cut made after, between
// whole characters and codes: at most max characters, and "..." where it was cut. written() says how a character that
// does show is put down.
function held(text, max, written) {
  const whole = String(text);
  // Only the start is read. Half a pair left at its end is dropped, not shown as a broken character the text never held.
  const units = whole.slice(0, max * 2).replace(/[\\ud800-\\udbff]$/, '').replace(/[\\p{Cc}\\p{Zl}\\p{Zp}]+/gu, ' ').match(/[^]/gu) ?? [];
  let line = '';
  for (const unit of units) {
    const code = unit.replace(UNSEEN, (c) => '\\\\u{' + c.codePointAt(0).toString(16) + '}');
    const next = code === unit ? written(unit.replace(/\\p{Cs}/u, '\\ufffd')) : code;
    if (line.length + next.length > max) return line + '...';
    line += next;
  }
  return whole.length > max * 2 ? line + '...' : line;
}

// As it goes into a value of JSON, which brings its own quotes.
export function shown(text, max = 120) {
  return held(text, max, (c) => c);
}

// As it goes into a message: in quotes, so that it cannot pass for the tool's own words.
export function quoted(text, max = 120) {
  return '"' + held(text, max, (c) => (c === '"' || c === '\\\\' ? '\\\\' + c : c)) + '"';
}

// A size for a message, rounded up: "15 MiB", "0.1 MiB".
export function inMib(bytes) {
  return Math.ceil(bytes / (1024 * 1024) * 10) / 10 + ' MiB';
}

function isSpace(c) {
  return c === ' ' || c === '\\n' || c === '\\t' || c === '\\r' || c === '\\f';
}

// Does a string, an escape or a comment start at i?
function opensSkip(css, i) {
  return css[i] === '"' || css[i] === "'" || css[i] === '\\\\' || (css[i] === '/' && css[i + 1] === '*');
}

// A character that makes what follows it part of a longer word: "myurl(", "@url(" and "\\url(" are not url(.
const IN_WORD = /[\\w\\-@#\\\\\\u0080-\\uffff]/;

// Is the "(" at i that of a url( with no quotes? Such an address runs to the next
// ")" whatever it holds: "/*" in it opens no comment.
function bareUrlAt(css, i) {
  if (css.slice(Math.max(0, i - 3), i).toLowerCase() !== 'url' || IN_WORD.test(css[i - 4] ?? '')) return false;
  let j = i + 1;
  while (isSpace(css[j])) j++;
  return css[j] !== '"' && css[j] !== "'";
}

// The index just past the string, comment, escape or bracketed group that
// starts at i, else i + 1. A brace or semicolon inside one of those ends nothing.
// Where the text ends first, what would close the token is added to unclosed,
// if that list is given: one scan answers both, so the answers cannot disagree.
export function skipToken(css, i, unclosed) {
  const c = css[i];
  if (c === '"' || c === "'") {
    let j = i + 1;
    for (; j < css.length; j++) {
      if (css[j] === '\\\\') j++;
      else if (css[j] === c || css[j] === '\\n') return j + 1;
    }
    // A browser takes the string as closed there. A backslash at the very end would escape the quote, so a line end uses it up.
    unclosed?.push((j > css.length ? '\\n' : '') + c);
    return css.length;
  }
  if (c === '/' && css[i + 1] === '*') {
    const end = css.indexOf('*/', i + 2);
    if (end < 0) unclosed?.push('*/');
    return end < 0 ? css.length : end + 2;
  }
  if (c === '\\\\') {
    // A backslash at the very end would escape whatever is added next, so a line end is added to use it up.
    if (i + 1 >= css.length) unclosed?.push('\\n');
    return i + 2;
  }
  if (c !== '(' && c !== '[') return i + 1;
  // Inside a group a brace opens a group too, and only its own mirror closes each.
  const open = [];
  for (let j = i; j < css.length;) {
    if (css[j] === '(' && bareUrlAt(css, j)) {
      for (j++; j < css.length && css[j] !== ')'; j++) if (css[j] === '\\\\') j++;
      if (j > css.length) unclosed?.push('\\n');
      if (j >= css.length) { open.push(')'); break; }
      j++;
    } else if (css[j] === '(' || css[j] === '[' || css[j] === '{') open.push(css[j] === '(' ? ')' : css[j] === '[' ? ']' : '}'), j++;
    else if (css[j] === open.at(-1)) { open.pop(); j++; } else j = opensSkip(css, j) ? skipToken(css, j, unclosed) : j + 1;
    if (open.length === 0) return j;
  }
  unclosed?.push(open.reverse().join(''));
  return css.length;
}

// A "/*" inside a string is text.
export function stripComments(css) {
  let out = '';
  let from = 0;
  for (let i = 0; i < css.length;) {
    const next = css[i] === '[' || (css[i] === '(' && !bareUrlAt(css, i)) ? i + 1 : skipToken(css, i);
    if (css[i] === '/' && css[i + 1] === '*') { out += css.slice(from, i) + ' '; from = next; }
    i = next;
  }
  return out + css.slice(from);
}

// The statements between start and end: { prelude, start, end, body, by }, body
// being [from, to] for a block and null for a statement with none. by is what
// ended the prelude: "{", ";", a stray "}", or "" for the end of the text.
// Comments and whitespace between statements belong to the one that follows.
export function cssStatements(css, start = 0, end = css.length) {
  const out = [];
  let at = start;
  while (at < end) {
    let i = at;
    while (i < end && (isSpace(css[i]) || (css[i] === '/' && css[i + 1] === '*'))) i = isSpace(css[i]) ? i + 1 : skipToken(css, i);
    if (i >= end) break;
    const head = i;
    let body = null;
    while (i < end && css[i] !== ';' && css[i] !== '{' && css[i] !== '}') i = skipToken(css, i);
    const prelude = css.slice(head, Math.min(i, end)).trim();
    const by = i < end ? css[i] : '';
    if (by === '{') {
      const from = i + 1;
      let depth = 1;
      i = from;
      while (i < end && depth > 0) {
        if (css[i] === '{') { depth++; i++; } else if (css[i] === '}') { depth--; i++; } else i = skipToken(css, i);
      }
      body = [from, depth === 0 ? i - 1 : Math.min(i, end)];
    } else if (i < end) i++;
    out.push({ prelude, start: at, end: Math.min(i, end), body, by });
    at = Math.min(i, end);
  }
  return out;
}

// Runs of white space become one space, except inside a string.
function squeeze(value) {
  let out = '';
  for (let i = 0; i < value.length;) {
    if (isSpace(value[i])) { out += ' '; while (isSpace(value[i])) i++; continue; }
    const next = value[i] === '"' || value[i] === "'" ? skipToken(value, i) : i + 1;
    out += value.slice(i, next);
    i = next;
  }
  return out.trim();
}

// The declarations of one block as [property, value] pairs. Nested rules are skipped.
export function cssDeclarations(css, from, to) {
  const out = [];
  for (const s of cssStatements(css, from, to)) {
    if (s.body) continue;
    const colon = s.prelude.indexOf(':');
    if (colon <= 0) continue;
    out.push([s.prelude.slice(0, colon).trim(), squeeze(stripComments(s.prelude.slice(colon + 1)))]);
  }
  return out;
}

export function splitTopLevel(value, sep) {
  const out = [];
  let from = 0;
  for (let i = 0; i < value.length;) {
    if (value[i] === sep) { out.push(value.slice(from, i)); from = ++i; } else i = skipToken(value, i);
  }
  out.push(value.slice(from));
  return out.map((s) => s.trim()).filter(Boolean);
}

// What would close whatever the text leaves open. A browser closes it at the end
// of a file; joined text would swallow the next file instead. Reads the text as
// cssStatements does, so the two agree on what is open.
function closers(css) {
  const unclosed = [];
  let depth = 0;
  for (let i = 0; i < css.length; i = skipToken(css, i, unclosed)) {
    if (css[i] === '{') depth++; else if (css[i] === '}' && depth > 0) depth--;
  }
  return unclosed.join('') + '}'.repeat(depth);
}

// The address at i, written url(...) or as a string: { url, end }, or null.
function readAddress(css, i) {
  if (css[i] === '"' || css[i] === "'") {
    const end = skipToken(css, i);
    return css[end - 1] === css[i] && end - i > 1 ? { url: css.slice(i + 1, end - 1), end } : null;
  }
  if (css.slice(i, i + 4).toLowerCase() !== 'url(') return null;
  let j = i + 4;
  while (isSpace(css[j])) j++;
  let url;
  if (css[j] === '"' || css[j] === "'") {
    const inner = readAddress(css, j);
    if (!inner) return null;
    url = inner.url;
    j = inner.end;
  } else {
    const from = j;
    while (j < css.length && !isSpace(css[j]) && !'()"\\''.includes(css[j])) j += css[j] === '\\\\' ? 2 : 1;
    url = css.slice(from, j);
  }
  while (isSpace(css[j])) j++;
  return css[j] === ')' ? { url, end: j + 1 } : null;
}

// css with each url(...) replaced by fn(address), or left alone where fn gives
// null. A url( inside a string or a comment is text, not an address.
function mapUrls(css, fn) {
  let out = '';
  let from = 0;
  for (let i = 0; i < css.length;) {
    if (opensSkip(css, i)) { i = skipToken(css, i); continue; }
    const hit = (css[i] === 'u' || css[i] === 'U') && !IN_WORD.test(css[i - 1] ?? '') ? readAddress(css, i) : null;
    if (!hit) { i++; continue; }
    const put = fn(hit.url);
    if (put !== null) { out += css.slice(from, i) + put; from = hit.end; }
    i = hit.end;
  }
  return out + css.slice(from);
}

// resolveInTree('a/b.css', '../c/d.png?x#y') is 'c/d.png'. Null for an absolute
// or remote address, a bare fragment, a path that climbs out of the folder, or one
// whose "%" escapes cannot be decoded. A name with "\\", ":" or a NUL byte is refused
// too: to Windows the first two are a separator and a drive.
export function resolveInTree(fromFile, url) {
  if (!url || /^[a-z][a-z0-9+.-]*:|^\\/|^#/i.test(url)) return null;
  const parts = fromFile.split('/').slice(0, -1);
  for (const seg of url.split(/[?#]/, 1)[0].split('/')) {
    if (seg === '' || seg === '.') continue;
    if (seg === '..') { if (!parts.length) return null; parts.pop(); } else parts.push(seg);
  }
  let path = parts.join('/');
  try { path = decodeURIComponent(path); } catch { return null; }
  return path.split('/').some((s) => s === '..' || s === '' || /[\\\\:\\0]/.test(s)) ? null : path;
}

// The parts of an @import statement, and its text with nothing left open, or null when it cannot be read.
function parseImport(statement) {
  // Without its comments, one of which the end of the file may have closed.
  const prelude = stripComments(statement);
  let i = '@import'.length;
  while (isSpace(prelude[i])) i++;
  const address = readAddress(prelude, i);
  if (!address) return null;
  const conditions = prelude.slice(address.end).trim();
  // These are written out with more text after them, which a string or bracket left open would swallow.
  if (closers(conditions) !== '') return null;
  let rest = conditions;
  let layer = null, supports = null;
  const l = /^layer(?:\\(([^)]*)\\)|(?=\\s|$))/i.exec(rest);
  if (l) { layer = l[1]?.trim() ?? ''; rest = rest.slice(l[0].length).trim(); }
  if (/^supports\\(/i.test(rest)) {
    const close = skipToken(rest, 'supports'.length);
    supports = rest.slice('supports'.length, close);
    rest = rest.slice(close).trim();
  }
  return { url: address.url, text: '@import ' + prelude.slice(i, address.end) + (conditions && ' ' + conditions) + ';', layer, supports, media: rest };
}

const WEIGHT = /^(?:[1-9]\\d{0,2}|1000)(?: (?:[1-9]\\d{0,2}|1000))?$/;
// Descriptors tokens.json has no field for. A face that carries one keeps its
// own rule: without unicode-range, for one, the subsets of a family would
// replace each other and only the last would be used.
const KEEPS_OWN_RULE = /^(?:unicode-range|font-stretch|font-width|size-adjust|ascent-override|descent-override|line-gap-override|font-feature-settings|font-variation-settings|font-named-instance|font-language-override)$/i;
// What the artifact's page accepts as a family name, less "|" and the backtick:
// the name is also printed in a table in the artifact's README.md.
const FAMILY = /^[^;{}<>()\\\\\\r\\n\\f"'|\`]{1,120}$/;
const FONT_FILE = /^[A-Za-z0-9][A-Za-z0-9._@+ -]*$/;
const FONT_FOLDERS = /^(?:[A-Za-z0-9._@+ -]+\\/)*$/;

// Reads one @font-face. local lists the build's font files that its src names, woff2 first.
function readFontFace(css, body, fromFile, tree) {
  const face = { family: '', weight: '400', style: 'normal', local: [], ownRule: false, decls: cssDeclarations(css, body[0], body[1]) };
  for (const [prop, value] of face.decls) {
    const p = prop.toLowerCase();
    if (p === 'font-family') face.family = value.replace(/^["']|["']$/g, '').trim();
    else if (p === 'font-weight') face.weight = value === 'normal' ? '400' : value === 'bold' ? '700' : value;
    else if (p === 'font-style') face.style = /^oblique\\b/.test(value) ? 'oblique' : value;
    else if (p === 'src') {
      mapUrls(value, (url) => {
        const path = resolveInTree(fromFile, url);
        if (path && FONT_RANK.includes(extOf(path)) && tree.has(path)) face.local.push(path);
        return null;
      });
    } else if (KEEPS_OWN_RULE.test(p) && !(/^font-(?:stretch|width)$/.test(p) && /^(?:normal|100%)$/.test(value))) face.ownRule = true;
  }
  face.local.sort((a, b) => FONT_RANK.indexOf(extOf(a)) - FONT_RANK.indexOf(extOf(b)));
  return face;
}

function warn(join, tag, text) {
  join.warnings.add('[' + tag + '] ' + text);
}

// text with each relative url() that names a picture or a font of the build
// turned into a data: URI, so that it loads wherever the stylesheet is put.
function rebase(join, text, fromFile) {
  const { tree, uris } = join;
  return mapUrls(text, (url) => {
    const where = quoted(fromFile) + ': url(' + quoted(url) + ') ';
    if (/^(?:https?:)?\\/\\//i.test(url)) warn(join, 'CSS_URL_REMOTE', where + 'names another site and was left as it is. It loads only if the artifact\\'s page allows that site: to be sure of it, put the file in the build and name it by a relative path');
    if (url === '' || /^(?:[a-z][a-z0-9+.-]*:|\\/\\/|#)/i.test(url)) return null;
    const path = resolveInTree(fromFile, url);
    if (path === null || !tree.has(path)) { warn(join, 'CSS_URL_MISSING', where + (url.startsWith('/') ? 'starts at the root of a site, which an artifact does not have' : 'names no file of this build') + ', so it will not load'); return null; }
    if (!MIME.has(extOf(path))) { warn(join, 'CSS_URL_KIND', where + 'is not a picture or a font, so it was left as it is and will not load'); return null; }
    if (!uris.has(path)) {
      const bytes = tree.bytes(path);
      uris.set(path, bytes.length > INLINE_MAX_BYTES ? null : 'data:' + MIME.get(extOf(path)) + ';base64,' + bytes.toString('base64'));
    }
    const uri = uris.get(path);
    if (uri === null || join.carriedBytes + uri.length > INLINE_TOTAL_BYTES) {
      warn(join, 'CSS_URL_TOO_LARGE', where + 'cannot be carried inside the stylesheet (at most ' + inMib(INLINE_MAX_BYTES) + ' a file, ' + inMib(INLINE_TOTAL_BYTES) + ' in all), so it will not load');
      return null;
    }
    join.carriedBytes += uri.length;
    join.used.add(path);
    const hash = url.indexOf('#');
    return 'url("' + uri + (hash < 0 ? '' : url.slice(hash).replace(/["\\\\\\s]/g, '')) + '")';
  });
}

// The text of file with its local imports written out in place.
// under: the conditions of every import on the way here.
function expand(join, file, under) {
  const { tree, fonts, spare, open, done } = join;
  join.used.add(file);
  open.add(file);
  // A browser reads every kind of line end as "\\n" before anything else.
  const css = tree.text(file).replace(/^\\uFEFF/, '').replace(/\\r\\n?|\\f/g, '\\n');
  join.joinedBytes += Buffer.byteLength(css);
  if (join.joinedBytes > SHEET_MAX_BYTES) throw new Refusal('[STYLESHEET_TOO_LARGE] styles.css and all it imports come to more than ' + inMib(SHEET_MAX_BYTES) + ', the most one file of an artifact may be. ' + quoted(file) + ' is where the limit was passed. A sheet imported under several conditions counts once for each: import it once, or make the sheets smaller, and build again.');
  let out = '';
  let early = true; // a browser ignores an @import that comes after a block or after @namespace
  let dead = false;
  for (const s of cssStatements(css)) {
    const at = /^@([a-z-]+)/i.exec(s.prelude)?.[1].toLowerCase();
    // At the top of a sheet, text cut off by ";" or "}" (or by the end of the file)
    // is to a browser the start of the next rule, which it then drops whole. Kept,
    // a stray "}" would also end the block an import's conditions are written as.
    if (dead || (!s.body && (at === undefined || s.by === '}'))) { dead = !s.body; continue; }
    if (at === 'charset') continue;
    if (at === 'import' && !s.body) {
      const imp = parseImport(s.prelude);
      const where = quoted(file) + ': ';
      if (!early) { warn(join, 'CSS_IMPORT_LATE', where + 'the statement ' + quoted(s.prelude) + ' comes after another rule, where a browser ignores it, so it was left out'); continue; }
      if (!imp) { warn(join, 'CSS_IMPORT_UNREADABLE', where + 'the statement ' + quoted(s.prelude) + ' cannot be read as an @import and was left out'); continue; }
      if (/^(?:https?:)?\\/\\//i.test(imp.url)) {
        join.remote.add(imp.text);
        if (!/^(?:https:)?\\/\\/fonts\\.googleapis\\.com\\//i.test(imp.url)) warn(join, 'CSS_REMOTE_IMPORT', where + 'the @import of ' + quoted(imp.url) + ' was kept but will not load: an artifact page loads a stylesheet by address only from Google Fonts');
        continue;
      }
      const target = resolveInTree(file, imp.url);
      if (target === null || !/\\.css$/i.test(target) || !tree.has(target)) { warn(join, 'CSS_IMPORT_MISSING', where + 'the @import of ' + quoted(imp.url) + ' names no stylesheet of this build and was left out'); continue; }
      // Written once for each set of conditions, at its first place. A browser would apply it again at each.
      const key = under + JSON.stringify([target, imp.layer, imp.supports, imp.media]);
      if (done.has(key) || open.has(target)) continue;
      if (open.size >= MAX_IMPORT_DEPTH) { warn(join, 'CSS_IMPORT_DEPTH', where + 'the @import of ' + quoted(imp.url) + ' is nested more than ' + MAX_IMPORT_DEPTH + ' deep and was left out'); continue; }
      done.add(key);
      let inner = '/* ' + target.replace(/\\*\\//g, '* /') + ' */\\n' + expand(join, target, imp.layer === null && imp.supports === null && !imp.media ? under : key).trimEnd() + '\\n';
      if (imp.media) inner = '@media ' + imp.media + ' {\\n' + inner + '}\\n';
      if (imp.supports !== null) inner = '@supports ' + imp.supports + ' {\\n' + inner + '}\\n';
      if (imp.layer !== null) inner = '@layer' + (imp.layer ? ' ' + imp.layer : '') + ' {\\n' + inner + '}\\n';
      out += inner;
      continue;
    }
    early &&= !s.body && at !== 'namespace';
    if (at === 'font-face' && s.body) {
      const face = readFontFace(css, s.body, file, tree);
      for (const p of face.local) spare.add(p);
      // A face tokens.json can hold whole is taken out of the stylesheet and listed there.
      if (face.local.length > 0 && !face.ownRule && WEIGHT.test(face.weight) && /^(?:normal|italic|oblique)$/.test(face.style) &&
        FAMILY.test(face.family) && !face.family.includes('/*') && !face.family.includes('*/') && FONT_FILE.test(face.local[0].split('/').pop()) && FONT_FOLDERS.test(face.local[0].replace(/[^/]*$/, ''))) {
        const key = JSON.stringify([face.family, face.weight, face.style]);
        const twin = fonts.get(key);
        if (!twin) fonts.set(key, { family: face.family, file: face.local[0], weight: face.weight, style: face.style });
        else if (twin.file !== face.local[0]) {
          warn(join, 'FONT_DUPLICATE', quoted(file) + ': a second ' + quoted(face.family) + ' ' + face.weight + ' ' + face.style + ' face (' + quoted(face.local[0]) + ') was left out; ' + quoted(twin.file) + ' is used');
        }
        continue;
      }
      if (face.local.length) {
        // Of the sources that name a file of the build, one is enough: the first that
        // names the best file. The same face often sits in two sheets, so it is
        // written once for each set of conditions.
        const best = face.local[0];
        const local = new Set(face.local);
        let isCarried = false;
        const rule = '@font-face{' + face.decls.map(([p, v]) => [p, p.toLowerCase() !== 'src' ? v : splitTopLevel(v, ',').filter((src) => {
          const named = [];
          mapUrls(src, (u) => { named.push(resolveInTree(file, u)); return null; });
          if (!named.some((path) => local.has(path))) return true;
          if (isCarried || !named.every((path) => path === best || !local.has(path))) return false;
          isCarried = true;
          return true;
        }).join(',')]).filter(([, v]) => v !== '').map(([p, v]) => p + ':' + v).join(';') + '}\\n';
        if (join.ownRules.has(under + best + rule)) continue;
        join.ownRules.add(under + best + rule);
        out += rebase(join, rule, file);
        continue;
      }
    }
    // The address in an @namespace is a name: nothing is loaded from it.
    out += at === 'namespace' ? css.slice(s.start, s.end) : rebase(join, css.slice(s.start, s.end), file);
    // An at-rule that the end of the file completes: what it leaves open is closed first, then the rule itself.
    if (s.by === '') out += closers(out) + ';';
  }
  open.delete(file);
  return out + closers(out);
}

// tree: { has(path), text(path), bytes(path) } over the build folder's files.
// css is '' when there is nothing to load. fonts are the plain @font-face rules,
// taken out of css for tokens.json, from which the page writes its own rules.
// used: files whose content now sits inside css. spare: font files a face names
// and no page will need, such as the .woff beside a .woff2.
export function joinStylesheets(tree, entry = 'styles.css') {
  const join = {
    tree, remote: new Set(), fonts: new Map(), ownRules: new Set(), used: new Set(), spare: new Set(), warnings: new Set(),
    uris: new Map(), carriedBytes: 0, open: new Set(), done: new Set(), joinedBytes: 0,
  };
  const { fonts, used, spare } = join;
  if (!tree.has(entry)) return { css: '', fonts: [], used, spare, warnings: [] };
  const body = expand(join, entry, '').trim();
  // A page that pastes the sheet into a <style> must not find the tag's end in it.
  // The escaped slash reads the same in a string, a url() and a comment.
  const css = [...join.remote, body].filter(Boolean).join('\\n').replace(/<\\/(?=style)/gi, '<\\\\/');
  for (const f of fonts.values()) spare.delete(f.file);
  for (const p of used) spare.delete(p);
  return { css: css ? css + '\\n' : '', fonts: [...fonts.values()], used, spare, warnings: [...join.warnings] };
}
