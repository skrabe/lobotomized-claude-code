<!--
name: 'Data: layout-tree.mjs'
description: >-
  design-sync artifact-road lib/layout-tree.mjs listing a finished ds-bundle's
  files, extracted with the skill for the model.
ccVersion: 2.1.332
-->
// The files of a finished ds-bundle/, for the layout stage to read. What is in
// the folder comes from the library being synced, so it is not trusted: a link
// planted there could lead to any file on the machine, and whatever the layout
// stage reads is published.

import { createHash } from 'node:crypto';
import { closeSync, constants, fstatSync, lstatSync, openSync, readdirSync, readFileSync, realpathSync } from 'node:fs';
import { join } from 'node:path';
import { inMib, quoted, Refusal } from './layout-css.mjs';
import { LIMITS } from './layout-preflight.mjs';

// Where the build puts what the artifact needs. A file here that cannot be read is a refusal, not a gap.
const HAS_A_PLACE = /^(?:_ds_bundle\\.(?:js|css)|styles\\.css|README\\.md|(?:_vendor|_preview|components|tokens|fonts|guidelines)(?:\\/|$))/;
// Every listed file is read once, for the digest.
const MAX_LISTED = 20000;
const MAX_LISTED_BYTES = 2 * LIMITS.totalBytes;
const WINDOWS = process.platform === 'win32';
// open() on Windows refuses O_NOFOLLOW, and some runtimes define it there all the same.
const O_NOFOLLOW = WINDOWS ? 0 : constants.O_NOFOLLOW;
// Without it, open() on a pipe put in a file's place would wait for a writer for ever.
const O_NONBLOCK = WINDOWS ? 0 : constants.O_NONBLOCK;
// A file's device and file number. Asked for as BigInt: Windows file numbers are 64-bit and can pass 2^53, where a
// Number rounds two files to one value. Windows can give one file's device in two widths, so there the file number stands alone.
const EXACT = { bigint: true };
const idOf = (st) => (WINDOWS ? '' : st.dev + ':') + st.ino;
// Says what was found and gives no order: what to do about a link is for the skill text to say. It must not read as advice
// to copy the file in, since a copy would pass every check here.
const LINKS_NOT_READ = '[LINK_FOUND] Links in the folder were not read. A link may lead to a private file, and a copy of that file put in its place would pass every check here and be published.';

// The regular files of the folder, listed once. A read of any other path
// throws, so no path written in a stylesheet or a card can reach a file outside
// the folder. A file that cannot be read is reported in errors or in warnings.
export class BuildFolder {
  #root;
  #realRoot;
  #errors;
  #warnings;
  #listed = new Map(); // path to idOf() the file
  #listedBytes = 0;
  #cache = new Map();
  #notUtf8 = new Set();

