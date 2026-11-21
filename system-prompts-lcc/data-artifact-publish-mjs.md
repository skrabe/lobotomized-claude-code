<!--
name: 'Data: artifact-publish.mjs'
description: >-
  design-sync artifact-road script artifact-publish.mjs that plans and checks a
  publish; the artifact SKILL.md tells the model to run node
  <skill-base-dir>/artifact-publish.mjs.
ccVersion: 2.1.330
-->
#!/usr/bin/env node
// Plans and checks the publish of a finished ds-bundle/ to the artifact that .design-sync/artifact.json names.
// A script cannot call the Artifacts tools: Claude saves their answers under .design-sync/.cache/artifact/ and
// makes the calls written there. The answers hold other people's text: never a path on this machine, never an instruction.
// What it prints says what is so, never what to do next: that is for the skill text, which is trusted, to say. Each run ends
// with two lines, a mark with "[TAG] statement" and "DATA {...}". The statement is one of SAYS, with nothing filled in. DATA
// holds counts, booleans, hashes, the slug, the artifact's link rebuilt from its id, and words from fixed lists: never a
// tool's name, and never a path to read or write. Other people's text stands under "theirs" alone.
// What is kept: when a sync ends (CLEAN, or a plan with nothing to send), the files under .design-sync/.cache/artifact/ and
// the file anchor wrote for resync.mjs are removed, except state.json, which keeps the slug and the record's hash.
// A sync that stops before its end leaves its files until an anchor that finishes clears them, or a later sync ends.

