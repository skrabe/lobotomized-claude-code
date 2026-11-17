<!--
name: 'Data: ct.mjs'
description: >-
  claude-test helper script (skills/run/scripts/ct.mjs) that the run skill has
  the model execute; its JSON output (status notes, needsInput questions,
  forClaude remedies, write-spec/file/finish errors) is read by the model.
ccVersion: 2.1.326
-->
#!/usr/bin/env node





















import fs from 'node:fs';
import { createHash, randomBytes } from 'node:crypto';
import path from 'node:path';
import http from 'node:http';
import https from 'node:https';
import net from 'node:net';
import { fileURLToPath } from 'node:url';
import { madeHereKey, madeHereMac, SECRET_FILE, loadConfig, commandLineClean, readStart, forgetStart, consentKey, localPortOf, readConsent, writeConsent, isLocalHost, reallyInsideDir, insideOpenedFolder, fromComment, listSpecs, ensureRunsDir, assertRunsDirInsideProject, parseSpec, mintSpecId, withSpecId, shown, shownDeep, shownText, draftTextFault, specNameOk, parseDotenv, resolveProjectDir, projectDirReason, projectsBelow, sessionRoot, specsDirProblem, appPointerInfo, rootConfiguresItself, sanitizeBrowserEnv, trackedClaudeTestSymlinks, RC_FILE, safeGit, gitOff, RUN_ID, joinWrappedCriteria, stemOk, withoutPrivateFolders, affectedPlan, fixPlan, touchedSince, reachesOnlyThisMachine, appRelative, RUN_PLACEHOLDER } from './lib/config.mjs';
import { ALLOW_TOOL, UP_TOOL, SHOW_TOOL } from './lib/allow-tool.mjs';
import { runFolders, runStart, writeInRunFolder, withinProject, writingIn as writingInFolder, keepsCreationTime, insideSomeCheckout, RUNNER_WORDS, LOG_MD_BYTES } from './lib/runs.mjs';
import { livePageFile, livePagePlan, prefsPath, readPrefs, writePrefs, openByHand } from './lib/open-page.mjs';
import { pathToFileURL } from 'node:url';
import { groupRefusedHosts, plainHostName, isBrowserServiceHost } from './lib/hosts.mjs';
import { toolsDir, mcpCliPath, installTools, toolsInstallInfo, findInstalledBrowser, INSTALLED_BROWSER_NAMES, browserSelection, browsersDir, useOwnBrowsersIfPresent, toolsProblem, browserProblem, chromeSandboxProblem, downloadBrowser, testBrowserMissing, browserMissingLibraries, wantsHeaded } from './lib/tools.mjs';
import { listSkills, authFileInfo, bypassHints } from './lib/signin.mjs';
import { readJson, discoverDevServer, candidateList, COMMON_PORTS, portOwner, cdTo, cdAndStart, recentWorkFrom, RECENT_COMMITS, RECENT_BULK } from './lib/discover.mjs';
import { environmentReport } from './lib/envreport.mjs';
import { writeReport } from './lib/live-page.mjs';

const args = process.argv.slice(2);
const projectDir = resolveProjectDir();


const STARTED_WITHIN = process.platform === 'win32' ? null : (() => { try { return withinProject(projectDir, 'Start the run again.', process.env.CLAUDE_TEST_PROJECT_ANCHOR || null); } catch (e) { return { refuse: e && e.code === 'CLAUDE_TEST_FOLDER_MOVED' ? shown(String(e.message), 200) + ', so nothing is written' : 'the project folder could not be read when this command started (' + shown(String((e && e.message) || e), 200) + '). Start the run again.' }; } })();
const withinOf = (cfg) => (cfg && path.resolve(cfg.projectDir) === path.resolve(projectDir) ? STARTED_WITHIN : { refuse: 'this command was started for another project folder' });

const writingIn = (cfg, dir, write) => writingInFolder(withinOf(cfg), cfg.projectDir, dir, write);

const makeFolderIn = (cfg, parent, name) => writingIn(cfg, parent, (at) => { try { fs.mkdirSync(at(name)); } catch (e) { if (!e || e.code !== 'EEXIST') throw e; } });

const readPlainFile = (file, most) => {
  let fd; try { fd = fs.openSync(file, fs.constants.O_RDONLY | (process.platform === 'win32' ? 0 : fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK)); } catch (e) { if (e && (e.code === 'ELOOP' || e.code === 'EMLINK')) throw new Error('a link is at that name'); throw e; }
  try { const s = fs.fstatSync(fd); if (!s.isFile() || s.nlink > 1) throw new Error('not a plain file (a link, a pipe, a folder, or a second name of another file)'); if (s.size > most) throw new Error('larger than ' + Math.round(most / 1024) + ' KB'); const bytes = Buffer.alloc(s.size); let got = 0; while (got < s.size) { const n = fs.readSync(fd, bytes, got, s.size - got, got); if (!n) break; got += n; } return bytes.subarray(0, got); }
  finally { fs.closeSync(fd); }
};
const PLAYWRIGHT_DOWNLOAD_HOST_SEEN = !!process.env.PLAYWRIGHT_DOWNLOAD_HOST;
sanitizeBrowserEnv();
const cmd = args[0] || 'status';
const scrubWhole = (x) => typeof x === 'string' ? shownText(x).replace(/\\r(?!\\n)|[\\u{E0000}-\\u{E007F}\\u{E0100}-\\u{E01EF}]/gu, ' ') : Array.isArray(x) ? x.map(scrubWhole) : x && typeof x === 'object' ? Object.fromEntries(Object.entries(x).map(([k, y]) => [k, scrubWhole(y)])) : x;
const out = (obj) => { const plain = obj && typeof obj === 'object' && !Array.isArray(obj); const { text, results, flagged: topFlagged, ...rest } = plain ? obj : {}; const clean = shownDeep(plain ? rest : obj); if (plain && typeof text === 'string') clean.text = text; if (plain && topFlagged) clean.flagged = scrubWhole(topFlagged); if (plain && Array.isArray(obj.held)) clean.held = obj.held.map((h) => { const { flagged: fl, ...hh } = h || {}; const c = shownDeep(hh); if (fl) c.flagged = scrubWhole(fl); return c; });                                                              if (plain && Array.isArray(results)) clean.results = results.map((r) => { const { text: t, flagged: fl, ...rr } = r || {}; const c = shownDeep(rr); if (typeof t === 'string') c.text = t; if (fl) c.flagged = scrubWhole(fl); return c; }); else if (plain && results !== undefined) clean.results = shownDeep(results); process.stdout.write(JSON.stringify(clean, null, 2) + '\\n'); };

async function get(url, timeoutMs = 8000) {


  const r = await getOnce(url, timeoutMs);
  let u; try { u = new URL(url); } catch { return r; }
  if (r.up || u.hostname !== 'localhost') return r;
  let unknown = r.up === null ? r : null;
  let refused = r.up === false ? r : null;
  for (const h of ['127.0.0.1', '[::1]']) {
    u.hostname = h; const r2 = await getOnce(u.href, timeoutMs);
    if (r2.up) return { ...r2, via: h };
    if (h === '[::1]' && r2.up === null && FAMILY_ABSENT.has(r2.code)) continue;
    if (r2.up === null && !unknown) unknown = { ...r2, via: h };
    if (r2.up === false && !refused) refused = { ...r2, via: h };
  }
  if (unknown && refused && unknown.via === undefined && FAMILY_ABSENT.has(unknown.code)) unknown = null;
  return unknown || refused || r;
}

function getOnce(url, timeoutMs = 8000) {
  return new Promise((resolve) => {
    const lib = url.startsWith('https:') ? https : http;
    const req = lib.get(url, { timeout: timeoutMs, headers: { 'user-agent': 'claude-test/0.1' } }, (res) => {


      resolve({ up: true, status: res.statusCode });
      res.destroy();
    });
    req.on('timeout', () => { req.destroy(); resolve({ up: null, error: 'timeout (no answer within ' + timeoutMs + ' ms) — unknown, not down; a dev server compiling its first page does this' }); });
    req.on('error', (e) => resolve(e.code !== 'ECONNREFUSED' || IN_SANDBOX ? { up: null, error: SANDBOX_CODES.has(e.code) || IN_SANDBOX ? 'blocked' : 'unknown', code: e.code, blocked: (SANDBOX_CODES.has(e.code) || IN_SANDBOX ? 'this process is not permitted to connect to ' + new URL(url).host + ' (' + e.code + ') — a sandbox (Claude Code\\'s, or the OS\\'s) is denying loopback connections' : 'connecting to ' + new URL(url).host + ' from the shell failed with ' + (e.code || e.message) + ', which is not a plain refusal') + '; the server may well be running — only the browser preflight decides' } : { up: false, error: 'refused (ECONNREFUSED) — nothing accepted the connection from the shell; still only advisory: the browser preflight decides' }));
  });
}



const SANDBOX_CODES = new Set(['EPERM', 'EACCES']);


const SANDBOX_WHY = (() => {
  if (process.env.SANDBOX_RUNTIME === '1') return 'SANDBOX_RUNTIME=1';
  const px = (process.env.HTTPS_PROXY || process.env.HTTP_PROXY || process.env.https_proxy || process.env.http_proxy || '');
  const np = (process.env.NO_PROXY || process.env.no_proxy || '');
  if (/^(https?:\\/\\/)?(srt[^/@]*@)?(localhost|127\\.0\\.0\\.1|\\[?::1\\]?):\\d+(\\/|$)/i.test(px) && /(^|,)\\s*(localhost|127\\.0\\.0\\.1)\\s*(,|$)/i.test(np)) return 'a local proxy with NO_PROXY=localhost (the shape Claude Code\\'s sandbox gives every command; possibly just a local proxy of yours)';
  return null;
})();
const IN_SANDBOX = SANDBOX_WHY !== null;
const FAMILY_ABSENT = new Set(['EADDRNOTAVAIL', 'EAFNOSUPPORT', 'ENETUNREACH', 'EHOSTUNREACH', 'EINVAL']);
let sandboxDenied = null;
async function portOpen(port, host = null, timeoutMs = 400) {
  if (!host) return (await portOpen(port, '127.0.0.1', timeoutMs)) || (await portOpen(port, '::1', timeoutMs));
  return new Promise((resolve) => {
    const s = net.connect({ port, host });
    const done = (v) => { s.destroy(); resolve(v); };
    s.setTimeout(timeoutMs, () => { sandboxDenied = sandboxDenied || 'timeout'; done(false); });
    s.on('connect', () => done(true));
    s.on('error', (e) => { if (e.code !== 'ECONNREFUSED' && !(host === '::1' && FAMILY_ABSENT.has(e.code))) sandboxDenied = e.code || 'error'; done(false); });
  });
}



function secretKeyCount(p) { try { return Object.values(parseDotenv(fs.readFileSync(p, 'utf8'))).filter((v) => v !== '').length; } catch { return 0; } }


function markedByClaudeTestDir(dir) { try { const ents = fs.readdirSync(path.join(dir, '.claude-test')); return ents.some((e) => e !== 'runs' && e !== '.gitignore'); } catch { return false; } }


function safeRel(rel) { return typeof rel === 'string' && rel.length > 0 && rel.length <= 80 && /^[\\w.@+ /-]+$/.test(rel) && !rel.split('/').includes('..') ? rel : null; }
function hasDevScript(d) { const pkg = readJson(path.join(d, 'package.json')); return !!(pkg && pkg.scripts && ['dev', 'start'].some((s) => pkg.scripts[s] || Object.keys(pkg.scripts).some((k) => k.startsWith(s + ':')))); }
function looksLikeApp(d) { const pkg = readJson(path.join(d, 'package.json')); return !!(pkg && pkg.scripts && ['dev', 'start', 'serve', 'preview'].some((s) => pkg.scripts[s] || Object.keys(pkg.scripts).some((k) => k.startsWith(s + ':')))) || ['manage.py', 'Gemfile', 'mix.exs', 'go.mod', 'Cargo.toml'].some((f) => fs.existsSync(path.join(d, f))); }
function appFoldersBelow(dir) {
  const out = [];
  const walk = (d, left) => { if (out.length >= 12) return; let ents; try { ents = fs.readdirSync(d, { withFileTypes: true }); } catch { return; } if (d !== dir && looksLikeApp(d)) { out.push(path.relative(dir, d)); return; } if (left === 0) return; for (const e of ents) if (e.isDirectory() && !e.name.startsWith('.') && !['node_modules', 'dist', 'build', 'vendor', 'target', 'coverage', 'out', 'tmp'].includes(e.name)) walk(path.join(d, e.name), left - 1); };
  walk(dir, 2);
  return out;
}


