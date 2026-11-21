<!--
name: 'Data: layout-preflight.mjs'
description: >-
  design-sync artifact-road lib/layout-preflight.mjs checking laid-out files
  before publish, extracted with the skill for the model.
ccVersion: 2.1.330
-->
// Checks the files laid out for a Design System artifact. The service that
// stores an artifact judges a publish call as a whole: one file it will not take
// refuses every file sent with it, often after all have been uploaded. So its
// rules, and those of the artifact's page, are applied here first, file by file.

import { inMib, quoted, SHEET_MAX_BYTES, UNSEEN } from './layout-css.mjs';

const MIB = 1024 * 1024;
export const LIMITS = {
  files: 4080, // the 4,096 the service lets one version hold, less the 16 kept for the artifact type's own files
  filesEditable: 1008, // past this the artifact's page shows a system but refuses to save an edit to it
  totalBytes: 256 * MIB,
  fileBytes: SHEET_MAX_BYTES, // the service's lowest limit for any kind of file is 16 MiB; this leaves a margin
  pathChars: 300,
  sections: 24, // further .md files the page shows as sections of their own
};

// A page or a type file is only ever read as text, so it goes as text/plain and
// cannot be opened as a live document at the artifact's own address.
const TYPES = new Map(Object.entries({
  html: 'text/plain', ts: 'text/plain', md: 'text/markdown', txt: 'text/plain',
  js: 'text/javascript', css: 'text/css', json: 'application/json',
  woff2: 'font/woff2', woff: 'font/woff', ttf: 'font/ttf', otf: 'font/otf',
}));
export function contentTypeOf(path) {
  return path.includes('.') ? TYPES.get(path.slice(path.lastIndexOf('.') + 1).toLowerCase()) ?? null : null;
}

