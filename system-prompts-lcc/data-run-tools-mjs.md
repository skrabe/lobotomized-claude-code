<!--
name: 'Data: run-tools.mjs'
description: >-
  claude-test browser-server module (skills/run/scripts/lib/run-tools.mjs)
  defining the background runner's claude_test_save / status / elapsed /
  progress / write_log / finish / read MCP tool descriptions, input schemas and
  result texts the model receives.
ccVersion: 2.1.314
-->



import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { createHash, randomBytes, timingSafeEqual } from 'node:crypto';
import { launcherConfig, loadConfig, assertRunsDirInsideProject, sessionRoot, appPointerInfo, reallyInsideDir, checkoutRootOf, trustedHome, withoutGit, browserServerEnv, withoutPrivateFolders, listSpecs, specsDirProblem, snapshotStemOk, stemOk, shown, draftTextFault, specNameOk, markedText, RC_FILE, RUN_ID, RUN_PLACEHOLDER, runStamp, fillRun, stepsRanFor } from './config.mjs';
import { runFolders, writeInRunFolder, withinProject, writingIn, anchorWords, keepsCreationTime, RUNNER_WORDS, LOG_MD_BYTES } from './runs.mjs';

export const SAVE_TOOL = 'claude_test_save';
export const STATUS_TOOL = 'claude_test_status';
export const ELAPSED_TOOL = 'claude_test_elapsed';
export const PROGRESS_TOOL = 'claude_test_progress';
export const LOG_TOOL = 'claude_test_write_log';
export const FINISH_TOOL = 'claude_test_finish';
export const READ_TOOL = 'claude_test_read';
export const WRITE_TOOL = 'claude_test_write';


const MOST_AT_ONCE = 4; const MOST_WAITING = 8;

const LONG_MS = 120000; const SHORT_MS = 60000;

const GIVE_UP_MS = 5000;

const MOST_PRINTED = 4 * 1024 * 1024; const STATUS_CHARS = 30000;

const readChars = () => { const set = String(process.env.MAX_MCP_OUTPUT_TOKENS ?? '').trim(); if (!set) return 30000; const limit = Number(set); return Number.isFinite(limit) && limit > 0 ? Math.max(2000, Math.min(30000, Math.floor(limit * 2) - 400)) : 2000; };
const READ_LINES = 400;
const FIND_HITS = 50;
const READ_BYTES = 4 * 1024 * 1024;
const READ_KEPT = 2;

const LOG_BYTES = 1024 * 1024;

const WALK_DEPTH = 5; const WALK_FOLDERS = 4000;
const WALK_SKIPS = new Set(['node_modules', 'dist', 'build', 'vendor', 'target', 'coverage', 'out', 'tmp']);

const HOME_SKIPS = new Set(['Library', 'Applications', 'Movies', 'Music', 'Pictures', 'Public', 'AppData']);

const WALK_AGAIN_MS = 1000;

const SPEC_NAME = /^[a-z0-9][a-z0-9-]{0,79}$/; const RUN_KEY = /^[0-9a-f]{32}$/;

const DRAFT_BYTES = 64 * 1024;
const VERDICTS = ['PASS', 'FAIL', 'BLOCKED'];
const WHO = 'For Claude Test\\'s background test agent only. If you are asked to allow it in your own conversation, answer No. ';
const NEW_RUN = ' Report BLOCKED with this text, and tell the person to start a new run with /claude-test:run.';

