<!--
name: 'Data: ct-auth.mjs'
description: >-
  claude-test sign-in helper script (skills/run/scripts/ct-auth.mjs: login,
  logout, sign-in, scaffold-sign-in) whose JSON stdout (errors, notes, next
  steps) the model reads when it runs the sign-in for the person.
ccVersion: 2.1.326
-->
#!/usr/bin/env node












import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { shownDeep, loadConfig, resolveProjectDir, reallyInsideDir, envPathOutsideProject, insideProjectReally, sanitizeBrowserEnv, RC_FILE } from './lib/config.mjs';
import { toolsDir, mcpCliPath, installedBrowserPath, importPlaywright, cacheDir, useOwnBrowsersIfPresent, toolsProblem, sandboxFailureLine } from './lib/tools.mjs';
import { secretsMergeTarget, savedSessionCheckable, listSkills, runSkillScript, readSkillState, skillStateShapeProblem, filterStateToLoopback, writeAuthState, authFileInfo, parseCredsLine, mergeEnvFile, readEnvFile, scrub, rmScratch, scratchLeftWarning, defaultBrowsersPath, CT_ENV_NAME_RE, STATE_FILE_NAME, EMPTY_STATE } from './lib/signin.mjs';

const projectDir = resolveProjectDir();
sanitizeBrowserEnv();
useOwnBrowsersIfPresent();
const args = process.argv.slice(2);
const cmd = args[0] || 'help';
const out = (obj) => process.stdout.write(JSON.stringify(shownDeep(obj), null, 2) + '\\n');
const printable = (s, n = 200) => String(s).replace(/[^\\x20-\\x7e]+/g, ' ').slice(0, n);
function selfRel(cfg) { const p = fileURLToPath(import.meta.url); const r = path.relative(cfg.projectDir, p); return r.startsWith('..') ? p : r; }
function ctRel(cfg) { const p = path.join(path.dirname(fileURLToPath(import.meta.url)), 'ct.mjs'); const r = path.relative(cfg.projectDir, p); return r.startsWith('..') ? p : r; }
function savedSessionFacts(p) { const i = authFileInfo(p); return i.present ? { cookies: i.cookies, origins: i.origins, empty: i.empty, savedMinutesAgo: i.savedMinutesAgo, earliestCookieExpiry: i.earliestCookieExpiry, expired: i.expired, ...(i.problem ? { problem: i.problem } : {}) } : {}; }
const refuse = (what, why) => { out({ ok: false, error: what + ' cannot be used: ' + why + ' — nothing was written there' }); process.exit(2); };
const authPathOf = (cfg) => { if (cfg.storageState.refused) refuse('the saved session (auth.json)', cfg.storageState.refused); return cfg.storageState.path || cfg.storageState.defaultPath; };
const secretsPathOf = (cfg) => { if (cfg.secretsFile.refused) refuse('secrets.env', cfg.secretsFile.refused); return cfg.secretsFile.path || cfg.secretsFile.defaultPath; };



function assertWritableAuth(cfg) { return authPathOf(cfg); }
function assertWritableSecrets(cfg) {
  secretsPathOf(cfg);
  return secretsMergeTarget(cfg);
}