// Names that tools and coding agents load by themselves from a working folder.
const TOOL_FILES = new Set(['package.json', 'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'bun.lock', 'bun.lockb', 'bunfig.toml', 'tsconfig.json', 'jsconfig.json', 'deno.json', 'deno.jsonc', 'claude.md', 'claude.local.md', 'agents.md', 'agent.md', 'gemini.md']);
const LOOKALIKE = /[\\u00a0\\u1680\\u2000-\\u200a\\u202f\\u205f\\u3000\\u2215\\u2044\\uff0f]/; // characters that look like a space or like "/"
const DEVICE = /^(?:con|prn|aux|nul|com[0-9\\u00b9\\u00b2\\u00b3]|lpt[0-9\\u00b9\\u00b2\\u00b3]|conin\\$|conout\\$) *(?:\\..*)?$/;

// The name a less exact file system would store a path part under: characters
// that do not show dropped, accents composed, case folded, trailing dots and
// spaces stripped. A name is judged by this form, so "CLAUDE.md" cannot pass
// with a hidden character in it.
export function foldName(part) {
  return part.replace(UNSEEN, '').normalize('NFC').toUpperCase().toLowerCase().replace(/[. ]+$/, '');
}

function pathProblem(path) {
  if (path.length > LIMITS.pathChars) return 'its path is longer than ' + LIMITS.pathChars + ' characters. Shorten it.';
  if (path.search(UNSEEN) >= 0 || LOOKALIKE.test(path)) return 'its path holds a character that does not show, or a lookalike of a space or of "/". Rename it.';
  if (/[%;:\\\\?#]/.test(path)) return 'its path holds one of % ; : \\\\ ? #, which an artifact path may not hold. Rename it.';
  const parts = path.split('/');
  const folded = parts.map(foldName);
  if (parts.some((s) => s === '' || s === '..') || folded.some((s) => s === '' || s.startsWith('.'))) return 'a part of its path is empty, "..", or starts with a dot. Rename it.';
  if (parts.some((s) => /[. ]$/.test(s)) || folded.some((s) => /~\\d/.test(s))) return 'a part of its path ends in a dot or a space, or looks like a Windows short name (NAME~1). Rename it.';
  if (folded.some((s) => s === '__proto__' || s === 'constructor' || s === 'prototype' || DEVICE.test(s))) return 'a part of its path is a name reserved by JavaScript or by Windows. Rename it.';
  if (folded.includes('node_modules') || TOOL_FILES.has(folded.at(-1))) return 'it has the name of a file or folder that tools and coding agents load by themselves. ' + (path.startsWith('guidelines/') ? 'The build copied it as a guideline: list the guidelines to keep under guidelinesGlob in .design-sync/config.json (a glob there cannot leave one file out), and build again.' : 'Rename it.');
  return null;
}

const SIGNATURE = /^(?:%PDF-|%!PS-Adobe-|BM|GIF8[79]a|ID3|OTTO|ttcf|wOFF|wOF2|FORM[^]{4}AIFF|RIFF[^]{4}(?:AVI |WAVE|WEBP))/;

function contentProblem(type, bytes) {
  if (bytes.length > LIMITS.fileBytes) return 'it is ' + inMib(bytes.length) + '; one file may be at most ' + inMib(LIMITS.fileBytes);
  if (type.startsWith('font/')) return ['wOF2', 'wOFF', 'OTTO', 'true', '\\u0000\\u0001\\u0000\\u0000'].includes(bytes.subarray(0, 4).toString('latin1')) ? null : 'its bytes are not those of a font file';
  if ((bytes[0] === 0xff && bytes[1] === 0xfe) || (bytes[0] === 0xfe && bytes[1] === 0xff)) return 'it is UTF-16 text. Save it as UTF-8.';
  let text;
  try { text = new TextDecoder('utf-8', { fatal: true }).decode(bytes); } catch { return 'it is not valid UTF-8 text. Save it as UTF-8.'; }
  const REMOVE = ', which the service that stores artifacts refuses. Remove it from the file of the library this was made from, and build again.';
  if (text.includes('\\uFFFD')) return 'it holds the replacement character U+FFFD (the mark of text damaged by an earlier conversion)' + REMOVE;
  if (/[\\u0000\\u001b]/.test(text)) return 'it holds a NUL or ESC character' + REMOVE;
  if (type !== 'text/javascript' && type !== 'text/css') return null;
  // The service looks at the start of a script or stylesheet for signs that it is some other kind of file.
  if (text.trimStart().startsWith('<')) return 'it starts with "<", so it would be taken for markup';
  const head = bytes.subarray(0, 512);
  const lead = head.subarray(0, 16).toString('latin1');
  const bom = head[0] === 0xef && head[1] === 0xbb && head[2] === 0xbf;
  if (/^[^]{4}ftyp[^]{4}/.test(lead) || (!bom && (SIGNATURE.test(lead) || (head[34] === 0x4c && head[35] === 0x50)))) return 'its first bytes are the mark of a picture, sound, font or document file, ("BM", "GIF89a", or "LP" at bytes 35 and 36, say), so it would be taken for one. Start the file of the library it came from with a comment (for tokens.css, pass another --title), and build again.';
  if (!bom && head.some((b) => b <= 0x08 || b === 0x0b || (b >= 0x0e && b <= 0x1a) || (b >= 0x1c && b <= 0x1f))) return 'it holds a control character in its first 512 bytes' + REMOVE;
  return null;
}

export function isSection(path) {
  return /\\.md$/i.test(path) && path !== 'README.md' && !/^(?:components|assets|fonts|archived)\\//.test(path);
}

// files: Map of path under project/ to Buffer. Any error means nothing may be published.
export function preflight(files) {
  const errors = [];
  const warnings = [];
  const folded = new Map();
  let total = 0;
  for (const [path, bytes] of files) {
    total += bytes.length;
    const type = contentTypeOf(path);
    const key = path.split('/').map(foldName).join('/');
    if (folded.has(key)) errors.push('[NAME_CLASH] ' + quoted(path) + ' and ' + quoted(folded.get(key)) + ' are the same name to a file system that ignores case, hidden characters or trailing dots. Rename one.');
    folded.set(key, path);
    const bad = pathProblem(path) ?? (type === null ? 'an artifact cannot serve a file with this ending' : contentProblem(type, bytes));
    if (bad !== null) errors.push('[FILE_REFUSED] ' + quoted(path) + ': ' + bad);
  }
  for (const [key, path] of folded) {
    for (let at = key.lastIndexOf('/'); at > 0; at = key.lastIndexOf('/', at - 1)) {
      if (folded.has(key.slice(0, at))) errors.push('[NAME_CLASH] ' + quoted(folded.get(key.slice(0, at))) + ' is a file, and ' + quoted(path) + ' needs a folder of the same name. Rename one.');
    }
  }
  if (files.size > LIMITS.files) errors.push('[TOO_MANY_FILES] ' + files.size + ' files; one design system may hold at most ' + LIMITS.files);
  else if (files.size > LIMITS.filesEditable) warnings.push('[MANY_FILES] ' + files.size + ' files. The artifact\\'s page cannot save a design system of more than ' + LIMITS.filesEditable + ' files, so this one can be viewed there but not edited');
  if (total > LIMITS.totalBytes) errors.push('[TOO_LARGE] ' + inMib(total) + ' in all; one design system may hold at most ' + inMib(LIMITS.totalBytes));
  const sections = [...files.keys()].filter(isSection).length;
  if (sections > LIMITS.sections) warnings.push('[MANY_SECTIONS] ' + sections + ' guideline files; the page shows the first ' + LIMITS.sections + ' as sections and lists the rest under Files');
  return { errors, warnings };
}