function folderVerdict(cfg) {
  const looksLikeProject = cfg.rcFound || markedByClaudeTestDir(cfg.projectDir) || ['package.json', 'manage.py', 'Gemfile', 'pyproject.toml', 'requirements.txt', 'Pipfile', 'go.mod', 'Cargo.toml', 'composer.json', 'mix.exs', 'deno.json', 'index.html', 'Procfile', 'docker-compose.yml', 'pom.xml', 'build.gradle', 'config.toml', 'hugo.toml', 'Makefile'].some((f) => fs.existsSync(path.join(cfg.projectDir, f))) || (() => { try { return fs.readdirSync(cfg.projectDir).some((e) => /\\.(csproj|sln|fsproj)$/.test(e)); } catch { return false; } })();
  const isWorkspaceRoot = ['pnpm-workspace.yaml', 'turbo.json', 'nx.json', 'lerna.json', 'rush.json'].some((f) => fs.existsSync(path.join(cfg.projectDir, f))) || !!(readJson(path.join(cfg.projectDir, 'package.json')) || {}).workspaces;
  const markedHere = cfg.rcFound || markedByClaudeTestDir(cfg.projectDir);






  let below = [], belowKind = 'app folders below it', blocked = false, suiteTrackedForLine = false, unprintable = 0;
  const ptr = cfg.projectDir === sessionRoot() ? appPointerInfo(sessionRoot()) : null;
  const rcConfiguresHere = cfg.rcFound && (cfg.projectDir !== sessionRoot() || rootConfiguresItself(cfg.projectDir)) && !(ptr && ptr.problem);
  if (!rcConfiguresHere) {
    const markedAll = projectsBelow(cfg.projectDir), appsAll = appFoldersBelow(cfg.projectDir).filter((a) => !markedAll.includes(a));
    const marked = markedAll.filter(safeRel), apps = appsAll.filter(safeRel);
    unprintable = markedAll.length + appsAll.length - marked.length - apps.length;
    below = [...marked, ...apps];
    if (marked.length && apps.length) belowKind = 'app folders below it (' + marked.join(', ') + ' already with Claude Test files)';
    else if (marked.length) belowKind = 'app folders below it with Claude Test files';
    const suiteTracked = (() => { try { return safeGit(cfg.projectDir, ['ls-files', '--', '.claude-test/specs']).toString().trim() !== ''; } catch { return false; } })();
    const selfIsApp = hasDevScript(cfg.projectDir) || suiteTracked; suiteTrackedForLine = suiteTracked;
    blocked = below.length >= 1 || unprintable > 0 || (isWorkspaceRoot && !selfIsApp && !markedHere) || !looksLikeProject || !!(ptr && ptr.problem);
    if (blocked && below.length && (selfIsApp || looksLikeProject)) below = suiteTracked ? ['.', ...below] : [...below, '.'];
  }
  const unprintableNote = unprintable ? ' (' + unprintable + ' app folder' + (unprintable > 1 ? 's' : '') + ' with ' + (unprintable > 1 ? 'names' : 'a name') + ' I cannot print safely ' + (unprintable > 1 ? 'are' : 'is') + ' not listed — if ' + (unprintable > 1 ? 'one of them' : 'it') + ' is the app, add "app: <folder>" to ' + path.join(sessionRoot(), RC_FILE) + ' yourself)' : '';
  const line = blocked ? 'BLOCKED — ' + (ptr && ptr.problem ? ptr.problem + '; ' : '') + (path.relative(sessionRoot(), cfg.projectDir) || 'the session root (' + cfg.projectDir + ')') + (below.length ? (markedByClaudeTestDir(cfg.projectDir) ? ' has a Claude Test suite AND ' : ' has ') + belowKind + ': ' + below.filter((b) => b !== '.').join(', ') + ' — which app?' + (markedByClaudeTestDir(cfg.projectDir) && !suiteTrackedForLine ? ' (the untracked suite here is usually a leftover of a run started in the wrong place; never add to it unanswered)' : below.includes('.') ? ' (this folder itself is one of the choices)' : ' (never write a suite here)') + '. status.needsInput carries the question — end the run with it (SKILL.md §6, NEEDS INPUT); only when the user\\'s request itself named the app folder is the helper started from there (from a shell: cd <dir> && node …/ct.mjs status)' : unprintable && looksLikeProject ? ' has app folders below it — which app? status.needsInput carries the question — end the run with it (SKILL.md §6, NEEDS INPUT)' : ' does not look like an app folder (no app manifest such as package.json, no .claude-testrc, no Claude Test specs); the helper must be started from the app folder you mean (from a shell: cd <dir> && node …/ct.mjs status), or ask the user which folder. If this folder IS the app, a .claude-testrc here (baseUrl: http://localhost:<port>) settles it') + unprintableNote : null;

  let elsewhere = [];
  const rootPtr = appPointerInfo(sessionRoot());
  if (!blocked && !markedHere && cfg.projectDir !== sessionRoot() && !(rootPtr && rootPtr.dir)) elsewhere = projectsBelow(sessionRoot()).filter(safeRel).map((r) => path.relative(cfg.projectDir, path.join(sessionRoot(), r)) || '.').filter((r) => r !== '.');


  let needsInput = null;
  const rootRc = path.join(sessionRoot(), RC_FILE);
  if (blocked && below.length) needsInput = { key: 'app', question: 'This folder holds more than one app, or is not itself the app. Which app should Claude Test use?', choices: below.map((b) => b === '.' ? { answer: 'this folder itself', rcLine: 'baseUrl: http://localhost:<port>', file: path.join(cfg.projectDir, RC_FILE) } : { answer: b, rcLine: 'app: ' + path.relative(sessionRoot(), path.join(cfg.projectDir, b)), file: rootRc }).filter((ch) => ch.answer === 'this folder itself' || safeRel(ch.rcLine.slice(5))), thenRun: 'run status again and carry on (when the answer came in a later turn, the person types /claude-test:run again instead). If a browser call already happened in this session and that app folder has its own .claude-testrc with origins or sign-in settings, the person runs /mcp → reconnect the claude-test browser server first, or starts a new session' };
  else if (blocked) needsInput = { key: 'app', question: (unprintable ? 'This folder has app folders below it whose names I cannot print safely. Which folder is the app?' : 'This folder does not look like the app. Which folder is it?') + ' (or, if it IS this one, say where the app answers)', choices: [{ answer: '<app folder>', rcLine: 'app: <relative path to the app folder>', file: rootRc }, { answer: 'this folder', rcLine: 'baseUrl: http://localhost:<port>', file: path.join(cfg.projectDir, RC_FILE) }], thenRun: 'run status again and carry on (when the answer came in a later turn, the person types /claude-test:run again instead). If a browser call already happened in this session and that app folder has its own .claude-testrc with origins or sign-in settings, the person runs /mcp → reconnect the claude-test browser server first, or starts a new session' };
  else if (elsewhere.length) needsInput = { key: 'app', question: 'This folder has no Claude Test specs, but ' + elsewhere.join(', ') + ' ' + (elsewhere.length === 1 ? 'does' : 'do') + '. Reuse those (point the root at that app), or start fresh here?', choices: [...elsewhere.map((e) => ({ answer: 'reuse ' + e, rcLine: 'app: ' + path.relative(sessionRoot(), path.join(cfg.projectDir, e)), file: rootRc })).filter((ch) => safeRel(ch.rcLine.slice(5))), { answer: 'start fresh here', rcLine: 'baseUrl: http://localhost:<port>', file: path.join(cfg.projectDir, RC_FILE) }], thenRun: 'run status again and carry on (when the answer came in a later turn, the person types /claude-test:run again instead). If a browser call already happened in this session and that app folder has its own .claude-testrc with origins or sign-in settings, the person runs /mcp → reconnect the claude-test browser server first, or starts a new session' };
  return { blocked, line, below, elsewhere, needsInput };
}
async function status() {
  const cfg = loadConfig(projectDir);
  const dev = discoverDevServer(cfg, { inSandbox: IN_SANDBOX });
  let baseUrl = cfg.baseUrl; let baseUrlSource = cfg.baseUrlSource; let probe = null; let answering = [];
  let otherPorts = [];
  let listeningBefore = [];


  let candidateUrls = cfg.baseUrl ? null : true;


  const candidates = candidateList(cfg, dev);
  if (IN_SANDBOX) {

    if (!baseUrl && dev.portHints.length) { baseUrl = 'http://localhost:' + dev.portHints[0] + '/'; baseUrlSource = 'guess from ' + (dev.portHintsSource || 'project files') + ' (not checked: sandboxed)'; }
    probe = { up: null, error: 'not checked', sandboxed: true };
  } else if (baseUrl && cfg.baseOrigin && !cfg.allowedOrigins.includes(cfg.baseOrigin) && !isLocalHost(new URL(baseUrl).hostname)) {
    probe = { up: null, error: 'not checked: ' + cfg.baseOrigin + ' is not a localhost address and waits for the person\\'s yes (needsConsent)' };
  } else if (baseUrl) {


    const asked = args.includes('--runner') ? new URL(baseUrl).origin + '/' : baseUrl;
    probe = await get(asked); if (asked !== baseUrl) probe = { ...probe, asked };
    if (!probe.up && !probe.blocked) {
      const want = Number(new URL(baseUrl).port) || (baseUrl.startsWith('https:') ? 443 : 80);
      const others = [...new Set([...dev.portHints, ...COMMON_PORTS, 8787])].filter((p) => p !== want);
      const listening = []; for (const p of others) if (await portOpen(p)) listening.push(p);
      if (listening.length) probe.alsoListening = listening;
    }
  } else {

    const candidates = [...new Set([...dev.portHints, ...COMMON_PORTS, 8787])];
    const listening = [];
    for (const p of candidates) if (await portOpen(p)) listening.push(p);
    listeningBefore = listening.slice(0, 32);
    const ownListening = listening.filter((p) => dev.portHints.includes(p));



    const rcNamed = new Set([].concat(cfg.rc && cfg.rc.allowedOrigins ? cfg.rc.allowedOrigins : []).map(localPortOf));
    const whose = new Map(ownListening.length ? [] : listening.filter((p) => !rcNamed.has(p)).map((p) => { let o = null; try { o = portOwner(p, cfg.projectDir); } catch {                   } return [p, o]; }));
    const otherPrograms = listening.filter((p) => whose.get(p) === 'other'); const startedHere = listening.filter((p) => whose.get(p) === 'this');
    const askable = listening.filter((p) => !otherPrograms.includes(p)).sort((a, b) => startedHere.includes(b) - startedHere.includes(a)); otherPorts = otherPrograms;
    answering = ownListening.length ? [ownListening[0]] : askable;
    if (ownListening.length) {
      baseUrl = 'http://localhost:' + ownListening[0] + '/'; baseUrlSource = 'detected: port ' + ownListening[0] + ' (named by ' + (dev.portHintFrom[ownListening[0]] || 'project files') + ') is listening'; probe = await get(baseUrl); if (listening.length > 1) probe.alsoListening = listening.filter((p) => p !== ownListening[0]);
    } else if (askable.length) {
      probe = { up: null, error: 'pages answer on common ports (' + askable.join(', ') + ') but nothing in this project names those ports — ' + (startedHere.length ? 'a program running from this project\\'s folder listens at ' + startedHere.join(', ') + '; ' : '') + (askable.length > startedHere.length ? 'which program listens at ' + askable.filter((p) => !startedHere.includes(p)).join(', ') + ' could not be told, so it may be another program on this machine; ' : '') + 'the preflight reports what they serve and asks which is yours', listening: askable, ...(startedHere.length ? { startedHere } : {}), ...(otherPrograms.length ? { otherPrograms } : {}) };
      if (dev.portHints.length) { baseUrl = 'http://localhost:' + dev.portHints[0] + '/'; baseUrlSource = 'guess from ' + (dev.portHintsSource || 'project files') + ' (nothing answered there from the shell)'; }
    } else if (otherPrograms.length && !sandboxDenied) {
      if (dev.portHints.length) { baseUrl = 'http://localhost:' + dev.portHints[0] + '/'; baseUrlSource = 'guess from ' + (dev.portHintsSource || dev.startCommandSource || 'project files') + ' (nothing accepted a connection from the shell)'; }
      probe = { up: false, error: 'only programs that work outside this project\\'s folder answer on common ports (' + otherPrograms.join(', ') + '): none is taken for this app, and none is asked about — advisory; the browser preflight decides', otherPrograms };
    } else if (sandboxDenied) {
      if (dev.portHints.length) { baseUrl = 'http://localhost:' + dev.portHints[0] + '/'; baseUrlSource = 'guess from ' + (dev.portHintsSource || 'project files') + ' (not checked: loopback denied)'; }
      probe = { up: null, error: 'not checked', sandboxed: true, code: sandboxDenied };
    } else if (dev.portHints.length) {
      baseUrl = 'http://localhost:' + dev.portHints[0] + '/'; baseUrlSource = 'guess from ' + (dev.portHintsSource || dev.startCommandSource || 'project files') + ' (nothing accepted a connection from the shell)'; probe = { up: false, error: 'refused on every candidate port from the shell — advisory; the browser preflight decides' };
    }
  }
  let gitDirty = null;
  try { gitDirty = safeGit(cfg.projectDir, ['status', '--porcelain', '--untracked-files=no'], { timeout: 60000 }).toString().trim() !== ''; } catch {                                                                    }
  if (gitOff()) { const at = args.indexOf('--run'); const id = at < 0 ? null : String(args[at + 1] ?? ''); const recorded = id && RUN_ID.test(id) ? recordedGit(cfg, id) : null; if (recorded) gitDirty = recorded.dirty; }
  const specsProblem = specsDirProblem(cfg);
  if (specsProblem) cfg.warnings.unshift('BLOCKED — ' + specsProblem + '. Do not write or run specs until this is fixed; report it and stop.');
  const specs = listSpecs(cfg);
  const verdict = folderVerdict(cfg); const below = verdict.below;
  let needsInput = verdict.needsInput;
  const links = trackedClaudeTestSymlinks(cfg.projectDir, sessionRoot());
  if (links.length) cfg.warnings.push('NOTE — symlink(s) inside .claude-test/ (committed, or present): ' + links.join('; ') + ' — nothing is written through them (run artifacts and spec files are refused there); mention it to the user, it is unusual');


  const ptrRoot = appPointerInfo(sessionRoot());
  if (!(ptrRoot && ptrRoot.dir) && cfg.projectDir !== sessionRoot() && projectsBelow(sessionRoot()).length >= 2 && (cfg.rcFound || cfg.signInApplies)) cfg.warnings.unshift('NOTE — the browser server of this session was configured from the session root, which has several app folders and no "app:" line: this folder\\'s own allowedOrigins and sign-in material are NOT active in it (the fence is the union of the apps\\' origins, no saved session is loaded). To test this folder signed in, add "app: ' + path.relative(sessionRoot(), cfg.projectDir) + '" to ' + path.join(sessionRoot(), RC_FILE) + ' and run /mcp → reconnect (or open Claude Code in this folder).');
  if (ptrRoot && ptrRoot.dir && ptrRoot.dir !== cfg.projectDir) cfg.warnings.unshift('NOTE — the root ' + RC_FILE + ' points the browser server at ' + path.relative(sessionRoot(), ptrRoot.dir) + ', not at this folder (' + (path.relative(sessionRoot(), cfg.projectDir) || '.') + '): this folder\\'s allowedOrigins and sign-in are not active in this session, and its address may be refused by the fence (ERR_BLOCKED_BY_CLIENT). To test this folder, change that line to "app: ' + path.relative(sessionRoot(), cfg.projectDir) + '" (or open Claude Code here) and run again.');
  const startCommandQuestion = !dev.startCommand && dev.startCommandCandidates && dev.startCommandCandidates.length > 1 ? { key: 'startCommand', question: 'Several ways to start this app were found; which one does this machine use?', choices: dev.startCommandCandidates.slice(0, 6).map((candidate) => { const line = cdAndStart(cfg.projectDir, candidate.cwd, candidate.command); return { answer: candidate.command + (candidate.cwd ? ' (in ' + candidate.cwd + ')' : ''), command: candidate.command, rcLine: 'startCommand: ' + candidate.command, file: path.join(cfg.projectDir, RC_FILE), ...(candidate.cwd ? { cwd: candidate.cwd } : {}), ...(line ? { line } : {}) }; }), thenRun: 'run status again and carry on (when the answer came in a later turn, the person types /claude-test:run again instead)' } : null;


  const toolsPresent = !!mcpCliPath({ report: true }); const toolsWhy = toolsPresent ? toolsProblem() : null; const browserWhy = browserProblem(cfg);
  let browserMissing = false; try { browserMissing = testBrowserMissing(cfg); } catch {                                  }
  let sandboxWhy = null; try { sandboxWhy = toolsWhy || (!toolsPresent && toolsProblem()) ? null : chromeSandboxProblem(cfg, null, { trial: process.env.SANDBOX_RUNTIME !== '1' && process.env.CLAUDE_TEST_NO_TRIAL !== '1' }); } catch {                                  }
  let libsMissing = []; try { libsMissing = !browserMissing && !browserWhy && toolsPresent && !toolsWhy ? browserMissingLibraries(cfg, { start: process.env.CLAUDE_TEST_NO_TRIAL !== '1' }) : []; } catch {                                  }
  let environment = null;
  if (!verdict.blocked) { try { environment = environmentReport(cfg, { tools: { installed: toolsPresent && !toolsWhy, problem: toolsWhy ? 'the tools folder is not private: ' + toolsWhy : null, remedy: 'run "node ' + fileURLToPath(import.meta.url) + ' install" in a terminal, or approve the claude_test_install tool of the claude-test browser server; the running server loads the tooling by itself afterwards (no reconnect)' } }); } catch (e) { environment = { summary: 'environment report failed: ' + (e.code || e.message), problems: [], notes: [] }; } }
  if (verdict.line) cfg.warnings.unshift(verdict.line);
  else if (verdict.elsewhere.length) cfg.warnings.unshift('NOTE — this folder has no Claude Test specs or .claude-testrc; under the session root they exist in: ' + verdict.elsewhere.join(', ') + ' — if one of those is the app you mean, the helper must be started from there (from a shell: cd <dir> && node …/ct.mjs status)');


  let runsDirWhy = null; try { assertRunsDirInsideProject(cfg); } catch (e) { runsDirWhy = e.message; }
  const past = runsDirWhy ? [] : pastRuns(cfg);
  const ran = past.find((r) => r.specs > 0); const paced = past.find((r) => r.judged > 0 && r.secondsPerSpec);
  const notFiled = specsProblem ? [] : specsNotFiled(cfg, specs);

  const candKey = (c) => 'http://localhost:' + c.port; const candKeys = cfg.baseUrl ? [] : candidates.filter((c) => !otherPorts.includes(c.port)).map(candKey);
  const hasYes = (k) => cfg.allowedOrigins.some((o) => consentKey(o) === k); const candAllowed = candKeys.filter(hasYes);

  const candAnswering = candKeys.filter((k) => answering.includes(Number(k.split(':').pop()))); const candOwn = candidates.filter((c) => c.own).map(candKey).filter((k) => candKeys.includes(k));
  const candPreferred = candAnswering.length ? [...new Set([...candAnswering, ...(candAnswering.some((k) => candOwn.includes(k)) ? [] : candOwn)])] : candOwn.length ? candOwn : candKeys;
  const otherKeys = otherPorts.map((p) => 'http://localhost:' + p);
  const askOrigins = [...cfg.pendingOrigins.filter((k) => !candKeys.includes(k) && !otherKeys.includes(k)), ...(candPreferred.some(hasYes) ? [] : candPreferred)];
  const waiting = [...new Set([...askOrigins, ...cfg.pendingHosts])];
  const needsConsent = waiting.length ? { addresses: askOrigins.map((a) => ({ address: a, localhost: isLocalHost(a.replace(/^https?:\\/\\//, '').replace(/:\\d+$/, '')) })), loadOnlyHosts: cfg.pendingHosts, tool: { name: ALLOW_TOOL, arguments: { address: waiting[0], project: cfg.projectDir } }, line: 'BLOCKED — you have not allowed the test browser to open: ' + waiting.join(', ') + '. A run starts when nothing is left waiting: allow the ones you want and take the rest out of ' + RC_FILE + ' (for guessed ports, set baseUrl there). You allow addresses once per project on this machine: type /claude-test in a Claude Code conversation and answer the dialog it opens, one address at a time. Claude Test has no terminal command for this.' } : null;
  const notReady = [...(needsInput ? ['which app is not settled (needsInput)'] : []), ...(needsConsent ? ['the person has not allowed the addresses the test browser would open (needsConsent)'] : []), ...(specsProblem ? ['the specs folder cannot be used: ' + specsProblem] : []), ...(runsDirWhy ? ['the runs folder cannot be used: ' + runsDirWhy] : []), ...(!toolsPresent ? ['the browser tooling is not installed (tools.note)'] : toolsWhy ? ['the browser tooling folder is not private (tools.problem)'] : []), ...(browserMissing && toolsPresent && !toolsWhy ? [wantsHeaded() ? 'there is no test browser for a window on this machine: the full Chromium build is not downloaded (tools.browser)' : 'there is no test browser on this machine (tools.browser)'] : []), ...(libsMissing.length ? ['the test browser cannot start on this machine: it needs the system ' + (libsMissing.length > 1 ? 'libraries ' : 'library ') + libsMissing.join(', ') + '. Fix: install the libraries Chrome needs. On Debian or Ubuntu, run this in a terminal (it runs apt-get with sudo): node ' + path.join(toolsDir(), 'node_modules', 'playwright-core', 'cli.js') + ' install-deps chromium' + (libsMissing.length === 1 && libsMissing[0] === 'libasound.so.2' ? ' (for this one library alone: sudo apt-get install libasound2t64, or libasound2 before Ubuntu 24.04)' : '') + '. On another Linux, install your distribution\\'s package for ' + (libsMissing.length > 1 ? 'each of them' : 'it') + '. Then type /claude-test again'] : []), ...(browserWhy ? [browserWhy] : []), ...(sandboxWhy ? [sandboxWhy] : [])];
  const startLine = cdAndStart(cfg.projectDir, dev.startCommandCwd, dev.startCommand); const cdPrefix = cdTo(cfg.projectDir, null);
  const setupLine = cdAndStart(cfg.projectDir, null, cfg.setupCommand);
  const lastRun = ran ? { runId: ran.runId, finishedAt: ran.finishedAt, outcome: ran.outcome, specs: ran.specs, secondsPerSpec: paced ? paced.secondsPerSpec : null } : null;
  const recentWork = !args.includes('--runner') && !verdict.blocked && !specsProblem && specs.filter((s) => !s.skipped).length === 0 ? recentWorkOf(cfg) : null;
  const answer = {
    ...(notFiled === null ? (specs.some((s) => !s.skipped) ? { specsNotFiled: { recordAbsent: true, count: 0, files: [], note: 'no .claude-test/filed record yet (specs written before this record existed, or by hand): nothing to compare. The record starts at the next write-spec, which adopts every spec then in the folder as-is and lists them — a notice, not a refusal' } } : {}) : notFiled.length ? { specsNotFiled: { files: notFiled.slice(0, 20), count: notFiled.length, note: 'edited or added outside write-spec — normal when the person wrote or changed them; otherwise Read each once and show it to the person before running (a notice, not a refusal)' } } : {}),
    ready: { runner: notReady.length === 0, firstRun: !specsProblem && specs.filter((s) => !s.skipped).length === 0, ...(notReady.length ? { reasons: notReady } : {}) },
    ...(lastRun ? { lastRun } : {}),
    projectDir: cfg.projectDir,
    projectDirReason: projectDirReason(cfg.projectDir), sessionRoot: sessionRoot(), ...(below.length ? { projectsBelow: below } : {}), ...(needsInput ? { needsInput } : {}), ...(needsConsent ? { needsConsent } : {}),
    config: { file: RC_FILE, found: cfg.rcFound, warnings: cfg.warnings },
    devServer: { baseUrl, source: baseUrlSource, up: probe ? probe.up : null, check: { name: UP_TOOL, arguments: { project: cfg.projectDir, ...(!cfg.baseUrl && listeningBefore.length ? { listening: listeningBefore } : {}) } }, verdictBy: 'the browser helper\\'s own check (devServer.check; SKILL.md §3 step 2), then the runner\\'s first page load: this view is advisory and never a reason to report the app down', ...(IN_SANDBOX || (probe && probe.blocked) || sandboxDenied ? { sandboxed: true, note: 'the shell could not check localhost reliably (' + (SANDBOX_WHY || ('connect gave ' + ((probe && probe.code) || sandboxDenied) + ', not a plain refusal')) + ' — a sandbox (typically Claude Code\\'s) or a local proxy setup), so "up" is unknown — NOT "down". Ask the browser helper, which can check localhost (devServer.check), before any run is started' + (cfg.baseUrl ? '.' : ': the address is ' + (baseUrl ? 'only a GUESS (' + baseUrlSource + ')' : 'unknown') + ' and ports cannot be scanned from here, so the preflight tries candidateUrls in order; if none serves this project, tell the user "if your server is running, tell me where — baseUrl: http://localhost:PORT in ' + RC_FILE + '; otherwise start it" rather than claiming it is down.') + ' A dev server started from inside the sandbox could not be reached by the test browser: SKILL.md §3 step 2 says how it is started outside.' } : {}), ...(candidateUrls ? { candidateUrls: candidates.filter((c) => !otherPorts.includes(c.port) && (!candAllowed.length || candAllowed.includes(candKey(c)))).map((x) => x.url) } : {}), candidates, probe, startCommand: dev.startCommand, startCommandSource: dev.startCommandSource, ...(startLine ? { startLine } : {}), ...(cdPrefix ? { cdPrefix } : {}), ...(startCommandQuestion ? { startCommandQuestion } : {}), ...(dev.startCommandCwd ? { startCommandCwd: dev.startCommandCwd } : {}), ...(dev.launchIgnored ? { launchJsonIgnored: dev.launchIgnored } : {}), ...(dev.unreadable ? { unreadable: dev.unreadable } : {}), ...(dev.startCommandNote ? { startCommandNote: dev.startCommandNote, startCommandCandidates: dev.startCommandCandidates.map((k) => { const line = cdAndStart(cfg.projectDir, k.cwd, k.command); return line ? { ...k, line } : k; }) } : {}), recipes: dev.recipes },
    setupCommand: cfg.setupCommand ? { command: cfg.setupCommand, source: RC_FILE, ...(setupLine ? { line: setupLine } : {}), note: 'The person is asked before it runs, each time (SKILL.md §3 step 3). It runs after the server answers and before the first spec, and again in later runs, so it must be safe to run twice. With no line, the person runs it.' } : null,
    browser: { allowedOrigins: cfg.allowedOrigins, reachableHosts: cfg.reachableHosts || [], pendingOrigins: cfg.pendingOrigins, pendingHosts: cfg.pendingHosts, note: (cfg.baseUrl ? 'the bundled browser only loads these origins' : 'no baseUrl yet: the bundled browser can load ONLY the candidate addresses under devServer.candidates (and their 127.0.0.1 / [::1] twins) — a baseUrl line in ' + RC_FILE + ' pins it to your app') + '; every address, a candidate found on this machine included, is opened only after the person allows it (needsConsent), once per project on this machine' },
    tools: { installed: !!mcpCliPath({ report: true }) && !toolsProblem(), dir: toolsDir(), ...(browserMissing ? { browser: { missing: true, ...(wantsHeaded() ? { forWindow: true } : {}), command: 'node ' + fileURLToPath(import.meta.url) + ' install chromium' + (wantsHeaded() ? ' --headed' : ''), note: 'no Google Chrome that Claude Test can use here or that this run chose, and no downloaded test browser of the kind it needs' + (wantsHeaded() ? ' (with CLAUDE_TEST_HEADED=1, the full build, for a window)' : '') + '. Where the browser helper offers its install dialog (onboarding.md, "Machine"), its Accept installs the test browser, the tooling too when it is missing. Else this one command installs the tooling when it is missing and downloads the test browser; claude_test_install downloads it only from a mirror the person names. The person runs it once, in their own terminal, not with ! at the Claude Code prompt, where Claude Code\\'s sandbox can keep the download from being saved' } } : installedUse(cfg)), ...(toolsInstallInfo() ? { pinned: !!toolsInstallInfo().pinned, install: toolsInstallInfo().mode } : mcpCliPath({ report: true }) ? { pinned: 'unknown', install: 'installed without a checksum record — run install once to pin it' } : {}), ...(mcpCliPath({ report: true }) && toolsProblem() ? { problem: 'the tools folder is not private: ' + toolsProblem() + ' — the browser server refuses to run from it until fixed' } : {}), note: mcpCliPath({ report: true }) ? (toolsProblem() ? 'browser tooling present but NOT usable (see problem)' : 'browser tooling present') : 'browser tooling NOT installed here: the bundled browser server offers only browser_setup_needed / claude_test_install until the user runs "node ' + fileURLToPath(import.meta.url) + ' install" (or approves claude_test_install); the running server then loads the tooling by itself and the next run has the browser tools — /mcp → Reconnect only if it does not' },
    signIn: {
      appliesToBaseUrl: cfg.signInApplies, note: cfg.signInNote,
      storageState: cfg.storageState.inUse ? { inUse: true, source: cfg.storageState.source, path: cfg.storageState.path, ...savedSessionFacts(cfg.storageState.path) } : { inUse: false, putItAt: cfg.storageState.defaultPath },
      skills: listSkills(cfg.projectDir).map((s) => ({ name: s.name, description: s.description ? s.description.slice(0, 160) : undefined, run: !!s.run, check: !!s.check, timeoutS: s.timeoutS, problem: s.problem || undefined })),
      howTo: signInHowTo(cfg),
      secrets: cfg.secretsFile.inUse ? { inUse: true, source: cfg.secretsFile.source, putItAt: cfg.secretsFile.path, keyCount: secretKeyCount(cfg.secretsFile.path) } : { inUse: false, putItAt: cfg.secretsFile.defaultPath },
    },
    ...(environment ? { environment } : {}),
    specs: specsProblem ? { dir: path.relative(cfg.projectDir, cfg.specsDir), error: specsProblem + ' — fix that before any run (BLOCKED)', count: 0, files: [] } : { dir: path.relative(cfg.projectDir, cfg.specsDir), count: specs.filter((s) => !s.skipped).length, files: specs },
    runsDir: path.relative(cfg.projectDir, cfg.runsDir),
    git: { dirty: gitDirty },
    ...(recentWork ? { recentWork } : {}),
    auth: { bypassHints: bypassHints(cfg.projectDir) },
  };
  if (!args.includes('--runner')) { out(answer); return; }



  const withoutFolders = withoutPrivateFolders(cfg.projectDir);
  const everyString = (value) => typeof value === 'string' ? withoutFolders(value) : Array.isArray(value) ? value.map(everyString) : value && typeof value === 'object' ? Object.fromEntries(Object.entries(value).map(([key, inner]) => [key, everyString(inner)])) : value;
  out(everyString(answer));
}



function recentWorkOf(cfg) {
  const git = (argv) => safeGit(cfg.projectDir, ['-c', 'core.quotePath=false', ...argv], { maxBuffer: 4 * 1024 * 1024, timeout: 30000 }).toString();
  try {
    const prefix = git(['rev-parse', '--show-prefix']).trim();
    let log = ''; try { log = git(['log', '-n', String(RECENT_COMMITS), '--no-merges', '--no-renames', '--no-ext-diff', '--no-textconv', '--no-show-signature', '--format=%x01%P', '--name-only', '--', '.']); } catch {                                            }
    const status = git(['status', '--porcelain', '--no-renames', '--untracked-files=all', '--', '.']);
    const isFile = (f) => { try { return reallyInsideDir(path.join(cfg.projectDir, f), cfg.projectDir) && fs.lstatSync(path.join(cfg.projectDir, f)).isFile(); } catch { return false; } };
    const found = recentWorkFrom({ log, status, prefix, isFile });
    return { ...found, note: found.files.length ? 'paths and counts from git only: the last ' + RECENT_COMMITS + ' commits in this folder and the uncommitted changes (the first commit and any commit touching more than ' + RECENT_BULK + ' app files are not counted). The crawl and the outline lean towards journeys through these files (onboarding.md, "What changed lately")' : 'no user-facing file changed lately (only the first commit, or only configuration, tests or docs): no preference — the outline follows the app\\'s core journeys' };
  } catch { return null; }
}

function authRel(cfg) { const p = path.join(path.dirname(fileURLToPath(import.meta.url)), 'ct-auth.mjs'); const r = path.relative(cfg.projectDir, p); return r.startsWith('..') ? p : r; }

function signInHowTo(cfg) {
  const usable = listSkills(cfg.projectDir).filter((s) => s.run && !s.problem);
  return {
    interactive: 'node ' + authRel(cfg) + ' login',
    skill: usable.length === 1 ? 'node ' + authRel(cfg) + ' sign-in ' + usable[0].name : usable.length > 1 ? usable.map((s) => 'node ' + authRel(cfg) + ' sign-in ' + s.name) : null,
    scaffold: 'node ' + authRel(cfg) + ' scaffold-sign-in',
    logout: 'node ' + authRel(cfg) + ' logout',
  };
}
function savedSessionFacts(p) { const i = authFileInfo(p); return i.present ? { cookies: i.cookies, origins: i.origins, empty: i.empty, savedMinutesAgo: i.savedMinutesAgo, earliestCookieExpiry: i.earliestCookieExpiry, expired: i.expired, ...(i.problem ? { problem: i.problem } : {}) } : {}; }

function newRun() {
  const cfg = loadConfig(projectDir);
  const symlinks = trackedClaudeTestSymlinks(cfg.projectDir, sessionRoot()); if (symlinks.length) process.stderr.write('[claude-test] note: symlink(s) inside .claude-test/: ' + symlinks.join('; ') + '\\n');
  const v = folderVerdict(cfg); if (v.blocked || (v.needsInput && v.needsInput.key === 'app')) { out({ error: v.line || v.needsInput.question, ...(v.needsInput ? { needsInput: v.needsInput } : {}) }); process.exit(2); }
  const sp = specsDirProblem(cfg); if (sp) { out({ error: sp }); process.exit(1); }
  try { ensureRunsDir(cfg); } catch (e) { out({ error: e.message }); process.exit(1); }
  const d = new Date();
  const pad = (n) => String(n).padStart(2, '0');
  let id = d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()) + 'T' + pad(d.getHours()) + '-' + pad(d.getMinutes()) + '-' + pad(d.getSeconds());
  let runDir = path.join(cfg.runsDir, id);
  for (let i = 2; fs.existsSync(runDir); i++) runDir = path.join(cfg.runsDir, id + '-' + i);
  fs.mkdirSync(runDir);
  let folders = []; try { folders = runFolders(cfg); } catch {                                      } endOldPages(cfg, folders.filter((d) => d !== path.basename(runDir)));
  try { for (const old of folders.slice(0, -8)) { const fdir = path.join(cfg.runsDir, old, 'frames'); try { if (fs.lstatSync(fdir).isDirectory()) fs.rmSync(fdir, { recursive: true, force: true }); } catch {            } } } catch {                             }
  let saveKey = null; try { saveKey = randomBytes(16).toString('hex'); fs.writeFileSync(path.join(runDir, 'save-key.sha256'), createHash('sha256').update(saveKey).digest('hex') + '\\n', { flag: 'wx', mode: 0o600 }); } catch (e) { out({ error: 'could not write this run\\'s key into ' + path.relative(cfg.projectDir, runDir) + ' (' + shown(String(e && e.message || e), 160) + '): without it the run\\'s save step refuses, so no run folder was handed out' }); try { fs.rmSync(runDir, { recursive: true, force: true }); } catch {                } process.exit(1); }
  let markNote = null; let markWarning = null; try { const key = madeHereKey(); fs.writeFileSync(path.join(runDir, 'made-here'), 'Claude Test made this run folder on this machine.\\n' + (key ? 'mac: ' + madeHereMac(key, path.basename(runDir)) + '\\n' : ''), { flag: 'wx' }); fs.linkSync(path.join(runDir, 'made-here'), path.join(runDir, 'made-here.again')); } catch (e) { try { if (insideSomeCheckout(cfg.projectDir) && !keepsCreationTime(fs.lstatSync(runDir))) markNote = 'this disk keeps neither hard links nor creation times, so the background test agent\\'s tools will not serve this run folder: run the specs from a folder on another disk'; } catch {                                                       } if (!markNote && !['ENOTSUP', 'EOPNOTSUPP', 'ENOSYS'].includes(e && e.code) && fs.existsSync(path.join(runDir, 'made-here'))) markWarning = 'Claude Test could not make made-here.again, a hard link to this run folder\\'s made-here file (error: ' + shown(String((e && e.code) || e), 40) + ').' + (e && e.code === 'EPERM' ? ' If this disk keeps no hard links (FAT or exFAT, for example), nothing changes. If a command sandbox blocked it, Claude Test cannot write new or changed tests for this run' : ' If a command sandbox blocked it, Claude Test cannot write new or changed tests for this run. Please report it with /bug'); }

  try { const at = gitState(cfg.projectDir); if (at) fs.writeFileSync(path.join(runDir, 'git.json'), JSON.stringify(at) + '\\n', { flag: 'wx' }); } catch {                                                                            }
  out({ runId: path.basename(runDir), runDir: path.relative(cfg.projectDir, runDir), absolute: runDir, ...(saveKey ? { saveKey } : {}), ...(markNote ? { note: markNote } : {}), ...(markWarning ? { warning: markWarning } : {}), ...(() => { const page = livePageFile(cfg, path.basename(runDir)); return { livePage: pathToFileURL(page).href, ...(openByHand(page) ? { livePageByHand: openByHand(page) } : {}), ...(() => { const plan = livePagePlan(cfg); return plan.opens ? { livePageShow: { name: SHOW_TOOL, arguments: { project: cfg.projectDir, run: path.basename(runDir) } } } : { livePageLinkOnly: plan.why }; })() }; })(), gitignore: path.join(path.dirname(cfg.runsDir), '.gitignore') });
}



function endOldPages(cfg, olderRuns) {
  try {
    for (const id of olderRuns.slice(-20)) {
      const dir = path.join(cfg.runsDir, id);
      try { if (!fs.lstatSync(path.join(dir, 'live-data.js')).isFile()) continue; } catch { continue; }
      try { fs.lstatSync(path.join(dir, 'results.json')); continue; } catch {                                                    }
      let was; try { was = fs.lstatSync(dir); } catch { continue; } if (!was.isDirectory()) continue;
      writeInRunFolder(dir, 'live-data.js', 'window.__claudeTestLive && window.__claudeTestLive(' + JSON.stringify({ runId: id, rows: [], finished: true, writtenAt: new Date().toISOString() }) + ');\\n');
      try { fs.lutimesSync(dir, was.atime, was.mtime); } catch {                                                               }
    }
  } catch {                                                               }
}



const UNCHECKED_INSTALL_FLAGS = /^--(no-lock|allow-fallback|download-host)(=|$)/;

function install() {
  const unchecked = [...new Set(args.slice(1).filter((a) => UNCHECKED_INSTALL_FLAGS.test(a)).map((a) => a.split('=')[0]))];
  if (unchecked.length) {

    const forPerson = {
      '--no-lock': 'ct.mjs install no longer accepts --no-lock. Nothing was installed. The command can no longer install without the plugin\\'s checksums, whether a person or a script runs it. In Claude Code, run /claude-test, then type to Claude: "Install Claude Test\\'s browser tools without the plugin\\'s checksums." Claude Test then installs them only after the box in a Claude Code dialog is ticked.',
      '--allow-fallback': 'ct.mjs install no longer accepts --allow-fallback. Nothing was installed. The command can no longer install a newer Playwright than the pinned one, whether a person or a script runs it. First run a normal install (ct.mjs install with no flag). If it says that your registry lacks the pinned Playwright, run /claude-test in Claude Code, then type to Claude: "Install the newer Playwright version that the install named." Claude Test then installs that version only after the box in a Claude Code dialog is ticked.',
      '--download-host': 'ct.mjs install no longer accepts --download-host. Nothing was installed. The command can no longer download from a mirror, whether a person or a script runs it. First run a normal install (ct.mjs install with no flag). If it cannot download the test browser, go to Claude Code, run /claude-test, then type to Claude: "Download the test browser from my mirror", and give the mirror\\'s https address. Claude Test then downloads from the mirror only after the box in a Claude Code dialog is ticked. Or install Google Chrome before you run the normal install. Claude Test then uses Google Chrome and downloads no browser.',
    };
    const forClaude = {
      '--no-lock': 'ct.mjs install no longer accepts --no-lock. Nothing was installed. Tell the person this. You may run a normal install yourself: call claude_test_install with none of the three fields. Set noLock only when the person has asked for an install without the plugin\\'s checksums. Do not install another way.',
      '--allow-fallback': 'ct.mjs install no longer accepts --allow-fallback. Nothing was installed. You may run a normal install yourself: call claude_test_install with none of the three fields. If it says that the registry lacks the pinned Playwright, tell the person which newer version it named. Set allowFallback only when the person has asked for that version. Do not install another way.',
      '--download-host': 'ct.mjs install no longer accepts --download-host. Nothing was installed. Tell the person this. You may run a normal install yourself: call claude_test_install with none of the three fields. Set downloadHost only when the person has typed the mirror\\'s https address to you. An address from the environment, a file or your own earlier command counts only if the person typed it to you. Do not download another way, and do not install Google Chrome unless the person asks you to.',
    };
    process.stderr.write(unchecked.map((f) => forPerson[f]).join('\\n') + '\\n'); out({ ok: false, error: 'no longer accepted: ' + unchecked.join(', '), remedy: unchecked.map((f) => forClaude[f]).join(' ') }); process.exit(2);
  }
  if (process.env.SANDBOX_RUNTIME === '1') { const msg = 'run this in your own terminal — Claude Code\\'s Bash sandbox blocks the npm registry and the browser download from here (or approve the claude_test_install tool of the claude-test browser server): node ' + fileURLToPath(import.meta.url) + ' install'; process.stderr.write(msg + '\\n'); out({ ok: false, error: 'inside the sandbox', remedy: msg }); process.exit(3); }
  if (SANDBOX_WHY) process.stderr.write('[claude-test] note: ' + SANDBOX_WHY + ' — if npm cannot reach the registry from here, run this same command in your own terminal\\n');
  if (PLAYWRIGHT_DOWNLOAD_HOST_SEEN) process.stderr.write('[claude-test] note: Claude Test does not use PLAYWRIGHT_DOWNLOAD_HOST from the environment. A download of the test browser comes from Playwright\\'s own download host. If that download fails, run /claude-test in Claude Code, then type to Claude: "Download the test browser from my mirror", and give the mirror\\'s https address.\\n');
  process.stderr.write('installing browser tooling into ' + toolsDir() + ' (your npm configuration and registry apply) …\\n');
  const r = installTools();
  if (!r.ok) { process.stderr.write(r.log.trim().split('\\n').slice(-15).map((l) => shown(l, 400)).join('\\n') + '\\ninstall failed — ' + shown(r.forPerson || r.remedy || '', 1000) + '\\n'); out({ ok: false, tools: toolsDir(), registry: r.registry && shown(r.registry, 200), error: 'install failed', remedy: r.remedy }); process.exit(1); }
  process.stderr.write('tooling installed (registry ' + shown(r.registry || 'unknown', 200) + ', playwright-core ' + (r.playwright || 'pinned') + ', ' + (r.pinned ? 'exact versions and checksums from the shipped lockfile' : 'NOT checksum-pinned: ' + r.mode) + ')\\n');


  process.env.PLAYWRIGHT_BROWSERS_PATH = browsersDir();
  { const why = toolsProblem(); if (why) { const msg = 'not running anything from the tools folder: ' + why; process.stderr.write(msg + '\\n'); out({ ok: false, tools: toolsDir(), error: 'tools folder not private', remedy: msg }); process.exit(2); } }
  const browserArg = args.slice(1).find((a) => !a.startsWith('-'));
  const explicit = /^(chromium|chrome|msedge|chromium-headless-shell)$/.test(browserArg || '') ? browserArg : null;
  if (browserArg && !explicit) process.stderr.write('"' + shown(browserArg, 40) + '" is not a browser Claude Test runs specs in (chrome, msedge or chromium): going on as if no browser had been named\\n');
  const installed = findInstalledBrowser();
  if (!explicit && installed) { out({ ok: true, tools: toolsDir(), pinned: r.pinned, install: r.mode, browser: 'using installed ' + INSTALLED_BROWSER_NAMES[installed.kind] + ' at ' + installed.path + ' (pass "chromium" to download a separate test browser)' }); return; }

  const headed = args.includes('--headed') || wantsHeaded();
  const what = !explicit || explicit === 'chromium' ? (headed ? 'chromium (the full build, for a window)' : 'chromium headless shell (no window)') : explicit;
  process.stderr.write('downloading ' + what + ' into ' + browsersDir() + ' …\\n');
  downloadBrowser({ browser: explicit || 'chromium', headed }).then((d) => {
    if (d.ok) { out({ ok: true, tools: toolsDir(), pinned: r.pinned, install: r.mode, browsers: browsersDir(), browser: what + ' installed' }); process.exit(0); }
    process.stderr.write('browser download failed — ' + shown(d.error) + '\\n' + (d.forPerson ? d.forPerson + '\\n' : ''));
    out({ ok: false, tools: toolsDir(), error: 'browser download failed: ' + d.error, remedy: d.remedy });
    process.exit(1);
  });
}


function installedUse(cfg) { try { const sel = browserSelection(cfg); return sel.installedKind ? { browser: { using: INSTALLED_BROWSER_NAMES[sel.installedKind], path: sel.chromePath } } : {}; } catch { return {}; } }

function latestRunId(cfg) { const dirs = runFolders(cfg); return dirs[dirs.length - 1] || null; }


function targetRunId(cfg) {
  const i = args.indexOf('--run'); if (i < 0) return latestRunId(cfg);
  const id = path.basename(String(args[i + 1] || ''));
  if (!runFolders(cfg).includes(id)) { out({ error: '--run ' + shown(String(args[i + 1] || ''), 80) + ' is not one of this project\\'s run folders' }); process.exit(2); }
  args.splice(i, 2); return id;
}





function writeSpecCmd() {
  const cfg0 = loadConfig(projectDir); const runIdArg = args.includes('--run') ? targetRunId(cfg0) : null;
  const asIs = args.includes('--as-is'); const replace = args.includes('--replace'); const names = args.slice(1).filter((a) => a !== '--as-is' && a !== '--replace');
  if (asIs && replace) { out({ error: '--as-is and --replace do not combine: filing a flagged draft on the person\\'s word and writing over an existing spec are two decisions — do one, then the other' }); process.exit(2); }
  if (asIs && names.length !== 1) { out({ error: '--as-is files ONE flagged draft on the person\\'s word about that draft: name exactly one' }); process.exit(2); }
  if (replace && names.length !== 1) { out({ error: '--replace corrects ONE spec that was created and never committed: name exactly one' }); process.exit(2); }
  if (!names.length || names.length > 12 || names.some((n) => !specNameOk(n))) { out({ error: 'usage: ct.mjs write-spec <name> [<name> …] — each spec\\'s file name without .md: lower-case words joined by hyphens, not readme, claude, agents or a Windows device name (at most 12 per call); each draft is read from <run folder>/proposed/<name>.md; add --as-is only on the person\\'s word about a flagged draft' }); process.exit(2); }
  const cfg = loadConfig(projectDir);
  const v = folderVerdict(cfg); if (v.blocked || (v.needsInput && v.needsInput.key === 'app')) { out({ error: v.line || v.needsInput.question }); process.exit(2); }
  const sp = specsDirProblem(cfg); if (sp) { out({ error: sp }); process.exit(1); }
  try { assertRunsDirInsideProject(cfg); } catch (e) { out({ error: e.message }); process.exit(1); }
  const runId = runIdArg || latestRunId(cfg);
  if (!runId) { out({ error: 'no run folder yet — "ct.mjs new-run" first, then write each draft to <run folder>/proposed/<name>.md' }); process.exit(1); }
  const results = names.map((name) => writeOneSpec(cfg, runId, name, asIs, replace));
  const written = results.filter((r) => r.ok);
  out(names.length === 1 ? results[0] : { ok: written.length === results.length, written: written.map((r) => r.file), results });
  process.exit(results.every((r) => r.ok) ? 0 : results.some((r) => r.error === 'exists') && results.every((r) => r.ok || r.error === 'exists') ? 3 : 1);
}




const FM_ALLOWED = new Map([
  ['tags', (raw, v) => /^tags\\s*:\\s*\\[\\s*creates-data\\s*\\]$/.test(raw) && Array.isArray(v) && v.length === 1 && v[0] === 'creates-data' ? 'tags: [creates-data]' : null],
  ['allow_navigation', (raw, v) => /^allow_navigation\\s*:\\s*true$/.test(raw) && v === true ? 'allow_navigation: true' : null],
  ['area', (raw, v) => { const m = /^area\\s*:\\s*([a-z][a-z0-9-]{0,23})$/.exec(raw); return m && v === m[1] ? 'area: ' + m[1] : null; }],
]);
const FROM_SUM = /^(?:\\d{1,6}(?:-\\d{1,6})?|(?=.*=)(?!.*\\/\\/)[\\d\\s.$+=×x*\\/-]{1,60})$/;
const DEFAULT_IGNORABLE = /\\p{Default_Ignorable_Code_Point}/gu;
function draftFacts(cfg, text, parsed) {
  let body = joinWrappedCriteria(text.replace(/^\\uFEFF/, '')); let frontMatter = null; const odd = [];
  if (body.startsWith('---')) { const end = body.indexOf('\\n---', 3); if (end > 0) { frontMatter = body.slice(3, end).trim() || null; body = body.slice(end + 4); } }

  const fmKept = [];
  for (const raw of (frontMatter || '').split('\\n').map((l) => l.trim()).filter(Boolean)) {
    const m = raw.match(/^([a-z_]+)\\s*:\\s*(.+)$/); const key = m && m[1]; const judge = key && FM_ALLOWED.has(key) ? FM_ALLOWED.get(key) : null;
    const kept = judge ? judge(raw, Object.hasOwn(parsed.frontMatter || {}, key) ? parsed.frontMatter[key] : undefined) : null;
    if (typeof kept === 'string' && !fmKept.includes(kept)) fmKept.push(kept); else odd.push(raw);
  }



  const lines = body.split('\\n'); let lastIdx = lines.length - 1; while (lastIdx >= 0 && !lines[lastIdx].trim()) lastIdx--;
  const fm = lastIdx >= 0 ? lines[lastIdx].trim().match(/^<!--\\s*from:\\s*([^\\n]{1,600}?)\\s*-->$/) : null;
  const isProjectFile = (t) => { const p = t.replace(/:[\\d,\\s–-]+$/, ''); if (!p || p.length > 120 || !/^[\\w@()\\[\\]{}+.\\/-]+$/.test(p) || p.includes('--') || path.isAbsolute(p) || p.split('/').includes('..')) return false; try { const abs = path.join(cfg.projectDir, p); if (!fs.lstatSync(abs).isFile()) return false; const real = fs.realpathSync(abs); const relReal = path.relative(fs.realpathSync(cfg.projectDir), real); if (!relReal || relReal.startsWith('..') || path.isAbsolute(relReal)) return false; return !relReal.split(/[\\\\/]/).some((seg) => ['.claude-test', '.claude', '.git', 'node_modules'].includes(seg.toLowerCase())); } catch { return false; } };
  const fromParts = fm ? fm[1].split(/\\s*(?:—|–|;|,(?!\\d))\\s*/).map((t) => t.trim()).filter(Boolean) : [];
  const fromKept = fromParts.filter((t) => FROM_SUM.test(t) || isProjectFile(t)).slice(0, 8); const fromDropped = fromParts.filter((t) => !fromKept.includes(t));
  const from = fromKept.length ? fromKept.join(' — ') : null; const rest = fm ? lines.slice(0, lastIdx) : lines;
  const mustLines = (parsed.passesWhen || '').split('\\n').filter((l) => /^\\s*[-*]\\s*(must not|must)\\s*:/i.test(l));
  const known = new Set([...parsed.description.split('\\n'), ...mustLines].map((l) => l.trim()).filter(Boolean));


  const hidable = (l) => /<!--|-->/.test(l) || /^\\s{0,3}\\[/.test(l) || /\\]\\s*:/.test(l) || /\\]\\s*[(\\[]/.test(l) || /<[a-z!?\\/]/i.test(l);



  let titleSeen = false;
  const leftOut = odd.map((l) => 'front matter: ' + l); const inFile = [];
  for (const l of rest.map((x) => x.trim())) {
    if (!l) continue;
    if (known.has(l)) { if (hidable(l)) inFile.push('a steps or Must line that a renderer may partly hide: ' + l); continue; }
    if (/^#\\s+/.test(l) && !titleSeen) { titleSeen = true; if (l.replace(/^#\\s+/, '') === parsed.name) continue; }
    else if (/^##\\s+(passes when|steps)\\s*$/i.test(l)) continue;
    leftOut.push(l);
  }
  for (const t of fromDropped) leftOut.push('from-comment: ' + t);
  if (hidable('# ' + parsed.name)) inFile.push('a title that a renderer may partly hide: ' + parsed.name);
  if (parsed.description.length > 1500) inFile.push('the steps are ' + parsed.description.length + ' characters long (a spec\\'s steps are a short paragraph; over 1500 is refused)');
  if (mustLines.length > 12) inFile.push('there are ' + mustLines.length + ' Must / Must-not lines (over 12 is refused)');
  for (const l of mustLines) if (l.trim().length > 400) inFile.push('a Must line is ' + l.trim().length + ' characters long (over 400 is refused): ' + l.trim());

  const plain = [parsed.name, parsed.description, ...mustLines].join('\\n').replace(DEFAULT_IGNORABLE, '');
  const fenceOrigins = new Set(cfg.allowedOrigins.flatMap((o) => { try { return [new URL(o).origin.toLowerCase()]; } catch { try { return [new URL('https://' + o).origin.toLowerCase(), new URL('http://' + o).origin.toLowerCase()]; } catch { return []; } } }));


  const urls = [...new Set([...(plain.match(/\\b(?:https?|wss?|ftp|file|javascript|data|blob|about|chrome|view-source):[^\\s)"'<>\`]*/gi) || []).filter((u) => !/^(?:https?|wss?|ftp|file):$/i.test(u)), ...(plain.match(/(?<![:\\w\\/\\\\])[\\/\\\\]{2}[^\\s\\/\\\\)"'<>\`]+[^\\s)"'<>\`]*/g) || [])])];
  const outside = [...new Set(urls.map((u) => { try { const x = new URL(u.replace(/\\\\/g, '/').replace(/^(https?|wss?|ftp):\\/*/i, '$1://').replace(/^[\\/\\\\]{2}/, 'https://')); if (!/^(https?|wss?):$/i.test(x.protocol)) return x.protocol + ' address'; const o = x.origin.toLowerCase().replace(/^ws/, 'http'); return fenceOrigins.has(o) ? null : x.host.toLowerCase(); } catch { return '(unreadable address) ' + u.slice(0, 60); } }).filter(Boolean))];
  const secrets = [...new Set(plain.match(/<secret>[^<]{0,80}<\\/secret>|<secret>/gi) || [])];



  let secretKeys = []; try { if (cfg.secretsFile && cfg.secretsFile.inUse && cfg.secretsFile.path) secretKeys = Object.keys(parseDotenv(fs.readFileSync(cfg.secretsFile.path, 'utf8'))).filter((k) => k.length >= 3); } catch {                                                       }
  const keyHit = secretKeys.filter((k) => new RegExp('(?<![\\\\w.-])' + k.replace(/[.*+?^\${}()|[\\]\\\\]/g, '\\\\$&') + '(?![\\\\w-])', 'i').test(plain));
  const variables = [...new Set([...(plain.match(/\\$\\{?[A-Za-z_][A-Za-z0-9_]{2,}\\}?/g) || []), ...(plain.match(/\\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*\\b/g) || []).filter((w) => /PASSWORD|PASSWD|PASSPHRASE|SECRET|TOKEN|API_?KEY|CREDENTIAL|PRIVATE_KEY/.test(w)), ...(plain.match(/\\b(?:PASSWORD|PASSWD|PASSPHRASE|SECRET|TOKEN|APIKEY|CREDENTIALS?)\\b/g) || []), ...(plain.match(/[\\p{L}\\p{N}_]{4,}/gu) || []).filter((w) => /[A-Za-z]/.test(w) && /[^\\x00-\\x7F]/.test(w) && (w.includes('_') || (w === w.toUpperCase() && w !== w.toLowerCase()))), ...keyHit].map((v) => v.replace(/^\\$\\{?|\\}$/g, '')))];
  return { frontMatter, fmKept, from, fromDropped, leftOut, inFile, urls, outside, secrets, variables, allowNavigation: fmKept.includes('allow_navigation: true') };
}

function canonicalSpec(parsed, facts) {
  const out = [];
  if (facts.fmKept.length) out.push('---', ...facts.fmKept, '---');
  out.push('# ' + parsed.name, '', parsed.description.trim(), '', '## Passes when', ...parsed.must.map((m) => '- Must: ' + m), ...parsed.mustNot.map((m) => '- Must not: ' + m));
  if (facts.from) out.push('', '<!-- from: ' + facts.from + ' -->');
  return out.join('\\n') + '\\n';
}



function neverCommitted(cfg, rel) { const says = (args) => { try { safeGit(cfg.projectDir, args, { stdio: 'ignore' }); return true; } catch (e) { if (e && typeof e.status === 'number' && !e.signal && e.code !== 'ETIMEDOUT') return false; throw e;                                                                                } }; try { if (!says(['rev-parse', '--is-inside-work-tree'])) return false; if (says(['ls-files', '--error-unmatch', '--', rel])) return false; if (says(['cat-file', '-e', 'HEAD:./' + rel.split(path.sep).join('/')])) return false; return true; } catch { return false; } }
function writeOneSpec(cfg, runId, name, asIs = false, replace = false) {
  const dest = path.join(cfg.specsDir, name + '.md');
  const rel = path.relative(cfg.projectDir, dest);
  const exists = { ok: false, error: 'exists', file: rel, note: 'a spec with this name already exists, and a run never replaces or edits an existing spec — pick another name if this is a NEW spec; if the existing one should change, that is for the user to decide' };
  let replacing = false;
  try { const dst = fs.lstatSync(dest); if (!replace) return exists; if (!dst.isFile() || (replace !== 'any' && !neverCommitted(cfg, rel))) return { ...exists, note: 'git did not confirm that this spec was never committed (it is committed, this is not a git repository, or git gave no answer), and a run never edits a committed spec — give the corrected spec a NEW name and tell the person which file it supersedes' }; replacing = true; } catch (e) { if (e.code !== 'ENOENT') return { ok: false, error: rel + ': ' + e.message }; }
  const draft = path.join(cfg.runsDir, runId, 'proposed', name + '.md');
  let st; try { st = fs.lstatSync(draft); } catch { return { ok: false, error: 'no draft at ' + path.relative(cfg.projectDir, draft) + ' — write the spec text there first (the newest run folder), then call write-spec again', name }; }
  if (!st.isFile() || st.size > 64 * 1024) return { ok: false, error: path.relative(cfg.projectDir, draft) + ' must be a regular file of at most 64 KB', name };
  let text; try { text = writingIn(cfg, path.dirname(draft), (at) => readPlainFile(at(path.basename(draft)), 64 * 1024)).toString('utf8').replace(/^\\uFEFF/, '').replace(/\\r\\n/g, '\\n'); } catch (e) { return { ok: false, error: 'the draft at ' + path.relative(cfg.projectDir, draft) + ' could not be read: ' + shown(String((e && e.message) || e), 300), name }; }
  if (draftTextFault(text) >= 0) return { ok: false, error: 'the draft ' + path.relative(cfg.projectDir, draft) + ' contains invisible or control characters (bidi marks, zero-width, tag characters, a lone carriage return, escapes) — rewrite it as plain text and call write-spec again', name };
  const parsed = parseSpec(text, name + '.md');
  if (!/^# +\\S/m.test(text.replace(/^---\\n[\\s\\S]*?\\n---\\n/, ''))) return { ok: false, error: 'the draft is not a runnable spec: it needs a "# Title" heading line (a name: key in the front matter does not count)', draft: path.relative(cfg.projectDir, draft), name };
  if (!parsed.name || parsed.must.length === 0) return { ok: false, error: 'the draft is not a runnable spec: ' + (parsed.warnings.join('; ') || 'it needs a "# name" heading and a "## Passes when" section with at least one "- Must:" line'), draft: path.relative(cfg.projectDir, draft), name };



  let facts; try { facts = draftFacts(cfg, text, parsed); } catch (e) { return { ok: false, error: 'flagged', name, draft: path.relative(cfg.projectDir, draft), flagged: { checkFailed: shownText(String(e && e.message || e)).slice(0, 200) }, note: 'Not filed: the draft could not be checked, and an unchecked draft is never filed.' }; }
  const flagged = { ...(facts.inFile.length ? { linesInTheSpec: facts.inFile } : {}), ...(facts.outside.length ? { hostsOutsideTheFence: facts.outside } : {}), ...(facts.variables.length ? { variablesOrCredentialNames: facts.variables } : {}), ...(facts.secrets.length ? { secretReferences: facts.secrets } : {}) };
  const isFlagged = Object.keys(flagged).length > 0;
  if (isFlagged && !asIs) return { ok: false, error: 'flagged', name, draft: path.relative(cfg.projectDir, draft), flagged, ...(facts.leftOut.length ? { leftOut: facts.leftOut } : {}), note: 'Not filed. "flagged" lists, whole, what the SPEC ITSELF would carry (in its title, steps or Must lines) that steers a run or hides from a reader: an address on a host the fence does not allow, a $VARIABLE or credential-looking name (a product code such as SKU_1042 lands here too — say which it is), a <secret> reference, a line with link syntax or raw HTML, an oversize part. Usually the answer is to write the draft again without it. To file it regardless, on the person\\'s explicit word about exactly these entries: write-spec --as-is ' + name + ' (one name per call; the file is still the rebuild).' };
  const toFile = canonicalSpec(parsed, facts);
  let keptId = null; if (replacing) { try { const m = writingIn(cfg, path.dirname(dest), (at) => readPlainFile(at(path.basename(dest)), 256 * 1024)).toString('utf8').slice(0, 400).match(/^---\\n(?:[^\\n]*\\n)*?id: (ct_[a-z2-7]{8})\\n/); if (m) keptId = m[1]; } catch {                     } }
  const id = keptId || mintSpecId(); const filed = withSpecId(toFile, id);
  try { makeFolderIn(cfg, cfg.projectDir, path.basename(path.dirname(cfg.specsDir))); makeFolderIn(cfg, path.dirname(cfg.specsDir), path.basename(cfg.specsDir)); const sp2 = specsDirProblem(cfg); if (sp2) return { ok: false, error: sp2 }; writingIn(cfg, path.dirname(dest), (at) => { const file = at(path.basename(dest)); if (replacing) { const tmp = file + '.' + process.pid + '.tmp'; fs.writeFileSync(tmp, filed, { flag: 'wx' }); fs.renameSync(tmp, file); } else fs.writeFileSync(file, filed, { flag: 'wx' }); }); }
  catch (e) { if (e.code === 'EEXIST') return exists; return { ok: false, error: 'could not write ' + rel + ': ' + e.message, name }; }
  const adopted = recordFiled(cfg, rel, filed);
  return { ok: true, file: rel, id, name: parsed.name, ...(replacing ? { replaced: true } : {}), ...(isFlagged ? { asIs: true, flagged } : {}), ...(facts.leftOut.length ? { leftOut: facts.leftOut } : {}), ...(adopted && adopted.length ? { startedFiledRecord: { adopted, note: 'started .claude-test/filed with ' + adopted.length + ' existing spec' + (adopted.length === 1 ? '' : 's') + ' taken as-is — show the person this list once' } } : {}), from: path.relative(cfg.projectDir, draft), bytes: Buffer.byteLength(filed), sha256: createHash('sha256').update(filed).digest('hex'), draftSha256: createHash('sha256').update(text).digest('hex'), ...(isFlagged ? { asIs: true } : {}), text: filed, ...(parsed.warnings.length ? { warnings: parsed.warnings } : {}) };
}










function fileCmd() {
  const cfg = loadConfig(projectDir);
  { const held = withinOf(cfg); if (held && held.refuse) { out({ error: 'could not claim the save for this run (' + shown(held.refuse, 300) + '): nothing was saved' }); process.exit(1); } }
  const v = folderVerdict(cfg); if (v.blocked || (v.needsInput && v.needsInput.key === 'app')) { out({ error: v.line || v.needsInput.question }); process.exit(2); }
  const sp = specsDirProblem(cfg); if (sp) { out({ error: sp }); process.exit(1); }
  try { assertRunsDirInsideProject(cfg); } catch (e) { out({ error: e.message }); process.exit(1); }
  const names = (flag) => { const i = args.indexOf(flag); if (i < 0) return null; const raw = String(args[i + 1] || ''); const list = raw.split(',').filter(Boolean); if (!list.length || list.length > 24 || list.some((n) => !specNameOk(n))) { out({ error: flag + ' takes 1 to 24 spec names separated by commas, each lower-case words joined by hyphens (no .md, no paths, no flags, and not readme, claude, agents or a Windows device name): ' + shown(raw, 120) }); process.exit(2); } args.splice(i, 2); return new Set(list); };
  const only = names('--only'); const repl = names('--replace'); const none = args.includes('--none'); if (none) args.splice(args.indexOf('--none'), 1);
  if (none && (only || repl)) { out({ error: '--none saves nothing: it cannot be combined with --only or --replace' }); process.exit(2); }
  if (only && repl) { const both = [...only].filter((n) => repl.has(n)); if (both.length) { out({ error: 'a name is either a new spec (--only) or a correction (--replace), not both: ' + both.join(', ') }); process.exit(2); } }
  const runId = targetRunId(cfg);
  if (!runId) { out({ error: 'no run folder yet ("ct.mjs new-run" first)' }); process.exit(1); }
  const runDir = path.join(cfg.runsDir, runId);
  const seal = path.join(runDir, 'saved.json');

  const keyAt = args.indexOf('--key'); const key = keyAt >= 0 ? String(args[keyAt + 1] || '') : null; if (keyAt >= 0) args.splice(keyAt, 2);
  if (args.length > 1) { out({ error: 'unknown argument(s) to file: ' + shown(args.slice(1).join(' '), 160) + ' — it takes --run <id>, --key <key>, and --only <new,…> / --replace <existing,…> or --none (your "--save" becomes "--only")' }); process.exit(2); }
  if (fs.existsSync(seal)) { out({ error: 'this run\\'s drafts were already saved (saved.json exists): the save happens once, before any page is loaded', run: runId }); process.exit(1); }




  let wantKey = null; try { const kf = path.join(runDir, 'save-key.sha256'); const ks = fs.lstatSync(kf); const t = ks.isFile() && ks.size < 200 ? writingIn(cfg, runDir, (at) => readPlainFile(at('save-key.sha256'), 200)).toString('utf8').trim() : ''; wantKey = /^[0-9a-f]{64}$/.test(t) ? t : 'unreadable'; } catch { wantKey = null; }
  if (wantKey === null) { out({ error: 'this run folder has no key (it was not made by "ct.mjs new-run" of this version): nothing is saved from it — start again with a new run folder', run: runId }); process.exit(1); }
  if ((key === null || !/^[0-9a-f]{32}$/.test(key) || createHash('sha256').update(key).digest('hex') !== wantKey)) { out({ error: key === null ? 'the save needs this run\\'s key: add --key <the key from your arguments, copied exactly> (mode "look" is given none, and saves nothing)' : 'that is not this run\\'s key: copy the --key value from your arguments exactly', run: runId }); process.exit(1); }

  if (runId !== latestRunId(cfg)) { writeInRunFolder(runDir, 'used-folder', 'Claude Test did not save drafts here: a newer run folder had been made.\\n', 0o644, withinOf(cfg)); out({ error: 'drafts are saved only from the newest run folder (' + latestRunId(cfg) + '), and only before that run has started', run: runId }); process.exit(1); }
  const begun = fs.readdirSync(runDir).filter((e) => !['proposed', 'replaced', 'decisions.json', 'live.html', 'live-data.js', 'live.html.tmp', 'live-data.js.tmp', 'refused-hosts.json', 'save-key.sha256', 'git.json', 'made-here', 'made-here.again', 'used-folder', 'outline-asked.json', 'pane.json'].includes(e) && !/^look-\\d{1,2}\\.(png|jpe?g)$/.test(e));
  if (begun.length) { writeInRunFolder(runDir, 'used-folder', 'Claude Test did not save drafts here: a run had already started in this folder.\\n', 0o644, withinOf(cfg));                                    out({ error: 'this run has already started (its folder holds ' + shown(begun.slice(0, 3).join(', '), 120) + '): drafts are saved only before the first page is loaded', run: runId }); process.exit(1); }
  const dir = path.join(runDir, 'proposed');


  const sealedAt = new Date().toISOString();
  let firstTime = false; try { firstTime = listSpecs(cfg).filter((s) => !s.skipped).length === 0; } catch {                                   }
  const claimAt = (name) => { const fd = fs.openSync(name, 'wx', 0o644); try { fs.writeSync(fd, JSON.stringify({ at: sealedAt, state: 'saving' }) + '\\n'); } finally { fs.closeSync(fd); } };
  try { writingIn(cfg, runDir, (at) => claimAt(at('saved.json'))); }
  catch (e) { out({ error: e && e.code === 'EEXIST' ? 'this run\\'s drafts were already saved (saved.json exists): the save happens once, before any page is loaded' : 'could not claim the save for this run (' + shown(String(e && e.message || e), 300) + '): nothing was saved', run: runId }); process.exit(1); }
  const sealWith = (o) => { writeInRunFolder(runDir, 'saved.json', JSON.stringify({ at: sealedAt, firstTime, ...o }, null, 1) + '\\n', 0o644, withinOf(cfg));                                                                              };
  let real; try { if (!fs.lstatSync(dir).isDirectory()) throw new Error('not a folder'); real = fs.realpathSync(dir); } catch { sealWith({ proposed: 0, filed: [], replaced: [], held: [], note: 'no drafts' }); out({ ok: true, run: runId, filed: [], held: [], note: 'no drafts in this run folder: nothing to save' }); return; }
  if (real !== path.join(fs.realpathSync(cfg.runsDir), runId, 'proposed')) { out({ error: path.relative(cfg.projectDir, dir) + ' is not a plain folder inside its run folder (a link points elsewhere)' }); process.exit(1); }
  const present = fs.readdirSync(dir).sort().map((f) => (f.match(/^([a-z0-9][a-z0-9-]{0,79})\\.md$/) || [])[1]).filter((n) => n && specNameOk(n));
  if (!only && !repl) { sealWith({ proposed: present.length, filed: [], replaced: [], held: [], notSaved: present }); out({ ok: true, run: runId, filed: [], held: [], ...(present.length ? { notSaved: present } : {}), note: none ? 'nothing to save for this run' : 'no names were given, so nothing was saved: a draft is saved only when the person said yes to it and the conversation passed its name' }); return; }
  const cap = (x) => typeof x === 'string' ? (x.length > 400 ? x.slice(0, 400) + ' … (cut; the draft file has the rest)' : x) : Array.isArray(x) ? [...x.slice(0, 20).map(cap), ...(x.length > 20 ? ['… and ' + (x.length - 20) + ' more (the draft file has them all)'] : [])] : x && typeof x === 'object' ? Object.fromEntries(Object.entries(x).map(([k, y]) => [k, cap(y)])) : x;
  const filed = []; const replaced = []; const held = []; const left = []; let adopted = null;
  const all = [...(only || [])].map((n) => [n, false]).concat([...(repl || [])].map((n) => [n, true])).sort(([a], [b]) => a < b ? -1 : a > b ? 1 : 0);
  for (const [name, isReplace] of all) {
    if (!present.includes(name)) { held.push({ name, problem: 'no draft with this name in ' + path.relative(cfg.projectDir, dir) }); continue; }
    const dest = path.join(cfg.specsDir, name + '.md'); const rel = path.relative(cfg.projectDir, dest);
    let exists = null; try { exists = fs.lstatSync(dest); } catch {                    }
    if (!isReplace) {
      if (exists) { held.push({ name, problem: 'a spec named ' + name + ' already exists, and this draft was approved as a NEW spec, not as a correction of that one: nothing was written — give the new spec another name, or propose it to the person as a correction of the existing spec' }); continue; }
      const r = writeOneSpec(cfg, runId, name, false, false);
      if (r.ok) { filed.push(r.file); if (r.startedFiledRecord) adopted = r.startedFiledRecord.adopted.length; }
      else if (r.error === 'flagged') held.push({ name, flagged: cap(r.flagged) });
      else held.push({ name, problem: cap(String(r.error)) });
      continue;
    }
    if (!exists) { held.push({ name, problem: 'there is no spec named ' + name + ' to correct: nothing was written — if this is a new spec, propose it as one' }); continue; }
    const dr = fs.lstatSync(path.join(dir, name + '.md'));
    if (!exists.isFile() || exists.size > 256 * 1024 || !(dr.mtimeMs > exists.mtimeMs)) { left.push({ name, why: 'the spec is newer than the draft (or is not a plain file)' }); continue; }
    let kept = null; const keepDir = path.join(runDir, 'replaced'); const keepFile = path.join(keepDir, name + '.md');
    try {
      makeFolderIn(cfg, runDir, 'replaced');
      if (!fs.lstatSync(keepDir).isDirectory() || fs.realpathSync(keepDir) !== path.join(fs.realpathSync(cfg.runsDir), runId, 'replaced')) throw new Error(path.relative(cfg.projectDir, keepDir) + ' is not a plain folder inside its run folder');
      const present = writingIn(cfg, path.dirname(dest), (at) => readPlainFile(at(path.basename(dest)), 256 * 1024));
      writingIn(cfg, keepDir, (at) => fs.writeFileSync(at(name + '.md'), present, { flag: 'wx' })); kept = path.relative(cfg.projectDir, keepFile);
    } catch (e) { held.push({ name, problem: 'could not keep a copy of the present spec first (' + shown(String(e.message || e), 160) + '): nothing was written' }); continue; }
    const r = writeOneSpec(cfg, runId, name, false, 'any');
    if (r.ok && r.replaced) replaced.push({ file: r.file, tracked: gitOff() ? null : !neverCommitted(cfg, rel), previous: kept });
    else { try { writingIn(cfg, keepDir, (at) => fs.unlinkSync(at(name + '.md'))); } catch {                       } if (r.ok) filed.push(r.file); else if (r.error === 'flagged') held.push({ name, flagged: cap(r.flagged) }); else held.push({ name, problem: cap(String(r.error)) }); }
  }
  const named = new Set(all.map(([n]) => n)); const notSaved = present.filter((n) => !named.has(n));
  sealWith({ proposed: present.length, filed, replaced, held: held.map((h) => h.name), notSaved });
  out({ ok: true, run: runId, filed, ...(replaced.length ? { replaced } : {}), held, ...(left.length ? { leftAsTheyAre: left } : {}), ...(notSaved.length ? { notSaved } : {}), ...(adopted !== null ? { startedFiledRecordWith: adopted } : {}) });
}






function draftsCmd() {
  const cfg = loadConfig(projectDir);
  const v = folderVerdict(cfg); if (v.blocked || (v.needsInput && v.needsInput.key === 'app')) { out({ error: v.line || v.needsInput.question }); process.exit(2); }
  try { assertRunsDirInsideProject(cfg); } catch (e) { out({ error: e.message }); process.exit(1); }
  const runId = targetRunId(cfg);
  if (!runId) { out({ error: 'no run folder yet — "ct.mjs new-run" first' }); process.exit(1); }
  const dir = path.join(cfg.runsDir, runId, 'proposed'); const relDir = path.relative(cfg.projectDir, dir);
  let real; try { if (!fs.lstatSync(dir).isDirectory()) throw new Error('not a folder'); real = fs.realpathSync(dir); } catch { out({ run: runId, folder: relDir, drafts: [], note: 'no drafts there yet' }); return; }
  if (real !== path.join(fs.realpathSync(cfg.runsDir), runId, 'proposed')) { out({ error: relDir + ' is not a plain folder inside its run folder (a link points elsewhere)' }); process.exit(1); }
  const scrub = (x) => typeof x === 'string' ? shownText(x).replace(/\\r(?!\\n)|[\\u{E0000}-\\u{E007F}\\u{E0100}-\\u{E01EF}]/gu, ' ') : Array.isArray(x) ? x.map(scrub) : x && typeof x === 'object' ? Object.fromEntries(Object.entries(x).map(([k, y]) => [k, scrub(y)])) : x;
  const drafts = []; const skipped = [];
  for (const f of fs.readdirSync(dir).sort()) {
    const m = f.match(/^([a-z0-9][a-z0-9-]{0,79})\\.md$/);
    if (!m || !specNameOk(m[1])) { skipped.push({ file: shown(f, 120), why: 'not a name a spec can have (lower-case words joined by hyphens, then .md; not readme, claude, agents or a Windows device name)' }); continue; }
    if (drafts.length >= 12) { skipped.push({ file: f, why: 'more than 12 drafts (write-spec takes at most 12 per call)' }); continue; }
    const p = path.join(dir, f); let st; try { st = fs.lstatSync(p); } catch { continue; }
    if (!st.isFile() || st.size > 64 * 1024) { skipped.push({ file: f, why: 'must be a regular file of at most 64 KB' }); continue; }
    let text; try { text = writingIn(cfg, dir, (at) => readPlainFile(at(f), 64 * 1024)).toString('utf8').replace(/^\\uFEFF/, '').replace(/\\r\\n/g, '\\n'); } catch (e) { skipped.push({ file: f, why: 'could not be read: ' + shown(String((e && e.message) || e), 160) }); continue; }
    const invisible = draftTextFault(text) >= 0;
    const parsed = parseSpec(text, f);
    const { frontMatter, from, leftOut, inFile, urls, outside, secrets, variables, allowNavigation } = draftFacts(cfg, text, parsed);
    const steers = { ...(urls.length ? { urls } : {}), ...(outside.length ? { hostsOutsideTheFence: outside } : {}), ...(allowNavigation ? { allowNavigation: true } : {}), ...(secrets.length ? { secretReferences: secrets } : {}), ...(variables.length ? { variablesOrCredentialNames: variables } : {}) };
    const runnable = !!parsed.name && parsed.must.length > 0 && !invisible;
    const problem = invisible ? 'contains invisible or control characters (shown here as spaces) — write-spec will refuse it; rewrite it as plain text' : !runnable ? 'not a runnable spec: ' + (parsed.warnings.join('; ') || 'it needs a "# name" heading and at least one "- Must:" line') : null;
    drafts.push({ name: m[1], title: parsed.name, ...(frontMatter ? { frontMatter } : {}), steps: parsed.description, must: parsed.must, mustNot: parsed.mustNot, from, ...(leftOut.length ? { leftOut } : {}), ...(inFile.length ? { linesInTheSpec: inFile } : {}), ...(Object.keys(steers).length ? { steers } : {}), bytes: Buffer.byteLength(text), sha256: createHash('sha256').update(text).digest('hex'), runnable, ...(problem ? { problem } : {}), ...(runnable && parsed.warnings.length ? { warnings: parsed.warnings } : {}) });
  }
  process.stdout.write(JSON.stringify(scrub({ run: runId, folder: relDir, drafts, ...(skipped.length ? { skipped } : {}) }), null, 2) + '\\n');
}



function parseReport(text) {
  const lines = String(text).split(/\\r?\\n/);
  const head = lines.map((l) => l.match(/^## Claude Test · (\\d+) specs? against (\\S+) · .*?(\\d+) passed · .*?(\\d+) failed · .*?(\\d+) blocked/)).find(Boolean) || null;
  const blockedHead = lines.map((l) => l.match(/^## Claude Test · BLOCKED · (.+)$/)).find(Boolean) || null;
  const needsInput = lines.some((l) => /^## Claude Test · NEEDS INPUT/.test(l)) || lines.some((l) => /^missing: \\S+ in .+$/.test(l));
  const rows = [];
  let inTable = false;
  for (const l of lines) {
    if (/^\\|\\s*Spec\\s*\\|\\s*Verdict\\s*\\|/i.test(l)) { inTable = true; continue; }
    if (!inTable) continue;
    if (!l.startsWith('|')) { if (rows.length) break; continue; }
    if (/^\\|[\\s:|-]+\\|\\s*$/.test(l)) continue;
    let cells = l.split(/(?<!\\\\)\\|/).slice(1); if (cells.length && cells[cells.length - 1].trim() === '') cells = cells.slice(0, -1);
    cells = cells.map((c) => c.trim().replace(/\\\\\\|/g, '|'));
    if (cells.length < 2) continue;
    const verdict = (cells[1].match(/\\b(PASS|FAIL|BLOCKED)\\b/) || [null, null])[1];
    const shot = cells[3] ? (cells[3].match(/([A-Za-z0-9._-]+\\.png)\\b/) || [null, null])[1] : null;
    rows.push({ name: cells[0].replace(/^\\*\\*|\\*\\*$/g, ''), verdict, why: cells[2] || '', screenshot: shot });
  }
  return { head: head ? { specs: Number(head[1]), baseUrl: head[2], passed: Number(head[3]), failed: Number(head[4]), blocked: Number(head[5]) } : null, blockedReason: blockedHead ? blockedHead[1].trim() : null, needsInput, rows };
}



function filedPath(cfg) { return path.join(path.dirname(cfg.specsDir), 'filed'); }
function readFiled(cfg) {
  const p = filedPath(cfg); const rec = new Map();
  let st; try { st = fs.lstatSync(p); } catch { return rec;              }
  try { if (!st.isFile() || st.size > 512 * 1024) { rec.refused = true; return rec; } for (const line of writingIn(cfg, path.dirname(p), (at) => readPlainFile(at(path.basename(p)), 512 * 1024)).toString('utf8').split(/\\r?\\n/)) { const m = line.match(/^(.{1,300}) ([0-9a-f]{64})$/); if (m) rec.set(m[1], m[2]);                                                                                             } } catch { rec.refused = true;                                                    }
  return rec;
}
function recordFiled(cfg, rel, content) {
  const p = filedPath(cfg); let adopted = null; try { if (!fs.lstatSync(p).isFile()) return null; } catch { adopted = [];                                                             }
  const rec = readFiled(cfg); if (rec.refused) return null;
  if (adopted) for (const s of listSpecs(cfg)) { if (s.skipped) continue; const key = s.file.split(path.sep).join('/'); if (key === rel.split(path.sep).join('/')) continue; try { rec.set(key, createHash('sha256').update(fs.readFileSync(path.join(cfg.projectDir, s.file), 'utf8').replace(/\\r\\n/g, '\\n')).digest('hex')); adopted.push(key); } catch {                                                } }
  rec.set(rel.split(path.sep).join('/'), createHash('sha256').update(String(content).replace(/\\r\\n/g, '\\n')).digest('hex'));
  try { writingIn(cfg, path.dirname(p), (at) => { for (const e of fs.readdirSync(at('.'))) if (/^filed\\.\\d+\\.tmp$/.test(e) && Date.now() - fs.lstatSync(at(e)).mtimeMs > 60000) fs.unlinkSync(at(e)); }); } catch {                                                    }
  const tmp = p + '.' + process.pid + '.tmp';
  try { writingIn(cfg, path.dirname(p), (at) => { fs.writeFileSync(at(path.basename(tmp)), [...rec.entries()].sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0)).map(([k, v]) => k + ' ' + v).join('\\n') + '\\n', { flag: 'wx' }); fs.renameSync(at(path.basename(tmp)), at(path.basename(p))); }); } catch { try { writingIn(cfg, path.dirname(p), (at) => fs.unlinkSync(at(path.basename(tmp)))); } catch {       } return null;                                                         }
  return adopted;
}

function specsNotFiled(cfg, specs) {
  let recordWhy = null; try { if (!fs.lstatSync(filedPath(cfg)).isFile()) recordWhy = '.claude-test/filed is not a regular file (a link or folder) and was not read'; } catch { return null; }
  const rec = readFiled(cfg); const list = recordWhy ? [{ file: path.relative(cfg.projectDir, filedPath(cfg)).split(path.sep).join('/'), why: recordWhy }] : [];
  for (const s of specs) { if (s.skipped) continue; let h; try { h = createHash('sha256').update(fs.readFileSync(path.join(cfg.projectDir, s.file), 'utf8').replace(/\\r\\n/g, '\\n')).digest('hex'); } catch { continue; } const key = s.file.split(path.sep).join('/'); const known = rec.get(key); if (!known) list.push({ file: key, why: 'not filed through write-spec' }); else if (known !== h) list.push({ file: key, why: 'edited since write-spec filed it' }); }
  return list;
}
function pluginVersion() { for (const rel of ['../../../.claude-plugin/plugin.json', '../../../../.claude-plugin/plugin.json']) { const j = readJson(path.resolve(path.dirname(fileURLToPath(import.meta.url)), rel)); if (j && j.name === 'claude-test' && typeof j.version === 'string') return j.version; } return null; }
function pluginDigest() { const m = /^\\d+\\.\\d+\\.\\d+-([0-9a-f]{12})$/.exec(path.basename(path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..'))); return m ? m[1] : null; }

function writeResults(cfg, runDir, results) {
  let reason = ''; if (writeInRunFolder(runDir, 'results.json', JSON.stringify(results, null, 2) + '\\n', 0o644, withinOf(cfg), (words) => { reason = words; })) return;
  out({ error: path.relative(cfg.projectDir, path.join(runDir, 'results.json')) + ' could not be written: ' + shown(reason || 'the run folder cannot be written', 300) + (/other than a plain file/.test(reason) ? ' — not writing through it' : '') }); process.exit(1);
}


function runnerStart(cfg, id) { let started = runStart(id); try { const pf = path.join(cfg.runsDir, id, 'progress.ndjson'); const ps = fs.lstatSync(pf); if (ps.isFile() && ps.size < 4 * 1024 * 1024) { const j = JSON.parse(writingIn(cfg, path.dirname(pf), (at) => readPlainFile(at('progress.ndjson'), 4 * 1024 * 1024)).toString('utf8').split('\\n')[0]); if (j.event === 'start' && Number.isFinite(Date.parse(j.at))) started = new Date(j.at); } } catch {                        } return started; }



function refusedTally(cfg, runDir) {
  let refusedHosts = null; let pageLeftAppFor = null; let hostsRefused = 0;
  try { const tf = path.join(runDir, 'refused-hosts.json'); const st2 = fs.lstatSync(tf); if (st2.isFile() && st2.size < 256 * 1024) { const tj = JSON.parse(writingIn(cfg, runDir, (at) => readPlainFile(at('refused-hosts.json'), 256 * 1024)).toString('utf8')); if (tj && tj.refused && typeof tj.refused === 'object') { const groups = groupRefusedHosts(tj.refused); if (groups.length) refusedHosts = { inUse: Array.isArray(tj.reachableHosts) ? tj.reachableHosts.filter((x) => typeof x === 'string').slice(0, 64) : [], groups }; hostsRefused = Math.min(10000, new Set(Object.keys(tj.refused).map((k) => k.replace(/:\\d+$/, '').toLowerCase()).filter((h) => plainHostName(h) && !isBrowserServiceHost(h))).size); } if (tj && tj.pageLeftAppFor && typeof tj.pageLeftAppFor === 'object') { const left = Object.entries(tj.pageLeftAppFor).filter(([h, n]) => /^[a-z0-9.:[\\]-]{1,260}$/i.test(h) && Number.isFinite(n)).slice(0, 20).map(([host, times]) => ({ host, times })); if (left.length) pageLeftAppFor = left; }                                                                                                                           } } catch {                                                                   }
  return { refusedHosts, pageLeftAppFor, hostsRefused };
}


function blockedWord(cfg, runDir, outcome, counts, whyGiven) {
  if (outcome === 'needs-input') return 'needs_input';
  if (!counts.blocked && outcome !== 'blocked') return null;
  if (!counts.specs) { try { if (fs.lstatSync(path.join(runDir, 'used-folder')).isFile()) return 'used_folder'; } catch {                             } }
  if (whyGiven !== null) return RUNNER_WORDS.includes(whyGiven) ? whyGiven : 'other';
  try { const saved = cfg.storageState.inUse ? authFileInfo(cfg.storageState.path) : null; if (saved && saved.expired) return 'signin_expired'; if (saved ? saved.empty : listSkills(cfg.projectDir).some((s) => s.run && !s.problem)) return 'signin_missing'; } catch {                                             }
  return counts.specs ? 'specs_blocked' : 'blocked_before_specs';
}






const REMEMBER_NOTE = 'remember-offered';

const MEMORY_FILES = ['CLAUDE.md', 'CLAUDE.local.md']; const REMEMBERED_COMMAND = '/claude-test:run';
const REMEMBERED_WORD = new RegExp('(^|[\\\\s\`\\'"(*_\\\\[])' + REMEMBERED_COMMAND.replace(/[.*+?^\${}()|[\\]\\\\]/g, '\\\\$&') + '(?![\\\\w/-])');
function rememberDue(cfg, runId) {
  try {
    try { fs.lstatSync(path.join(cfg.runsDir, REMEMBER_NOTE)); return false; } catch (e) { if (e.code !== 'ENOENT') return false; }
    if (!pastRuns(cfg).some((r) => r.specs > 0 && r.runId !== runId)) return false;

    let saved = null; try { saved = JSON.parse(readPlainFile(path.join(cfg.runsDir, runId, 'saved.json'), 1024 * 1024).toString('utf8')); } catch (e) { if (!e || e.code !== 'ENOENT') return false; }
    if (saved && Array.isArray(saved.held) && saved.held.length) return false;

    const root = insideOpenedFolder(cfg.projectDir) ? process.env.CLAUDE_TEST_OPENED_DIR : sessionRoot();
    for (const dir of new Set([cfg.projectDir, root])) {
      for (const name of MEMORY_FILES) {
        let text = ''; try { text = readPlainFile(path.join(dir, name), 1024 * 1024).toString('utf8'); } catch (e) { if (e && e.code === 'ENOENT') continue; return false; }
        if (REMEMBERED_WORD.test(text)) return false;
      }
    }
    return writeInRunFolder(cfg.runsDir, REMEMBER_NOTE, new Date().toISOString() + '\\n', 0o644, withinOf(cfg));
  } catch { return false; }
}


function reportAfter(cfg, runDir, results) {
  try { writeReport(cfg, runDir, results, withinOf(cfg)); } catch {                 }
}



function finishCmd() {
  const cfg = loadConfig(projectDir);
  try { assertRunsDirInsideProject(cfg); } catch (e) { out({ error: e.message }); process.exit(1); }
  const runId = targetRunId(cfg);
  if (!runId) { out({ error: 'no run folder (a run that ended before "new-run" has no results file to write)' }); process.exit(1); }
  const whyAt = args.indexOf('--why'); const whyGiven = whyAt < 0 ? null : String(args[whyAt + 1] ?? '');
  const runDir = path.join(cfg.runsDir, runId);
  const logPath = path.join(runDir, 'log.md');
  let st; try { st = fs.lstatSync(logPath); } catch { out({ error: 'write ' + path.relative(cfg.projectDir, logPath) + ' first (the report: header line, verdict table, per-spec log), then finish' }); process.exit(1); }
  if (!st.isFile() || st.size > LOG_MD_BYTES) { out({ error: path.relative(cfg.projectDir, logPath) + ' must be a regular file of at most 4 MiB (' + LOG_MD_BYTES + ' bytes)' + (st.isFile() ? ': it is ' + st.size + ' bytes; shorten the log of each spec, write the whole log.md again, then finish again' : '') }); process.exit(1); }

  let logText; try { logText = writingIn(cfg, runDir, (at) => readPlainFile(at('log.md'), LOG_MD_BYTES)).toString('utf8'); } catch (e) { out({ error: path.relative(cfg.projectDir, logPath) + ' could not be read: ' + shown(String((e && e.message) || e), 300) + '. Write the whole log.md again, then finish again' }); process.exit(1); }
  const rep = parseReport(logText);
  const finishedAt = new Date(); const runnerSeconds = Math.min(86400, Math.max(0, Math.round((finishedAt.getTime() - runnerStart(cfg, runId).getTime()) / 1000)));
  const { refusedHosts, pageLeftAppFor, hostsRefused } = refusedTally(cfg, runDir);
  if (!rep.rows.length && !rep.blockedReason && rep.needsInput) {
    const missing = (logText.match(/^missing: (\\S+) in (.+)$/m) || []).slice(1, 3);
    const results = { schema: 'claude-test-results/1', tool: 'claude-test', toolVersion: pluginVersion(), toolDigest: pluginDigest(), runId, startedAt: runStart(runId).toISOString(), finishedAt: finishedAt.toISOString(), runnerSeconds, hostsRefused, blockedWord: blockedWord(cfg, runDir, 'needs-input', null, whyGiven), git: gitFor(cfg, runId), baseUrl: null, outcome: 'needs-input', ...(missing.length ? { missing: { key: shown(missing[0], 60), file: shown(missing[1], 200) } } : {}), counts: { specs: 0, passed: 0, failed: 0, blocked: 0 }, specs: [] };
    writeResults(cfg, runDir, results); reportAfter(cfg, runDir, results);
    out({ results: path.relative(cfg.projectDir, path.join(runDir, 'results.json')), outcome: 'needs-input', counts: results.counts }); return;
  }
  if (!rep.rows.length && !rep.blockedReason) { out({ error: 'log.md has no verdict table (| Spec | Verdict | Why | Screenshot | with one row per spec, each verdict cell holding PASS, FAIL or BLOCKED) and no "## Claude Test · BLOCKED · …" line — write the whole corrected log.md again, then finish again' }); process.exit(1); }
  const bad = rep.rows.filter((r) => !r.verdict);
  if (bad.length) { out({ error: 'verdict cell without the literal word PASS, FAIL or BLOCKED for: ' + bad.map((r) => r.name).join('; ') + ' — correct those rows, write the whole log.md again, then finish again' }); process.exit(1); }
  const specs = listSpecs(cfg);
  const byName = new Map(specs.filter((s) => s.name).map((s) => [s.name.trim().toLowerCase(), s]));
  const byStem = new Map(specs.map((s) => [path.basename(s.file, '.md'), s]));

  let progressLines = null; try { const pf = path.join(runDir, 'progress.ndjson'); const ps = fs.lstatSync(pf); if (!ps.isFile() || ps.size >= 4 * 1024 * 1024) throw new Error('not a progress file'); progressLines = writingIn(cfg, runDir, (at) => readPlainFile(at('progress.ndjson'), 4 * 1024 * 1024)).toString('utf8').split('\\n').filter(Boolean).map((l) => { try { return JSON.parse(l); } catch { return {}; } }); } catch {                        }
  const retriedStems = new Set((progressLines || []).filter((l) => l && l.retried === true && typeof l.spec === 'string').map((l) => l.spec));
  const RETRIED_WHY = /^(passed on retry|failed twice|blocked on retry)\\b/i;
  const rows = rep.rows.map((r) => { const s = byName.get(r.name.trim().toLowerCase()) || (r.screenshot ? byStem.get(path.basename(r.screenshot, '.png')) : null) || null; const stem = s ? path.basename(s.file, '.md') : r.screenshot ? path.basename(r.screenshot, '.png') : null; const retried = (stem !== null && retriedStems.has(stem)) || RETRIED_WHY.test(r.why); return { file: s ? s.file : null, id: s ? s.id : null, name: s && typeof s.name === 'string' && s.name.trim() ? shown(s.name.trim(), 140) : r.name, verdict: r.verdict, why: r.why, screenshot: r.screenshot && fs.existsSync(path.join(runDir, r.screenshot)) ? r.screenshot : null, ...(retried ? { retried: true } : {}) }; });


  {
    const recorded = new Map(); for (const l of progressLines || []) if (l && typeof l.spec === 'string' && ['PASS', 'FAIL', 'BLOCKED'].includes(l.verdict)) recorded.set(l.spec.normalize('NFC'), l.verdict);
    const linked = new Set(specs.filter((s) => s.skipped).map((s) => s.file));
    const unrecordable = (file) => { if (linked.has(file)) return 'unreadable'; try { const at = path.join(cfg.projectDir, file); return writingIn(cfg, path.dirname(at), (inDir) => readPlainFile(inDir(path.basename(at)), 4 * 1024 * 1024)).toString('utf8').includes(RUN_PLACEHOLDER) ? 'run' : null; } catch { return 'unreadable'; } };
    const key = (x) => shown(String(x).trim(), 160).trim().toLowerCase().normalize('NFC'); const specByStem = new Map(specs.map((s) => [path.basename(s.file, '.md').normalize('NFC'), s]));
    const byHeading = new Map(); for (const s of specs) if (typeof s.name === 'string' && s.name.trim()) { const k = key(s.name); if (!byHeading.has(k)) byHeading.set(k, []); byHeading.get(k).push(s); }
    const misnamed = new Set();
    rep.rows.forEach((raw, i) => {
      const r = rows[i]; const group = byHeading.get(key(raw.name)) || []; const shot = raw.screenshot ? specByStem.get(path.basename(raw.screenshot, '.png').normalize('NFC')) : null;
      let s = null; if (shot && (!group.length || group.includes(shot))) s = shot; else if (shot) { misnamed.add(r); if (group.length === 1) s = group[0]; } else if (group.length === 1) s = group[0];
      r.file = s ? s.file : null; r.id = s ? s.id : null; if (s && typeof s.name === 'string' && s.name.trim()) r.name = shown(s.name.trim(), 140);
      const stem = s ? path.basename(s.file, '.md') : raw.screenshot ? path.basename(raw.screenshot, '.png') : null; if ((stem !== null && retriedStems.has(stem)) || RETRIED_WHY.test(raw.why)) r.retried = true; else delete r.retried;
    });
    const rowsOf = new Map(); for (const r of rows) if (r.file) rowsOf.set(r.file, (rowsOf.get(r.file) || 0) + 1);
    const unproven = [];
    for (const r of rows.filter((x) => x.verdict === 'PASS')) {
      if (misnamed.has(r)) { unproven.push({ r, stem: null, why: 'its screenshot is of another spec: put the screenshot of the spec it names in its Screenshot cell, or leave the cell empty' }); continue; }
      if (!r.file) continue;
      if (rowsOf.get(r.file) > 1) { unproven.push({ r, stem: null, why: 'more than one row stands for the spec ' + shown(r.file, 140) + ': keep one row for each spec, under its own # heading' }); continue; }
      if (!stemOk(path.basename(r.file, '.md'))) continue;
      const stem = path.basename(r.file, '.md').normalize('NFC'); const why = recorded.has(stem) ? (recorded.get(stem) === 'PASS' ? null : 'you recorded ' + recorded.get(stem)) : unrecordable(r.file); if (why) unproven.push({ r, stem, why });
    }

    const matched = new Set(rows.filter((r) => r.file).map((r) => path.basename(r.file, '.md').normalize('NFC'))); const unmatched = rows.filter((r) => r.verdict === 'PASS' && !r.file && !misnamed.has(r)); const specStems = new Set(specs.filter((s) => !s.skipped).map((s) => path.basename(s.file, '.md').normalize('NFC')));
    if (unmatched.length > [...recorded].filter(([stem, verdict]) => verdict === 'PASS' && specStems.has(stem) && !matched.has(stem)).length) for (const r of unmatched) unproven.push({ r, stem: null, why: 'it names no spec file, and there are more such rows than recorded PASSes that no row names: write its Spec cell as the spec\\'s own # heading, or, when no spec file is behind the row, make it BLOCKED' });
    const said = (why) => (why === 'run' ? 'no verdict was recorded, and its steps hold ' + RUN_PLACEHOLDER + ': claude_test_progress records such a PASS only after this run\\'s value was typed and then acted on' : why === 'unreadable' ? 'no verdict was recorded, and its file could not be read: no PASS can be recorded for it, so make it BLOCKED with that reason' : why);
    const shape = unproven.filter((u) => u.stem === null); if (shape.length) { out({ error: 'the table\\'s shape: ' + shape.map((u) => '"' + shown(u.r.name, 140) + '" (' + u.why + ')').join('; ') + '. Fix each as its reason says; a fault of form alone is no reason to change a row\\'s verdict. Then write the whole log.md again and finish again' }); process.exit(1); }
    if (unproven.length) { out({ error: 'the table says PASS for specs whose PASS was not recorded: ' + unproven.map((u) => '"' + shown(u.r.name, 140) + '" (' + said(u.why) + ')').join('; ') + '. Change each of these rows to the verdict you recorded; where none was recorded, to FAIL naming the step that did not run, or to BLOCKED with the reason (BLOCKED "its PASS could not be recorded" when the steps ran but claude_test_progress recorded nothing). Correct the counts in the header line, write the whole log.md again, then finish again' }); process.exit(1); }
  }
  const counts = { specs: rows.length, passed: rows.filter((r) => r.verdict === 'PASS').length, failed: rows.filter((r) => r.verdict === 'FAIL').length, blocked: rows.filter((r) => r.verdict === 'BLOCKED').length };
  const outcome = counts.failed ? 'failed' : (counts.blocked || (rep.blockedReason && !rows.length)) ? 'blocked' : counts.passed ? 'passed' : 'blocked';
  const m = runId.match(/^(\\d{4})-(\\d{2})-(\\d{2})T(\\d{2})-(\\d{2})-(\\d{2})/);
  const startedAt = new Date(Number(m[1]), Number(m[2]) - 1, Number(m[3]), Number(m[4]), Number(m[5]), Number(m[6])).toISOString();

  let secondsPerSpec = null; try { if (!progressLines) throw new Error('no progress file'); const ls = progressLines; const start = ls.find((l) => l.event === 'start'); const specsAt = ls.filter((l) => typeof l.spec === 'string').map((l) => Date.parse(l.at)).filter(Number.isFinite).sort((a, b) => a - b); if (start && specsAt.length) secondsPerSpec = Math.round((specsAt[specsAt.length - 1] - Date.parse(start.at)) / specsAt.length / 1000); else if (specsAt.length >= 2) secondsPerSpec = Math.round((specsAt[specsAt.length - 1] - specsAt[0]) / (specsAt.length - 1) / 1000); } catch {                        }
  const word = blockedWord(cfg, runDir, outcome, counts, whyGiven);

  const full = rows.length > 0 && specs.filter((s) => !s.skipped && stemOk(path.basename(s.file, '.md'))).every((s) => rows.some((r) => r.file === s.file));
  const rememberOffer = outcome === 'passed' && rememberDue(cfg, runId);
  const results = { schema: 'claude-test-results/1', tool: 'claude-test', toolVersion: pluginVersion(), toolDigest: pluginDigest(), runId, startedAt, finishedAt: finishedAt.toISOString(), runnerSeconds, hostsRefused, ...(word ? { blockedWord: word } : {}), ...(rememberOffer ? { rememberOffer: true } : {}), ...(full ? { full: true } : {}), ...(secondsPerSpec ? { secondsPerSpec } : {}), ...(refusedHosts ? { refusedHosts } : {}), ...(pageLeftAppFor ? { pageLeftAppFor } : {}), git: gitFor(cfg, runId), baseUrl: cfg.baseUrl || (rep.head && /^https?:\\/\\//.test(rep.head.baseUrl) ? rep.head.baseUrl : null), outcome, counts, ...(rep.blockedReason ? { blockedReason: rep.blockedReason } : {}), specs: rows };
  writeResults(cfg, runDir, results); reportAfter(cfg, runDir, results);
  const notes = [];
  const unmatched = rows.filter((r) => !r.file).map((r) => r.name); if (unmatched.length) notes.push('rows whose Spec cell matches no spec file\\'s "# name" (file and id are null for them): ' + unmatched.join('; '));
  const files = rows.map((r) => r.file).filter(Boolean); const dup = [...new Set(files.filter((f, i) => files.indexOf(f) !== i))]; if (dup.length) notes.push('more than one row for the same spec file: ' + dup.join(', '));
  if (rep.head && rep.head.specs !== rows.length) notes.push('the header says ' + rep.head.specs + ' specs but the table has ' + rows.length + ' rows');
  const unlisted = specs.filter((s) => !s.skipped && !listableStem(path.basename(s.file, '.md')) && !rows.some((r) => r.file === s.file)).length;
  const leftOutLine = !unlisted ? null : unlisted === 1 ? '1 spec file in the specs folder is left out whenever every spec runs: its file name is longer than 120 characters or holds an invisible character such as a tab or a line break; rename it' : unlisted + ' spec files in the specs folder are left out whenever every spec runs: their file names are longer than 120 characters or hold an invisible character such as a tab or a line break; rename them';


  const noticed = (([...logText.matchAll(/^Noticed: (.+)$/gm)].pop() || [])[1] || '').split(' · ').map((item) => item.trim().replace(/^(\\d{1,5}) console errors?\\b/, (_, n) => n + (n === '1' ? ' console error' : ' console errors'))).filter((item) => NOTICED_ITEMS.some((shape) => shape.test(item))).slice(0, 4);
  const noticedLine = noticed.length ? 'Noticed: ' + noticed.join(' · ') : null;

  const specName = new Map(specs.map((s) => [s.file, s.name]));
  const flaky = rows.filter((r) => r.retried && r.verdict === 'PASS' && r.file).map((r) => shown(specName.get(r.file) || r.name, 140));
  const retriedLine = flaky.length ? 'Passed on a second try (may be flaky): ' + flaky.join(', ') : null;
  out({ ok: true, results: path.relative(cfg.projectDir, path.join(runDir, 'results.json')), outcome, counts, ...(retriedLine ? { retriedLine } : {}), ...(noticedLine ? { noticedLine } : {}), ...(leftOutLine ? { leftOutLine } : {}), ...(refusedHosts ? { refusedHosts } : {}), ...(pageLeftAppFor ? { pageLeftAppFor } : {}), ...(notes.length ? { note: notes.join(' · ') } : {}) });
}



function listableStem(stem) { return !!stem && stem.length <= 120 && !/[\\u0000-\\u001f\\u007f\\u2028\\u2029]/.test(stem); }




const NOTICED_PATH = String.raw\`\\/(?!\\/)[A-Za-z0-9._~:@\\/-]{0,119}\`;
const NOTICED_ITEMS = [
  /^\\d{1,4} console errors? \\([A-Z][A-Za-z0-9]{0,40}(, [A-Z][A-Za-z0-9]{0,40}){0,2}\\)$/,
  /^\\d{1,4} console errors?$/,
  new RegExp('^(?:[45]\\\\d\\\\d|failed) ' + NOTICED_PATH + '$'),
  new RegExp('^(?:NaN|undefined|\\\\[object Object\\\\]|Invalid Date) on ' + NOTICED_PATH + '$'),
];



function pastRuns(cfg) {
  const rows = [];
  for (const d of runFolders(cfg)) {
    const t = runStart(d).getTime();
    const r = readJson(path.join(cfg.runsDir, d, 'results.json')); if (!r || r.schema !== 'claude-test-results/1') continue;
    const specs = r.counts && Number.isInteger(r.counts.specs) && r.counts.specs >= 0 ? r.counts.specs : 0;
    const judged = r.counts && Number.isInteger(r.counts.passed) && Number.isInteger(r.counts.failed) ? r.counts.passed + r.counts.failed : 0;
    rows.push({ runId: d, at: t, judged, outcome: ['passed', 'failed', 'blocked'].includes(r.outcome) ? r.outcome : null, finishedAt: typeof r.finishedAt === 'string' && /^\\d{4}-\\d{2}-\\d{2}T[\\d:.]+Z$/.test(r.finishedAt) ? r.finishedAt : null, specs, secondsPerSpec: Number.isFinite(r.secondsPerSpec) && r.secondsPerSpec >= 1 && r.secondsPerSpec <= 3600 ? Math.round(r.secondsPerSpec) : null, head: r.git && typeof r.git.head === 'string' && /^[0-9a-f]{40}$/.test(r.git.head) ? r.git.head : null, dirty: r.git && typeof r.git.dirty === 'boolean' ? r.git.dirty : null, changed: changedOf(r.git), secretChanged: !!(r.git && r.git.secretChanged === true), full: r.full === true });
  }
  return rows.reverse();
}


function recordedGit(cfg, runId) {
  try { const at = JSON.parse(writingIn(cfg, path.join(cfg.runsDir, runId), (name) => readPlainFile(name('git.json'), 256 * 1024)).toString('utf8')); if (!(at && typeof at === 'object' && typeof at.head === 'string' && /^[0-9a-f]{40}$/.test(at.head) && (typeof at.dirty === 'boolean' || at.dirty === null))) return null; const changed = changedOf(at); return { head: at.head, dirty: at.dirty, ...(changed !== null ? { changed } : {}), ...(changed !== null && at.secretChanged === true ? { secretChanged: true } : {}) }; } catch { return null; }
}

function gitFor(cfg, runId) { return gitOff() ? recordedGit(cfg, runId) : gitState(cfg.projectDir); }




const CHANGED_AT_MOST = 400;
function gitState(dir) {

  try {
    const head = safeGit(dir, ['rev-parse', 'HEAD']).toString().trim(); let dirty = null; let changed = null; let secretChanged = false;
    try { dirty = safeGit(dir, ['status', '--porcelain', '--untracked-files=no'], { timeout: 60000 }).toString().trim() !== ''; } catch {                                                                      }
    try { const files = safeGit(dir, ['-c', 'core.quotePath=false', 'status', '--porcelain', '--no-renames', '--untracked-files=all', '--', '.'], { maxBuffer: 4 * 1024 * 1024, timeout: 60000 }).toString().split('\\n').filter(Boolean).map((l) => l.slice(3).replace(/^"(.*)"$/, '$1')); const shown = files.filter((f) => !SECRET_FILE.test(f)); changed = shown.length <= CHANGED_AT_MOST && Buffer.byteLength(JSON.stringify(shown)) <= 200 * 1024 ? changedOf({ changed: shown }) : null; secretChanged = shown.length < files.length; } catch {                                                }
    return /^[0-9a-f]{40}$/.test(head) ? { head, dirty, ...(changed !== null ? { changed } : {}), ...(changed !== null && secretChanged ? { secretChanged: true } : {}) } : null;
  } catch { return null; }
}

function changedOf(git) { const c = git && git.changed; return Array.isArray(c) && c.length <= CHANGED_AT_MOST && c.every((f) => typeof f === 'string' && f.length > 0 && f.length <= 400 && !f.includes('\\0')) ? c : null; }



function prefsCmd() {
  const cfg = loadConfig(projectDir);
  if (args.length === 1) { const p = readPrefs(cfg); const st = readStart(cfg.projectDir); out({ prefs: { livePage: p.livePage === 'link' ? 'link' : 'open', start: st.start && typeof st.start.command === 'string' ? { command: shown(st.start.command, 400), folder: shown(String(st.start.folder), 400) } : null }, file: prefsPath(cfg), startFile: st.file, ...(st.refused ? { startProblem: st.refused } : {}) }); return; }

  if (args[1] === 'start' && args[2] === 'forget' && args.length === 3) { const r = forgetStart(cfg.projectDir); if (r.why) { out({ error: shown(r.why, 600), file: r.file }); process.exit(1); } out({ ok: true, forgotten: r.removed, file: r.file, note: r.removed ? 'the next run asks again before it starts the app' : 'no start was remembered for this project on this machine' }); return; }
  if (args[1] !== 'live-page' || !['open', 'link'].includes(args[2]) || args.length !== 3) { out({ error: 'usage: ct.mjs prefs live-page open|link — open: a run opens its live page in your browser; link: it only prints the address. ct.mjs prefs start forget \\u2014 forget the app start you accepted, so the next run asks again' }); process.exit(2); }
  const ok = writePrefs(cfg, { ...readPrefs(cfg), livePage: args[2] });
  if (!ok) { out({ error: 'could not write ' + prefsPath(cfg) }); process.exit(1); }
  out({ ok: true, livePage: args[2], file: prefsPath(cfg), note: args[2] === 'link' ? 'runs will print the live page\\'s address and open nothing' : 'a run will open its live page in your browser when it starts' });
}




function allowCmd() {
  const cfg = loadConfig(projectDir); const remove = args[1] === '--remove'; const given = args.slice(remove ? 2 : 1);
  const rec = readConsent(cfg.projectDir);
  if (!given.length && !remove) { out({ file: rec.file, allowed: { addresses: [...rec.origins], loadOnlyHosts: [...rec.hosts] }, waiting: { addresses: cfg.pendingOrigins, loadOnlyHosts: cfg.pendingHosts }, ...(rec.refused ? { problem: rec.refused } : {}) }); return; }
  if (!remove) { out({ error: 'ct.mjs has no command that allows an address — nothing was changed. Type /claude-test in a Claude Code conversation and answer the dialog it opens: only that records your yes. ("allow" alone prints the record; "allow --remove <address>" drops an entry.)' }); process.exit(2); }
  if (!given.length) { out({ error: 'allow --remove needs the addresses to drop ("allow" alone prints the record)' }); process.exit(2); }
  const origins = []; const hosts = []; const refused = [];
  for (const a of given) {
    const k = consentKey(a); const h = String(a).trim().toLowerCase();
    const asOrigin = rec.origins.has(k); const asHost = rec.hosts.has(h);
    if (asOrigin) origins.push(k);
    if (asHost) hosts.push(h);
    if (!asOrigin && !asHost) refused.push(shown(a, 120));
  }
  if (refused.length) { out({ error: 'not in the record: ' + refused.join(', ') + ' — nothing was changed' }); process.exit(2); }
  const why = writeConsent(cfg.projectDir, { origins, hosts, remove: true });
  if (why) { out({ error: why + (why.includes('may not write there') ? ': to take an address back, run this command in your own terminal' : '') }); process.exit(1); }
  out({ ok: true, removed: [...origins, ...hosts], file: rec.file, note: 'for this project on this machine only; the test browser of a session already started keeps its addresses until Claude Code restarts' });
}




async function progressCmd() {
  const cfg = loadConfig(projectDir);
  try { assertRunsDirInsideProject(cfg); } catch (e) { out({ error: e.message }); process.exit(1); }
  const runId = targetRunId(cfg);
  if (!runId) { out({ error: 'no run folder yet ("ct.mjs new-run" first)' }); process.exit(1); }

  const retriedAt = args.indexOf('--retried'); const retried = retriedAt > 0; if (retried) args.splice(retriedAt, 1);
  const file = path.join(cfg.runsDir, runId, 'progress.ndjson');
  try { const st = fs.lstatSync(file); if (!st.isFile()) { out({ error: path.relative(cfg.projectDir, file) + ' exists and is not a regular file — not writing through it' }); process.exit(1); } } catch {                                            }
  const read = () => { try { return fs.readFileSync(file, 'utf8').split('\\n').filter(Boolean).map((l) => { try { return JSON.parse(l); } catch { return null; } }).filter(Boolean); } catch { return []; } };

  const addLine = (line) => {

    try { writingIn(cfg, path.dirname(file), (at) => addLineAt(at(path.basename(file)), line)); }
    catch (e) { out({ error: shown(String((e && e.message) || e), 300) + ' — nothing was recorded. Go on, and say so under Notes' }); process.exit(1); }
  };
  const addLineAt = (file, line) => {
    let fd; try { fd = fs.openSync(file, fs.constants.O_WRONLY | fs.constants.O_APPEND | fs.constants.O_CREAT | (process.platform === 'win32' ? 0 : fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK), 0o644); } catch (e) { out({ error: path.relative(cfg.projectDir, file) + ' could not be opened (' + (e && (e.code === 'ELOOP' || e.code === 'EMLINK') ? 'a link is at that name — not writing through it' : 'the disk or the folder refused it: ' + shown(String(e && e.code || e), 40)) + ')' }); process.exit(1); }
    try { const st = fs.fstatSync(fd); if (!st.isFile() || st.nlink > 1) { out({ error: path.relative(cfg.projectDir, file) + ' is not a regular file of its own (a second name of another file) — not writing through it' }); process.exit(1); } fs.writeSync(fd, JSON.stringify(line) + '\\n'); } finally { fs.closeSync(fd); }
  };
  const specLines = () => read().filter((l) => l && typeof l.spec === 'string');


  let drop = []; try { const d = readJson(path.join(cfg.runsDir, runId, 'decisions.json')); if (d && Array.isArray(d.drop)) drop = d.drop.filter((s) => stemOk(s)).slice(0, 50); } catch {            }






  const startLine = () => read().find((l) => l.event === 'start') || null;
  const summary = () => {
    const lines = specLines(); const st = startLine(); const planned = st && Array.isArray(st.specs) ? st.specs.filter((x) => typeof x === 'string' && !drop.includes(x)) : null;
    const doneSet = new Set(lines.map((l) => l.spec)); const last = lines[lines.length - 1] || null;
    const runningNow = planned ? planned.find((x) => !doneSet.has(x)) || null : null;
    const secondsPerSpec = last && typeof last.s === 'number' && lines.length ? Math.max(1, Math.round(last.s / lines.length)) : null;
    const left = planned ? planned.filter((x) => !doneSet.has(x)).length : null;
    return { done: lines.length, ...(planned ? { of: planned.length, left, runningNow } : {}), counts: { PASS: lines.filter((l) => l.verdict === 'PASS').length, FAIL: lines.filter((l) => l.verdict === 'FAIL').length, BLOCKED: lines.filter((l) => l.verdict === 'BLOCKED').length }, ...(secondsPerSpec ? { secondsPerSpec, ...(left !== null ? { aboutSecondsLeft: left * secondsPerSpec } : {}) } : {}), lines };
  };



  const specNamedStart = () => { try { return listSpecs(cfg).some((x) => path.basename(x.file, '.md') === 'start'); } catch { return false; } };
  const startWithStems = args[1] === 'start' && args.length > 2 && !(args.length === 3 && ['PASS', 'FAIL', 'BLOCKED'].includes(String(args[2]).toUpperCase()) && specNamedStart());
  if (startWithStems && !args.slice(2).every((x) => stemOk(x))) { out({ error: 'usage: ct.mjs progress start [<spec file stem> …] — the stems of a run limited to some specs, each in single quotes' }); process.exit(2); }
  if (args.length === 1 || (args[1] === 'start' && args.length === 2) || startWithStems) {
    if (retried) { out({ error: 'usage: --retried goes with a verdict only: ct.mjs progress <spec file stem> PASS|FAIL|BLOCKED --retried' }); process.exit(2); }
    if (args[1] === 'start' && !startLine()) {
      let specs = []; let names = {}; let areas = {}; let data = []; try {
        const all = listSpecs(cfg).filter((x) => !x.skipped).map((x) => ({ stem: path.basename(x.file, '.md'), name: typeof x.name === 'string' && x.name.trim() ? x.name.trim().slice(0, 140) : null, area: typeof x.area === 'string' ? x.area : null, last: Array.isArray(x.tags) && x.tags.includes('creates-data') })).filter((x) => listableStem(x.stem));
        const want = startWithStems ? [...new Set(args.slice(2))] : null;
        const chosen = want ? want.map((w) => all.find((x) => x.stem === w) || { stem: w, last: false }) : all.sort((a, b) => a.stem < b.stem ? -1 : a.stem > b.stem ? 1 : 0);
        const ordered = [...chosen.filter((x) => !x.last), ...chosen.filter((x) => x.last)].slice(0, 500);
        specs = ordered.map((x) => x.stem); names = Object.fromEntries(ordered.filter((x) => x.name).map((x) => [x.stem, x.name])); areas = Object.fromEntries(ordered.filter((x) => x.area).map((x) => [x.stem, x.area])); data = ordered.filter((x) => x.last).map((x) => x.stem);
      } catch {                                                                       }
      writeInRunFolder(path.join(cfg.runsDir, runId), 'names.json', JSON.stringify({ names, ...(Object.keys(areas).length ? { areas } : {}), ...(data.length ? { data } : {}) }) + '\\n', 0o644, withinOf(cfg));
      addLine({ event: 'start', at: new Date().toISOString(), ...(specs.length ? { specs } : {}) });
    }
    const sl = startLine(); out({ runId, file: path.relative(cfg.projectDir, file), absolute: file, ...(args[1] === 'start' && sl && Array.isArray(sl.specs) ? { order: sl.specs } : {}), ...summary(), ...(drop.length ? { drop } : {}) }); return;
  }
  const stem = args[1]; const verdict = String(args[2] || '').toUpperCase();
  if (!stemOk(stem) || !['PASS', 'FAIL', 'BLOCKED'].includes(verdict)) { out({ error: 'usage: ct.mjs progress <spec file stem> PASS|FAIL|BLOCKED [--retried]' }); process.exit(2); }
  const now = new Date(); const st0 = startLine(); const t0 = st0 && st0.at ? Date.parse(st0.at) : NaN;


  let frames = []; try { const taken = new Set(read().flatMap((l) => Array.isArray(l.frames) ? l.frames : [])); const all = fs.readdirSync(path.join(cfg.runsDir, runId, 'frames')).filter((f) => /^f-\\d{4}\\.jpeg$/.test(f) && !taken.has(f)).sort(); frames = all.length <= 40 ? all : [...new Set(Array.from({ length: 40 }, (_, k) => all[Math.round(k * (all.length - 1) / 39)]))]; } catch {                                                                                }
  const line = { spec: stem, verdict, at: now.toISOString(), ...(Number.isFinite(t0) ? { s: Math.max(0, Math.round((now.getTime() - t0) / 1000)) } : {}), ...(retried ? { retried: true } : {}), ...(frames.length ? { frames } : {}) };
  addLine(line);
  out({ ok: true, file: path.relative(cfg.projectDir, file), done: specLines().length, ...(drop.length ? { drop } : {}) });
}







function planSpecsOf(cfg, failedLast, changed = new Set(), judged = null, verdictAt = new Map()) {
  const planSpecs = [];
  for (const s of listSpecs(cfg)) {
    if (s.skipped) continue;
    const stem = path.basename(s.file, '.md');
    let text = null; try { text = fs.readFileSync(path.join(cfg.projectDir, s.file), 'utf8'); } catch {                                                        }
    const fc = text === null ? null : fromComment(text);
    const named = [...new Set((fc ? fc.files : []).map((f) => appRelative(cfg.projectDir, f)).filter((f) => f !== null))];
    const there = (f) => { const p = path.join(cfg.projectDir, f); try { return reallyInsideDir(p, cfg.projectDir) && fs.existsSync(p); } catch { return false; } };
    const live = named.filter((f) => changed.has(f) || there(f));
    let edited = false; if (verdictAt.has(s.file)) { try { edited = fs.lstatSync(path.join(cfg.projectDir, s.file)).mtimeMs > verdictAt.get(s.file); } catch {                                               } }
    planSpecs.push({ stem, files: live.length ? live : null, data: Array.isArray(s.tags) && s.tags.includes('creates-data'), failedLast: failedLast.has(stem), noRecentResult: judged !== null && !judged.has(s.file), edited });
  }
  return planSpecs;
}



const NOT_SOURCE_FOLDER = /(^|\\/)(\\.claude-test|\\.claude|node_modules)\\/|^(dist|build|coverage|\\.next)\\//;

function notASourceChange(f) { return NOT_SOURCE_FOLDER.test(f) || /(^|\\/)(package-lock\\.json|pnpm-lock\\.yaml|yarn\\.lock|bun\\.lockb?)$|\\.lock$/.test(f); }




function fixPlanCmd() {
  const cfg = loadConfig(projectDir);
  if (args.length > 1) { out({ error: 'usage: ct.mjs fix-plan (it takes no arguments: it reads the tests that did not pass from the recent runs, and the changed files from git)' }); process.exit(1); }
  try { assertRunsDirInsideProject(cfg); } catch (e) { out({ error: e.message }); process.exit(1); }
  const past = pastRuns(cfg).filter((r) => r.specs > 0); const newest = past[0];
  const results = newest ? readJson(path.join(cfg.runsDir, newest.runId, 'results.json')) : null;
  const rowsOf = (r) => (r && Array.isArray(r.specs) ? r.specs : []).filter((row) => row && typeof row === 'object');


  let present = new Set(); try { present = new Set(listSpecs(cfg).map((s) => s.file)); } catch {                                                  }
  const judged = new Set(rowsOf(results).map((row) => row.file)); const carried = [];
  for (const p of past.slice(1, 31)) for (const row of rowsOf(readJson(path.join(cfg.runsDir, p.runId, 'results.json')))) { if (typeof row.file !== 'string' || judged.has(row.file)) continue; judged.add(row.file); if (row.verdict !== 'PASS' && present.has(row.file)) carried.push(row); }
  const notPassed = [...rowsOf(results).filter((row) => row.verdict !== 'PASS'), ...carried];
  const failedAll = [...new Set(notPassed.filter((row) => typeof row.file === 'string').map((row) => path.basename(row.file, '.md')))];
  if (!results) { out({ error: 'no run has test results yet, so there is nothing to re-run' }); process.exit(1); }
  if (!notPassed.length) { out({ error: 'no test\\'s newest verdict is failed or blocked, so there is nothing to re-run' }); process.exit(1); }

  if (failedAll.some((s) => !stemOk(s))) { out({ error: 'the file name of a test that did not pass has a character the runner cannot take, such as a quote or a leading hyphen: re-run every spec instead, giving the runner no stems' }); process.exit(1); }


  const git = (argv) => { try { return safeGit(cfg.projectDir, ['-c', 'core.quotePath=false', ...argv], { maxBuffer: 4 * 1024 * 1024, timeout: 60000 }).toString(); } catch { return null; } };
  const prefix = git(['rev-parse', '--show-prefix']);
  const status = git(['status', '--porcelain', '--no-renames', '--untracked-files=all', '--', '.']);

  const changedUnknown = prefix === null || status === null;
  const at = (prefix || '').trim(); const rel = (f) => at && f.startsWith(at) ? f.slice(at.length) : (at ? null : f);
  const listed = changedUnknown ? [] : [...new Set(status.split('\\n').filter(Boolean).map((l) => rel(l.slice(3).replace(/^"(.*)"$/, '$1'))).filter((f) => f && !notASourceChange(f)))];

  const recorded = newest.changed ? new Set(newest.changed.map(rel).filter((f) => f && appRelative(cfg.projectDir, f) === f && !notASourceChange(f))) : null;

  let startedAt = newest.at; try { startedAt = Math.min(startedAt, fs.lstatSync(path.join(cfg.runsDir, newest.runId, 'save-key.sha256')).mtimeMs); } catch {                                           }

  const modifiedAt = (f) => { const p = path.join(cfg.projectDir, f); if (appRelative(cfg.projectDir, f) !== f) return null; for (const q of [p, path.dirname(p)]) { try { if (!reallyInsideDir(q, cfg.projectDir)) return null; return fs.lstatSync(q).mtimeMs; } catch (e) { if (e.code !== 'ENOENT' && e.code !== 'ENOTDIR') return null; } } return null; };
  const touched = changedUnknown ? [] : touchedSince({ uncommitted: listed, recorded, startedAt, modifiedAt, secret: (f) => SECRET_FILE.test(at + f) });
  const planSpecs = planSpecsOf(cfg, new Set(failedAll), new Set(touched));
  if (notPassed.some((row) => typeof row.file !== 'string') || failedAll.some((s) => !planSpecs.some((p) => p.stem === s))) { out({ error: 'a test that did not pass is not a spec the runner can take now: re-run every spec instead, giving the runner no stems' }); process.exit(1); }
  const plan = fixPlan(planSpecs, failedAll, touched, { local: reachesOnlyThisMachine(cfg) });
  const named = [...plan.run, ...(plan.notRerun || [])];
  const titles = {}; try { for (const x of listSpecs(cfg)) { const stem = path.basename(x.file, '.md'); const name = typeof x.name === 'string' && x.name.trim() ? shown(x.name.trim(), 140) : null; if (named.includes(stem) && name) titles[stem] = name; } } catch {                      }
  out({ run: plan.run, ...(Object.keys(titles).length ? { titles } : {}), also: plan.also, ...(plan.notRerun ? { notRerun: plan.notRerun } : {}), ...(plan.unnamed ? { unnamed: plan.unnamed } : {}), ...(changedUnknown ? { changedUnknown: true } : {}) });
}




function changesCmd() {
  const cfg = loadConfig(projectDir);
  try { assertRunsDirInsideProject(cfg); } catch (e) { out({ error: e.message }); process.exit(1); }
  const past = pastRuns(cfg);
  const last = past.find((r) => r.specs > 0 && r.head && r.full);
  let since = last ? { runId: last.runId, head: last.head, finishedAt: last.finishedAt, outcome: last.outcome } : null;

  const git = (argv) => { try { return safeGit(cfg.projectDir, ['-c', 'core.quotePath=false', ...argv], { maxBuffer: 4 * 1024 * 1024, timeout: 60000 }).toString(); } catch { return null; } };
  const head = (git(['rev-parse', 'HEAD']) || '').trim() || null;
  const prefix = (git(['rev-parse', '--show-prefix']) || '').trim();
  const rel = (f) => prefix && f.startsWith(prefix) ? f.slice(prefix.length) : (prefix ? null : f);
  const keep = (f) => f && !NOT_SOURCE_FOLDER.test(f) && !/(^|\\/)(package-lock\\.json|pnpm-lock\\.yaml|yarn\\.lock|bun\\.lockb?|\\.gitignore)$/.test(f) && !/\\.(test|spec)\\.[a-z]+$|\\.(md|lock|log|png|jpg|svg|ico|map)$/.test(f) && !SECRET_FILE.test(f);
  const gone = !!(since && git(['cat-file', '-e', since.head + '^{commit}']) === null);
  if (gone) since = { ...since, gone: true };
  const diffOut = since && !gone && head && since.head !== head ? git(['diff', '--no-ext-diff', '--no-textconv', '--no-renames', '--name-only', since.head, 'HEAD', '--', '.']) : '';
  const statusOut = git(['status', '--porcelain', '--no-renames', '--untracked-files=all', '--', '.']);
  const committedAny = (diffOut || '').split('\\n').map(rel);
  const porcelainAny = (statusOut || '').split('\\n').filter(Boolean).map((l) => ({ untracked: l.startsWith('??'), file: rel(l.slice(3).replace(/^.* -> /, '').replace(/^"(.*)"$/, '$1')) }));
  const committed = committedAny.filter(keep);
  const porcelain = porcelainAny.filter((e) => keep(e.file));
  const uncommitted = porcelain.map((e) => e.file); const untracked = new Set(porcelain.filter((e) => e.untracked).map((e) => e.file));
  const changedAll = [...new Set([...committed, ...uncommitted])]; const changed = changedAll.slice(0, 200);






  const judgingRuns = last ? past.slice(0, past.indexOf(last) + 1).filter((r) => r.specs > 0) : [];
  const testedLists = judgingRuns.map((r) => r.changed ?? (r.dirty === false ? [] : null));
  const testedDirty = testedLists.includes(null) ? null : [...new Set(testedLists.flat())];
  const planChangedAll = [...new Set([...committedAny, ...porcelainAny.map((e) => e.file), ...(testedDirty || []).map(rel)])].filter((f) => f && !notASourceChange(f));
  const planChanged = planChangedAll.slice(0, 400);
  const answered = head !== null && diffOut !== null && statusOut !== null;

  const citedBy = Object.create(null);

  const latest = new Map(); const verdictAt = new Map(); for (const p of past.filter((x) => x.specs > 0).slice(0, 30)) { const r = readJson(path.join(cfg.runsDir, p.runId, 'results.json')); for (const row of r && Array.isArray(r.specs) ? r.specs : []) if (row && typeof row.file === 'string' && typeof row.verdict === 'string' && !latest.has(row.file)) { latest.set(row.file, row.verdict); verdictAt.set(row.file, Date.parse(p.finishedAt ?? '') || p.at); } }
  const failedLast = new Set([...latest].filter(([, verdict]) => verdict !== 'PASS').map(([file]) => path.basename(file, '.md')));
  const planSpecs = planSpecsOf(cfg, failedLast, new Set(planChanged), new Set(latest.keys()), verdictAt);
  for (const { stem, files: cites } of planSpecs) for (const clean of cites || []) { (citedBy[clean] = citedBy[clean] || []); if (!citedBy[clean].includes(stem)) citedBy[clean].push(stem); }

  const secretTested = judgingRuns.some((r) => r.secretChanged) ? planSpecs.flatMap((s) => (s.files || []).filter((f) => SECRET_FILE.test(prefix + f) || SECRET_FILE.test(f))) : [];
  const plan = affectedPlan(planSpecs, [...new Set([...planChanged, ...secretTested])], { complete: !!since && !gone && answered && testedDirty !== null && planChangedAll.length <= planChanged.length });
  const covered = changed.filter((f) => citedBy[f]); const uncovered = changed.filter((f) => !citedBy[f]);


  const base = since && !gone ? since.head : (head || null);
  const files = changed.slice(0, 50).map((f) => {
    if (untracked.has(f)) { let lines = null; try { const p = path.join(cfg.projectDir, f); const st = fs.lstatSync(p); if (st.isFile() && st.size <= 1024 * 1024) lines = fs.readFileSync(p, 'utf8').split('\\n').length; } catch {                  } return { file: f, status: 'untracked', ...(lines !== null ? { lines } : {}) }; }
    if (!base) return { file: f, status: 'modified' };
    const num = (git(['diff', '--no-ext-diff', '--no-textconv', '--numstat', base, '--', ':(literal)' + f]) || '').trim().split('\\t');
    const hunks = (git(['diff', '--no-ext-diff', '--no-textconv', '--no-color', '--unified=0', base, '--', ':(literal)' + f]) || '').split('\\n').map((l) => l.match(/^@@ -\\d+(?:,\\d+)? \\+(\\d+)(?:,(\\d+))? @@/)).filter(Boolean).slice(0, 40).map((m) => { const start = Number(m[1]); const n = m[2] === undefined ? 1 : Number(m[2]); return n === 0 ? start + ' (lines removed here)' : n === 1 ? String(start) : start + '-' + (start + n - 1); });
    const exists = fs.existsSync(path.join(cfg.projectDir, f));
    return { file: f, status: !exists ? 'deleted' : num.length === 3 && num[0] !== '-' && git(['cat-file', '-e', base + ':' + prefix + f]) === null ? 'added' : 'modified', ...(num.length === 3 && /^\\d+$/.test(num[0]) ? { added: Number(num[0]), removed: Number(num[1]) } : {}), ...(hunks.length ? { changedLines: hunks } : {}) };
  });
  out({ since, head, ...(since && head === since.head ? { sameCommit: true } : {}), plan, changedFiles: changed, uncommittedFiles: uncommitted.slice(0, 100), cited: covered.map((f) => ({ file: f, specs: citedBy[f] })), uncovered, files, ...(covered.length ? { citedNote: 'cited is not covered — check the behaviour: a spec names these files as a source, which says nothing about the NEW behaviour in them; read the change and ask whether that spec\\'s steps and Must lines would notice it — if not, it needs a spec of its own' } : {}), note: since && gone ? 'the last run (' + since.runId + ') recorded commit ' + since.head.slice(0, 8) + ', which is no longer in this repository (rebased away, or the run folder came from elsewhere): committed history was NOT compared — only uncommitted files are listed; say so rather than "nothing changed"' : since ? 'changed since run ' + since.runId + ' (' + since.head.slice(0, 8) + ')' + (changed.length ? '' : ': nothing in the app\\'s source') : 'no earlier run that ran every test recorded a commit (results.json full and git.head): everything uncommitted is listed; committed history is not compared' });
}



function elapsedCmd() {
  const cfg = loadConfig(projectDir);
  try { assertRunsDirInsideProject(cfg); } catch (e) { out({ error: e.message }); process.exit(1); }
  const id = targetRunId(cfg);
  if (!id) { out({ error: 'no run folder yet (run "ct.mjs new-run" first)' }); process.exit(1); }
  const started = runnerStart(cfg, id);
  const s = Math.max(0, Math.round((Date.now() - started.getTime()) / 1000));
  out({ runId: id, startedAt: started.toISOString(), elapsedSeconds: s, human: (s >= 60 ? Math.floor(s / 60) + ' m ' : '') + (s % 60) + ' s', tokensAndCost: 'not visible to this helper — see Claude Code\\'s task line for this run, or /cost' });
}

switch (cmd) {
  case 'status': await status(); break;
  case 'elapsed': elapsedCmd(); break;

  case 'ci': console.error('[claude-test ci] Claude Test has no ci command: it starts its browser helper only in an interactive terminal session. Run claude in the project folder and type /claude-test:run there.'); process.exitCode = 4; break;
  case 'login': case 'logout': case 'sign-in': case 'scaffold-sign-in':


    process.stderr.write('moved: run  node ' + path.join(path.dirname(fileURLToPath(import.meta.url)), 'ct-auth.mjs') + ' ' + args.join(' ') + '\\n');
    process.exit(2);
    break;
  case 'new-run': newRun(); break;
  case 'write-spec': writeSpecCmd(); break;
  case 'file': fileCmd(); break;
  case 'drafts': draftsCmd(); break;
  case 'progress': await progressCmd(); break;
  case 'prefs': prefsCmd(); break;
  case 'allow': allowCmd(); break;
  case 'changes': changesCmd(); break;
  case 'fix-plan': fixPlanCmd(); break;
  case 'finish': finishCmd(); break;
  case 'install': case 'install-browser': install(); break;
  case 'browser':
    process.stderr.write('ct.mjs browser is not available: specs run only through the Claude Test browser tools, which are held to the allowed addresses. Nothing was started.\\n');
    process.exit(2);
  default:
    process.stderr.write('usage: ct.mjs status | new-run | allow [--remove <address>…] | prefs [live-page open|link | start forget] | write-spec <name…> | drafts | progress [start | <stem> <verdict> [--retried]] | changes | fix-plan | finish [--why <word>] | elapsed | install [browser]   (sign-in commands: ct-auth.mjs)\\n');
    process.exit(2);
}
