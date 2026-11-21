<!--
name: 'Data: publish-plan.mjs'
description: >-
  design-sync artifact-road lib/publish-plan.mjs working out the calls a sync
  makes, extracted with the skill for the model.
ccVersion: 2.1.330
-->
// Works out what a sync sends to a Design System artifact on claude.ai. Nothing
// here touches the disk or the network: artifact-publish.mjs reads the files,
// and Claude makes the calls this module lays out.

import { createHash } from 'node:crypto';
import { shown } from './layout-css.mjs';

export const INDEX = 'project/design-system.json';
export const RECORD = 'project/_ds_sync.json';
// One publish call: the stricter of what the service takes and what the
// artifact type's own instructions ask writers to stay under.
export const CALL_LIMITS = { paths: 256, bytes: 16 * 1024 * 1024 };
// The record is read back through the conversation, so it keeps the start of each hash: 128 bits, since anyone who can
// edit the artifact chooses what is hashed, and with fewer could search for a change that reads as none.
const SHORT = 32;

// How a command of artifact-publish.mjs ends short of its goal. tag and which pick the statement it prints. data holds
// values of the scripts' own making, theirs lists of text that other people wrote: neither is ever put into a sentence.
export class Told extends Error {
  constructor(tag, { which = '', data = {}, theirs = {} } = {}) {
    super(tag);
    Object.assign(this, { tag, which, data, theirs });
  }
}

// A saved answer that cannot be used, so that it has to be fetched again. why: one word from a fixed list.
export class Need extends Told {
  constructor(why, theirs = {}) {
    super('NEEDS_ANSWERS', { data: { why }, theirs });
  }
}

const BASE58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz';
const UUID = '[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}';
// The two kinds of link the service takes. On claude.ai's own hosts the id ends the path segment after /artifact/,
// /code/artifact/ or /code/frame/, behind a title if there is one. Or the id begins the host that serves the content.
const LINKS = [
  new RegExp('^(?<before>https://(?:preview\\\\.)?(?:claude\\\\.ai|claude\\\\.com)/(?:code/(?:artifact|frame)|artifact)/)(?:[A-Za-z0-9_-]*-)?(?<id>' + UUID + '|[1-9A-HJ-NP-Za-km-z]{22})(?<after>)(?<tail>(?:[/?#].*)?)$'),
  new RegExp('^(?<before>https://)(?<id>' + UUID + ')(?<after>\\\\.frame\\\\.claudeusercontent\\\\.com)(?<tail>(?:[/?#].*)?)$'),
];

// Whether the path after the id could lead a browser to another artifact. The service's rule, a little stricter: a
// segment that is "." or "..", that holds a slash, a backslash or a control character once decoded, or does not decode.
function leadsElsewhere(tail) {
  return tail.split(/[?#]/)[0].split('/').some((segment) => {
    try { return /^\\.{1,2}$|[/\\\\\\x00-\\x1f\\x7f]/.test(decodeURIComponent(segment)); } catch { return true; }
  });
}