  constructor(root, errors, warnings) {
    this.#root = root;
    try { this.#realRoot = realpathSync.native(root); } catch (e) { throw new Refusal('[UNREADABLE] the full path of the folder could not be worked out (' + quoted(e?.code) + ')'); }
    this.#errors = errors;
    this.#warnings = warnings;
    this.#list(root, '');
    if ([...errors, ...warnings].some((line) => line.startsWith('[LINK] '))) warnings.push(LINKS_NOT_READ);
  }

  #skip(p, tag, why) {
    (HAS_A_PLACE.test(p) ? this.#errors : this.#warnings).push('[' + tag + '] ' + quoted(p) + ' ' + why);
  }

  #list(dir, prefix) {
    let names;
    try { names = readdirSync(dir).sort(); } catch (e) {
      if (prefix === '') throw new Refusal('[UNREADABLE] the folder could not be listed (' + quoted(e?.code) + ')');
      this.#skip(prefix.slice(0, -1), 'UNREADABLE', 'could not be listed (' + quoted(e?.code) + ') and was not read');
      return;
    }
    for (const name of names) {
      // Dot files, and the screenshots of the build's own render check.
      if (name.startsWith('.') || (prefix === '' && name === '_screenshots')) continue;
      const p = prefix + name;
      let st;
      try { st = lstatSync(join(dir, name), EXACT); } catch (e) { this.#skip(p, 'UNREADABLE', 'could not be looked at (' + quoted(e?.code) + '; a name that is not valid UTF-8 gives ENOENT) and was not read'); continue; }
      if (st.isSymbolicLink()) this.#skip(p, 'LINK', 'is a symbolic link and was not read');
      else if (st.isDirectory()) this.#list(join(dir, name), p + '/');
      else if (!st.isFile()) this.#skip(p, 'NOT_A_FILE', 'is a pipe, a socket or a device, not a file, and was not read');
      else if (st.nlink > 1) this.#skip(p, 'LINK', 'is a hard link (the same file has another name elsewhere on this disk) and was not read');
      else if (st.size > LIMITS.fileBytes) this.#skip(p, 'TOO_LARGE_TO_READ', 'is ' + inMib(Number(st.size)) + ', more than the ' + inMib(LIMITS.fileBytes) + ' a file of an artifact may be, and was not read');
      else if (this.#listed.size >= MAX_LISTED) throw new Refusal('[TOO_MANY_FILES_TO_READ] the folder holds more than ' + MAX_LISTED + ' files, far more than a build writes.');
      else if ((this.#listedBytes += Number(st.size)) > MAX_LISTED_BYTES) throw new Refusal('[TOO_MUCH_TO_READ] the folder holds more than ' + inMib(MAX_LISTED_BYTES) + ', far more than an artifact may hold.');
      else this.#listed.set(p, idOf(st));
    }
  }

  // The open file must be the one listed, and its path with every link followed must still be the listed path
  // inside the folder. O_NOFOLLOW checks only the last part of a path, Windows has no O_NOFOLLOW, and not every
  // Windows disk gives each file its own number, so both checks are needed. A link put there since the listing is
  // refused, and another file wherever files can be told apart; one swapped back at just the right moment is not caught.
  #read(p) {
    if (!this.#listed.has(p)) throw new Error('read of a path that is not in the listing: ' + p);
    const changed = new Refusal('[CHANGED_WHILE_READING] ' + quoted(p) + ' changed while the layout was being made.');
    const failed = (e, what) => (['ELOOP', 'ENOENT', 'ENOTDIR'].includes(e?.code) ? changed : new Refusal('[UNREADABLE] ' + quoted(p) + ' ' + what + ' (' + quoted(e?.code) + ')'));
    const full = join(this.#root, p);
    let fd;
    try { fd = openSync(full, constants.O_RDONLY | O_NOFOLLOW | O_NONBLOCK); } catch (e) { throw failed(e, 'could not be opened'); }
    try {
      const st = fstatSync(fd, EXACT);
      if (!st.isFile() || st.nlink > 1 || st.size > LIMITS.fileBytes || idOf(st) !== this.#listed.get(p)) throw changed;
      let real;
      try { real = realpathSync.native(full); } catch (e) { throw failed(e, 'was opened, but its full path could not be worked out'); }
      if (real !== join(this.#realRoot, p)) throw changed;
      return readFileSync(fd);
    } finally { closeSync(fd); }
  }

  get paths() {
    return [...this.#listed.keys()];
  }

  has(p) {
    return this.#listed.has(p);
  }

  bytes(p) {
    if (!this.#cache.has(p)) this.#cache.set(p, this.#read(p));
    return this.#cache.get(p);
  }

  text(p) {
    const b = this.bytes(p);
    try { return new TextDecoder('utf-8', { fatal: true, ignoreBOM: true }).decode(b); } catch {
      if (!this.#notUtf8.has(p)) this.#errors.push('[NOT_UTF8] ' + quoted(p) + ' is not valid UTF-8 text.');
      this.#notUtf8.add(p);
      // The layout is refused already. No U+FFFD, so that the file this text goes into is not blamed as well.
      return b.toString('latin1');
    }
  }

  // Changes whenever a listed file does. Files nothing else reads are hashed and let go.
  digest() {
    const all = createHash('sha256');
    for (const p of this.#listed.keys()) all.update(p + '\\0' + createHash('sha256').update(this.#cache.get(p) ?? this.#read(p)).digest('hex') + '\\n');
    return all.digest('hex');
  }
}
