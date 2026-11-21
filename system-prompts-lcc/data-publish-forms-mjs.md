<!--
name: 'Data: publish-forms.mjs'
description: >-
  design-sync artifact-road lib/publish-forms.mjs normalising the two tool sets'
  listings and call forms, extracted with the skill for the model.
ccVersion: 2.1.330
-->
// A session reaches an artifact through one of two sets of tools, and they differ in two things a script meets: how a
// listing of the artifact's files reads, and which arguments a publish call takes. This module reads either listing
// into one shape and writes a call in either form. It names no tool: the skill text says which calls to make.
// 'json': the listing is a JSON object, and a call names the version it builds on.
// 'text': the listing is a sentence, with the service's own list of the files beside it, and a call maps each published
// path to a file on this machine.

import { contentTypeOf } from './layout-preflight.mjs';
import { CALL_LIMITS, INDEX, Need, readListing, RECORD, slugIn, Told } from './publish-plan.mjs';

// One publish call in each form. In the 'text' form the tool takes 255 entries, removals among them, and counts the
// file that is named apart from the map a second time.
export const LIMITS = { json: CALL_LIMITS, text: { ...CALL_LIMITS, paths: 254 } };
// The most rows the tool's listing shows. A publish may remove a file only if the session has seen it listed or has read it,
// so an artifact that holds more can't be synced with this tool.
export const TEXT_ROWS_SHOWN = 1024;

const QUOTED = '"(?:[^"\\\\\\\\]|\\\\\\\\.)*"';
const SHARED_WITH = new Map([['your organization', 'org'], ['specific users', 'users'], ['anyone with the link', 'public']]);
// What the line says of the person's grant, as [canWrite, owned]. An older build of the tool says nothing of who owns the artifact.
const GRANT = new Map([['the user owns it', [true, true]], ['the user can publish to it but does not own it', [true, false]],
  ['the user can publish to it', [true, null]], ['the user can read it but not publish to it', [false, false]]]);
// The line that opens the tool's listing, as far as it is read. A notice may stand above it, and the rows below it are not read. The type and what stands in brackets after it are left out where the tool has nothing to say.
const HEAD = new RegExp('^Published files of (?<url>\\\\S+) \\\\(version (?<version>[\\\\w.:-]{1,128})\\\\)' +
  '(?<typed>, an Artifact (?:of type (?<type>' + QUOTED + ')|made from a type))?' +
  '(?: \\\\((?<access>[^\\\\n]{1,300}?)\\\\))?' +
  '(?:, (?<count>\\\\d{1,6}) files? by path\\\\b|: none\\\\b)', 'm');

// What was saved of a tool's answer, as one text: as it is, or the texts of the list of content blocks that an answer
// too long for the conversation is saved as.
function savedText(saved) {
  let blocks;
  try { blocks = JSON.parse(saved); } catch { return saved; }
  return Array.isArray(blocks) ? blocks.map((block) => String(block?.text ?? '')).join('\\n') : saved;
}

function unquoted(text) {
  try { return JSON.parse(text); } catch { return null; }
}

// A 'text' listing in the shape readListing gives, with url, the artifact's link as the tool spells it. It is read from
// two things: the line that opens the tool's listing, and the service's own list of the version's files,
// { ver, files: { path: { sha256 } } }, which the tool saves as a file (list: its text, or null if it was not saved).
// Throws Need if either is not that, the line is of another artifact or the list of another version, the line does not
// say who can open the artifact, or the list leaves files out; Told where the artifact was made from no type, or holds more files than the tool shows.
function readTextListing(text, list, slug) {
  const head = HEAD.exec(text)?.groups;
  if (!head) throw new Need('notAListing');
  if (slugIn(head.url) !== slug) throw new Need('otherArtifact', { listedSlug: [head.url] });
  // Checked before access: a single page's line names no type and no access.
  if (!head.typed) throw new Told('NOT_A_DESIGN_SYSTEM', { which: 'type' });
  const access = (head.access ?? '').split('; ');
  const shared = access.map((part) => /^it is (?:(private)\\b|shared with (.+)$)/.exec(part)).find(Boolean);
  if (!shared) throw new Need('noReadValue');
  const type = head.type === undefined ? null : unquoted(head.type);
  const [canWrite, owned] = access.map((part) => GRANT.get(part)).find(Boolean) ?? [null, null];
  const listing = {
    form: 'text', url: head.url, version: head.version, read: shared[1] ? 'owner' : SHARED_WITH.get(shared[2]) ?? shared[2],
    files: new Map(), typeFiles: new Set(), unnameable: [], stateTitle: null,
    canWrite, owned,
    // The tool names the type only once the service has vouched for it as one of Anthropic's own: null where it says only
    // that the artifact was made from some type.
    content: type === null ? null : { index: type === 'Design System' ? INDEX : null, type },
  };
  // The caller refuses these on the line alone, so the list of the files isn't needed.
  if (listing.canWrite === false || (listing.content !== null && listing.content.index !== INDEX)) return listing;
  if (list === null) throw new Need('noFileList');
  // A copy of a file, so it is JSON and nothing else.
  const listed = unquoted(list);
  if (typeof listed?.ver !== 'string' || listed.files === null || typeof listed.files !== 'object' || Array.isArray(listed.files)) throw new Need('notAListing');
  if (listed.ver !== head.version) throw new Need('otherVersion', { listedVersion: [listed.ver] });
  for (const [path, row] of Object.entries(listed.files)) {
    if (!/^[0-9a-f]{64}$/.test(row?.sha256 ?? '')) throw new Need('badRow', { row: [JSON.stringify([path, row])] });
    // An artifact's own files are all under project/. Whatever else is listed came with the type, or has a name the tool
    // can't give (it takes only the NFC spelling, and the other tools store what they're given): this sync leaves it alone.
    if (path.startsWith('project/') && path === path.normalize('NFC')) listing.files.set(path, row.sha256);
    else listing.typeFiles.add(path);
    // Such a name under project/ is someone's file and not the type's, so the person is told of it.
    if (path.startsWith('project/') && path !== path.normalize('NFC')) listing.unnameable.push(path);
  }
  // The service says so where it leaves files out of the list: what the caller may not see, or another artifact's files.
  if (listed.narrowed === true) throw new Need('rowsMissing');
  const holds = listing.files.size + listing.typeFiles.size;
  if (holds > TEXT_ROWS_SHOWN) throw new Told('LISTING_CUT', { data: { holds, shown: TEXT_ROWS_SHOWN } });
  return listing;
}