async function loginCmd() {
  const cfg = loadConfig(projectDir);
  if (!cfg.baseUrl) { out({ ok: false, error: 'no baseUrl: put "baseUrl: http://localhost:<port>" in ' + RC_FILE + ' first' }); process.exit(2); }
  authPathOf(cfg);
  if (!cfg.signInApplies) { out({ ok: false, error: 'the base URL is not on this machine; a saved session is only used for a local dev server (' + cfg.signInNote + ')' }); process.exit(2); }
  let startPath = '/'; let until = null; let timeoutS = 300;
  for (let i = 1; i < args.length; i++) {
    if (args[i] === '--until') until = String(args[++i] || '');
    else if (args[i] === '--timeout') timeoutS = Math.max(10, Math.min(900, Number(args[++i]) || 300));
    else if (!args[i].startsWith('--')) startPath = args[i];
  }
  let start; try { start = /^([a-z][a-z0-9+.-]*:|\\/\\/)/i.test(startPath) ? null : new URL(startPath, cfg.baseUrl); } catch { start = null; }
  if (!start || start.origin !== new URL(cfg.baseUrl).origin) { out({ ok: false, error: 'login starts on the dev server: give a path on ' + cfg.baseUrl + ', not ' + startPath }); process.exit(2); }
  const found = await importPlaywright();
  if (!found) { out({ ok: false, error: 'browser tooling not installed: run "node ' + ctRel(cfg) + ' install" first' }); process.exit(1); }
  const { chromium } = found.pw;
  const headed = process.env.CLAUDE_TEST_HEADED !== '0' && (process.platform !== 'linux' || !!process.env.DISPLAY || !!process.env.WAYLAND_DISPLAY);
  const exe = envPathOutsideProject('CLAUDE_TEST_BROWSER_EXECUTABLE') || null;
  const asRoot = typeof process.getuid === 'function' && process.getuid() === 0;
  const launchOpts = { headless: !headed, args: asRoot ? ['--no-sandbox'] : [], chromiumSandbox: !asRoot };
  if (exe) launchOpts.executablePath = exe; else { const chromePath = installedBrowserPath(); if (chromePath) launchOpts.executablePath = chromePath; }
  const marker = typeof cfg.rc.signedInMarker === 'string' && cfg.rc.signedInMarker.trim() ? cfg.rc.signedInMarker.trim() : null;
  if (!process.stdin.isTTY && !until && !marker) { out({ ok: false, error: 'no way to know when you are done: run this in a terminal (press Enter when signed in), or pass --until <text the signed-in page shows>, or set signedInMarker in ' + RC_FILE }); process.exit(2); }
  process.stderr.write('[claude-test] opening ' + start.href + (headed ? ' in a browser window' : ' headless') + '. Sign in with a TEST account. The window is not fenced while you do this.\\n'
    + '[claude-test] I save the session when ' + [until ? 'the page shows or reaches "' + printable(until) + '"' : null, marker ? 'the text "' + printable(marker) + '" appears on ' + new URL(cfg.baseUrl).origin : null, process.stdin.isTTY ? 'you press Enter here' : null].filter(Boolean).join(', or ') + ' (giving up after ' + timeoutS + ' s).\\n');
  let browser;
  try { browser = await chromium.launch(launchOpts); if (asRoot) process.stderr.write('[claude-test] As root, Chrome cannot start its own sandbox, so this browser runs without that sandbox: a page that breaks Chrome could run programs as you. Go on only with a test account.\\n'); }
  catch (first) {
    let e = first; const why = launchOpts.chromiumSandbox ? sandboxFailureLine(first && first.message) : null;
    if (why) { launchOpts.chromiumSandbox = false; try { browser = await chromium.launch(launchOpts); process.stderr.write('[claude-test] Chrome could not start with its own sandbox here, so this browser runs without that sandbox: a page that breaks Chrome could run programs as you. Go on only with a test account.\\n'); } catch (second) { e = second; } }
    if (!browser) { out({ ok: false, error: 'could not start a browser: ' + String(e.message || e).split('\\n')[0].slice(0, 200) + ' — run "node ' + ctRel(cfg) + ' install chromium' + (headed ? ' --headed' : '') + '" or install Chrome' }); process.exit(1); }
  }
  const hosts = new Set();
  let result = null;
  try {
    const context = await browser.newContext({ viewport: headed ? null : { width: 1280, height: 800 } });
    context.on('request', (req) => { try { const h = new URL(req.url()).host; if (h && !/^(localhost|127\\.0\\.0\\.1|\\[::1\\])(:\\d+)?$/i.test(h)) hosts.add(h); } catch {       } });
    const page = await context.newPage();
    await page.goto(start.href, { waitUntil: 'domcontentloaded', timeout: 45000 });
    const baseOrigin = new URL(cfg.baseUrl).origin;
    const done = new Promise((resolveDone) => {
      const timer = setTimeout(() => resolveDone('timeout'), timeoutS * 1000);
      if (process.stdin.isTTY) { process.stdin.setEncoding('utf8'); process.stdin.once('data', () => { clearTimeout(timer); resolveDone('enter'); }); }
      const poll = setInterval(async () => {
        try {
          const url = page.url();
          if (until && (url.startsWith(until) || (await page.getByText(until, { exact: false }).first().isVisible().catch(() => false)))) { clearInterval(poll); clearTimeout(timer); resolveDone('until'); }
          else if (marker && url.startsWith(baseOrigin) && (await page.getByText(marker, { exact: false }).first().isVisible().catch(() => false))) { clearInterval(poll); clearTimeout(timer); resolveDone('marker'); }
        } catch {                       }
      }, 1000);
    });
    const how = await done;
    if (how === 'timeout') { result = { ok: false, error: 'gave up after ' + timeoutS + ' s without a finish signal; nothing saved' }; }
    else {
      const raw = await context.storageState({ indexedDB: true });
      const f = filterStateToLoopback(raw, cfg.baseUrl);
      if (f.kept.cookies === 0 && f.kept.origins === 0) result = { ok: false, error: 'the browser holds no cookie or local storage for this machine after sign-in (' + f.dropped.cookies + ' third-party cookies dropped); nothing saved', finishedBy: how };
      else { writeAuthState(assertWritableAuth(cfg), f.state, { privateFolder: true, projectDir: cfg.projectDir }); result = { ok: true, finishedBy: how, savedTo: authPathOf(cfg), kept: f.kept, dropped: f.dropped, ...savedSessionFacts(authPathOf(cfg)), thirdPartyHostsVisited: [...hosts].slice(0, 20), note: 'cookies for remote hosts (an external identity provider) were dropped; only this machine\\'s loopback cookies are kept' + (f.otherLoopbackPorts.length ? ' — including cookies other LOCAL services set (ports ' + f.otherLoopbackPorts.join(', ') + ', e.g. a local identity provider), which the dev server will also receive: run "ct-auth.mjs logout" when you are done if that matters' : '') + '. In an already-running Claude Code session the browser picks this up on its next fresh page (after browser_close); typed secrets need a /mcp reconnect.' }; }
    }
  } catch (e) { result = { ok: false, error: String(e.message || e).split('\\n')[0].slice(0, 300) }; }
  finally { await browser.close().catch(() => {}); }
  out(result);
  process.exit(result.ok ? 0 : 1);
}




function logoutCmd() {
  const cfg = loadConfig(projectDir);
  const p = assertWritableAuth(cfg);
  const had = authFileInfo(p);
  writeAuthState(p, EMPTY_STATE, { privateFolder: true, projectDir: cfg.projectDir });

  let swept = 0; try { const sr = path.join(cacheDir(), 'scratch'); for (const e of fs.readdirSync(sr)) if (e.startsWith('ct-skill-')) { const d = path.join(sr, e); try { if (Date.now() - fs.statSync(d).mtimeMs < 10 * 60 * 1000) continue; } catch { continue; } fs.rmSync(d, { recursive: true, force: true }); swept++; } } catch {            }
  out({ ok: true, path: p, cleared: had.present && !had.empty ? { cookies: had.cookies, origins: had.origins } : null, ...(swept ? { staleScratchFoldersRemoved: swept } : {}), note: 'takes effect on the browser tool\\'s next fresh page (after browser_close)' });
}


function scratchFoldersLeftFields(removals) {
  const left = removals.filter((removal) => !removal.removed);
  return left.length ? { scratchFoldersLeft: left.map((removal) => ({ folder: removal.folder, why: removal.why })), scratchFoldersLeftNote: 'Sign-in could not delete each temporary folder listed here. Each can hold a signed-in browser session or test credentials. Close any sign-in browser that is still open, then delete each folder that is still there.' } : {};
}





async function signInCmd() {
  const cfg = loadConfig(projectDir);
  if (!cfg.baseUrl) { out({ ok: false, error: 'no baseUrl: put "baseUrl: …" in ' + RC_FILE + ' first' }); process.exit(2); }
  if (!cfg.signInApplies) { out({ ok: false, error: 'the base URL is not on this machine; sign-in material is only used for a local dev server' }); process.exit(2); }
  const skills = listSkills(cfg.projectDir);
  const want = args[1] && !args[1].startsWith('--') ? args[1] : null;
  const usable = skills.filter((s) => s.run && !s.problem);
  const skill = want ? skills.find((s) => s.name === want) : usable.length === 1 ? usable[0] : null;
  if (!skill) { out({ ok: false, error: want ? 'no skill named ' + JSON.stringify(want) + ' under .claude-test/skills' : usable.length ? 'several sign-in skills; name one: ' + usable.map((s) => s.name).join(', ') : 'no runnable skill under .claude-test/skills (a folder with SKILL.md whose front matter has a claude-test: run: block)', skills: skills.map((s) => ({ name: s.name, problem: s.problem || undefined })) }); process.exit(2); }
  if (skill.problem || !skill.run) { out({ ok: false, error: 'skill ' + skill.name + ': ' + (skill.problem || 'has no run script') }); process.exit(2); }
  if (!mcpCliPath({ report: true })) { out({ ok: false, error: 'browser tooling not installed: run "node ' + ctRel(cfg) + ' install" first (the skill imports playwright from there)' }); process.exit(1); }
  if (toolsProblem()) { out({ ok: false, error: 'the tools folder is not private: ' + toolsProblem() + ' — the sign-in skill imports playwright from there, so nothing is run until that is fixed' }); process.exit(2); }

  const authTarget = assertWritableAuth(cfg); assertWritableSecrets(cfg);
  const fromFile = readEnvFile(secretsPathOf(cfg));
  const ctVars = {}; for (const [k, v] of Object.entries(process.env)) if (CT_ENV_NAME_RE.test(k) && v) ctVars[k] = v; for (const [k, v] of Object.entries(fromFile)) if (CT_ENV_NAME_RE.test(k)) ctVars[k] = v;

  const secretValues = [...Object.values(fromFile).filter((v) => v && v.length >= 3), ...Object.values(ctVars).filter((v) => v && v.length >= 8)];
  let browserExecutable = envPathOutsideProject('CLAUDE_TEST_BROWSER_EXECUTABLE') || installedBrowserPath() || null;
  if (!browserExecutable) {
    try { const found = await importPlaywright(); const p = found && found.pw.chromium.executablePath(); if (p && fs.existsSync(p) && !insideProjectReally(p)) browserExecutable = p; } catch {                                            }
  }
  const removals = [];

  if (skill.check && savedSessionCheckable(authPathOf(cfg))) {
    const chk = await runSkillScript({ skill, phase: 'check', cfg, toolsDir: toolsDir(), browserExecutable, ctVars, scratchRoot: path.join(cacheDir(), 'scratch'), prepare: (outDir) => fs.copyFileSync(authPathOf(cfg), path.join(outDir, STATE_FILE_NAME)) });
    const checkRemoval = rmScratch(chk.scratch);
    removals.push(checkRemoval);
    if (!checkRemoval.removed) process.stderr.write(scratchLeftWarning(chk.scratch));
    if (chk.exitCode === 0 && !chk.timedOut) { out({ ok: true, skill: skill.name, reused: true, note: 'the check script says the saved session is still signed in; nothing re-run', session: savedSessionFacts(authPathOf(cfg)), ...scratchFoldersLeftFields(removals) }); return; }
  }
  if (!browserExecutable && !fs.existsSync(defaultBrowsersPath())) process.stderr.write('[claude-test] no browser for the sign-in skill was found (no Chrome, nothing under ' + defaultBrowsersPath() + '): if it fails to launch, run "node ' + ctRel(cfg) + ' install chromium" or set CLAUDE_TEST_BROWSER_EXECUTABLE\\n');
  process.stderr.write('[claude-test] running sign-in skill "' + printable(skill.name, 64) + '" (' + printable(path.relative(cfg.projectDir, skill.run.path)) + ', timeout ' + skill.timeoutS + ' s, ' + Object.keys(ctVars).length + ' CT_* variable(s))\\n');
  process.on('exit', () => { if (r && !rmScratch(r.scratch).removed) process.stderr.write(scratchLeftWarning(r.scratch)); });
  var r = null;
  r = await runSkillScript({ skill, phase: 'run', cfg, toolsDir: toolsDir(), browserExecutable, ctVars, scratchRoot: path.join(cacheDir(), 'scratch') });
  const ended = r.spawnError ? 'could not start: ' + r.spawnError : r.timedOut ? 'timed out after ' + skill.timeoutS + ' s' : r.signal ? 'killed by ' + r.signal : 'exit ' + r.exitCode;
  const credsParsed = parseCredsLine(r.stdout);
  const credVals = credsParsed.creds ? Object.values(credsParsed.creds) : credsParsed.salvage || [];
  const tail = scrub(r.stderrTail, [...secretValues, ...credVals]).trim().split('\\n').slice(-6).join(' | ').slice(-400);
  if (r.exitCode !== 0 || r.timedOut || r.spawnError) { removals.push(rmScratch(r.scratch)); out({ ok: false, skill: skill.name, error: 'sign-in unavailable: ' + ended + (tail ? ' — ' + tail : ''), durationMs: r.durationMs, ...scratchFoldersLeftFields(removals) }); process.exit(1); }
  const result = { ok: true, skill: skill.name, ended, durationMs: r.durationMs };

  if (/^claude-test-note: no-chrome-sandbox$/m.test(r.stderrTail)) result.browserSandbox = 'The sign-in browser ran without Chrome\\'s own sandbox, because Chrome could not start with it here; a page that breaks Chrome could then run programs as you. Use only a test account for sign-in.';
  const st = readSkillState(r.outDir);
  if (st.problem) { removals.push(rmScratch(r.scratch)); out({ ok: false, skill: skill.name, error: 'sign-in unavailable: ' + st.problem, ...scratchFoldersLeftFields(removals) }); process.exit(1); }
  if (st.state) {
    if (!st.state || typeof st.state !== 'object' || !Array.isArray(st.state.cookies) || !Array.isArray(st.state.origins)) { removals.push(rmScratch(r.scratch)); out({ ok: false, skill: skill.name, error: 'sign-in unavailable: storageState.json is not a Playwright storage state (need cookies[] and origins[])', ...scratchFoldersLeftFields(removals) }); process.exit(1); }
    const f = filterStateToLoopback(st.state, cfg.baseUrl);
    const shape = skillStateShapeProblem(f.state);
    if (shape) { removals.push(rmScratch(r.scratch)); out({ ok: false, skill: skill.name, error: 'sign-in unavailable: storageState.json ' + shape, ...scratchFoldersLeftFields(removals) }); process.exit(1); }
    if (f.kept.cookies === 0 && f.kept.origins === 0 && (f.dropped.cookies || f.dropped.origins)) { removals.push(rmScratch(r.scratch)); out({ ok: false, skill: skill.name, error: 'sign-in unavailable: the state the skill wrote has nothing for this machine after filtering (' + f.dropped.cookies + ' cookies, ' + f.dropped.origins + ' origins dropped)', ...scratchFoldersLeftFields(removals) }); process.exit(1); }
    if (f.kept.cookies === 0 && f.kept.origins === 0) result.session = null;
    else { writeAuthState(authTarget, f.state, { privateFolder: true, projectDir: cfg.projectDir }); result.session = { savedTo: authPathOf(cfg), kept: f.kept, dropped: f.dropped, ...(f.otherLoopbackPorts.length ? { otherLocalServices: 'cookies set by other local services (ports ' + f.otherLoopbackPorts.join(', ') + ') are kept too and will reach the dev server; their storage was dropped' } : {}), ...savedSessionFacts(authPathOf(cfg)) }; }
  } else result.session = null;
  removals.push(rmScratch(r.scratch));
  Object.assign(result, scratchFoldersLeftFields(removals));
  if (credsParsed.problem) result.credentials = { problem: credsParsed.problem };
  else if (Object.keys(credsParsed.creds).length) {
    const refused = Object.keys(credsParsed.creds).filter((k) => /^(CT_|CLAUDE_TEST)/i.test(k)); for (const k of refused) delete credsParsed.creds[k];
const target = assertWritableSecrets(cfg);
    if (!target) { result.credentials = { names: [], refused: Object.fromEntries(Object.keys(credsParsed.creds).map((k) => [k, 'not merged: ' + cfg.secretsFile.defaultPath + ' is a symlink or not a regular file — typed credentials are appended only to the private folder\\'s own secrets.env'])) }; }
    else { const m = mergeEnvFile(target, credsParsed.creds, { privateFolder: true }); const refusedAll = { ...Object.fromEntries(refused.map((k) => [k, 'names starting CT_ / CLAUDE_TEST are reserved for your own variables'])), ...m.refused }; result.credentials = { names: m.written, ...(Object.keys(refusedAll).length ? { refused: refusedAll } : {}), savedTo: secretsPathOf(cfg), keysInFile: m.keysInFile, note: 'typed credentials take effect when the browser tool next starts (new session or /mcp reconnect); a spec types the NAME, the tool fills the value' }; } }
  result.note = 'In a running Claude Code session the saved session applies from the next fresh page (after browser_close).';
  out(result);
}



function scaffoldCmd() {
  const cfg = loadConfig(projectDir);
  const dst = path.join(cfg.projectDir, '.claude-test', 'skills', 'sign-in');
  if (fs.existsSync(dst)) { out({ ok: false, error: path.relative(cfg.projectDir, dst) + ' already exists; edit it instead' }); process.exit(2); }
  for (const d of [path.join(cfg.projectDir, '.claude-test'), path.join(cfg.projectDir, '.claude-test', 'skills')]) { try { if (fs.lstatSync(d).isSymbolicLink() || !reallyInsideDir(d, cfg.projectDir)) { out({ ok: false, error: path.relative(cfg.projectDir, d) + ' is a symlink or resolves outside the project; not writing through it' }); process.exit(2); } } catch (e) { if (e.code !== 'ENOENT') throw e; } }
  const src = fileURLToPath(new URL('../templates/sign-in/', import.meta.url));
  fs.mkdirSync(path.join(dst, 'scripts'), { recursive: true });
  for (const rel of ['SKILL.md', 'scripts/sign-in.mjs', 'scripts/check.mjs']) fs.copyFileSync(path.join(src, rel), path.join(dst, rel));
  out({ ok: true, created: ['SKILL.md', 'scripts/sign-in.mjs', 'scripts/check.mjs'].map((r) => path.relative(cfg.projectDir, path.join(dst, r))), next: ['edit the EDIT block in scripts/sign-in.mjs (LOGIN_PATH, the three selectors, SIGNED_IN_MARKER) and CHECK_PATH in scripts/check.mjs to match your login form', 'put CT_TEST_MEMBER_EMAIL=… and CT_TEST_MEMBER_PASSWORD=… (a TEST account) in ' + cfg.secretsFile.defaultPath + ' — never in the repo', 'run: node ' + selfRel(cfg) + ' sign-in', 'commit .claude-test/skills/sign-in/'] });
}


switch (cmd) {
  case 'login': await loginCmd(); break;
  case 'logout': logoutCmd(); break;
  case 'sign-in': await signInCmd(); break;
  case 'scaffold-sign-in': scaffoldCmd(); break;
  default:
    process.stderr.write('usage: ct-auth.mjs login [path] [--until <text>] [--timeout <s>] | logout | sign-in [name] | scaffold-sign-in\\n');
    process.exit(cmd === 'help' || cmd === '--help' ? 0 : 2);
}