// The parts of a bare UUID or of a link the service takes: what stands before the id, the id, what follows it. Else null.
function partsOf(text) {
  // Case counts in a short id, and not in the scheme and the host.
  const link = text.trim().replace(/^[^/?#]*\\/\\/[^/?#]*/, (origin) => origin.replace(/[A-Z]/g, (letter) => letter.toLowerCase()));
  // A longer link would be cut short where it is shown to the person.
  if (link.length > 300 || /[\\x00-\\x1f\\x7f]/.test(link)) return null;
  const parts = (new RegExp('^(?<id>' + UUID + ')$').exec(link) ?? LINKS.map((form) => form.exec(link)).find(Boolean))?.groups;
  return !parts || leadsElsewhere(parts.tail ?? '') ? null : parts;
}

// The link in text with nothing around its id but the site: a title before the id and a tail after it can be worded at will.
// Null if text is no link that slugIn reads.
export function plainLink(text) {
  const parts = slugIn(text) === null ? null : partsOf(text);
  return parts?.before ? parts.before + parts.id + parts.after : null;
}

// The UUID that a slug or a link names, or null. A link's short id is the UUID's 128 bits in base58, most significant
// digit first: the service keeps that spelling for good, since links already handed out hold it.
export function slugIn(text) {
  const { id = '' } = partsOf(text) ?? {};
  if (id.length !== 22) return id.toLowerCase() || null;
  let bits = 0n;
  for (const digit of id) bits = bits * 58n + BigInt(BASE58.indexOf(digit));
  return bits >> 128n ? null : bits.toString(16).padStart(32, '0').replace(/^(.{8})(.{4})(.{4})(.{4})/, '$1-$2-$3-$4-');
}

export function sha256(bytes) {
  return createHash('sha256').update(bytes).digest('hex');
}

function isObject(value) {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

function parsed(text) {
  try { return JSON.parse(text); } catch { return undefined; }
}

// The JSON object in what was saved from a tool's answer. It may stand alone,
// have the tool's own words or a wrapper tag around it, or sit in the list of
// content blocks that an answer too long for the conversation is saved as.
export function savedObject(text) {
  const whole = parsed(text);
  if (isObject(whole)) return whole;
  if (Array.isArray(whole)) return whole.map((block) => savedObject(String(block?.text ?? ''))).find(isObject) ?? null;
  const inner = parsed(text.slice(text.indexOf('{'), text.lastIndexOf('}') + 1));
  return isObject(inner) ? inner : null;
}

// Each text, then its other spellings, one at a time: a stored file can be large.
function* spellings(texts, respell) {
  for (const text of texts) {
    yield text;
    yield* respell(text);
  }
}

// What stands between read_file's tag and its closing tag, or the text as it is. Only the first tag is tried.
function insideTag(text) {
  const open = /<(untrusted-document[^>\\s<]{0,64})>\\n?/.exec(text);
  const end = open ? text.indexOf('</' + open[1] + '>', open.index + open[0].length) : -1;
  return end < 0 ? text : text.slice(open.index + open[0].length, end);
}

// The stored file's own text, recovered from what was saved of read_file's answer, or null if that is some other
// text (an older copy merged into the index would undo what people did since). The listing's hash is the judge, so
// each harmless difference is tried: content blocks or a tag round it, read_file's backslashes, a last newline, line ends, a BOM.
export function storedText(saved, hash) {
  const blocks = parsed(saved);
  let tries = spellings([saved], () => (Array.isArray(blocks) ? blocks.slice(0, 16).map((block) => String(block?.text ?? '')) : []));
  tries = spellings(tries, (text) => [insideTag(text)]);
  tries = spellings(tries, (text) => [text.replace(/<\\\\/g, '<').replace(/^([ \\t]*(?:Human|Assistant)[ \\t]*)\\\\:/gim, '$1:')]);
  tries = spellings(tries, (text) => [text + '\\n', text.replace(/\\n$/, ''), text + '\\n\\n']);
  tries = spellings(tries, (text) => [text.replace(/\\r?\\n/g, '\\r\\n')]);
  tries = spellings(tries, (text) => ['\\ufeff' + text]);
  for (const text of tries) if (sha256(text) === hash) return text;
  return null;
}

// list_files' answer as { version, read, files, typeFiles, content, owned, stateTitle }; throws Need if it is not that, or is of
// another artifact. files: its own paths to their sha256 ('' where none is given). typeFiles: the paths marked of_type,
// which no one can change. read: who it is shared with, as the answer says it. content: the answer's "content" object, or
// null. owned: false where the answer says owned_by_user false, which it says to no owner; else true. stateTitle: null
// for an owner, whose publish call is refused for stating the artifact's title where the tool doesn't list them that
// argument. Anyone else's has to state it, exactly: for them, the title the answer gives, or { missing } where it gives
// none that can be sent. 'withheld': its title can't be sent, or it says why it has none. 'none': it has neither a title as
// text nor title_withheld, which is what the service answers while it takes files only from the owner.
export function readListing(text, slug) {
  const listing = savedObject(text);
  if (!Array.isArray(listing?.files) || typeof listing.version !== 'string' || !/^[\\w.:-]{1,128}$/.test(listing.version) || typeof listing.slug !== 'string') {
    throw new Need('notAListing');
  }
  if (listing.slug !== slug) throw new Need('otherArtifact', { listedSlug: [listing.slug] });
  // list_files gives "read" for an artifact made from a type, unless its sharing was never set. Without it, nothing says who would see what is sent.
  if (typeof listing.read !== 'string' || listing.read === '') throw new Need('noReadValue');
  // It is an object or it is left out. In any other form the copy went wrong, and what it said of the type is not known.
  if (listing.content !== undefined && !isObject(listing.content)) throw new Need('contentNotAnObject');
  const files = new Map();
  const typeFiles = new Set();
  for (const row of listing.files) {
    if (typeof row?.path !== 'string' || !/^(?:[0-9a-f]{64})?$/.test(row.sha256 ?? '')) {
      throw new Need('badRow', { row: [JSON.stringify(row)] });
    }
    if (row.of_type === true) typeFiles.add(row.path);
    else files.set(row.path, row.sha256 ?? '');
  }
  const hasTitle = typeof listing.title === 'string' && listing.title !== '';
  // title_withheld, where present, says why there is no title. An empty title, or one with a control character or a line or
  // paragraph separator, counts as withheld too: stricter than the service, which lets a tab and a line break through.
  const stateTitle = listing.owned_by_user !== false ? null
    : listing.title_withheld || listing.title === '' || (hasTitle && /[\\p{Cc}\\p{Zl}\\p{Zp}]/u.test(listing.title)) ? { missing: 'withheld' }
      : hasTitle ? listing.title : { missing: 'none' };
  return { version: listing.version, read: listing.read, files, typeFiles, content: listing.content ?? null, owned: listing.owned_by_user !== false, stateTitle };
}

// Text on one line, of no more than max characters, with no character in it that is not seen or that stands for a
// broken one (U+FFFD, half of a pair), which an artifact's files may not hold.
export function isShown(text, max) {
  return shown(text, max) === text && !/[\\ufffd\\p{Cs}]/u.test(text);
}

function pathTable(value) {
  if (!isObject(value)) return {};
  return Object.fromEntries(Object.entries(value).filter(([path, hash]) => typeof hash === 'string' && /^[0-9a-f]{32}$/.test(hash) && !path.split('/').includes('..') && isShown(path, 300)));
}

const isHash = (value) => typeof value === 'string' && /^[0-9a-f]{8,64}$/.test(value);
const isTableOf = (key) => (value) => isObject(value) && Object.entries(value).every(([name, hash]) => key.test(name) && isHash(hash));
// A component's name as artifact-layout.mjs takes one, and the three files package-build.mjs hashes for each component.
const NAME = /^(?!(?:__proto__|constructor|prototype)$)[A-Za-z_$][A-Za-z0-9_$]{0,63}$/;
const SOURCE = /^components\\/[a-z0-9-]{1,100}\\/([A-Za-z_$][A-Za-z0-9_$]{0,63})\\/\\1\\.(?:jsx|d\\.ts|prompt\\.md)$/;
// The keys package-build.mjs writes, each with the form it gives them.
const BUILD_KEYS = {
  shape: (value) => value === 'package' || value === 'storybook',
  styleSha: isHash, scriptsSha: isHash, auxSha: isHash, bundleSha12: isHash,
  keyRecipe: (value) => Number.isSafeInteger(value),
  renderHashes: isTableOf(NAME), sourceKeys: isTableOf(NAME), sourceHashes: isTableOf(SOURCE),
};

// The record, or null if it is no JSON object. files: what the last finished sync left in the artifact; pending: what
// one that stopped halfway had sent; removing: what the last sync was to remove; all without project/. build: the
// build's own keys, which anyone who can edit the artifact can write and which go on to other scripts: if one is not as
// a build writes it, the record is foreign.
export function readRecord(text) {
  const record = savedObject(text);
  if (record === null) return null;
  const known = Object.entries(record).filter(([key]) => Object.hasOwn(BUILD_KEYS, key));
  const build = Object.fromEntries(known);
  // A build hashes a .jsx for every component it names.
  const hashed = new Set(Object.keys(build.sourceHashes ?? {}).filter((path) => path.endsWith('.jsx')).map((path) => path.split('/')[2]));
  const isForeign = !known.every(([key, value]) => BUILD_KEYS[key](value)) ||
    [...Object.keys(build.renderHashes ?? {}), ...Object.keys(build.sourceKeys ?? {})].some((name) => !hashed.has(name));
  return { build: isForeign ? {} : build, isForeign, files: pathTable(record.artifact?.files), pending: pathTable(record.artifact?.pending), removing: pathTable(record.artifact?.removing) };
}

// Turns a Map of path to sha256 into the record's table: paths without project/, hashes cut to their first 32 digits.
export function recordTable(hashes) {
  return Object.fromEntries([...hashes].map(([path, hash]) => [path.slice('project/'.length), hash.slice(0, SHORT)]).sort());
}

// build: the keys of the build's own _ds_sync.json, which a later sync reads to
// skip what was verified. Holds no time, so the same build gives the same bytes.
export function writeRecord(build, files, pending, removing) {
  return JSON.stringify({ ...build, artifact: { v: 1, files, ...(pending ? { pending } : {}), ...(Object.keys(removing).length ? { removing } : {}) } }, null, 1) + '\\n';
}

function recorded(table, path) {
  const key = path.slice('project/'.length);
  return path.startsWith('project/') && Object.hasOwn(table, key) ? table[key] : undefined;
}

// Whether an earlier sync, finished or not, put the file there and means it to be there.
function isKept(record, path) {
  return recorded(record.files, path) !== undefined || recorded(record.pending, path) !== undefined;
}

// Whether an earlier sync put the file there. What one was to remove is its own until it is gone.
function isOwned(record, path) {
  return isKept(record, path) || recorded(record.removing, path) !== undefined;
}

// Whether someone else has since changed a file that a sync put there: it is neither what the last finished sync left,
// nor what an unfinished one had sent, nor what one was to remove; or it is gone though a sync meant it to stay.
function isChangedThere(record, path, theirs) {
  if (theirs === undefined) return isKept(record, path);
  const known = [recorded(record.files, path), recorded(record.pending, path), recorded(record.removing, path)].filter((hash) => hash !== undefined);
  return known.length > 0 && !known.some((hash) => theirs.startsWith(hash));
}

// Files that a sync to claude.ai/design, or that app's compiler, writes to every synced project, whatever the build holds:
// the compiled bundle and list of cards, and what the preview cards load.
const OLD_SYNC_NAMES = /^project\\/(?:_ds_bundle\\.js|_ds_bundle\\.css|_ds_manifest\\.json|(?:components\\/)?(?:_vendor|_preview)\\/.+)$/;
// What a sync sends to claude.ai/design of a build (the "Writes" list in that road's texts, less its record and sentinel).
const OLD_SYNC_SENDS = /^(?:(?:components|tokens|fonts|guidelines|_vendor|_preview)\\/.+|_ds_bundle\\.js|_ds_bundle\\.css|styles\\.css|README\\.md)$/;

// The paths, as an artifact has them after a move, of a build's files as a sync sent them to claude.ai/design.
// built: the paths of the files in ds-bundle/.
export function oldLayoutOf(built) {
  return new Set(built.filter((path) => OLD_SYNC_SENDS.test(path)).map((path) => 'project/' + path));
}

// ours, theirs: Maps of path to sha256, without the index and the record. The repo's files replace the artifact's where
// they differ. Of the files only the artifact has, those a sync put there are removed and the rest are left alone.
// changedThere names each replaced or removed file that someone changed there.
// oldLayout: null, or, for an artifact still as the move left it, moved from the project this repo synced to on
// claude.ai/design, oldLayoutOf this build. A move keeps nearly every file's path and brings no record. So a file there
// counts as an earlier sync's, and is removed, if its path is in oldLayout or matches OLD_SYNC_NAMES: beside this build it
// would be a second, older copy of it.
export function compare(ours, theirs, record, oldLayout = null) {
  const push = [...ours.keys()].filter((path) => ours.get(path) !== theirs.get(path));
  const onlyThere = [...theirs.keys()].filter((path) => !ours.has(path));
  const movedToRemove = oldLayout === null ? [] : onlyThere.filter((path) => !isOwned(record, path) && (oldLayout.has(path) || OLD_SYNC_NAMES.test(path)));
  const remove = [...onlyThere.filter((path) => isOwned(record, path)), ...movedToRemove];
  return {
    push,
    remove,
    changedThere: [...push, ...remove].filter((path) => isChangedThere(record, path, theirs.get(path))),
    // About to be replaced, though no sync put them there.
    notOursToReplace: push.filter((path) => theirs.has(path) && !isOwned(record, path)),
    // About to be removed, though no record says that a sync put them there.
    movedToRemove,
    leftAlone: onlyThere.filter((path) => !remove.includes(path)),
  };
}

// "editing" in the index of a system that is synced from code: its page on
// claude.ai is read-only, and writes nothing over what a sync sent.
export const SYNCED_FROM_CODE = 'code';
// "editing" in the index of a system as a move from claude.ai/design left it: nearly every file is where it was there, and its
// page shows the README and the list of files, and lets nobody edit. A clean-up on claude.ai takes the entry out.
export const AS_MOVED = 'off';

// The artifact's index from its stored text (null: it has none), refused if a
// sync may not write over it. syncedTo: the claude.ai/design project that the repo's config names, or null.
export function readLiveIndex(text, syncedTo = null) {
  if (text === null) return null;
  const live = savedObject(text);
  if (live === null) throw new Told('INDEX_UNREADABLE');
  if (!isObject(live.createdOnFiles) && !isObject(live.convertedFrom)) {
    throw new Told('INDEX_UNMARKED');
  }
  if (live.editing !== undefined && live.editing !== SYNCED_FROM_CODE && live.editing !== AS_MOVED) {
    throw new Told('EDITING_UNKNOWN');
  }
  // A move writes down which project it brought over, if it was told, and a sync keeps that.
  const movedFrom = live.source?.projectId;
  if (syncedTo !== null && typeof movedFrom === 'string' && !isMovedFrom(live, syncedTo)) {
    throw new Told('MOVED_FROM_ELSEWHERE', { theirs: { movedFrom: [movedFrom], repoSyncedTo: [syncedTo] } });
  }
  return live;
}

// Whether the index says that the system was moved here from this claude.ai/design project.
export function isMovedFrom(live, projectId) {
  const movedFrom = live?.source?.projectId;
  return typeof movedFrom === 'string' && typeof projectId === 'string' && movedFrom.toLowerCase() === projectId.toLowerCase();
}

// Of the files an artifact holds, those its page shows as sections of their
// own, in the order the page lists them in the index.
export function sectionsOf(paths) {
  return paths.filter((path) => /^project\\/(?!README\\.md$|(?:components|assets|fonts|archived)\\/)/.test(path) && /\\.(?:mdx?|markdown)$/i.test(path)).sort();
}

// The index is merged, never replaced: people and the artifact's page keep things in it. Only these are set: editing,
// namespace, libraries, docs.readme, a title if it has none, and docs.sections, from the sections argument (the page
// works the same list out from the files). And, in a system that was moved here, source.upgradedAt (the at argument) if
// it has none: the Design System type's mark that a moved system now has the type's own layout. Without it, a later move
// takes the system for one that nobody has touched since the last.
export function mergeIndex(built, live, sections, at) {
  if (live === null) return { ...built, editing: SYNCED_FROM_CODE, docs: { ...built.docs, sections } };
  return {
    ...live,
    ...(isObject(live.source) && live.source.upgradedAt == null ? { source: { ...live.source, upgradedAt: at } } : {}),
    editing: SYNCED_FROM_CODE,
    namespace: built.namespace,
    libraries: built.libraries,
    docs: { ...(isObject(live.docs) ? live.docs : {}), readme: built.docs.readme, sections },
    ...(typeof live.title === 'string' ? {} : { title: built.title }),
  };
}

const KINDS = [
  [/^fonts\\//, 'font'],
  [/^components\\/lib\\//, 'library'],
  [/^components\\/bundle\\.js$/, 'bundle'],
  [/^components\\/bundle\\.css$/, 'stylesheet'],
  [/^components\\/index\\.d\\.ts$/, 'types'],
  [/^components\\/[^/]+\\/preview\\.html$/, 'preview'],
  [/^components\\/[^/]+\\/README\\.md$/, 'usage note'],
  [/^tokens\\.(?:json|css)$/, 'tokens'],
  [/^guidelines\\//, 'guideline'],
  [/^README\\.md$/, 'readme'],
  [/^design-system\\.json$/, 'index'],
  [/^_ds_sync\\.json$/, 'record'],
];

// What a published file is, in a word, for a person reading the list of them.
export function kindOf(path) {
  return KINDS.find(([pattern]) => pattern.test(path.slice('project/'.length)))?.[1] ?? 'other';
}

function sortedKeys(key, value) {
  return isObject(value) ? Object.fromEntries(Object.entries(value).sort()) : value;
}

// Whether two indexes say the same, whatever their key order. lastChange is
// left out: it holds the time, so it differs at every sync.
export function sameIndex(one, other) {
  return JSON.stringify({ ...one, lastChange: null }, sortedKeys) === JSON.stringify({ ...other, lastChange: null }, sortedKeys);
}

function emptyCall() {
  return { files: [], remove: [], bytes: 0 };
}

function fits(call, count, bytes, limits) {
  return call.files.length + call.remove.length + count <= limits.paths && call.bytes + bytes <= limits.bytes;
}

function sizeOf(entries) {
  return entries.reduce((sum, entry) => sum + entry.size, 0);
}

// The publish calls for entries (files { as, path, size }, then removals { as, size: 0 }) and last (the index and the
// record, which close a sync). If all of it fits in one call, the artifact changes at once. Otherwise, while entries are
// left, last waits for the next plan (isWhole false), and each call keeps room for a journal of up to journalBytes.
// after: removals that go with last or after it, never before, so that the old index is never left naming files that are
// gone. They may take further calls, and don't keep last waiting.
export function planCalls(entries, last, journalBytes, limits = CALL_LIMITS, after = []) {
  // With nothing else left to send, last goes whatever its size: waiting for a next plan would never end.
  const isWhole = entries.length === 0 || fits(emptyCall(), entries.length + last.length, sizeOf(entries) + sizeOf(last), limits);
  const room = isWhole ? limits : { paths: limits.paths - 1, bytes: limits.bytes - journalBytes };
  const calls = [emptyCall()];
  const put = (entry) => {
    if (entry.path === undefined) calls.at(-1).remove.push(entry.as);
    else calls.at(-1).files.push({ as: entry.as, path: entry.path });
    calls.at(-1).bytes += entry.size;
  };
  const late = new Set(after);
  for (const entry of isWhole ? [...entries, ...last, ...after] : entries) {
    // A file larger than the limit still goes, in a call of its own.
    const isEmpty = calls.at(-1).files.length + calls.at(-1).remove.length === 0;
    if (!isEmpty && !fits(calls.at(-1), 1, entry.size, room)) {
      calls.push(emptyCall());
      // It is not known whether the service takes a call that sends no file, so the record goes once more, unchanged.
      if (late.has(entry)) put(last.at(-1));
    }
    put(entry);
  }
  return { isWhole, calls: calls.map(({ files, remove }) => ({ files, remove })) };
}