// A listing in the given form as { form, version, read, files, typeFiles, unnameable, content, owned, stateTitle, canWrite, url }.
// canWrite: whether the person can publish to the artifact, or null where the listing does not say. owned: whether they
// own it, or null likewise. url: null in the 'json' form. unnameable: files a sync can't reach but must report, 'text' form
// alone. list: for the 'text' form alone.
// The caller says which form it is. What was saved does not: a 'text' listing can end in a note that holds a JSON object
// of an artifact writer's making, which must not pass for a listing.
export function readListingAs(form, saved, slug, list = null) {
  const text = savedText(saved);
  if (form === 'text') return readTextListing(text, list, slug);
  // Saved under the other form's name by mistake: readListing would find that JSON object in it.
  if (HEAD.test(text)) throw new Need('notAListing');
  return { form, url: null, canWrite: null, unnameable: [], ...readListing(saved, slug) };
}

// One line per file, so that a long call can be read in parts.
function jsonCall(call) {
  const files = call.files.map((file) => '  ' + JSON.stringify(file)).join(',\\n');
  const remove = call.remove.length ? ',\\n "remove": ' + JSON.stringify(call.remove, null, 2).replace(/\\n/g, '\\n ') : '';
  const sharedWith = call.sharedWith ? ',\\n "shared_live": ' + JSON.stringify(call.sharedWith) : '';
  // It has to arrive exactly as it is, so whatever is not plain ASCII is written as an escape, which can be copied by eye.
  const title = typeof call.stateTitle === 'string' ? ',\\n "artifact_title": ' + JSON.stringify(call.stateTitle).replace(/[^\\x20-\\x7e]/g, (unit) => '\\\\u' + unit.charCodeAt(0).toString(16).padStart(4, '0')) : '';
  return '{\\n "slug": ' + JSON.stringify(call.slug) + ',\\n "base_version": ' + JSON.stringify(call.base_version) + sharedWith + title + ',\\n "mode": "patch",\\n "files": [\\n' + files + '\\n ]' + remove + '\\n}\\n';
}

// The tool wants one of the files named outside the map as well, and takes no call without one: the record, which every
// call of a sync carries. Each file goes with the type the layout gave it, so that a page is stored as plain text here too:
// left to itself, the tool would store it as a page that opens at the artifact's own address.
function textCall(call) {
  const named = call.files.find((file) => file.as === RECORD);
  if (!named) throw new Error('a call with no record in it');
  const entries = [
    ...call.files.map((file) => [file.as, { from: file.path, contentType: contentTypeOf(file.as) }]),
    ...call.remove.map((path) => [path, null]),
  ];
  const replaces = call.replaces?.length ? ',\\n "overwrite_unread": ' + JSON.stringify(call.replaces, null, 2).replace(/\\n/g, '\\n ') : '';
  return '{\\n "action": "publish",\\n "url": ' + JSON.stringify(call.url) + ',\\n "file_path": ' + JSON.stringify(named.path) + ',\\n "files": {\\n' +
    entries.map(([as, from]) => '  ' + JSON.stringify(as) + ': ' + JSON.stringify(from)).join(',\\n') + '\\n }' + replaces + '\\n}\\n';
}

// The arguments of one publish call, as the text of a file. call: { files: [{ as, path }], remove: [path] } and, for
// 'json', slug, base_version, sharedWith, stateTitle (left out unless it is a string); for 'text', url and replaces, the
// paths of this call that the artifact already holds (left out if empty).
export function callText(form, call) {
  return form === 'text' ? textCall(call) : jsonCall(call);
}