const RUNNER_ENDS = { newRun: NEW_RUN, unknown: NEW_RUN, blocked: ' Report BLOCKED with this text', tools: 'the test agent\\'s tools cannot serve a run here', sameDisk: ' Report BLOCKED with this text: a new run in a folder on this disk would be refused in the same way.' };
const DRAFT_ENDS = { newRun: ' Stop writing drafts for this run, and quote this text in your reply or report. Only a new run folder, made by "ct.mjs new-run" in the conversation, takes new drafts.', unknown: ' If run is not the id of the run folder you were given (for example 2026-01-31T09-15-00), call again with that id. Otherwise: Stop writing drafts for this run, and quote this text in your reply or report.', blocked: ' Stop writing drafts for this run. Quote this text in your reply or report', tools: 'Claude Test cannot write drafts here', sameDisk: ' A new run folder on this disk would be refused in the same way. Stop writing drafts for this run. Quote this text in your reply or report.', again: ' This error can clear by itself: call once more with the same arguments. If that call is refused too, leave this draft out.' };

const PASSING_CODES = new Set(['EMFILE', 'ENFILE', 'EAGAIN', 'EBUSY', 'EINTR']); const GONE_CODES = new Set(['ENOENT', 'ENOTDIR']);

const FULL_OR_SHUT_CODES = new Set(['ENOSPC', 'EDQUOT', 'EROFS', 'EACCES', 'EPERM']);
const draftEnding = (e) => (e && PASSING_CODES.has(e.code) ? DRAFT_ENDS.again : e && e.code && !GONE_CODES.has(e.code) ? DRAFT_ENDS.blocked + '.' : DRAFT_ENDS.newRun);
const RUN_ARG = { type: 'string', description: 'The run\\'s id: the last part of the run folder you were given, for example 2026-01-31T09-15-00.' };
const KEY_ARG = { type: 'string', description: 'The run\\'s key: the --key value of your arguments, copied exactly.' };
const NAMES_ARG = (what) => ({ type: 'array', items: { type: 'string' }, minItems: 1, maxItems: 24, description: what });

const TOOLS = [
  { name: SAVE_TOOL, description: WHO + 'First, before anything else in mode "run", and again only when its answer says so: save the drafts the person said yes to as specs, and seal the run. Pass the names as your arguments gave them, one entry for each name in the comma list: --save becomes "only", --replace stays "replace"; with neither, pass only run and key, and nothing is saved.', inputSchema: { type: 'object', properties: { run: RUN_ARG, key: { type: 'string', description: 'The --key value of your arguments, copied exactly.' }, only: NAMES_ARG('Drafts to save as NEW specs.'), replace: NAMES_ARG('Drafts that correct specs that exist.') }, required: ['run', 'key'], additionalProperties: false } },
  { name: STATUS_TOOL, description: WHO + 'The settings of the project that holds the run folder that "run" names: where its dev server answers, what the test browser may open, and its spec files, as JSON.', inputSchema: { type: 'object', properties: { run: RUN_ARG }, required: ['run'], additionalProperties: false } },
  { name: ELAPSED_TOOL, description: WHO + 'How long this run has taken so far.', inputSchema: { type: 'object', properties: { run: RUN_ARG }, required: ['run'], additionalProperties: false } },
  { name: PROGRESS_TOOL, description: WHO + 'Every call carries the run\\'s key. Before the first spec: { run, key, start: true }, with "stems" when your arguments named spec stems; the answer\\'s "order" is the order to run the specs in. After each verdict: { run, key, stem, verdict }, with retried: true when that verdict came from the spec\\'s one retry. Every answer may carry "drop": specs the person withdrew. It serves a run after its save and until its results.json is written.', inputSchema: { type: 'object', properties: { run: RUN_ARG, key: KEY_ARG, start: { type: 'boolean', description: 'true opens the run\\'s progress file.' }, stems: { type: 'array', items: { type: 'string' }, maxItems: 500, description: 'With start: the spec file stems of a run limited to some specs.' }, stem: { type: 'string', description: 'The spec file\\'s name without .md.' }, verdict: { type: 'string', enum: VERDICTS }, retried: { type: 'boolean', description: 'With stem and verdict: true when the spec was tried a second time, from a fresh page, and this is the verdict of that second try.' } }, required: ['run', 'key'], additionalProperties: false } },
  { name: LOG_TOOL, description: WHO + 'Write the run\\'s report, log.md in its run folder, with this text as the whole file. Call it again with the whole corrected text to change it. Then call ' + FINISH_TOOL + '. It works only after the run\\'s save and until its results.json is written.', inputSchema: { type: 'object', properties: { run: RUN_ARG, key: KEY_ARG, text: { type: 'string', description: 'The whole report: the header line and the verdict table first, then the log of each spec.' } }, required: ['run', 'key', 'text'], additionalProperties: false } },
  { name: FINISH_TOOL, description: WHO + 'After ' + LOG_TOOL + ': write results.json from the report\\'s verdict table, which ends the run. When the run or any spec ended BLOCKED, "why" is the one word that names the main cause.', inputSchema: { type: 'object', properties: { run: RUN_ARG, key: KEY_ARG, why: { type: 'string', enum: [...RUNNER_WORDS] } }, required: ['run', 'key'], additionalProperties: false } },
  { name: READ_TOOL, description: WHO + 'Read text that belongs to this run, one part at a time, and one call at a time. Every call carries the run\\'s key. { run, key, spec: "<stem>" }: a spec file of the project, by its file\\'s stem: "home" for .claude-test/specs/home.md, as the "order" of ' + PROGRESS_TOOL + ' gives it and as the "file" of each spec in the answer of ' + STATUS_TOOL + ' ends; never the spec\\'s heading. { run, key, snapshot: "<name>" }: a page snapshot that you saved into the run folder with a browser tool\\'s filename, by its file name without .snapshot.md; add find: "<words>" for only the lines that hold those words, each with the two lines before and after it. { run, key, log: true }: the report you wrote. Every answer begins with one line of this tool\\'s own that says which part it holds, of how many, and the "from" to pass for the next part. It works only after the run\\'s save and until its results.json is written. It takes no path.', inputSchema: { type: 'object', properties: { run: RUN_ARG, key: KEY_ARG, spec: { type: 'string', maxLength: 123 }, snapshot: { type: 'string', maxLength: 120 }, log: { type: 'boolean' }, from: { type: 'integer', minimum: 1 }, find: { type: 'string', minLength: 1, maxLength: 200 } }, required: ['run', 'key'], additionalProperties: false } },
  { name: WRITE_TOOL, description: 'Writes one Claude Test draft spec into proposed/ in the run folder named by run, with text as the whole file. For the person\\'s conversation and Claude Test\\'s background spec author. To change a draft, call again with the whole corrected text. It takes no path: it finds the project from run, and writes only into a run folder that Claude Test made on this machine and whose drafts are not saved yet. Never use it for any other file.', inputSchema: { type: 'object', properties: { run: RUN_ARG, name: { type: 'string', maxLength: 83, description: 'A draft\\'s file name: the spec\\'s title in lower-case ASCII letters, digits and hyphens, starting with a letter or digit and at most 80 characters long, then .md, for example cart-total.md. Never a path.' }, text: { type: 'string', description: 'The whole file, as plain text, at most 64 KiB.' } }, required: ['run', 'name', 'text'], additionalProperties: false } },
];


const started = new Set(); let stopsAtExit = false;
const MARK_ALONE = 'Claude Test cannot confirm that it made this run folder: made-here.again, a hard link to its made-here file, is missing, though this disk supports hard links. A command sandbox may have blocked the link, as it would in a new run folder, or Claude Test did not make this folder';


function madeHereFault(runDir, takesSecondName) {
  const at = (name) => { try { return fs.lstatSync(path.join(runDir, name), { bigint: true }); } catch { return null; } };
  const one = at('made-here'); const two = at('made-here.again'); const not = 'Claude Test cannot confirm that it made this run folder on this machine, because the made-here files that "ct.mjs new-run" puts in every run folder it makes are missing or changed';
  if (!one || !one.isFile()) return not;
  if (two) return two.isFile() && one.nlink === 2n && one.ino === two.ino && one.dev === two.dev ? null : not;
  if (one.nlink !== 1n) return not;
  return takesSecondName() ? MARK_ALONE : null;
}


function placeOwnFile(at, name, text) {
  const bytes = Buffer.from(text, 'utf8');
  let there = null; try { there = fs.lstatSync(at(name)); } catch { there = null; }
  if (there && there.isSymbolicLink()) return { why: 'a symbolic link stands at that name, and this tool does not write through one. Give the draft another name.' };
  if (there && !there.isFile()) return { why: 'a folder, or something else that is not a file, stands at that name. Give the draft another name.' };
  if (there && there.nlink > 1) return { why: 'the file at that name is a hard link (it has a second name), so it is not replaced. Give the draft another name.' };
  const tmp = at('.' + name + '.' + process.pid + '.' + randomBytes(6).toString('hex') + '.tmp');
  try {
    const fd = fs.openSync(tmp, fs.constants.O_WRONLY | fs.constants.O_CREAT | fs.constants.O_EXCL | (process.platform === 'win32' ? 0 : fs.constants.O_NOFOLLOW), 0o644);
    try { let put = 0; while (put < bytes.length) put += fs.writeSync(fd, bytes, put, bytes.length - put); } finally { fs.closeSync(fd); }
    fs.renameSync(tmp, at(name));
    return { bytes: bytes.length, sha256: createHash('sha256').update(bytes).digest('hex') };
  } finally { try { fs.unlinkSync(tmp); } catch {                                         } }
}
const stopChild = (child) => { try { if (process.platform !== 'win32' && child.pid) process.kill(-child.pid, 'SIGKILL'); } catch {                         } try { child.kill('SIGKILL'); } catch {            } };






export function makeRunTools({ send, settings = launcherConfig, root = sessionRoot, env = process.env, limits = {}, home = trustedHome, script = fileURLToPath(new URL('../ct.mjs', import.meta.url)) }) {
  const longMs = limits.longMs || LONG_MS; const shortMs = limits.shortMs || SHORT_MS; const giveUpMs = limits.giveUpMs || GIVE_UP_MS; const mostPrinted = limits.mostPrinted || MOST_PRINTED;
  const top = root();
  const homeDir = (() => { try { return fs.realpathSync(home()); } catch { return null; } })();
  const bound = new Map();
  let walked = null;
  let scrubState = () => '';
  let runValue = null; let forgetRunValues = () => {};
  let scrub = (text) => text;
  const keptLines = new Map();
  const toldYet = new Set();
  let servedKept = null;
  const turns = new Map();
  let running = 0;
  const answer = (id, text, isError = false) => send({ jsonrpc: '2.0', id, result: { content: [{ type: 'text', text }], ...(isError ? { isError: true } : {}) } });
  const refuse = (id, text) => answer(id, text, true);
  const words = (e) => shown(e && e.message ? e.message : e, 300);
  const quoted = (value) => typeof value === 'string' ? '"' + shown(value, 80) + '"' : 'a value that is not text';


  function argsOf(msg, allowed, nothing) {
    const a = msg.params.arguments;
    if (!a || typeof a !== 'object' || Array.isArray(a)) { refuse(msg.id, nothing + ': the arguments must be an object with ' + allowed.join(', ') + '.'); return null; }
    const other = Object.keys(a).find((k) => !allowed.includes(k));
    if (other !== undefined) { refuse(msg.id, nothing + ': this tool takes ' + allowed.join(', ') + ' and nothing else; it does not take ' + quoted(other) + '. It takes no path and no folder: it finds the project from run.'); return null; }
    return a;
  }

  function isRunId(id, run, nothing) {
    if (typeof run === 'string' && run.length <= 32 && RUN_ID.test(run)) return true;
    refuse(id, nothing + ': ' + (run === undefined ? 'run is missing. It' : quoted(run) + ' is not a run\\'s id. run') + ' must be the run\\'s id, which is the last part of the run folder you were given, like 2026-01-31T09-15-00.'); return false;
  }

  function namesFault(list, called) {
    if (list === undefined) return null;
    if (!Array.isArray(list) || list.length < 1 || list.length > 24) return called + ' must be a list of 1 to 24 draft names; with no draft to name, leave ' + called + ' out';
    const bad = list.find((n) => !specNameOk(n));
    if (bad !== undefined) return quoted(bad) + ' in ' + called + ' is not a draft\\'s name: a name is the draft\\'s file name without .md, in lower-case letters, digits and hyphens, and not readme, claude, agents or a Windows device name such as con';
    if (new Set(list).size !== list.length) return called + ' names a draft twice';
    return null;
  }

  const oncePerRealPath = (dirs) => { const seen = new Set(); return dirs.filter((dir) => { let real = dir; try { real = fs.realpathSync(dir); } catch {                } if (seen.has(real)) return false; seen.add(real); return true; }); };






  function foldersWithRuns() {
    const now = Date.now();
    if (walked && now >= walked.at && now - walked.at <= WALK_AGAIN_MS) return walked;
    const dirs = []; let left = WALK_FOLDERS; let level = [top];
    const isRealFolder = (p) => { try { return fs.lstatSync(p).isDirectory(); } catch { return false; } };
    for (let depth = 0; depth <= WALK_DEPTH && level.length && left > 0; depth++) {
      const next = [];
      for (const dir of level) {
        if (left-- <= 0) break;
        if (isRealFolder(path.join(dir, '.claude-test', 'runs'))) dirs.push(dir);
        if (depth === WALK_DEPTH) continue;
        let entries; try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { continue; }
        let underHome = false; try { underHome = homeDir !== null && fs.realpathSync(dir) === homeDir; } catch { underHome = false; }
        for (const name of entries.filter((e) => e.isDirectory() && !e.name.startsWith('.') && !WALK_SKIPS.has(e.name) && !(underHome && HOME_SKIPS.has(e.name))).map((e) => e.name).sort()) next.push(path.join(dir, name));
        const worktrees = path.join(dir, '.claude', 'worktrees');
        if (isRealFolder(path.join(dir, '.claude')) && isRealFolder(worktrees)) { try { for (const name of fs.readdirSync(worktrees, { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => e.name).sort()) next.push(path.join(worktrees, name)); } catch {                      } }
      }
      level = next;
    }
    walked = { at: Date.now(), dirs: oncePerRealPath(dirs), cutShort: left <= 0 };
    return walked;
  }








  function ownerOf(id, run, nothing, last = '', ends = RUNNER_ENDS) {
    const again = bound.get(run);
    if (again) {
      try {
        const cfg = again.cfg; const runDir = path.join(cfg.runsDir, run);
        if (appPointerInfo(cfg.projectDir)) throw new Error('the project\\'s .claude-testrc now names another folder as the app');
        assertRunsDirInsideProject(cfg);
        if (!fs.lstatSync(runDir).isDirectory() || fs.realpathSync(runDir) !== path.join(fs.realpathSync(cfg.runsDir), run)) throw new Error(shown(path.relative(cfg.projectDir, runDir), 200) + ' is no longer a plain folder directly inside the runs folder');
        return again;
      } catch (e) { refuse(id, nothing + ': ' + words(e) + '.' + ends.newRun + last); return null; }
    }

    const listed = (parent, name) => { try { return fs.readdirSync(parent).includes(name); } catch { return false; } };
    const has = (dir) => { try { return listed(dir, '.claude-test') && listed(path.join(dir, '.claude-test'), 'runs') && listed(path.join(dir, '.claude-test', 'runs'), run) && fs.lstatSync(path.join(dir, '.claude-test', 'runs', run)).isDirectory(); } catch { return false; } };
    let holders; let served; let cutShort = false;
    try {
      const at = Date.now();
      if (!servedKept || at < servedKept.at || at - servedKept.at > WALK_AGAIN_MS) { const now = settings(); servedKept = { at: Date.now(), served: [...(now.cfg ? [now.cfg] : []), ...(now.served || [])] }; }
      served = servedKept.served;
      holders = oncePerRealPath(served.map((c) => c.projectDir)).filter(has);
      if (!holders.length) { const found = foldersWithRuns(); cutShort = found.cutShort; holders = found.dirs.filter((dir) => has(dir) && reallyInsideDir(dir, top)); }
    } catch (e) { refuse(id, nothing + ': the Claude Test settings here could not be read: ' + words(e) + '.' + ends.newRun + last); return null; }
    const stoppedLooking = cutShort ? ' (this helper stopped looking after ' + WALK_FOLDERS + ' folders under ' + shown(top, 200) + ')' : '';
    if (!holders.length && cutShort) { refuse(id, nothing + ': Claude Test could not find the run folder named ' + run + ' among the first ' + WALK_FOLDERS + ' folders under ' + shown(top, 200) + '.' + ends.blocked + ', and tell the person to start Claude Code in the app\\'s folder, or to name the app with a line "app: <folder>" in ' + shown(path.join(top, RC_FILE), 200) + '.' + last); return null; }
    if (holders.length !== 1) { refuse(id, nothing + ': ' + (holders.length ? 'more than one folder in this session has a run folder named ' + run + ' (' + holders.slice(0, 5).map((dir) => shown(dir, 200)).join(', ') + (holders.length > 5 ? ', and ' + (holders.length - 5) + ' more' : '') + '), so this helper cannot tell which one is meant' + stoppedLooking : 'no project in this session has a run folder named ' + run) + '.' + (holders.length ? ends.newRun : ends.unknown) + last); return null; }
    const dir = holders[0];
    try {
      if (appPointerInfo(dir)) throw new Error('its .claude-testrc names another folder as the app');
      const cfg = served.find((c) => c.projectDir === dir) || loadConfig(dir);
      assertRunsDirInsideProject(cfg);
      if (!runFolders(cfg).includes(run)) {

        let halfMarked = false; try { const at = path.join(cfg.runsDir, run); const s = fs.lstatSync(at); halfMarked = fs.lstatSync(path.join(at, 'made-here')).isFile() && !fs.existsSync(path.join(at, 'made-here.again')) && !keepsCreationTime(s); } catch { halfMarked = false; }
        throw Object.assign(new Error(halfMarked ? 'this disk keeps neither hard links nor creation times, so ' + ends.tools : 'Claude Test did not make that folder on this machine'), { noNewRun: halfMarked });
      }
      let mask = (text) => String(text); try { mask = withoutPrivateFolders(cfg.projectDir); } catch {                                                                     }
      let within = null;
      if (process.platform !== 'win32') { try { within = withinProject(cfg.projectDir); } catch (e) { throw new Error('its folder could not be read just now (' + words((e && e.code) || e) + ')'); } }
      let checkout = null; try { checkout = checkoutRootOf(cfg.projectDir); } catch { checkout = null; }
      const entry = { cfg, mask, within, checkout, note: cutShort ? 'this helper stopped looking for run folders named ' + run + ' after ' + WALK_FOLDERS + ' folders under ' + shown(top, 200) + ': ' + shown(dir, 200) + ' is the only one it saw' : '' };
      bound.set(run, entry);
      return entry;
    } catch (e) { refuse(id, nothing + ': the run folder named ' + run + ' in ' + shown(dir, 200) + ' cannot be used: ' + words(e) + stoppedLooking + '.' + (e && e.noNewRun ? ends.sameDisk : ends.newRun) + last); return null; }
  }

  function marksOf(owner, run) {
    const at = (name) => { try { return fs.lstatSync(path.join(owner.cfg.runsDir, run, name)); } catch { return null; } };
    return { begun: ['saved.json', 'used-folder'].some((name) => { const s = at(name); return !!s && s.isFile(); }), finished: (() => { const s = at('results.json'); return !!s && s.isFile(); })() };
  }

  function isKeyOf(owner, run, key) {
    try {
      const wanted = writingIn(owner.within, owner.cfg.projectDir, path.join(owner.cfg.runsDir, run), (at) => {
        const fd = fs.openSync(at('save-key.sha256'), fs.constants.O_RDONLY | (process.platform === 'win32' ? 0 : fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK));
        try { const s = fs.fstatSync(fd); if (!s.isFile() || s.nlink > 1 || s.size > 200) return ''; const bytes = Buffer.alloc(Number(s.size)); fs.readSync(fd, bytes, 0, bytes.length, 0); return bytes.toString('utf8').trim(); } finally { fs.closeSync(fd); }
      });
      if (!/^[0-9a-f]{64}$/.test(wanted)) return { unchecked: 'the file that holds its hash, save-key.sha256 in the run folder, is not a plain file of one name with a hash in it' };
      return timingSafeEqual(Buffer.from(wanted, 'hex'), createHash('sha256').update(key).digest());
    } catch (e) { return { unchecked: e && e.code === 'ENOENT' ? (fs.existsSync(path.join(owner.cfg.runsDir, run)) ? 'the run folder holds no save-key.sha256' : 'the run folder is no longer there') : e && (e.code === 'ELOOP' || e.code === 'EMLINK') ? 'a link is at save-key.sha256 in the run folder' : words((e && e.code) || e) }; }
  }


  function isOpen(id, owner, run, nothing, key) {
    const keyIs = isKeyOf(owner, run, key);
    if (keyIs !== true && keyIs !== false) { refuse(id, nothing + ': the key of run ' + run + ' could not be checked (' + shown(keyIs.unchecked, 300) + '). Do not call again for this: go on without this record, and say so under Notes.'); return false; }
    if (!keyIs) { refuse(id, nothing + ': that is not the key of run ' + run + '. Pass the key that your arguments gave you (--key), as you passed it to ' + SAVE_TOOL + '. A first look has no key, and records nothing.'); return false; }
    const marks = marksOf(owner, run);
    if (marks.finished) { refuse(id, nothing + ': run ' + run + ' is finished (its results.json is written), and a finished run is not added to. Go on with your final message.'); return false; }
    if (!marks.begun) { refuse(id, nothing + ': the save of run ' + run + ' has not been made. In mode "run", call ' + SAVE_TOOL + ' first. If it was refused, this run cannot be recorded: end now, with the whole-run BLOCKED report and the save\\'s refusal in your final message. A first look records nothing.'); return false; }
    return true;
  }

  function inTurn(id, run, nothing, act, last = '', ends = RUNNER_ENDS) {
    const turn = turns.get(run) || { tail: Promise.resolve(), waiting: 0 };
    if (turn.waiting >= MOST_WAITING) return refuse(id, nothing + ': ' + MOST_WAITING + ' calls for run ' + run + ' are still waiting for their answers. Wait for them, then call again.');
    turn.waiting++; turns.set(run, turn);
    turn.tail = turn.tail.then(() => withoutGit(() => { const owner = ownerOf(id, run, nothing, last, ends); return owner ? act(owner) : undefined; })).catch((e) => refuse(id, nothing + ': ' + words(e) + '.')).finally(() => { if (--turn.waiting === 0) turns.delete(run); });
  }


  function childEnv(owner) {
    const kept = browserServerEnv(env);
    for (const name of Object.keys(kept)) {
      if (name.toUpperCase() === 'LD_LIBRARY_PATH') { delete kept[name]; continue; }
      if (name.toUpperCase() !== 'PATH') continue;
      const parts = kept[name].split(path.delimiter).filter((part) => path.isAbsolute(part) && !reallyInsideDir(part, owner.cfg.projectDir) && !(owner.checkout && reallyInsideDir(part, owner.checkout)));
      if (parts.length) kept[name] = parts.join(path.delimiter); else delete kept[name];
    }
    const own = { ...kept, CLAUDE_TEST_PROJECT_DIR: owner.cfg.projectDir, CLAUDE_TEST_OPENED_DIR: top, CLAUDE_TEST_NO_GIT: '1', CLAUDE_TEST_NO_TRIAL: '1', GIT_OPTIONAL_LOCKS: '0' };
    delete own.CLAUDE_TEST_PROJECT_ANCHOR; if (owner.within) own.CLAUDE_TEST_PROJECT_ANCHOR = anchorWords(owner.within);
    return own;
  }

  function fitStatus(text) {
    if (text.length <= STATUS_CHARS) return text;
    let all; try { all = JSON.parse(text); } catch { all = null; }
    const files = all && all.specs && Array.isArray(all.specs.files) ? all.specs.files : null;
    if (files) {
      const withFiles = (kept) => JSON.stringify({ ...all, specs: { ...all.specs, files: kept, filesLeftOut: { count: files.length - kept.length, note: 'this answer was too long, so the last spec files are left out of "files". The order in which to run the specs comes in the answer of your ' + PROGRESS_TOOL + ' start call, before the first spec. Each spec\\'s file is <stem>.md in the folder that "dir" names.' } } });
      let low = 0; let high = files.length;
      while (low < high) { const middle = Math.ceil((low + high) / 2); if (withFiles(files.slice(0, middle)).length <= STATUS_CHARS) low = middle; else high = middle - 1; }
      const shorter = withFiles(files.slice(0, low)); if (shorter.length <= STATUS_CHARS) return shorter;
      text = shorter;
    }
    const note = '\\n[Claude Test: this answer was ' + text.length + ' characters long. Its end is left out here.]';
    return cutWhole(text, STATUS_CHARS - note.length) + note;
  }

  function fitProgress(text) {
    if (text.length <= STATUS_CHARS) return text;
    let all; try { all = JSON.parse(text); } catch { all = null; }
    if (all && typeof all === 'object' && !Array.isArray(all)) {
      const kept = { ...all }; const leftOut = [];
      for (const key of Object.keys(all).filter((k) => !['runId', 'order', 'drop'].includes(k)).sort((a, b) => JSON.stringify(all[b]).length - JSON.stringify(all[a]).length)) {
        if (JSON.stringify({ ...kept, leftOut }).length <= STATUS_CHARS) break;
        delete kept[key]; leftOut.push(key);
      }
      const withOrder = (order, cut) => JSON.stringify({ ...kept, ...(order ? { order } : {}), ...(leftOut.length ? { leftOut: { parts: leftOut, note: 'this answer was too long, so these parts are left out.' } } : {}), ...(cut ? { orderLeftOut: { count: cut, note: 'the order was too long for one answer: its last ' + cut + ' names are left out. Run the specs named here in this order; the rest are the other spec files that ' + STATUS_TOOL + ' lists, in file-name order. Say so under Notes.' } } : {}) });
      const order = Array.isArray(kept.order) ? kept.order : null;
      const whole = withOrder(order, 0); if (whole.length <= STATUS_CHARS) return whole;
      if (order) {
        let low = 0; let high = order.length;
        while (low < high) { const middle = Math.ceil((low + high) / 2); if (withOrder(order.slice(0, middle), order.length - middle).length <= STATUS_CHARS) low = middle; else high = middle - 1; }
        const shorter = withOrder(order.slice(0, low), order.length - low); if (shorter.length <= STATUS_CHARS) return shorter;
        text = shorter;
      } else text = whole;
    }
    const note = '\\n[Claude Test: this answer was ' + text.length + ' characters long. Its end is left out here.]';
    return cutWhole(text, STATUS_CHARS - note.length) + note;
  }






  function runCt(id, owner, argv, told, { ms = shortMs, fit = null, last = null, recorded = null } = {}) {
    return new Promise((done) => {
      const ending = (final) => (last ? last(final) : '');
      if (running >= MOST_AT_ONCE) { const closing = ending(false); refuse(id, told.nothing + ': ' + MOST_AT_ONCE + ' calls of these tools are still running.' + (closing && !closing.startsWith('\\nThis run cannot be recorded yet') ? '' : ' Wait for their answers, then call again.') + closing); return done(); }
      let child;
      try { child = spawn(process.execPath, [script, ...argv], { cwd: owner.cfg.projectDir, env: childEnv(owner), stdio: ['ignore', 'pipe', 'pipe'], shell: false, windowsHide: true, detached: process.platform !== 'win32' }); }
      catch (e) { refuse(id, told.nothing + ': the Claude Test helper script could not be started (' + words(e) + ').' + (last ? ending(false) : NEW_RUN)); return done(); }
      running++; started.add(child);
      if (!stopsAtExit) { stopsAtExit = true; process.once('exit', () => { for (const c of started) stopChild(c); }); }
      let printed = ''; let notes = ''; let notesCut = false; let stopped = null; let ended = false;
      const end = (code, failure) => {
        if (ended) return; ended = true; clearTimeout(timer); running--; started.delete(child);
        let text = printed.trim(); let json = null; try { json = JSON.parse(text); } catch {                            }
        if (json !== null) { if (owner.note && json && typeof json === 'object' && !Array.isArray(json)) { json.projectSearch = owner.note; owner.note = ''; } text = JSON.stringify(json); }
        if (fit) text = fit(text);
        if (code === 0 && !stopped && !failure) { answer(id, text); if (recorded) { try { recorded(); } catch {                                       } } return done(); }
        if (!stopped && !failure && text) { refuse(id, text + ending(true)); return done(); }
        const why = stopped || (failure ? 'the Claude Test helper script could not be started (' + words(failure) + ')' : 'the command ended with code ' + code + ' and printed nothing');
        const tail = (notesCut ? (notes.includes('\\n') ? notes.slice(notes.indexOf('\\n') + 1) : '') : notes).trim().split('\\n').filter(Boolean).slice(-6).map((line) => shown(owner.mask(line), 400)).join('\\n');
        const closing = ending(false); const next = stopped ? told.stopped : told.notRun;
        refuse(id, told.what + ' did not finish: ' + why + '. ' + (typeof next === 'function' ? next(closing) : next) + (tail ? '\\nWhat the command said last:\\n' + tail : '') + closing);
        done();
      };
      const stop = (why) => { if (stopped) return; stopped = why; stopChild(child); setTimeout(() => end(null, null), giveUpMs).unref(); };
      const timer = setTimeout(() => stop('the command was stopped after ' + Math.round(ms / 1000) + ' seconds'), ms); timer.unref();
      child.stdout.setEncoding('utf8'); child.stdout.on('data', (chunk) => { if (printed.length + chunk.length > mostPrinted) stop('the command printed more than ' + mostPrinted + ' characters and was stopped'); else printed += chunk; });
      child.stderr.setEncoding('utf8'); child.stderr.on('data', (chunk) => { notes += chunk; if (notes.length > 16384) { notes = notes.slice(-16384); notesCut = true; } });
      child.on('error', (e) => end(null, e));
      child.on('close', (code) => end(code, null));
    });
  }






  function linesOf(owner, dir, name) {
    return writingIn(owner.within, owner.cfg.projectDir, dir, (at) => {
      let fd;
      if (process.platform === 'win32') { try { if (fs.lstatSync(at(name)).isSymbolicLink()) return { why: 'a link is at that name' }; } catch {                                         } }
      try { fd = fs.openSync(at(name), fs.constants.O_RDONLY | (process.platform === 'win32' ? 0 : fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK)); }
      catch (e) { return e && e.code === 'ENOENT' ? { why: 'there is no such file', missing: true } : { why: e && (e.code === 'ELOOP' || e.code === 'EMLINK') ? 'a link is at that name' : 'it could not be opened (' + words((e && e.code) || e) + ')' }; }
      try {
        const s = fs.fstatSync(fd, { bigint: true });
        if (!s.isFile()) return { why: 'something other than a plain file is at that name' };
        if (s.nlink > 1n) return { why: 'the file at that name has a second name', second: true };
        if (s.size > BigInt(READ_BYTES)) return { why: 'it is ' + s.size + ' bytes; the limit is 4 MiB (' + READ_BYTES + ' bytes)', tooLarge: true };
        const about = { bytes: Number(s.size), changed: new Date(Number(s.mtimeMs)).toISOString() };
        const key = s.dev + ':' + s.ino + ':' + s.size + ':' + s.mtimeNs + ':' + s.ctimeNs + ':' + scrubState();
        const kept = keptLines.get(key); if (kept) { keptLines.delete(key); keptLines.set(key, kept); return { lines: kept, ...about }; }
        const size = Number(s.size); const bytes = Buffer.alloc(size); let got = 0;
        while (got < size) { const n = fs.readSync(fd, bytes, got, size - got, got); if (!n) break; got += n; }
        let text; try { text = markedText(String(scrub(bytes.subarray(0, got).toString('utf8'))).replace(/\\r\\n/g, '\\n').replace(/\\r/g, '\\n')).text; } catch (e) { if (e instanceof RangeError) return { why: 'it holds a run of hidden or control characters too long to write out. Narrow the snapshot with depth, target or browser_find', narrow: true }; throw e; }
        const lines = text === '' ? [] : (text.endsWith('\\n') ? text.slice(0, -1) : text).split('\\n');
        keptLines.set(key, lines); while (keptLines.size > READ_KEPT) keptLines.delete(keptLines.keys().next().value);
        return { lines, ...about };
      } finally { fs.closeSync(fd); }
    });
  }


  function cutWhole(text, most) { let end = Math.max(0, Math.min(text.length, most)); const code = text.charCodeAt(end - 1); if (end < text.length && code >= 0xd800 && code <= 0xdbff) end--; return text.slice(0, end); }
  function heldLine(line, most) {
    if (line.length <= most) return line;
    let end = Math.max(0, most - 60); const code = line.charCodeAt(end - 1); if (code >= 0xd800 && code <= 0xdbff) end--;
    return line.slice(0, end) + ' [... ' + (line.length - end) + ' more characters of this line are left out]';
  }

  function partOf(what, file, from) {
    const total = file.lines.length; const first = '[' + READ_TOOL + ': ' + what + ', ' + file.bytes + ' bytes, last changed ' + file.changed + ': ';
    if (!total) return first + 'empty, 0 lines]';
    const out = []; let used = 0; let at = from;
    while (at <= total && out.length < READ_LINES) { const line = heldLine(file.lines[at - 1], readChars()); if (out.length && used + line.length + 1 > readChars()) break; out.push(line); used += line.length + 1; at++; }
    return first + 'lines ' + from + ' to ' + (at - 1) + ' of ' + total + (at <= total ? '; pass from: ' + at + ' for the next part]' : '; this is the last part]') + '\\n' + out.join('\\n');
  }

  function hitsOf(what, file, find, from) {

    const wanted = markedText(find).text.toLowerCase(); const hits = []; for (let i = 0; i < file.lines.length; i++) if (file.lines[i].toLowerCase().includes(wanted)) hits.push(i + 1);
    const first = '[' + READ_TOOL + ': ' + what + ', ' + file.bytes + ' bytes, last changed ' + file.changed + ': the lines that hold ' + quoted(markedText(find).text) + ': ';
    if (!hits.length) return first + 'none, in ' + file.lines.length + ' lines]';
    if (from > hits.length) return null;
    const out = []; let used = 0; let at = from; let given = 0;
    const isHit = new Set(hits);
    while (at <= hits.length && at - from < FIND_HITS) {
      const n = hits[at - 1]; const block = []; for (let k = Math.max(1, n - 2, given + 1); k <= Math.min(file.lines.length, n + 2); k++) { block.push((isHit.has(k) ? '> ' : '  ') + k + ': ' + heldLine(file.lines[k - 1], Math.min(2000, Math.floor(readChars() / 5) - 60))); }
      if (!block.length) { at++; continue; }
      given = Math.min(file.lines.length, n + 2);
      const text = block.join('\\n'); if (out.length && used + text.length + 2 > readChars()) break; out.push(text); used += text.length + 2; at++;
    }
    return first + 'hits ' + from + ' to ' + (at - 1) + ' of ' + hits.length + (at <= hits.length ? '; pass from: ' + at + ' for the next hits]' : '; these are the last]') + '\\n' + out.join('\\n\\n');
  }


  function stepsNotRan(owner, run, stem) {
    let text = null; let why = null;
    try {
      const wanted = (stem + '.md').normalize('NFC'); const entries = writingIn(owner.within, owner.cfg.projectDir, owner.cfg.specsDir, (at) => fs.readdirSync(at('.'), { withFileTypes: true })).filter((e) => e.name.normalize('NFC') === wanted && !e.name.startsWith('_') && e.name.toLowerCase() !== 'readme.md'); const entry = entries[0];
      if (entries.length > 1) return 'This PASS was not recorded. Two spec files have the name ' + quoted(stem) + ', written in different Unicode forms, so no PASS can be recorded for either. Record this spec as BLOCKED, put this answer in its Why cell, and copy it into its log.';
      if (!entry) return 'This PASS was not recorded. The specs folder has no spec named ' + quoted(stem) + '. Name a spec by its file\\'s stem: "home" for .claude-test/specs/home.md, as the "order" of ' + PROGRESS_TOOL + ' gives it; never its heading, and no ".md". Call again with the stem. If that is the stem you were given, record this spec as BLOCKED, put this answer in its Why cell, and copy it into its log.';
      if (!entry.isFile()) why = entry.isSymbolicLink() ? 'a link is at that name' : 'something other than a plain file is at that name';
      else { const file = linesOf(owner, owner.cfg.specsDir, entry.name); if (file.lines) text = file.lines.join('\\n'); else why = file.why; }
    } catch (e) { why = words(e); }
    if (text === null) return 'This PASS was not recorded. The spec ' + quoted(stem) + ' could not be read here (' + (why || 'the reason is not known') + '), and the read tool serves no steps from such a file, so no PASS can be recorded for it. Record this spec as BLOCKED, put this answer in its Why cell, and copy it into its log.';
    if (!text.includes(RUN_PLACEHOLDER)) return null;
    const stamp = runStamp(run); let state = null; try { state = runValue ? runValue(stamp) : null; } catch { state = null; }
    const said = stepsRanFor(state, stamp);
    return said.ok ? null : 'This PASS was not recorded. The spec ' + quoted(stem) + ' holds ' + RUN_PLACEHOLDER + ', and ' + said.why + '. Record this spec as FAIL "' + said.fail + '", or as BLOCKED with the reason if something outside the app stopped you, and copy this answer into the spec\\'s log.';
  }

  const CALLS = {
    [SAVE_TOOL](msg) {
      const id = msg.id; const nothing = 'Nothing was saved'; const a = argsOf(msg, ['run', 'key', 'only', 'replace'], nothing);
      if (!a || !isRunId(id, a.run, nothing)) return;
      if (typeof a.key !== 'string' || !RUN_KEY.test(a.key)) return refuse(id, nothing + ': ' + (a.key === undefined ? 'key is missing. It' : 'key') + ' must be the --key value of your arguments, copied exactly: 32 characters, each one of 0 to 9 and a to f. A first look is given no key and saves nothing.');
      const fault = namesFault(a.only, 'only') || namesFault(a.replace, 'replace'); if (fault) return refuse(id, nothing + ': ' + fault + '.');
      const cannot = '\\nThis run cannot be recorded: ' + PROGRESS_TOOL + ', ' + LOG_TOOL + ' and ' + FINISH_TOOL + ' serve a run only after its save. End now, before any page is loaded: your final message is the whole-run BLOCKED report, with this answer under its header, but not this last line.';
      const both = a.only && a.replace ? a.only.find((name) => a.replace.includes(name)) : undefined;
      if (both !== undefined) return refuse(id, nothing + ': ' + quoted(both) + ' is in only and in replace. Your arguments name it under both --save and --replace, and this cannot be mended here.' + cannot);



      inTurn(id, a.run, nothing, (owner) => {
        const canBeRecorded = () => { const marks = marksOf(owner, a.run); return marks.begun && !marks.finished; };

        const last = (final) => {
          if (canBeRecorded()) return '\\nThis run can still be recorded: quote this answer in your report, and go on.';
          if (final || marksOf(owner, a.run).finished || toldYet.has(a.run)) return cannot;
          toldYet.add(a.run);
          return '\\nThis run cannot be recorded yet. Call ' + SAVE_TOOL + ' once more. If that answer is an error again and does not end with "This run can still be recorded", end at once: your final message is the whole-run BLOCKED report, with that answer under its header, but not its last line.';
        };
        const again = 'Call ' + SAVE_TOOL + ' once more. If it answers that the drafts were already saved, the first save went through but may be incomplete: say so in your report, with the names you asked for.';
        const unlessDone = (text) => (closing) => (closing.startsWith('\\nThis run can still be recorded') || closing === cannot ? text.replace(' ' + again, '') : text);
        return runCt(id, owner, ['file', '--run', a.run, '--key', a.key, ...(a.only ? ['--only', a.only.join(',')] : []), ...(a.replace ? ['--replace', a.replace.join(',')] : []), ...(a.only || a.replace ? [] : ['--none'])], { nothing, what: 'The save', stopped: unlessDone('Some drafts may already be saved, and the run may already be sealed. ' + again), notRun: unlessDone('The drafts may or may not have been saved. ' + again) }, { ms: longMs, last });
      }, cannot);
    },
    [STATUS_TOOL](msg) {
      const id = msg.id; const nothing = 'Nothing was read'; const a = argsOf(msg, ['run'], nothing);
      if (!a || !isRunId(id, a.run, nothing)) return;
      const owner = ownerOf(id, a.run, nothing); if (!owner) return;
      const again = 'Call ' + STATUS_TOOL + ' once more. If it does not finish again, report BLOCKED with this text.';
      runCt(id, owner, ['status', '--runner', '--run', a.run], { nothing, what: 'The status command', stopped: again, notRun: again }, { ms: longMs, fit: fitStatus });
    },
    [ELAPSED_TOOL](msg) {
      const id = msg.id; const nothing = 'Nothing was read'; const a = argsOf(msg, ['run'], nothing);
      if (!a || !isRunId(id, a.run, nothing)) return;
      const owner = ownerOf(id, a.run, nothing); if (!owner) return;
      const again = 'Call ' + ELAPSED_TOOL + ' once more. If it does not finish again, go on without the time, and say so under Notes.';
      runCt(id, owner, ['elapsed', '--run', a.run], { nothing, what: 'The elapsed command', stopped: again, notRun: again });
    },
    [PROGRESS_TOOL](msg) {
      const id = msg.id; const nothing = 'Nothing was recorded'; const a = argsOf(msg, ['run', 'key', 'start', 'stems', 'stem', 'verdict', 'retried'], nothing);
      if (!a || !isRunId(id, a.run, nothing)) return;
      if (typeof a.key !== 'string' || !RUN_KEY.test(a.key)) return refuse(id, nothing + ': ' + (a.key === undefined ? 'key is missing. It' : 'key') + ' must be the --key value of your arguments, copied exactly: 32 characters, each one of 0 to 9 and a to f. A first look is given no key and records nothing.');
      const starts = a.start !== undefined || a.stems !== undefined; const records = a.stem !== undefined || a.verdict !== undefined || a.retried !== undefined;
      if (starts === records || (starts && a.start !== true)) return refuse(id, nothing + ': pass either { run, key, start: true } before the first spec, with stems: ["<stem>", ...] for a run limited to some specs, or { run, key, stem: "<the spec file\\'s name without .md>", verdict: "PASS" | "FAIL" | "BLOCKED" } after a verdict.');
      const opened = nothing + ' and the progress file was not opened: ';
      const unnamed = (stem) => typeof stem === 'string' ? 'the stem ' + quoted(stem) : 'a stem that is not text';
      if (starts) {
        if (a.stems !== undefined && (!Array.isArray(a.stems) || a.stems.length > 500)) return refuse(id, opened + 'stems must be a list of at most 500 spec file stems.');
        const stems = a.stems || []; const bad = stems.filter((s) => !stemOk(s));
        if (bad.length && bad.length === stems.length) return refuse(id, opened + (bad.length === 1 ? unnamed(bad[0]) + ' cannot be named here' : 'none of these stems can be named here') + '. Call again with start: true and no stems; then run only the specs that your arguments named, in file-name order with the ones tagged creates-data last, whatever the answer\\'s "order" lists, and say so under Notes.');
        if (bad.length) return refuse(id, opened + (bad.length === 1 ? unnamed(bad[0]) + ' cannot be named here' : 'these stems cannot be named here: ' + bad.slice(0, 8).map((s) => typeof s === 'string' ? quoted(s) : 'one that is not text').join(', ')) + '. Call again with start: true and the other stems. Run the specs left out all the same, and say so under Notes.');
        if (new Set(stems).size !== stems.length) return refuse(id, opened + 'stems names a spec twice. Call again with each stem once.');
      } else {
        if (a.stem === undefined) return refuse(id, 'This verdict was not recorded: stem is missing. Pass the spec file\\'s name without .md.');
        if (!stemOk(a.stem)) return refuse(id, 'This verdict was not recorded: ' + unnamed(a.stem) + ' cannot be named here. Say so under Notes, and leave that spec\\'s Screenshot cell empty.');
        if (!VERDICTS.includes(a.verdict)) return refuse(id, 'This verdict was not recorded: ' + (a.verdict === undefined ? 'verdict is missing. It' : quoted(a.verdict) + ' is not a verdict. verdict') + ' must be PASS, FAIL or BLOCKED, in capitals. Call again with the right word.');
        if (a.retried !== undefined && typeof a.retried !== 'boolean') return refuse(id, 'This verdict was not recorded: retried must be true or false. Call again with retried: true for a verdict of the spec\\'s second try, or leave it out.');
      }
      inTurn(id, a.run, nothing, (owner) => {
        if (!isOpen(id, owner, a.run, nothing, a.key)) return;


        let named = false; try { named = listSpecs(owner.cfg).some((spec) => path.basename(spec.file, '.md') === 'start'); } catch { named = false; }
        if (records && a.stem === 'start' && !named) return refuse(id, 'This verdict was not recorded: this project has no spec file named start.md. Pass start: true to open the progress file, or the stem of the spec you judged.');
        if (starts && named && a.stems && a.stems.length === 1 && VERDICTS.includes(a.stems[0].toUpperCase())) return refuse(id, opened + 'this project has a spec file named start.md, and a start with the one stem ' + quoted(a.stems[0]) + ' would be taken as a verdict for that spec. Call again with start: true and no stems, run only the spec you were given, and say so under Notes.');
        if (records && a.verdict === 'PASS') { const unran = stepsNotRan(owner, a.run, a.stem); if (unran) return refuse(id, unran); }
        const again = starts ? 'Call ' + PROGRESS_TOOL + ' with start: true once more; a second start only reads the progress file and gives the order. If it does not finish again, go on, and say so under Notes.' : 'The line may or may not be recorded. Go on, and say so under Notes.';
        return runCt(id, owner, starts ? ['progress', 'start', ...(a.stems || []), '--run', a.run] : ['progress', a.stem, a.verdict, ...(a.retried ? ['--retried'] : []), '--run', a.run], { nothing, what: 'The progress command', stopped: again, notRun: again }, { fit: fitProgress, ...(records && { recorded: forgetRunValues }) });
      });
    },
    [LOG_TOOL](msg) {
      const id = msg.id; const nothing = 'Nothing was written'; const a = argsOf(msg, ['run', 'key', 'text'], nothing);
      if (!a || !isRunId(id, a.run, nothing)) return;
      if (typeof a.key !== 'string' || !RUN_KEY.test(a.key)) return refuse(id, nothing + ': ' + (a.key === undefined ? 'key is missing. It' : 'key') + ' must be the --key value of your arguments, copied exactly: 32 characters, each one of 0 to 9 and a to f. A first look is given no key and records nothing.');
      if (typeof a.text !== 'string') return refuse(id, nothing + ': ' + (a.text === undefined ? 'text is missing. It' : 'text') + ' must be the whole report, as text.');
      if (!a.text.trim()) return refuse(id, nothing + ': text is empty. Pass the whole report: the header line and the verdict table first, then the log of each spec.');
      const given = Buffer.byteLength(a.text);
      if (given > LOG_BYTES) return refuse(id, nothing + ': the report is ' + given + ' bytes; the limit is 1 MiB (' + LOG_BYTES + ' bytes). Shorten the log of each spec, and call again with the whole report.');
      inTurn(id, a.run, nothing, (owner) => {
        if (!isOpen(id, owner, a.run, nothing, a.key)) return;
        const cfg = owner.cfg; const runDir = path.join(cfg.runsDir, a.run); const shownDir = shown(path.relative(cfg.projectDir, runDir), 200);


        try { assertRunsDirInsideProject(cfg); if (fs.realpathSync(runDir) !== path.join(fs.realpathSync(cfg.runsDir), a.run)) throw new Error(shownDir + ' is not a plain folder directly inside the runs folder'); }
        catch (e) { return refuse(id, nothing + ': ' + words(e) + '.' + NEW_RUN); }


        const { text: marked, replaced } = markedText(a.text.replace(/\\r\\n/g, '\\n').replace(/\\r/g, ' ')); const text = marked.endsWith('\\n') ? marked : marked + '\\n'; const bytes = Buffer.byteLength(text);
        if (bytes > LOG_MD_BYTES) return refuse(id, nothing + ': the report holds ' + replaced + ' characters that cannot be shown, and with each written out as its code point it is ' + bytes + ' bytes; the limit is 4 MiB (' + LOG_MD_BYTES + ' bytes). Leave out copied page text, and call again with the whole report.');
        let reason = ''; if (!writeInRunFolder(runDir, 'log.md', text, 0o644, owner.within, (words) => { reason = words; })) return refuse(id, nothing + ' in ' + shownDir + '/log.md: ' + shown(reason || 'the folder cannot be written', 300) + '. Put the report in your final message, and say this under Notes.');
        answer(id, JSON.stringify({ ok: true, file: path.relative(cfg.projectDir, path.join(runDir, 'log.md')), bytes, ...(replaced ? { replaced, note: replaced + ' characters that cannot be shown (control, invisible or text-direction characters) were written as their code points, like [U+202E]' } : {}) }));
      });
    },
    [READ_TOOL](msg) {
      const id = msg.id; const nothing = 'Nothing was read'; const a = argsOf(msg, ['run', 'key', 'spec', 'snapshot', 'log', 'from', 'find'], nothing);
      if (!a || !isRunId(id, a.run, nothing)) return;
      if (typeof a.key !== 'string' || !RUN_KEY.test(a.key)) return refuse(id, nothing + ': ' + (a.key === undefined ? 'key is missing. It' : 'key') + ' must be the --key value of your arguments, copied exactly: 32 characters, each one of 0 to 9 and a to f. A first look is given no key and reads nothing with this tool.');
      const forms = ['spec', 'snapshot', 'log'].filter((key) => a[key] !== undefined);
      const shapes = ' Pass { run, key, spec: "<a spec file\\'s stem: home for home.md>" }, { run, key, snapshot: "<the name you saved it under, without .snapshot.md>" } or { run, key, log: true }; "from" asks for a later part, and "find" goes with snapshot.';
      const plain = (value) => (typeof value === 'string' ? quoted(value) : shown(String(JSON.stringify(value)), 40));
      if (forms.length !== 1) return refuse(id, nothing + ': ' + (forms.length ? 'only one of spec, snapshot and log goes into one call; this call has ' + forms.join(' and ') : 'none of spec, snapshot and log is there') + '.' + shapes);
      if (a.log !== undefined && a.log !== true) return refuse(id, nothing + ': log must be true; ' + plain(a.log) + ' is not.' + shapes);
      if (a.from !== undefined && !(Number.isSafeInteger(a.from) && a.from >= 1)) return refuse(id, nothing + ': from must be a whole number of 1 or more; ' + plain(a.from) + ' is not. Pass the number that the part before this one named, or leave from out for the first part.');
      if (a.find !== undefined && forms[0] !== 'snapshot') return refuse(id, nothing + ': find goes with snapshot only.' + shapes);
      if (a.find !== undefined && (typeof a.find !== 'string' || !a.find.length || a.find.length > 200 || /[\\u0000-\\u001f\\u007f-\\u009f\\u2028\\u2029]/.test(a.find))) return refuse(id, nothing + ': find must be 1 to 200 characters of one line; ' + plain(a.find) + ' is not. It is looked for as it stands, whatever the case of its letters; it is no pattern.');
      const named = a.spec !== undefined ? a.spec : a.snapshot;
      if (forms[0] !== 'log' && (typeof named !== 'string' || !named.length || named.length > 123 || /[\\u0000-\\u001f\\u007f-\\u009f\\u2028\\u2029]/.test(named))) return refuse(id, nothing + ': ' + forms[0] + ' must be a name of 1 to 120 characters (a spec\\'s name may end in .md besides) with no control character in it; ' + plain(named) + ' is not.' + shapes);

      if (forms[0] === 'snapshot' && !snapshotStemOk(a.snapshot)) return refuse(id, nothing + ': no browser tool can have saved a snapshot under the name ' + quoted(a.snapshot) + '. Pass the name you gave the browser tool as filename, without the folder and without .snapshot.md: letters, digits, and . _ - inside it.');
      const owner = ownerOf(id, a.run, nothing); if (!owner) return;

      const keyIs = isKeyOf(owner, a.run, a.key);
      if (keyIs !== true && keyIs !== false) return refuse(id, nothing + ': the key of run ' + a.run + ' could not be checked (' + shown(keyIs.unchecked, 300) + '). Do not call again for this: say so under Notes.');
      if (!keyIs) return refuse(id, nothing + ': that is not the key of run ' + a.run + '. Pass the key that your arguments gave you (--key), as you passed it to ' + SAVE_TOOL + '. This tool serves your own run only.');
      const marks = marksOf(owner, a.run);
      if (marks.finished) return refuse(id, nothing + ': this run is finished. Paste your report from the text you wrote.');
      if (!marks.begun) return refuse(id, nothing + ': a first look gets nothing from this tool. Narrow the snapshot with depth, target or browser_find. In mode "run", call ' + SAVE_TOOL + ' first.');
      const cfg = owner.cfg; const runDir = path.join(cfg.runsDir, a.run); const from = a.from === undefined ? 1 : a.from;
      let what; let file;
      try {
        if (forms[0] === 'spec') {
          const problem = specsDirProblem(cfg); if (problem) return refuse(id, nothing + ': ' + shown(problem, 300) + '. Report BLOCKED for this spec with this text.');

          const stem = a.spec.toLowerCase().endsWith('.md') ? a.spec.slice(0, -3) : a.spec; const wanted = (stem + '.md').normalize('NFC');
          const inFolder = writingIn(owner.within, cfg.projectDir, cfg.specsDir, (at) => fs.readdirSync(at('.'), { withFileTypes: true }));
          const isSpec = (entry) => !entry.name.startsWith('_') && entry.name.toLowerCase() !== 'readme.md' && entry.name.toLowerCase().endsWith('.md');
          const listed = inFolder.find((entry) => entry.name.normalize('NFC') === wanted && isSpec(entry));
          if (!listed) {
            const how = 'Name a spec by its file\\'s stem: "home" for .claude-test/specs/home.md, as the "order" of ' + PROGRESS_TOOL + ' gives it; never its heading, and no folder.';
            if (/[\\\\/]/.test(a.spec)) return refuse(id, nothing + ': ' + quoted(a.spec) + ' holds a folder. ' + how + ' Call again with the stem.');

            let byHeading = null;
            try {
              byHeading = writingIn(owner.within, cfg.projectDir, cfg.specsDir, (at) => inFolder.filter((entry) => isSpec(entry) && entry.isFile()).slice(0, 200).find((entry) => {
                if (process.platform === 'win32') { try { if (fs.lstatSync(at(entry.name)).isSymbolicLink()) return false; } catch { return false; } }
                let fd; try { fd = fs.openSync(at(entry.name), fs.constants.O_RDONLY | (process.platform === 'win32' ? 0 : fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK)); } catch { return false; }

                try { const st = fs.fstatSync(fd); if (!st.isFile() || st.nlink !== 1) return false; const head = Buffer.alloc(2000); const got = fs.readSync(fd, head, 0, 2000, 0); const line = /^# (.+)$/m.exec(head.subarray(0, got).toString('utf8')); return !!line && line[1].trim() === stem.trim(); } catch { return false; } finally { fs.closeSync(fd); }
              })) || null;
            } catch { byHeading = null; }
            if (byHeading) return refuse(id, nothing + ': ' + quoted(a.spec) + ' is the heading of the spec whose stem is ' + quoted(byHeading.name.slice(0, -3)) + '. ' + how + ' Call again with the stem.');
            return refuse(id, nothing + ': the specs folder has no spec named ' + quoted(stem) + '. ' + how + ' If that is the stem you were given, report BLOCKED for this spec with this text.');
          }
          if (!listed.isFile()) return refuse(id, nothing + ': ' + quoted(stem) + ' in the specs folder is ' + (listed.isSymbolicLink() ? 'a link' : 'not a plain file') + ', and is not read. Report BLOCKED for this spec with this text.');
          what = 'the spec ' + quoted(stem); file = linesOf(owner, cfg.specsDir, listed.name);

          if (file.lines && file.lines.some((line) => line.includes(RUN_PLACEHOLDER))) { file = { ...file, lines: file.lines.map((line) => fillRun(line, a.run)) }; what += ' (' + RUN_PLACEHOLDER + ' in this file is shown as this run\\'s value, ' + runStamp(a.run) + ')'; }
        } else {
          assertRunsDirInsideProject(cfg); if (fs.realpathSync(runDir) !== path.join(fs.realpathSync(cfg.runsDir), a.run)) throw new Error('the run folder is not a plain folder directly inside the runs folder');
          const name = forms[0] === 'log' ? 'log.md' : a.snapshot + '.snapshot.md';
          what = forms[0] === 'log' ? 'the report log.md' : 'the snapshot ' + quoted(a.snapshot); file = linesOf(owner, runDir, name);
        }
      } catch (e) { return refuse(id, nothing + ': ' + words(e).replace('refusing to write run artifacts through it', 'nothing is read through it').replace('refusing to write run artifacts there', 'nothing is read there') + '.'); }
      if (file.why) return refuse(id, nothing + ' of ' + what + ': ' + file.why + '.' + (file.narrow ? '' : file.tooLarge && forms[0] === 'snapshot' ? ' Taking it again gives the same file: narrow the snapshot with depth, target or browser_find.' : forms[0] === 'snapshot' ? (file.missing ? ' Take the snapshot again with filename "<the run folder>/<name>.snapshot.md", then read it here.' : ' Taking it again under this name will not help: take the snapshot under the next working name (the next number), and say so under Notes.') : forms[0] === 'log' ? (file.missing ? ' Write the report with ' + LOG_TOOL + ' first.' : ' Write the whole report again with ' + LOG_TOOL + '.') : (file.second ? ' It is a hard link: the person can make it a file of its own (copy it, and put the copy in its place).' : '') + ' Report BLOCKED for this spec with this text.'));
      if (file.lines.length && from > file.lines.length && a.find === undefined) return refuse(id, nothing + ': ' + what + ' has ' + file.lines.length + ' lines, and from is ' + from + '. Call again without from.');
      if (a.find !== undefined) { const hits = hitsOf(what, file, a.find, from); return hits === null ? refuse(id, nothing + ': there are fewer than ' + from + ' hits. Call again without from.') : answer(id, hits); }
      answer(id, partOf(what, file, from));
    },
    [FINISH_TOOL](msg) {
      const id = msg.id; const nothing = 'Nothing was written'; const a = argsOf(msg, ['run', 'key', 'why'], nothing);
      if (!a || !isRunId(id, a.run, nothing)) return;
      if (typeof a.key !== 'string' || !RUN_KEY.test(a.key)) return refuse(id, nothing + ': ' + (a.key === undefined ? 'key is missing. It' : 'key') + ' must be the --key value of your arguments, copied exactly: 32 characters, each one of 0 to 9 and a to f. A first look is given no key and records nothing.');
      if (a.why !== undefined && !RUNNER_WORDS.includes(a.why)) return refuse(id, nothing + ': why must be one of ' + RUNNER_WORDS.join(', ') + '; ' + quoted(a.why) + ' is none of them. When none fits, leave why out.');
      const again = 'Call ' + FINISH_TOOL + ' once more: an answer that the run is finished means that results.json was written. If the command does not finish again, go on with your final message, and say so under Notes.';
      inTurn(id, a.run, nothing, (owner) => isOpen(id, owner, a.run, nothing, a.key) ? runCt(id, owner, ['finish', '--run', a.run, ...(a.why ? ['--why', a.why] : [])], { nothing, what: 'The finish command', stopped: 'results.json may or may not be written. ' + again, notRun: again }, { ms: longMs }) : undefined);
    },
    [WRITE_TOOL](msg) {
      const id = msg.id; const nothing = 'Nothing was written'; const a = argsOf(msg, ['run', 'name', 'text'], nothing);
      if (!a || !isRunId(id, a.run, nothing)) return;

      const stem = typeof a.name === 'string' && a.name.endsWith('.md') ? a.name.slice(0, -3) : null;
      if (stem === null || !SPEC_NAME.test(stem)) return refuse(id, nothing + ': ' + (a.name === undefined ? 'name is missing. It' : quoted(a.name) + ' is not a name this tool writes. The name') + ' must be the spec\\'s title in lower-case ASCII letters, digits and hyphens, starting with a letter or digit and at most 80 characters long, then .md (for example cart-total.md). It is a name, never a path.');
      if (!specNameOk(stem)) return refuse(id, nothing + ': this tool does not write ' + quoted(a.name) + '. Claude Code can read claude.md, agents.md and architecture.md as instructions, readme.md is never saved as a spec, and Windows reserves con, prn, aux, nul, and com or lpt followed by a digit (com1, lpt1) for devices, even with .md after them. Give the draft another name.');
      if (typeof a.text !== 'string') return refuse(id, nothing + ': ' + (a.text === undefined ? 'text is missing. It' : 'text') + ' must be the whole file, as text.');
      const text = a.text.replace(/^\\uFEFF/, '');
      if (!text.trim()) return refuse(id, nothing + ': text is empty or only white space. Pass the whole file.');
      const bytes = Buffer.byteLength(text);
      if (bytes > DRAFT_BYTES) return refuse(id, nothing + ': the text is ' + bytes + ' bytes; the limit is 64 KiB (' + DRAFT_BYTES + ' bytes). Shorten it, and call again with the whole text.');
      const bad = draftTextFault(text);
      if (bad >= 0) return refuse(id, nothing + ': the text holds U+' + text.codePointAt(bad).toString(16).toUpperCase().padStart(4, '0') + ' at character ' + ([...text.slice(0, bad)].length + 1 + (text.length < a.text.length ? 1 : 0)) + '. A draft may hold tabs and line ends, but not this character here. Remove it, and call again with the whole text.');
      inTurn(id, a.run, nothing, (owner) => {
        const marks = marksOf(owner, a.run);
        if (marks.begun || marks.finished) return refuse(id, nothing + ': run ' + a.run + (marks.finished ? ' has finished' : ' has had its drafts saved, or their save refused') + ', so it takes no more drafts.' + DRAFT_ENDS.newRun);
        const cfg = owner.cfg; const runDir = path.join(cfg.runsDir, a.run); const dir = path.join(runDir, 'proposed'); const shownDir = shown(path.relative(cfg.projectDir, dir), 200);


        let madeProposed = false; let marked = false;
        try {
          assertRunsDirInsideProject(cfg); if (fs.realpathSync(runDir) !== path.join(fs.realpathSync(cfg.runsDir), a.run)) throw new Error(shown(path.relative(cfg.projectDir, runDir), 200) + ' is not a plain folder directly inside the runs folder');
          writingIn(owner.within, cfg.projectDir, runDir, (at) => {
            try { fs.mkdirSync(at('proposed')); madeProposed = true; } catch (e) { if (!e || e.code !== 'EEXIST') throw e; }
            if (!fs.readdirSync(at('.')).includes('proposed') || !fs.lstatSync(at('proposed')).isDirectory()) throw new Error(shownDir + ' is not a plain folder: a link, or something other than a folder, stands at that name');
          });

          const mark = madeHereFault(runDir, () => writingIn(owner.within, cfg.projectDir, dir, (at) => {
            const probe = at('.probe-' + randomBytes(6).toString('hex')); const second = probe + '.again'; let made = false; let linked = false;
            try {
              const fd = fs.openSync(probe, fs.constants.O_WRONLY | fs.constants.O_CREAT | fs.constants.O_EXCL | (process.platform === 'win32' ? 0 : fs.constants.O_NOFOLLOW), 0o600); made = true; fs.closeSync(fd);
              try { fs.linkSync(probe, second); linked = true; return true; } catch (e) { if (e && ['EPERM', 'ENOTSUP', 'EOPNOTSUPP', 'ENOSYS'].includes(e.code)) return false; throw e; }
            } finally { if (linked) { try { fs.unlinkSync(second); } catch {            } } if (made) { try { fs.unlinkSync(probe); } catch {            } } }
          }));
          if (mark) throw Object.assign(new Error(mark), { alone: mark === MARK_ALONE });
          marked = true;
        } catch (e) {
          if (madeProposed && !marked) { try { writingIn(owner.within, cfg.projectDir, runDir, (at) => fs.rmdirSync(at('proposed'))); } catch {                   } }

          return refuse(id, nothing + ': ' + (e && e.alone ? e.message : words(e)) + '.' + (e && e.alone ? DRAFT_ENDS.blocked + '.' : draftEnding(e)));
        }
        let placed; try { placed = writingIn(owner.within, cfg.projectDir, dir, (at) => placeOwnFile(at, a.name, text)); } catch (e) { return refuse(id, nothing + ' in ' + shownDir + ' (' + words(e) + ').' + (e && FULL_OR_SHUT_CODES.has(e.code) ? ' If the disk is full or the folder cannot be written to, the person must fix that before any draft can be written.' + DRAFT_ENDS.blocked + '.' : draftEnding(e))); }
        if (placed.why) return refuse(id, nothing + ' at ' + shownDir + '/' + a.name + ': ' + placed.why);
        answer(id, JSON.stringify({ ok: true, file: path.relative(cfg.projectDir, path.join(dir, a.name)), bytes: placed.bytes, sha256: placed.sha256 }));
      }, '', DRAFT_ENDS);
    },
  };

  function take(msg) {
    if (!msg || typeof msg !== 'object' || Array.isArray(msg) || msg.method !== 'tools/call' || msg.id === undefined || !msg.params || typeof msg.params !== 'object' || typeof msg.params.name !== 'string' || !Object.hasOwn(CALLS, msg.params.name)) return false;

    try { withoutGit(() => CALLS[msg.params.name](msg)); } catch (e) { refuse(msg.id, 'Nothing was done: ' + words(e) + '.' + NEW_RUN); }
    return true;
  }

  const scrubWith = (fn, stateOf) => { if (typeof fn === 'function') { scrub = fn; scrubState = typeof stateOf === 'function' ? () => String(stateOf()) : () => ''; keptLines.clear(); } };

  const runValueWith = (stateOf, forget) => { if (typeof stateOf === 'function') runValue = stateOf; if (typeof forget === 'function') forgetRunValues = forget; };

  const runValues = () => [...bound.keys()].map(runStamp).filter(Boolean);
  return { tools: TOOLS, names: TOOLS.map((t) => t.name), take, scrubWith, runValueWith, runValues };
}