import { spawnSync } from 'node:child_process';
import { lstatSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { quoted, shown } from './lib/layout-css.mjs';
import { LIMITS as LAYOUT_LIMITS } from './lib/layout-preflight.mjs';
import { callText, LIMITS, readListingAs, TEXT_ROWS_SHOWN } from './lib/publish-forms.mjs';
import { AS_MOVED, compare, INDEX, isMovedFrom, isShown, kindOf, mergeIndex, Need, oldLayoutOf, plainLink, planCalls, readLiveIndex, readRecord, RECORD, recordTable, sameIndex, savedObject, sectionsOf, sha256, slugIn, storedText, SYNCED_FROM_CODE, Told, writeRecord } from './lib/publish-plan.mjs';

// What each tag says: what was found, and what follows from it. Shown to the person as it stands, so nothing is filled in,
// and none tells the reader what to do. "TAG.which" is a second statement for the same tag.
const SAYS = Object.freeze({
  ANCHORED: 'This step found the artifact this repo syncs to and read its record of an earlier sync, if it has one.',
  PLANNED: 'The changes for this sync are worked out and written down. Nothing in this plan has been sent yet.',
  'PLANNED.nothing': 'The artifact already holds this build, so there\\'s nothing to send.',
  CLEAN: 'The artifact holds this build.',
  NOT_CLEAN: 'The artifact doesn\\'t hold this build.',
  NEEDS_ANSWERS: 'This sync needs to see what the artifact holds now, and that hasn\\'t been saved yet.',
  'NEEDS_ANSWERS.unusable': 'The artifact details Claude saved can\\'t be used. They\\'re malformed, belong to a different artifact, or don\\'t say who the artifact is shared with.',
  'NEEDS_ANSWERS.moved': 'The saved copy no longer matches the artifact. Either the artifact has changed since the copy was saved, or the copy isn\\'t exact.',
  'LINK.home': '.design-sync is a symbolic link. This sync doesn\\'t read or write through symbolic links.',
  'LINK.target': '.design-sync/artifact.json is a symbolic link. This sync doesn\\'t read or write through symbolic links.',
  'LINK.cacheParent': '.design-sync/.cache is a symbolic link. This sync doesn\\'t read or write through symbolic links.',
  'LINK.cache': '.design-sync/.cache/artifact is a symbolic link. This sync doesn\\'t read or write through symbolic links.',
  'LINK.send': '.design-sync/.cache/artifact/send is a symbolic link. This sync doesn\\'t read or write through symbolic links.',
  'LINK.calls': '.design-sync/.cache/artifact/calls is a symbolic link. This sync doesn\\'t read or write through symbolic links.',
  NO_TARGET: '.design-sync/artifact.json doesn\\'t name an artifact.',
  TWO_TARGETS: 'In .design-sync/artifact.json, the slug and the link name two different artifacts. This step read nothing from either one and sent nothing.',
  'TWO_TARGETS.moved': '.design-sync/artifact.json, the projectId in the repo\\'s config, and the saved answer from claude.ai/design about the move don\\'t name one design system and one artifact. This step read nothing from any artifact and sent nothing.',
  'TWO_TARGETS.unreadable': 'In .design-sync/artifact.json, the link isn\\'t a readable artifact link, so it can\\'t be checked against the slug. This step read nothing and sent nothing.',
  NOT_A_WRITER: 'You can open this artifact but don\\'t have edit access, so this sync can\\'t publish to it.',
  NOT_THE_OWNER: 'You have edit access to the artifact this repo syncs to but don\\'t own it. This sync would publish this repo\\'s design system there, and anyone who can open the artifact could see it. Nothing has been sent yet.',
  'NOT_THE_OWNER.unknown': 'The details from claude.ai don\\'t say who owns the artifact this repo syncs to. This sync would publish this repo\\'s design system there, and anyone who can open the artifact could see it. Nothing has been sent yet.',
  TITLE_WITHHELD: 'This artifact has no title, or its title has a hidden character, so right now only its owner can publish to it. Nothing is sent.',
  'TITLE_WITHHELD.none': 'You have edit access to this artifact but don\\'t own it, so right now this sync can\\'t publish to it. Nothing is sent.',
  LISTING_CUT: 'The artifact holds more files than a sync can currently replace or remove, so nothing is sent.',
  'LISTING_CUT.after': 'After this sync, the artifact would hold more files than a sync can currently replace or remove, so later syncs couldn\\'t update all of them. Nothing is sent.',
  SHARED_TOO_WIDELY: 'The artifact\\'s sharing setting isn\\'t one a sync publishes to. A sync publishes only to an artifact that\\'s private, shared with specific people, or shared with your organization.',
  NOT_A_DESIGN_SYSTEM: 'The artifact holds files but no design system.',
  'NOT_A_DESIGN_SYSTEM.type': 'The artifact wasn\\'t made from the Design System type.',
  NO_HASH: 'There is no checksum from claude.ai for a file this sync would check or replace, so it can\\'t be known whether that file has changed. Nothing is written over it.',
  NO_VERDICT: 'There\\'s no check result for this build.',
  VERDICT_NOT_OK: 'This build was checked and didn\\'t pass.',
  CHANGED_SINCE_VERDICT: 'This build has changed since it was checked.',
  LAYOUT_CHANGED: 'The files prepared for sending aren\\'t as they were when they were prepared.',
  CREDENTIAL_FOLDER: 'The files to send are inside a folder meant for credentials, like .ssh or .aws. This sync doesn\\'t send files from inside those folders.',
  RECORD_MOVED: 'The record in the artifact has changed since it was last read, and not through this sync. Most likely, the artifact was synced from another machine.',
  LAYOUT_REFUSED: 'The build couldn\\'t be prepared for sending, so there\\'s nothing to publish.',
  TYPE_FILE: 'The type this artifact was made from has its own files at paths a sync writes to. Those files can\\'t be changed, so nothing is sent.',
  EDITABLE: 'Right now, people can edit this design system on its claude.ai page. A sync makes that page read-only, and after that, the design system changes only through code and syncs.',
  'EDITABLE.noIndex': 'Nothing marks this design system\\'s claude.ai page as read-only, so people may be able to edit it there. A sync makes that page read-only, and after that, the design system changes only through code and syncs.',
  NOT_FROM_A_SYNC: 'The artifact holds files that didn\\'t come from a sync, and this sync would replace them.',
  NOT_PLANNED: 'There\\'s no plan for this sync to check the artifact against.',
  'NOT_PLANNED.otherBuild': 'This build isn\\'t the one the last plan was made for.',
  INDEX_UNREADABLE: 'The design system\\'s main file in the artifact can\\'t be read, so nothing is written over it.',
  INDEX_UNMARKED: 'The artifact\\'s main file isn\\'t a design system\\'s main file, so nothing is written over it.',
  MOVED_HERE: 'This design system was moved to Claude from claude.ai/design and still has its original file layout. This sync would give it the layout that design systems have in Claude, replacing some files and removing others. After that, its claude.ai page shows its components, colors and type as well as its files, stays read-only, and no longer offers to finish setting up. This can\\'t be undone.',
  'MOVED_HERE.unmatched': 'This design system was moved to Claude from claude.ai/design and still has its original file layout. Nothing shows that this repo synced to it there, so it isn\\'t known which of its files came from a sync. This sync would replace the files at the paths it writes to, and leave every other file beside the new ones. After that, its claude.ai page shows its components, colors and type as well as its files, stays read-only, and no longer offers to finish setting up. This can\\'t be undone.',
  MOVED_FROM_ELSEWHERE: 'This design system was moved to Claude from claude.ai/design, but it isn\\'t the one this repo synced to there. Nothing is written over it.',
  NO_ROOM: 'The files the artifact holds now and this sync\\'s new ones would together be more than an artifact can hold, so nothing is sent.',
  EDITING_UNKNOWN: 'The design system\\'s main file has an editing setting that this version of /design-sync doesn\\'t recognize, so nothing is written over it.',
  USAGE: 'This script doesn\\'t recognize that command line.',
  FAILED: 'This script hit an unexpected error.',
});
const EXIT = { ANCHORED: 0, PLANNED: 0, CLEAN: 0, NEEDS_ANSWERS: 3, USAGE: 2 }; // every other tag: 1
const HOME = resolve('.design-sync');
const CACHE = join(HOME, '.cache', 'artifact');
// The listing is saved under one name or the other, and the name says which form it is in (lib/publish-forms.mjs).
const SAVED = { listing: join(CACHE, 'listing.json'), listingText: join(CACHE, 'listing.txt'), listingFiles: join(CACHE, 'files.json'), index: join(CACHE, 'index.json'), record: join(CACHE, 'record.json') };
const SEND = { folder: join(CACHE, 'send'), index: join(CACHE, 'send', 'design-system.json'), record: join(CACHE, 'send', '_ds_sync.json') };
// The artifact's record and index as this run last read them, which saves the next anchor or plan reading them back.
const KEPT_RECORD = join(CACHE, 'kept-record.json');
const KEPT_INDEX = join(CACHE, 'kept-index.json');
const TAKE_OVER = join(CACHE, 'take-over.txt');
// Where Claude saves what claude.ai/design answered about the project this repo synced to, when it follows a move.
const MOVED = join(CACHE, 'moved.json');
// What the last take-over question was about, line by line. It records no yes: it only says what a code stands for.
const ASKED_ABOUT = join(CACHE, 'take-over-lines.json');
const STATE = join(CACHE, 'state.json');
const MANIFEST = join(CACHE, 'manifest.txt');
const ANCHOR = join(HOME, '.cache', 'remote-sync.json');
const MAX_SAID = 20; // the most strings shown of one list under theirs; "more" counts the rest
// Above this much text DATA says askFirst: Claude reads what it sends, at a cost in tokens that grows with it.
const ASK_ABOVE_BYTES = 500_000;
// What the artifact's page generates at a save and a sync never sends. A page that
// was open when the system became read-only can have saved once more.
const PAGE_WRITES = /^project\\/(?:manifest\\.json|api\\/(?:icons|tokens)\\.md|api\\/(?:tokens|components|assets)\\/[^/]+\\.md)$/;
const BYTES_A_TOKEN = 2; // roughly, for markup and minified script
// base_version in every call after the first, until Claude puts in the version that the call before returned. It is
// not the live version, so a call sent with it left in is refused, where an empty one might go unchecked.
const NOT_YET_KNOWN = 'unknown';

// Claude Code sends no file whose folder or name is one that credentials are kept under, and one refused file fails the
// whole call. Its rules are many and it is the judge; these few of its folders get a plain answer before any call is written.
const CREDENTIAL_FOLDERS = ['.ssh', '.aws', '.azure', '.gnupg', '.kube', '.docker', '.config/git', '.config/gh', '.config/gcloud', '.claude/state'];

// Nothing at the path, or a file where one of its folders should be.
const isAbsent = (error) => error?.code === 'ENOENT' || error?.code === 'ENOTDIR';

// Anything but a regular file counts as no file: a link or a pipe planted at one of this script's paths is not read.
function readOrNull(path) {
  try { return lstatSync(path).isFile() ? readFileSync(path) : null; } catch (error) {
    if (isAbsent(error)) return null;
    throw error;
  }
}

// Null only when nothing is at the path. Any other error is thrown: a path that cannot be checked might be a link.
function statOrNull(path) {
  try { return lstatSync(path); } catch (error) {
    if (isAbsent(error)) return null;
    throw error;
  }
}

// A link committed to the repo at one of these paths would have this script, or Claude, read or write somewhere else.
// Where Claude saves an answer, anything but a regular file goes, so that it can save there; and where this script keeps
// what it sends, anything but a folder.
function requireNoLinks() {
  for (const [which, path] of Object.entries({ home: HOME, target: join(HOME, 'artifact.json'), cacheParent: join(HOME, '.cache'), cache: CACHE, send: SEND.folder, calls: join(CACHE, 'calls') })) {
    if (statOrNull(path)?.isSymbolicLink()) throw new Told('LINK', { which });
  }
  for (const path of Object.values(SAVED)) if (statOrNull(path)?.isFile() === false) rmSync(path, { recursive: true });
  if (statOrNull(SEND.folder)?.isDirectory() === false) rmSync(SEND.folder);
}

function write(path, content) {
  mkdirSync(dirname(path), { recursive: true });
  // Removed first, so that a link at the path is replaced, not followed.
  rmSync(path, { recursive: true, force: true });
  writeFileSync(path, content);
}

// The two lines that end a run, in one write, so that nothing comes between them. theirs: lists of other people's text, of
// which a few are shown, each made one short line; "more" says how many of each list are not.
function end(tag, { which = '', data = {}, theirs = {} } = {}) {
  const lists = Object.entries(theirs).filter(([, list]) => list.length);
  const more = Object.fromEntries(lists.filter(([, list]) => list.length > MAX_SAID).map(([name, list]) => [name, list.length - MAX_SAID]));
  const code = EXIT[tag] ?? 1;
  const text = (code === 0 ? '\\u2713' : code === 3 ? '\\u2026' : '\\u2717') + ' [' + tag + '] ' + SAYS[which ? tag + '.' + which : tag] + '\\nDATA ' + JSON.stringify({
    ...data,
    ...(Object.keys(more).length ? { more } : {}),
    ...(lists.length ? { theirs: Object.fromEntries(lists.map(([name, list]) => [name, list.slice(0, MAX_SAID).map((entry) => shown(entry))])) } : {}),
  }) + '\\n';
  (code === 0 || code === 3 ? process.stdout : process.stderr).write(text);
  process.exitCode = code;
}

function readTarget() {
  const target = savedObject(readOrNull(join(HOME, 'artifact.json'))?.toString('utf8') ?? '');
  // The service gives an empty link where it has no address for its pages.
  const url = String(target?.url ?? '').trim();
  const linked = slugIn(url);
  const slug = target?.slug == null ? linked : slugIn(String(target.slug));
  if (!slug) throw new Told('NO_TARGET');
  // The person is shown the link, and the tools are given the slug. A link that cannot be read could hide another artifact.
  if (url !== '' && linked !== slug) {
    throw new Told('TWO_TARGETS', { which: linked === null ? 'unreadable' : '', data: { slug, linkIsOf: linked }, theirs: { url: [url] } });
  }
  return { slug, title: target.title, url };
}

// The claude.ai/design project that the repo's config says it synced to, or null. The config may still have its old name and place.
function syncedTo() {
  const text = readOrNull(join(HOME, 'config.json')) ?? readOrNull(resolve('design-sync.config.json'));
  const id = savedObject(text?.toString('utf8') ?? '')?.projectId;
  return typeof id === 'string' && id.trim() ? id.trim() : null;
}

// A run that follows a move has Claude write artifact.json from claude.ai/design's answer. The saved answer is held against
// it, and against the project the repo's config names. This catches a slip of Claude's. It is no guard against the repo: all
// three files can come from a commit.
function requireTheMovedTarget(slug, answer) {
  if (answer === null) return;
  const isOfThisRepo = typeof answer.projectId === 'string' && answer.projectId.toLowerCase() === syncedTo()?.toLowerCase();
  if (!isOfThisRepo || slugIn(String(answer.movedTo ?? '')) !== slug) {
    throw new Told('TWO_TARGETS', { which: 'moved', data: { slug }, theirs: { movedTo: [String(answer.movedTo ?? '')], project: [String(answer.projectId ?? '')] } });
  }
}

// What this script noted for its own later commands. The file sits in the repo's folder, where a commit can put one, so
// only these keys are taken, each in the form this script writes, and none of them records the person's consent.
// anchor and ownRecords feed [RECORD_MOVED] alone, a guard against accidents: the anchor command sets the first anew and clears the second.
function readState(slug) {
  const state = savedObject(readOrNull(STATE)?.toString('utf8') ?? '');
  if (state?.slug !== slug) return { slug, ownRecords: [] };
  const isHash = (value) => typeof value === 'string' && /^[0-9a-f]{64}$/.test(value);
  const { anchor, ownRecords, planned } = state;
  const isPlanned = [planned?.files, planned?.index, planned?.record].every(isHash) && Array.isArray(planned.remove) && planned.remove.every((path) => typeof path === 'string');
  return {
    slug,
    ...(anchor === null || isHash(anchor) ? { anchor } : {}),
    ownRecords: Array.isArray(ownRecords) ? ownRecords.filter(isHash) : [],
    ...(isPlanned ? { planned: { files: planned.files, index: planned.index, record: planned.record, remove: planned.remove } } : {}),
  };
}

// need: which of the artifact's answers are wanted, of 'listing', 'index' and 'record'. why: one word from a fixed list.
function asks(slug, need, why, theirs = {}) {
  return new Told('NEEDS_ANSWERS', { which: why === 'nothingSaved' || why === 'noFileList' ? '' : why === 'hashDiffers' || why === 'otherVersion' ? 'moved' : 'unusable', data: { need, slug, link: plainLink(readTarget().url), why }, theirs });
}

function dropListing() {
  for (const path of [SAVED.listing, SAVED.listingText, SAVED.listingFiles]) rmSync(path, { recursive: true, force: true });
}

// The saved listing, of an artifact that a sync can publish to. toSend: true for anchor and plan, whose runs end in publish
// calls: the listing then has to give the title that those calls state as well.
function takeListing(slug, toSend) {
  const asJson = readOrNull(SAVED.listing);
  const bytes = asJson ?? readOrNull(SAVED.listingText);
  if (bytes === null) throw asks(slug, ['listing'], 'nothingSaved');
  let listing;
  try { listing = readListingAs(asJson ? 'json' : 'text', bytes.toString('utf8'), slug, readOrNull(SAVED.listingFiles)?.toString('utf8') ?? null); } catch (error) {
    if (!(error instanceof Need)) throw error;
    // Under every name: one saved under the other form's name would be read first the next time too.
    dropListing();
    throw asks(slug, ['listing'], error.data.why, error.theirs);
  }
  if (listing.canWrite === false) throw new Told('NOT_A_WRITER');
  if (!['owner', 'users', 'org'].includes(listing.read)) {
    throw new Told('SHARED_TOO_WIDELY', { theirs: { read: [listing.read] } });
  }
  if (listing.files.size > 0 && !listing.files.has(INDEX) && !listing.files.has(RECORD)) {
    throw new Told('NOT_A_DESIGN_SYSTEM');
  }
  if (listing.content !== null && listing.content.index !== INDEX) {
    throw new Told('NOT_A_DESIGN_SYSTEM', { which: 'type', theirs: { content: [JSON.stringify(listing.content)] } });
  }
  if (toSend && listing.stateTitle?.missing) throw new Told('TITLE_WITHHELD', { which: listing.stateTitle.missing === 'none' ? 'none' : '' });
  return listing;
}

// The repo, or a move that the run followed, may have named an artifact that is not the user's own, and whoever can open it
// sees what is published there. So it wants their yes. The code stands for the artifact and for who can open it. Like the
// other questions' yes, it is the command's flag and is kept nowhere: a file in the repo's folder could fake it.
function requireYesToAnothersArtifact(slug, url, listing, title, agreed) {
  if (listing.owned === true) return;
  const code = sha256('not the user\\'s own: ' + slug + ' ' + listing.read).slice(0, 32);
  if (agreed === code) return;
  throw new Told('NOT_THE_OWNER', { which: listing.owned === false ? '' : 'unknown', data: { slug, link: plainLink(url), sharedWith: listing.read, code }, theirs: { title } });
}

// The text of the artifact's copy of a file, or null if it has none or no copy at hand is that text. A copy this script
// wrote itself, or one Claude saved from read_file, serves when it hashes to what the listing says; otherwise the file
// is put on toFetch.
function takeStored(listing, path, saveTo, ownCopies, toFetch) {
  const hash = listing.files.get(path);
  if (hash === undefined) return null;
  if (hash === '') throw new Told('NO_HASH', { data: { count: 1 }, theirs: { files: [path] } });
  const copies = [...ownCopies, saveTo].map(readOrNull).filter((bytes) => bytes !== null);
  const text = copies.map((bytes) => storedText(bytes.toString('utf8'), hash)).find((found) => found !== null);
  if (text === undefined) toFetch.push({ path, saveTo });
  return text ?? null;
}

// A journal is the record as it stands once one call of a sync that takes several has arrived. Journals are named
// by their hash: those of this sync's earlier plans stay, since any of them may be the one that arrived.
function journalFiles() {
  let names = [];
  try { names = readdirSync(SEND.folder); } catch (error) {
    if (!isAbsent(error)) throw error; // absent: nothing sent yet
  }
  return names.filter((name) => /^journal-[0-9a-f]{12}\\.json$/.test(name)).map((name) => join(SEND.folder, name));
}

function takeRecord(listing, toFetch) {
  return takeStored(listing, RECORD, SAVED.record, [KEPT_RECORD, SEND.record, ...journalFiles()], toFetch);
}

// A copy that was saved and does not hash to the listing's row is most often
// newer than the listing: someone saved on the page in between. Reading it again
// would bring the same text, so the listing is asked for again as well.
function requireFetched(slug, toFetch) {
  if (toFetch.length === 0) return;
  const need = toFetch.map((file) => (file.path === INDEX ? 'index' : 'record'));
  if (!toFetch.some((file) => readOrNull(file.saveTo) !== null)) throw asks(slug, need, 'nothingSaved');
  dropListing();
  for (const file of toFetch) rmSync(file.saveTo, { recursive: true, force: true });
  throw asks(slug, ['listing', ...need], 'hashDiffers');
}

function parseRecord(text) {
  return (text === null ? null : readRecord(text)) ?? { build: {}, files: {}, pending: {}, removing: {} };
}

// Saved answers are used once: a run without --fetched drops them, and so does a command that ends, well or in a refusal
// (but for [LINK], which removes nothing). [NEEDS_ANSWERS] keeps those that still serve.
function dropSaved() {
  for (const path of Object.values(SAVED)) rmSync(path, { recursive: true, force: true });
}

function keep(path, text) {
  if (text === null) rmSync(path, { recursive: true, force: true });
  else write(path, text);
}

// A sync has ended: remove what came from the artifact or was written to be sent to it. state.json keeps only the slug and the record's hash.
function forgetTheSync(slug, anchor) {
  for (const path of [join(CACHE, 'calls'), SEND.folder, MANIFEST, TAKE_OVER, ASKED_ABOUT, KEPT_RECORD, KEPT_INDEX, ANCHOR]) rmSync(path, { recursive: true, force: true });
  dropSaved();
  write(STATE, JSON.stringify({ slug, anchor }) + '\\n');
}

// Everything below root, folders too, with what lstat says of it. No link below root is followed.
function entriesBelow(root, isSkipped, prefix = '') {
  const found = [];
  for (const name of readdirSync(join(root, prefix)).sort()) {
    const path = prefix + name;
    if (isSkipped(path)) continue;
    const stat = lstatSync(join(root, path));
    found.push({ path, stat });
    if (stat.isDirectory()) found.push(...entriesBelow(root, isSkipped, path + '/'));
  }
  return found;
}

// Left out of the comparison with the verdict's time: dot names (.artifact/, which plan writes, among them) and _screenshots.
function isBuildScratch(path) {
  return isDotName(path) || path === '_screenshots';
}

// Under project/, artifact-layout.mjs writes no dot name; a file manager can leave some there (.DS_Store).
function isDotName(path) {
  return /(?:^|\\/)\\./.test(path);
}

// Only a build that resync.mjs checked is published, unchanged: no file or folder in it may be newer than the verdict,
// by its change time either, which moves when a file is moved in or re-dated. A guard against accidents, not intent.
// A removal from the build's top folder is not caught, since plan changes that folder's time itself.
function requireVerdict(bundle) {
  const path = join(bundle, '.resync-verdict.json');
  const verdict = savedObject(readOrNull(path)?.toString('utf8') ?? '');
  if (verdict === null) throw new Told('NO_VERDICT');
  if (verdict.ok !== true) throw new Told('VERDICT_NOT_OK');
  const checkedAt = lstatSync(path).mtimeMs;
  const newer = entriesBelow(bundle, isBuildScratch).filter((entry) => Math.max(entry.stat.mtimeMs, entry.stat.ctimeMs) > checkedAt).map((entry) => entry.path);
  if (newer.length) throw new Told('CHANGED_SINCE_VERDICT', { data: { count: newer.length }, theirs: { files: newer } });
}

// The laid-out files as they are on disk now: Map of published path to { hash, size, file }. Each has to be as
// layout.json says artifact-layout.mjs wrote it; any other file under project/, dot names aside, refuses the plan.
function readLayout(bundle) {
  const root = join(bundle, '.artifact');
  const wrote = new Map((savedObject(readOrNull(join(root, 'layout.json'))?.toString('utf8') ?? '')?.files ?? []).map((row) => [row.path, row.sha256]));
  const files = new Map();
  let entries;
  try { entries = entriesBelow(root, isDotName, 'project/'); } catch (error) {
    // A build made since the plan removes the whole folder, and so does a layout that was refused.
    if (!isAbsent(error)) throw error;
    throw new Told('LAYOUT_CHANGED');
  }
  for (const { path, stat } of entries) {
    if (stat.isDirectory()) continue;
    const file = join(root, ...path.split('/'));
    if (!stat.isFile() || stat.nlink > 1) throw new Told('LAYOUT_CHANGED', { theirs: { files: [path] } });
    const hash = sha256(readFileSync(file));
    // layout.json has the path in NFC, and some disks give every name back decomposed.
    const published = path.normalize('NFC');
    if (wrote.get(published) !== hash) throw new Told('LAYOUT_CHANGED', { theirs: { files: [path] } });
    files.set(published, { hash, size: stat.size, file });
  }
  if (files.size !== wrote.size || !files.has(INDEX)) throw new Told('LAYOUT_CHANGED');
  for (const sentFrom of [root, SEND.folder]) {
    const refused = CREDENTIAL_FOLDERS.find((run) => ('/' + sentFrom.toLowerCase().split(sep).join('/') + '/').includes('/' + run + '/'));
    if (refused) throw new Told('CREDENTIAL_FOLDER', { data: { folder: refused } });
  }
  return files;
}

// CLAUDE_CODE_ARTIFACT_PATH_PIN set to 0, false, no or off takes overwrite_unread out of the built-in tool, which then refuses a call that has it.
function toolTakesOverwriteUnread() {
  return !['0', 'false', 'no', 'off'].includes(String(process.env.CLAUDE_CODE_ARTIFACT_PATH_PIN ?? '').trim().toLowerCase());
}

function hashesOf(files) {
  return new Map([...files].filter(([path]) => path !== INDEX).map(([path, file]) => [path, file.hash]));
}

const SHARED_WITH = { owner: 'nobody but its owner', users: 'the people its owner named', org: 'everyone in the organization' };

// Where it all goes, then one line for each file the calls send or remove: what a person, and Claude, can look through before anything goes.
function manifestText(sent, removed, diff, target) {
  const changedThere = new Set(diff.changedThere);
  // In a system as a move left it, an earlier sync to claude.ai/design may well have made what no sync put in the artifact.
  const notOurs = new Set(target.isAsMoved ? [] : diff.notOursToReplace);
  const moved = new Set(target.isAsMoved ? [...diff.notOursToReplace, ...diff.movedToRemove] : []);
  const rows = [
    ...sent.map((entry) => ['send  ', String(entry.size).padStart(9), sha256(readFileSync(entry.path)).slice(0, 12), entry.as, entry.note]),
    ...removed.map((path) => ['remove', ' '.repeat(9), ' '.repeat(12), path]),
  ];
  return ['Goes to artifact ' + target.slug + (plainLink(target.url) ? ' (' + plainLink(target.url) + ')' : '') + ', which is shared with ' + SHARED_WITH[target.read] + '.', 'action       size  sha256        kind        path', ...rows.map(([action, size, hash, path, note]) =>
    [action, size, hash, kindOf(path).padEnd(10), quoted(path, 300) + (note ?? (changedThere.has(path) ? '  CHANGED OR DELETED ON CLAUDE.AI' : notOurs.has(path) ? '  NOT FROM A SYNC' : moved.has(path) ? '  BROUGHT BY THE MOVE' : ''))].join('  '))].join('\\n') + '\\n';
}

function totalsByKind(sent) {
  const totals = {};
  for (const entry of sent) {
    const so = totals[kindOf(entry.as)] ?? { files: 0, bytes: 0 };
    totals[kindOf(entry.as)] = { files: so.files + 1, bytes: so.bytes + entry.size };
  }
  return totals;
}

// Whether code is the code of the last take-over question and every line in lines was part of that question. A sync that
// takes several plans has less left to replace and remove at each, and the person's yes to the whole covers what is left.
// The yes is still the flag alone: the file says what a code stood for, and counts only if it hashes to that code.
function isPartOf(lines, code) {
  let asked = null;
  try { asked = JSON.parse(readOrNull(ASKED_ABOUT)?.toString('utf8') ?? 'null'); } catch { /* not as this script writes it: it says nothing */ }
  if (code === undefined || !Array.isArray(asked) || sha256(asked.join('\\n')).slice(0, 32) !== code) return false;
  return lines.every((line) => asked.includes(line));
}

function anchor(flags) {
  rmSync(join(CACHE, 'calls'), { recursive: true, force: true });
  // If this command is refused, resync.mjs is not to be handed what an earlier one wrote.
  rmSync(ANCHOR, { recursive: true, force: true });
  // Read once, however this command ends: it is about the target as the run first wrote it, not about one that the person names later.
  const movedAnswer = savedObject(readOrNull(MOVED)?.toString('utf8') ?? '');
  rmSync(MOVED, { recursive: true, force: true });
  const { slug, url } = readTarget();
  requireTheMovedTarget(slug, movedAnswer);
  const listing = takeListing(slug, true);
  const toFetch = [];
  const record = takeRecord(listing, toFetch);
  const liveIndexText = takeStored(listing, INDEX, SAVED.index, [KEPT_INDEX, SEND.index], toFetch);
  requireFetched(slug, toFetch);
  // An artifact that a sync may not write to is refused now, not after the build.
  const liveIndex = readLiveIndex(liveIndexText, syncedTo());
  const itsTitle = typeof liveIndex?.title === 'string' && liveIndex.title.trim() ? [liveIndex.title] : [];
  // Asked before the build. A system still as a move left it is asked about at the plan, where [MOVED_HERE] names the same things.
  if (liveIndex?.editing !== AS_MOVED) requireYesToAnothersArtifact(slug, url, listing, itsTitle, flags.agreed);
  // A first sync that stopped halfway left a record with none of the build's keys: nothing for resync.mjs to go by.
  const { build, isForeign, pending } = parseRecord(record);
  const hasBuildKeys = Object.keys(build).length > 0;
  if (hasBuildKeys) write(ANCHOR, JSON.stringify(build, null, 1) + '\\n');
  // A new run: what an earlier one left goes, its progress records among it.
  for (const path of [SEND.folder, MANIFEST, TAKE_OVER, ASKED_ABOUT]) rmSync(path, { recursive: true, force: true });
  keep(KEPT_RECORD, record);
  keep(KEPT_INDEX, liveIndexText);
  write(STATE, JSON.stringify({ slug, anchor: listing.files.get(RECORD) ?? null }) + '\\n');
  dropSaved();
  const asMoved = liveIndex?.editing === AS_MOVED;
  // plan refuses this after the build, which can take hours, so the person is told now. It's only an estimate: plan still
  // decides, and can count a little higher where the repo has gained components or guidelines since the move.
  const names = [...listing.files.keys()].map((path) => /^project\\/components\\/[^/]+\\/([^/]+)\\/\\1\\.html$/.exec(path)?.[1]).filter(Boolean);
  const added = names.flatMap((name) => ['project/components/' + name + '/preview.html', 'project/components/' + name + '/README.md']);
  const holdsWithNewLayout = listing.typeFiles.size + new Set([...listing.files.keys(), ...added, ...['components/bundle.js', 'components/bundle.css', 'components/index.d.ts', 'tokens.json', 'tokens.css'].map((path) => 'project/' + path), RECORD]).size;
  const cutAfter = asMoved && listing.form === 'text' && holdsWithNewLayout > TEXT_ROWS_SHOWN;
  // artifact.json's own title comes from the repo: the page's title lets the person see which artifact the slug names.
  // The link is the one held against the slug, without a title before its id or a path after it, which the repo can word as it likes.
  end('ANCHORED', {
    data: { slug, link: plainLink(url), remote: hasBuildKeys, unfinished: Object.keys(pending).length > 0, foreignRecord: isForeign === true, asMoved, ...(cutAfter ? { cutAfter } : {}) },
    theirs: { title: itsTitle },
  });
}

function plan(bundle, flags) {
  // Whatever comes of this plan, the calls of an earlier one are no longer to be made.
  rmSync(join(CACHE, 'calls'), { recursive: true, force: true });
  rmSync(MANIFEST, { recursive: true, force: true });
  rmSync(TAKE_OVER, { recursive: true, force: true });
  // An artifact that this run made is not anchored, so an answer saved before the person chose a new one is still there.
  rmSync(MOVED, { recursive: true, force: true });
  const { slug, title, url } = readTarget();
  // Nor is check to go by what an earlier plan planned.
  const { planned: _earlier, ...state } = readState(slug);
  write(STATE, JSON.stringify(state) + '\\n');
  requireVerdict(bundle);
  const listing = takeListing(slug, true);
  const toFetch = [];
  const recordText = takeRecord(listing, toFetch);
  const liveIndexText = takeStored(listing, INDEX, SAVED.index, [KEPT_INDEX, SEND.index], toFetch);
  requireFetched(slug, toFetch);
  const record = parseRecord(recordText);
  const liveIndex = readLiveIndex(liveIndexText, syncedTo());
  const isAsMoved = liveIndex?.editing === AS_MOVED;

  // resync.mjs did not verify again what the anchored record lists. If another sync has replaced that record since,
  // the artifact no longer holds what resync.mjs took for verified.
  const liveRecord = listing.files.get(RECORD) ?? null;
  const { ownRecords } = state;
  // Without an anchor command, the first plan keeps the record it saw as the anchor, even if it goes on to refuse, so
  // that a later plan still notices another machine's sync.
  const anchored = state.anchor === undefined ? liveRecord : state.anchor;
  if (liveRecord !== anchored && !ownRecords.includes(liveRecord)) {
    throw new Told('RECORD_MOVED');
  }
  write(STATE, JSON.stringify({ ...state, anchor: anchored }) + '\\n');

  // The name the system has on claude.ai now, where someone may have renamed it. One that cannot be passed on is passed
  // over: it starts with a dash or a space, runs over a line or 200 characters, or holds a character that is not seen.
  const named = [liveIndex?.title, title].find((name) => typeof name === 'string' && /^[^\\s-]/.test(name) && isShown(name, 200));
  const stage = spawnSync(process.execPath, [join(dirname(fileURLToPath(import.meta.url)), 'artifact-layout.mjs'), bundle, ...(named ? ['--title', named] : [])], { stdio: ['ignore', 2, 2] });
  if (stage.status !== 0) throw new Told('LAYOUT_REFUSED');
  const files = readLayout(bundle);
  const ours = hashesOf(files);
  const typesOwn = [...files.keys(), RECORD].filter((path) => listing.typeFiles.has(path));
  if (typesOwn.length) throw new Told('TYPE_FILE', { data: { count: typesOwn.length }, theirs: { files: typesOwn } });

  // Only where the index and the repo's config name one project is it known that this repo's syncs filled what the move brought.
  const isThisReposOwn = isAsMoved && isMovedFrom(liveIndex, syncedTo());
  const oldLayout = isThisReposOwn ? oldLayoutOf(entriesBelow(bundle, isBuildScratch).filter((entry) => entry.stat.isFile()).map((entry) => entry.path)) : null;
  const diff = compare(ours, new Map([...listing.files].filter(([path]) => path !== INDEX && path !== RECORD)), record, oldLayout);
  // The tool lists only so many of an artifact's files, the type's among them, and lets a publish remove none that it has not listed or read. An artifact filled beyond that could not be synced again.
  // Counted before anything is removed: removals go last, and a sync that stops halfway must leave an artifact that can still be listed.
  const holdsAfter = listing.typeFiles.size + new Set([...listing.files.keys(), ...ours.keys(), INDEX, RECORD]).size;
  if (listing.form === 'text' && holdsAfter > TEXT_ROWS_SHOWN) throw new Told('LISTING_CUT', { which: 'after', data: { holds: holdsAfter, shown: TEXT_ROWS_SHOWN } });
  // Without its hash, a file could change after the person's yes and the take-over code would stay the same. Refused before any question is asked: no yes makes up for a missing hash.
  // What a question names the artifact by, given with every ending that leads to one: ANCHORED's may be long gone from
  // the conversation. As there, the title is the page's own and the link is the plain one, null where the service gave none.
  const link = plainLink(url);
  const itsTitle = typeof liveIndex?.title === 'string' && liveIndex.title.trim() ? [liveIndex.title] : [];
  const unhashed = [...diff.notOursToReplace, ...diff.movedToRemove].filter((path) => !listing.files.get(path));
  if (unhashed.length) throw new Told('NO_HASH', { data: { count: unhashed.length }, theirs: { files: unhashed } });
  // Until the last call of a take-over has landed, the artifact may hold all that the move brought and all that is new.
  const most = listing.files.size + [...ours.keys(), INDEX, RECORD].filter((path) => !listing.files.has(path)).length;
  if (isAsMoved && most > LAYOUT_LIMITS.files) throw new Told('NO_ROOM', { data: { files: most, limit: LAYOUT_LIMITS.files } });
  // A system still as a move left it is asked about by [MOVED_HERE], below, which names the same things.
  if (!isAsMoved) requireYesToAnothersArtifact(slug, url, listing, itsTitle, flags.agreed);
  // Written out in codes: such a name can look exactly like a file this build sends.
  const outOfReach = listing.unnameable.map((path) => path.replace(/\\\\/g, '\\\\\\\\').replace(/[^\\x20-\\x7e]/gu, (c) => '\\\\u{' + c.codePointAt(0).toString(16) + '}'));
  // An index alone is what the page writes when it is first opened: nobody has made anything there yet.
  const hasWork = Object.keys(record.files).length + diff.notOursToReplace.length + diff.leftAlone.length + listing.unnameable.length > 0;
  // Where there is no index, none says that the page is read-only, so it is asked about as an editable one.
  // A system as a move left it can't be edited on its page either: what a sync changes there is asked about below.
  const isEditable = liveIndex?.editing !== SYNCED_FROM_CODE && !isAsMoved && hasWork;
  // The yes is this command's flag and is kept nowhere: a file in the repo could fake it.
  if (isEditable && !flags.readOnly) {
    throw new Told('EDITABLE', { which: liveIndex === null ? 'noIndex' : '', data: { slug, link }, theirs: { title: itsTitle } });
  }
  // The code stands for these files as they are now, so that the person's yes covers what they were shown and nothing later.
  // The first 128 bits: anyone who can edit the artifact chooses what is hashed, and with a short code could search for another list that gives the same code.
  // The artifact and who can open it are among what is hashed: a yes to one is none to another that holds the same files, or to a wider audience.
  const toAgree = ['in ' + slug + ', shared with ' + listing.read, ...diff.notOursToReplace.map((path) => path + ' ' + listing.files.get(path)), ...diff.movedToRemove.map((path) => 'remove ' + path + ' ' + listing.files.get(path))];
  const takeOverCode = sha256(toAgree.join('\\n')).slice(0, 32);
  if ((isAsMoved || toAgree.length > 1) && flags.takeOver !== takeOverCode && !isPartOf(toAgree, flags.takeOver)) {
    write(ASKED_ABOUT, JSON.stringify(toAgree) + '\\n');
    if (isAsMoved) {
      const listed = (paths) => (paths.length ? paths.map((path) => quoted(path, 300)) : ['(none)']);
      write(TAKE_OVER, [
        'Files that this sync would replace:', ...listed(diff.notOursToReplace),
        '', 'Files from earlier syncs to claude.ai/design that this sync would remove from the artifact:', ...listed(diff.movedToRemove),
        '', 'Files that this sync would leave as they are:', ...listed(diff.leftAlone),
        ...(outOfReach.length ? ['', 'Files stored under a spelling that no sync can give, so it can neither change nor remove them:', ...outOfReach.map((path) => '"' + path.replace(/"/g, '\\\\"') + '"')] : []),
      ].join('\\n') + '\\n');
      throw new Told('MOVED_HERE', { which: isThisReposOwn ? '' : 'unmatched', data: { slug, link, sharedWith: listing.read, owned: listing.owned, replace: diff.notOursToReplace.length, remove: diff.movedToRemove.length, stay: diff.leftAlone.length, code: takeOverCode }, theirs: { title: itsTitle } });
    }
    write(TAKE_OVER, ['Files in the artifact that no sync put there, and that this sync would replace:', ...diff.notOursToReplace.map((path) => quoted(path, 300))].join('\\n') + '\\n');
    throw new Told('NOT_FROM_A_SYNC', { data: { slug, link, count: diff.notOursToReplace.length, code: takeOverCode }, theirs: { title: itsTitle, files: diff.notOursToReplace } });
  }
  const now = new Date().toISOString();
  const index = mergeIndex(JSON.parse(readFileSync(files.get(INDEX).file, 'utf8')), liveIndex, sectionsOf([...ours.keys(), ...diff.leftAlone.filter((path) => !PAGE_WRITES.test(path))]), now);
  const build = savedObject(readOrNull(join(bundle, '_ds_sync.json'))?.toString('utf8') ?? '') ?? {};
  // What this sync removes stays a sync's own until a listing shows it gone: a call may land without its removal.
  const finalRecord = writeRecord(build, recordTable(ours), null, recordTable(new Map(diff.remove.map((path) => [path, listing.files.get(path)]))));

  // remove counts what is still to be asked about: the person has said yes to what the take-over removes.
  const summary = { slug, link, sharedWith: listing.read, remove: diff.remove.length - diff.movedToRemove.length, unchanged: ours.size - diff.push.length };
  const theirs = {
    title: itsTitle,
    changedOnClaudeAiSinceTheLastSync: diff.changedThere,
    replacedThoughNoSyncPutThemThere: diff.notOursToReplace,
    leftAloneNotFromThisBuild: diff.leftAlone.filter((path) => !PAGE_WRITES.test(path)),
    leftAloneWrittenByThePage: diff.leftAlone.filter((path) => PAGE_WRITES.test(path)),
    underANameNoSyncCanGive: outOfReach,
  };
  const settled = diff.push.length + diff.remove.length === 0 && liveIndex !== null && sameIndex(liveIndex, index) && sha256(finalRecord) === liveRecord;
  if (settled) {
    forgetTheSync(slug, liveRecord);
    end('PLANNED', { which: 'nothing', data: { send: 0, ...summary, calls: 0 }, theirs });
    return;
  }

  const sentIndex = JSON.stringify({
    ...index,
    ...(liveIndex === null ? { createdOnFiles: { ...index.createdOnFiles, at: now } } : {}),
    lastChange: { by: gitUserName() ?? 'Claude', at: now, via: 'Claude Code /design-sync', note: 'Synced from the design system\\'s code' },
  }, null, 2) + '\\n';
  write(SEND.index, sentIndex);
  write(SEND.record, finalRecord);
  // Both as they are now. When these calls leave the index for a later plan, that plan takes the index from here; if the
  // calls are never made, it takes both.
  keep(KEPT_RECORD, recordText);
  keep(KEPT_INDEX, liveIndexText);
  const changed = diff.push.map((path) => ({ as: path, path: files.get(path).file, size: files.get(path).size }));
  const last = [{ as: INDEX, path: SEND.index, size: Buffer.byteLength(sentIndex) }, { as: RECORD, path: SEND.record, size: Buffer.byteLength(finalRecord) }];
  const fullestJournal = writeRecord(record.build, record.files, { ...record.pending, ...recordTable(new Map(diff.push.map((path) => [path, ours.get(path)]))) }, record.removing);
  const removal = (path) => ({ as: path, size: 0 });
  const ownToRemove = diff.remove.filter((path) => !diff.movedToRemove.includes(path));
  // What the move brought goes with the new index or after it: until then the old index goes on describing files that are there.
  const { isWhole, calls } = planCalls([...changed, ...ownToRemove.map(removal)], last, Buffer.byteLength(fullestJournal), flags.callMib ? { ...LIMITS[listing.form], bytes: flags.callMib * 1024 * 1024 } : LIMITS[listing.form], diff.movedToRemove.map(removal));

  // A call lands whole or not at all, so the journal that is live says exactly which files have arrived.
  const journals = [];
  let arrived = record.pending;
  for (const call of isWhole ? [] : calls) {
    arrived = { ...arrived, ...recordTable(new Map(call.files.map((file) => [file.as, ours.get(file.as)]))) };
    const text = writeRecord(record.build, record.files, arrived, record.removing);
    journals.push({ as: RECORD, path: join(SEND.folder, 'journal-' + sha256(text).slice(0, 12) + '.json'), size: Buffer.byteLength(text), hash: sha256(text), note: '  PROGRESS RECORD, SENT WITH CALL ' + (journals.length + 1) });
    write(journals.at(-1).path, text);
    call.files.unshift({ as: RECORD, path: journals.at(-1).path });
  }
  const sent = isWhole ? [...changed, ...last] : [...journals, ...changed];
  const sentBytes = sent.reduce((sum, entry) => sum + entry.size, 0);
  const textBytes = sent.reduce((sum, entry) => sum + (kindOf(entry.as) === 'font' ? 0 : entry.size), 0);
  const callFiles = calls.map((call, i) => join(CACHE, 'calls', 'call-' + (i + 1) + '.json'));
  // A sync reads hardly any of what it replaces, so the built-in tool is told which files it replaces. This plan compared each with the listing and the record: the take-over questions above cover what no sync put there, and the skill asks about what someone changed. The tool goes on refusing a file that changed since the session's last listing of it, but it has no such listing to go by after a new login, or a rewind to before the listing.
  const replacedIn = (call) => (toolTakesOverwriteUnread() ? call.files.map((file) => file.as).filter((path) => listing.files.has(path)) : []);
  calls.forEach((call, i) => write(callFiles[i], callText(listing.form, { slug, base_version: i === 0 ? listing.version : NOT_YET_KNOWN, sharedWith: listing.read === 'owner' ? null : listing.read, stateTitle: listing.stateTitle, url: listing.url, replaces: replacedIn(call), ...call })));
  write(STATE, JSON.stringify({
    slug,
    anchor: anchored,
    ownRecords: [...new Set([...ownRecords, sha256(finalRecord), ...journals.map((journal) => journal.hash)])],
    ...(isWhole ? { planned: { files: sha256(JSON.stringify([...ours])), index: sha256(sentIndex), record: sha256(finalRecord), remove: diff.remove } } : {}),
  }) + '\\n');
  write(MANIFEST, manifestText(sent, isWhole ? diff.remove : ownToRemove, diff, { slug, url, read: listing.read, isAsMoved }));
  dropSaved();
  end('PLANNED', {
    data: {
      send: sent.length,
      ...summary,
      sendBytes: sentBytes,
      sendByKind: totalsByKind(sent),
      tokensToReadItAllOnce: Math.ceil(textBytes / BYTES_A_TOKEN / 1000) * 1000,
      askFirst: textBytes > ASK_ABOVE_BYTES,
      calls: calls.length,
      planAgainAfterTheCalls: !isWhole,
    },
    // Named by the plan whose calls remove them.
    theirs: { ...theirs, removedAsTheMoveLeftThem: isWhole ? diff.movedToRemove : [] },
  });
}

function check(bundle) {
  const { slug } = readTarget();
  const state = readState(slug);
  if (!state.planned) throw new Told('NOT_PLANNED');
  const ours = hashesOf(readLayout(bundle));
  if (state.planned.files !== sha256(JSON.stringify([...ours]))) throw new Told('NOT_PLANNED', { which: 'otherBuild' });
  const listing = takeListing(slug);
  const expected = new Map([...ours, [INDEX, state.planned.index], [RECORD, state.planned.record]]);
  const differs = [...expected].filter(([path, hash]) => listing.files.get(path) !== hash).map(([path]) => path);
  const stillThere = state.planned.remove.filter((path) => listing.files.has(path));
  dropSaved();
  const isClean = differs.length + stillThere.length === 0;
  if (isClean) forgetTheSync(slug, state.planned.record);
  end(isClean ? 'CLEAN' : 'NOT_CLEAN', {
    data: { same: expected.size - differs.length, of: expected.size, differs: differs.length, shouldBeGone: stillThere.length },
    theirs: { version: [listing.version], differs, shouldBeGone: stillThere },
  });
}

// Whose sync it is, by git. Asked here, with no shell between, and not passed in on the command line: the repo's own
// scripts can set the name, and a shell would run what is in it. It is published and shown to whoever opens the artifact:
// one line of at most 200 seen characters, like the title. Any other name is dropped, and "Claude" stands in.
function gitUserName() {
  // Started from node's own folder: on Windows a program is looked for in the starting folder first, and a repo can hold a git.exe.
  // Hooks and fsmonitor are switched off because a repo's own .git/config can name a program for either.
  const asked = spawnSync('git', ['-C', process.cwd(), '-c', 'core.hooksPath=/dev/null', '-c', 'core.fsmonitor=', 'config', 'user.name'], { cwd: dirname(process.execPath), encoding: 'utf8', timeout: 10_000, stdio: ['ignore', 'pipe', 'ignore'] });
  const name = asked.status === 0 ? asked.stdout.trim() : '';
  return name && isShown(name, 200) ? name : null;
}

function parseFlags(argv) {
  const flags = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--read-only') flags.readOnly = true;
    else if (argv[i] === '--take-over' && /^[0-9a-f]{32}$/.test(argv[i + 1] ?? '')) flags.takeOver = argv[++i];
    else if (argv[i] === '--agreed' && /^[0-9a-f]{32}$/.test(argv[i + 1] ?? '')) flags.agreed = argv[++i];
    else if (argv[i] === '--call-mib' && Number(argv[i + 1]) >= 1 && Number(argv[i + 1]) <= 16) flags.callMib = Number(argv[++i]);
    else return null;
  }
  return flags;
}

function main() {
  const [command, ...given] = process.argv.slice(2);
  const rest = given.filter((arg) => arg !== '--fetched');
  const bundle = rest[0] && !rest[0].startsWith('--') ? resolve(rest[0]) : null;
  const flags = parseFlags(rest.slice(bundle ? 1 : 0));
  const wellFormed = (command === 'anchor' && !bundle && flags && Object.keys(flags).every((flag) => flag === 'agreed')) || (command === 'plan' && bundle && flags) || (command === 'check' && bundle && rest.length === 1);
  if (!wellFormed) return end('USAGE');
  let foldersAreReal = false;
  try {
    requireNoLinks();
    foldersAreReal = true;
    // .design-sync/.cache/.gitignore has git ignore the tools' saved answers. The build writes it too, but this script can run
    // before any build, and a broad "git add" in between would track them. The mkdir makes no parent, so it fails where
    // .design-sync/ is missing or is not a folder. Nothing is written then: a run in the wrong folder leaves nothing behind.
    let hasHome = true;
    try {
      mkdirSync(join(HOME, '.cache'));
    } catch (error) {
      // Where the folder is there already, or the fault is another, write() goes on: it meets that fault again and reports it.
      hasHome = !isAbsent(error);
    }
    if (hasHome) write(join(HOME, '.cache', '.gitignore'), '*\\n');
    // Without --fetched, what is saved is removed unread: a listing committed to the repo would otherwise pass for the artifact's.
    if (!given.includes('--fetched')) dropSaved();
    if (command === 'anchor') anchor(flags);
    else if (command === 'plan') plan(bundle, flags);
    else check(bundle);
  } catch (error) {
    // Through a folder that is a link, this would remove someone else's files.
    try { if (foldersAreReal && error?.tag !== 'NEEDS_ANSWERS') dropSaved(); } catch { /* what stopped the command is what has to be said */ }
    if (error instanceof Told) end(error.tag, error);
    else end('FAILED', { theirs: { error: [String(error?.message ?? error)] } });
  }
}

main();
