<!--
name: 'Data: config.mjs'
description: >-
  claude-test shared library (skills/run/scripts/lib/config.mjs) whose config
  warnings, consent and sign-in notes surface in ct.mjs status JSON and the
  browser server's tool results that the model reads.
ccVersion: 2.1.314
-->






import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { execFile, execFileSync } from 'node:child_process';
import { discoverDevServer, candidateList } from './discover.mjs';

export const RC_FILE = '.claude-testrc';
export const SPECS_DIR = path.join('.claude-test', 'specs');
export const RUNS_DIR = path.join('.claude-test', 'runs');
export const DEFAULT_BASE_URL = 'http://localhost:3000';


export const PLAYWRIGHT_MCP_PACKAGE = '@playwright/mcp@0.0.79';
export const PLAYWRIGHT_MCP_VERSION = '0.0.79';



export const PLAYWRIGHT_PIN = '1.62.1';

export const MAX_OWN_STATE_BYTES = 16 * 1024 * 1024;

function stripComment(line) {

  let inS = false, inD = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (c === "'" && !inD) inS = !inS;
    else if (c === '"' && !inS) inD = !inD;
    else if (c === '#' && !inS && !inD && (i === 0 || /\\s/.test(line[i - 1]))) return line.slice(0, i);
  }
  return line;
}

const BAD_KEYS = new Set(['__proto__', 'constructor', 'prototype']);
const dict = () => Object.create(null);

function parseScalar(raw) {
  const v = raw.trim();
  if (v === '') return '';
  if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) return v.slice(1, -1);
  if (v === 'true' || v === 'yes' || v === 'on') return true;
  if (v === 'false' || v === 'no' || v === 'off') return false;
  if (v === 'null' || v === '~') return null;
  if (/^-?\\d+(\\.\\d+)?$/.test(v)) return Number(v);
  if (v.startsWith('[') && v.endsWith(']')) {
    const inner = v.slice(1, -1).trim();
    return inner === '' ? [] : inner.split(',').map((s) => parseScalar(s));
  }
  if (v.startsWith('{') && v.endsWith('}')) {
    const obj = dict();
    const inner = v.slice(1, -1).trim();
    if (inner) for (const part of inner.split(',')) {
      const k = part.indexOf(':');
      const key = k > 0 ? part.slice(0, k).trim() : '';
      if (key && !BAD_KEYS.has(key)) obj[key] = parseScalar(part.slice(k + 1));
    }
    return obj;
  }
  return v;
}


export function parseRc(text) {
  const data = dict();
  const warnings = [];
  const lines = text.replace(/^\\uFEFF/, '').split(/\\r?\\n/);
  let currentKey = null;
  for (let n = 0; n < lines.length; n++) {
    const rawLine = stripComment(lines[n]);
    if (rawLine.trim() === '' || rawLine.trim() === '---') continue;
    if (/^\\t/.test(rawLine)) { warnings.push('line ' + (n + 1) + ': starts with a tab (YAML indents with spaces), ignored'); continue; }
    const indent = rawLine.match(/^ */)[0].length;
    const line = rawLine.trim();
    if (indent === 0) {
      const m = line.match(/^([A-Za-z_][\\w.-]*)\\s*:\\s*(.*)$/);
      if (!m) { warnings.push('line ' + (n + 1) + ': not understood, ignored'); currentKey = null; continue; }
      const [, key, rest] = m;
      if (BAD_KEYS.has(key)) { warnings.push('line ' + (n + 1) + ': key "' + key + '" refused'); currentKey = null; continue; }
      if (rest === '' ) { data[key] = undefined; currentKey = key; }
      else { data[key] = parseScalar(rest); currentKey = null; }
    } else if (currentKey) {
      if (line.startsWith('- ')) {
        if (!Array.isArray(data[currentKey])) data[currentKey] = [];
        data[currentKey].push(parseScalar(line.slice(2)));
      } else {
        const m = line.match(/^([A-Za-z_][\\w.-]*)\\s*:\\s*(.*)$/);
        if (!m) { warnings.push('line ' + (n + 1) + ': not understood, ignored'); continue; }
        if (BAD_KEYS.has(m[1])) { warnings.push('line ' + (n + 1) + ': key "' + m[1] + '" refused'); continue; }
        if (data[currentKey] === undefined) data[currentKey] = dict();
        if (typeof data[currentKey] === 'object' && data[currentKey] !== null && !Array.isArray(data[currentKey])) data[currentKey][m[1]] = parseScalar(m[2]);
        else warnings.push('line ' + (n + 1) + ': mapping entry under a non-mapping key, ignored');
      }
    } else {
      warnings.push('line ' + (n + 1) + ': unexpected indentation, ignored');
    }
  }
  for (const k of Object.keys(data)) if (data[k] === undefined) delete data[k];
  return { data, warnings };
}







const HOST = /^(?=.{1,253}$)(?!\\d+$)[a-z0-9]([a-z0-9-]*[a-z0-9])?(\\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*$/;
const V6 = /^\\[[0-9a-f:]+\\]$/;
const hostOk = (h) => HOST.test(h) || V6.test(h) || /^\\d{1,3}(\\.\\d{1,3}){3}$/.test(h);
const LOOPBACK_HOSTS = ['localhost', '127.0.0.1', '[::1]'];


import { reachableEntryProblem } from './hosts.mjs';

export function isLocalHost(h) {
  let x = String(h).trim().toLowerCase(); if (!x) return false;
  if (!x.startsWith('[') && x.includes(':')) x = '[' + x + ']';
  let canon; try { canon = new URL('http://' + x + '/').hostname; } catch { return false; }
  if (/^localhost\\.?$/.test(canon) || /\\.localhost\\.?$/.test(canon)) return true;
  if (/^\\d+\\.\\d+\\.\\d+\\.\\d+$/.test(canon)) return /^127\\./.test(canon) || canon === '0.0.0.0';
  if (canon.startsWith('[')) { const v6 = canon.slice(1, -1); if (v6 === '::1' || v6 === '::') return true; const m4 = v6.match(/^::ffff:([0-9a-f]{1,4}):([0-9a-f]{1,4})$/); if (m4) { const a = parseInt(m4[1], 16) >> 8; return a === 127 || (parseInt(m4[1], 16) === 0 && parseInt(m4[2], 16) === 0); } const d4 = v6.match(/^::ffff:(\\d+)\\.\\d+\\.\\d+\\.\\d+$/); if (d4) return d4[1] === '127' || /^::ffff:0\\.0\\.0\\.0$/.test(v6); }
  return false;
}

export function normaliseOrigin(entry) {
  if (typeof entry !== 'string') return null;
  const s = entry.trim().toLowerCase();
  if (s === '' || /[\\s/?#]/.test(s.replace(/^https?:\\/\\//, ''))) return null;
  const wildcardPort = s.match(/^(https?:\\/\\/)([^/:]+|\\[[0-9a-f:]+\\]):\\*$/);
  if (wildcardPort) return null;
  if (/^https?:\\/\\//.test(s)) {
    try { const u = new URL(s); if (u.origin !== 'null' && hostOk(u.hostname) && (u.pathname === '/' || u.pathname === '')) return u.origin; } catch {                    }
    return null;
  }

  const m = s.match(/^([^:\\[\\]]+|\\[[0-9a-f:]+\\])(:\\d{1,5})?$/);
  if (m && hostOk(m[1])) { if (m[2] && (Number(m[2].slice(1)) < 1 || Number(m[2].slice(1)) > 65535)) return null; try { const u = new URL('http://' + s); return u.hostname + (u.port ? ':' + u.port : (m[2] ? ':' + Number(m[2].slice(1)) : '')); } catch { return null; } }
  return null;
}

export function parseBaseUrl(value) {
  if (typeof value !== 'string' || value.trim() === '') return null;
  try {
    const u = new URL(value.trim());
    if (u.protocol !== 'http:' && u.protocol !== 'https:') return null;
    if (u.username || u.password) return null;
    if (!hostOk(u.hostname.toLowerCase())) return null;
    u.hash = '';
    return u;
  } catch { return null; }
}





export function projectIdentityPath(projectDir) { return path.resolve(projectDir); }



export function projectSlug(projectDir) { const identity = projectIdentityPath(projectDir); return path.basename(identity).replace(/[^A-Za-z0-9._-]/g, '_').slice(0, 48) + '-' + crypto.createHash('sha256').update(identity).digest('hex'); }


export function wrongProject(parsed, projectDir) {
  const got = parsed && typeof parsed === 'object' && !Array.isArray(parsed) ? parsed.project : undefined;
  if (got === projectIdentityPath(projectDir)) return null;
  return typeof got === 'string' && got !== '' ? 'was saved for another project folder (' + shown(got, 200) + ')' : 'does not say which project folder it was saved for';
}


export function privateDir(projectDir, orNull = false) {
  const fallback = process.platform === 'darwin' ? path.join(os.homedir(), 'Library', 'Application Support') : path.join(os.homedir(), '.config');
  const fromEnv = [process.env.XDG_CONFIG_HOME, process.platform === 'win32' ? process.env.APPDATA : null].find((v) => v && path.isAbsolute(v));
  let base = path.resolve(fromEnv || fallback);
  if (insideDir(base, projectDir) || reallyInsideDir(base, projectDir) || insideProjectReally(base)) base = process.platform === 'darwin' ? path.join(trustedHome(), 'Library', 'Application Support') : path.join(trustedHome(), '.config');
  if (homeTampered() && (reallyInsideDir(base, projectDir) || insideProjectReally(base))) { if (orNull) return null; process.stderr.write('[claude-test] refusing to run: HOME points into the project\\n'); process.exit(2); }
  return path.join(base, 'claude-test', projectSlug(projectDir));
}



export function withoutPrivateFolders(projectDir) {
  const privateFolder = privateDir(projectDir, true); if (privateFolder === null) return (text) => String(text);
  const itsParent = path.dirname(privateFolder);
  const endsHere = '(?![A-Za-z0-9_-]|\\\\.[A-Za-z0-9])'; const literal = (text) => text.replace(/[.*+?^\${}()|[\\]\\\\]/g, '\\\\$&');
  const folder = new RegExp(literal(privateFolder) + endsHere, 'g'); const parent = new RegExp(literal(itsParent) + endsHere, 'g');
  return (text) => String(text).replace(folder, '<private folder>').replace(parent, "<the private folder's parent>");
}



let pinNote = null; let openedNote = null;



export function pinnedProjectDir() {
  const v = process.env.CLAUDE_TEST_PROJECT_DIR; if (!v || /^\\$\\{.*\\}$/.test(v)) return null;
  const pinned = path.resolve(v); const cwd = path.resolve(process.cwd());
  const opened = openedProjectDir();
  const same = reallyInsideDir(pinned, cwd) && reallyInsideDir(cwd, pinned);
  let why = null;
  if (!reallyInsideDir(pinned, cwd) && !reallyInsideDir(cwd, pinned)) why = 'it names a folder this session is not in';
  else if (opened && !(pinned === opened || reallyInsideDir(pinned, opened))) { const raw = path.resolve(process.env.CLAUDE_PROJECT_DIR); why = raw === opened ? 'it lies outside the folder Claude Code opened (' + opened + ')' : 'it lies outside this checkout\\'s top folder (' + opened + '), which is as far up as the folder Claude Code opened (' + raw + ') counts here'; }
  else if (!same && reallyInsideDir(cwd, pinned) && !ancestorMayAnchor(pinned, cwd, opened)) why = checkoutRootOf(cwd) ? 'it names a folder above this checkout (' + checkoutRootOf(cwd) + ')' : 'it names a folder above the current directory, and no .git folder marks a checkout that would make it part of this project';
  if (why) { pinNote = 'CLAUDE_TEST_PROJECT_DIR=' + pinned + ' is ignored: ' + why + ' — a session setting must not move the project, and with it the private sign-in folder, somewhere else'; return null; }
  return pinned;
}



function ancestorMayAnchor(dir, cwd, opened) { if (opened && reallyInsideDir(dir, opened) && reallyInsideDir(opened, dir)) return true; const top = checkoutRootOf(cwd); return !!top && reallyInsideDir(dir, top); }



export function openedProjectDir() {
  const v = process.env.CLAUDE_PROJECT_DIR; if (!v || /^\\$\\{.*\\}$/.test(v)) return null;
  const opened = path.resolve(v); const cwd = path.resolve(process.cwd());
  if (!(opened === cwd || reallyInsideDir(cwd, opened) || reallyInsideDir(opened, cwd))) { openedNote = 'CLAUDE_PROJECT_DIR=' + opened + ' is ignored: this process is not running inside it'; return null; }


  const top = reallyInsideDir(cwd, opened) && !reallyInsideDir(opened, cwd) ? checkoutRootOf(cwd) : null;
  return top && !reallyInsideDir(opened, top) ? top : opened;
}
export function sessionRoot() {
  return path.resolve(openedProjectDir() || pinnedProjectDir() || process.cwd());
}
const PROJECT_MARKERS = ['.claude-testrc', '.claude-test'];


export function isMarked(d) {
  try { fs.lstatSync(path.join(d, '.claude-testrc')); return true; } catch {       }
  try { return fs.readdirSync(path.join(d, '.claude-test')).some((e) => e !== 'runs' && e !== '.gitignore'); } catch { return false; }
}












export function launcherConfig() {
  let cfg = loadConfig(resolveProjectDir());
  const root = sessionRoot();
  let note = null; let served = null;
  const runsOwnApp = (() => { try { const pkg = JSON.parse(fs.readFileSync(path.join(cfg.projectDir, 'package.json'), 'utf8')); return !!(pkg && pkg.scripts && ['dev', 'start'].some((s) => pkg.scripts[s] || Object.keys(pkg.scripts).some((k) => k.startsWith(s + ':')))); } catch { return false; } })();
  if (cfg.projectDir === root && !rootConfiguresItself(cfg.projectDir) && !runsOwnApp) {
    const below = projectsBelow(cfg.projectDir);
    const cwd = process.cwd(); const onlyApp = below.length === 1 ? path.join(cfg.projectDir, below[0]) : null;
    const here = onlyApp && ((reallyInsideDir(cwd, root) && reallyInsideDir(root, cwd)) || reallyInsideDir(cwd, onlyApp));
    if (onlyApp && here) { note = 'no .claude-testrc at ' + cfg.projectDir + '; using the app folder ' + below[0]; cfg = loadConfig(onlyApp); }
    else if (onlyApp) { note = 'no .claude-testrc at ' + cfg.projectDir + ' and this process runs in ' + cwd + ', not in the app folder ' + below[0] + ' — that app\\'s settings and sign-in files are not applied from here; start Claude Code in ' + onlyApp + ' or put a .claude-testrc at the root'; }
    else if (below.length > 1) { const apps = below.map((b) => { try { return loadConfig(path.join(cfg.projectDir, b)); } catch { return null; } }).filter(Boolean); if (apps.length) { cfg.allowedOrigins = [...new Set(apps.flatMap((a) => a.allowedOrigins))]; served = apps; } note = 'several app folders with Claude Test files (' + below.join(', ') + '): the browser fence is the union of their allowed origins (a configured app gives its base URL; an unconfigured one its candidate ports); sign-in material is per app and is not applied from the root — put a .claude-testrc at ' + cfg.projectDir + ' to choose one'; }
  }
  return { cfg, note, served: served || [cfg] };
}
export function appPointer(root) { const r = appPointerInfo(root); return r && r.dir ? r.dir : null; }


export function appPointerInfo(root) {
  let txt; try { const p = path.join(root, RC_FILE); if (!fs.lstatSync(p).isFile()) return null; txt = fs.readFileSync(p, 'utf8'); } catch { return null; }
  const m = txt.match(/^\\s*app\\s*:\\s*["']?([^"'\\n#]+?)["']?\\s*(#.*)?$/m);
  if (!m) return null;
  const rel = m[1].trim();
  const bad = (problem) => ({ dir: null, value: rel, problem: 'the "app: ' + rel.replace(/[^\\x20-\\x7e]/g, '?').slice(0, 80) + '" line in ' + path.join(root, RC_FILE) + ' ' + problem });
  if (!rel || path.isAbsolute(rel) || rel.split(/[\\\\/]/).includes('..')) return bad('must be a plain relative path inside the repo');
  const abs = path.resolve(root, rel);
  try { if (!fs.statSync(abs).isDirectory()) return bad('is not a directory'); } catch { return bad('names a folder that does not exist'); }
  return reallyInsideDir(abs, root) ? { dir: abs, value: rel } : bad('resolves outside the repo');
}


export function rootConfiguresItself(root) {
  try { const txt = fs.readFileSync(path.join(root, RC_FILE), 'utf8'); return txt.split(/\\r?\\n/).some((l) => /^\\s*[A-Za-z][\\w-]*\\s*:/.test(l) && !/^\\s*app\\s*:/.test(l)); } catch { return false; }
}
export function resolveProjectDir() {



  { const pinned = pinnedProjectDir(); if (pinned) return appPointer(pinned) || pinned; }
  const root = sessionRoot();
  const cwd = path.resolve(process.cwd());
  const pointed = appPointer(root);
  if (!insideDir(cwd, root)) return pointed || root;
  for (let d = cwd; ; d = path.dirname(d)) {
    if (d === root) break;
    if (isMarked(d)) return d;
    if (path.dirname(d) === d) break;
  }
  if (cwd !== root && fs.existsSync(path.join(cwd, 'package.json'))) return cwd;
  if (pointed) return pointed;
  if (rootConfiguresItself(root)) return root;
  return root;
}

export function projectDirReason(dir) {
  if (pinnedProjectDir() === dir) return 'CLAUDE_TEST_PROJECT_DIR';
  if (appPointer(sessionRoot()) === dir) return 'the "app:" line in the session root\\'s ' + RC_FILE;
  const marked = PROJECT_MARKERS.filter((m) => { try { fs.lstatSync(path.join(dir, m)); return true; } catch { return false; } });
  if (marked.length && isMarked(dir)) return 'nearest folder with ' + marked.join(' + ') + (dir === sessionRoot() ? ' (the session root)' : ' (walking up from the current directory, inside the session root ' + sessionRoot() + ')');
  if (dir !== sessionRoot()) return 'the current directory (it has a package.json; nothing above it up to the session root is marked with .claude-testrc / .claude-test)';
  return 'the session root (no .claude-testrc or .claude-test found from the current directory up)';
}


export function projectsBelow(dir, depth = 3) {
  const found = [];
  const walk = (d, left) => {
    if (found.length >= 8) return;
    let ents; try { ents = fs.readdirSync(d, { withFileTypes: true }); } catch { return; }
    if (d !== dir && isMarked(d)) { found.push(path.relative(dir, d)); return; }
    if (left === 0) return;
    for (const e of ents) if (e.isDirectory() && !e.name.startsWith('.') && e.name !== 'node_modules' && e.name !== 'dist' && e.name !== 'build') walk(path.join(d, e.name), left - 1);
  };
  walk(dir, depth);
  return found;
}


export function insideDir(p, dir) { return p === dir || p.startsWith(dir + path.sep); }




function realish(p) {
  let head = path.resolve(p); const tail = [];
  while (!fs.existsSync(head)) { const up = path.dirname(head); if (up === head) break; tail.unshift(path.basename(head)); head = up; }
  try { head = fs.realpathSync(head); } catch {                        }
  const full = path.join(head, ...tail);
  return process.platform === 'darwin' || process.platform === 'win32' ? full.toLowerCase() : full;
}
export function reallyInsideDir(p, dir) { return insideDir(realish(p), realish(dir)); }




const checkoutRootMemo = new Map();




export function checkoutRootOf(dir) { if (checkoutRootMemo.has(dir)) return checkoutRootMemo.get(dir); const r = checkoutRootWalk(dir); checkoutRootMemo.set(dir, r); return r; }
function checkoutRootWalk(dir) { let d; try { d = fs.realpathSync(dir); } catch { d = path.resolve(dir); } const home = path.resolve(trustedHome()); let top = null; for (;;) { if (d === home || reallyInsideDir(home, d)) break;                                     let has = false; try { fs.lstatSync(path.join(d, '.git')); has = true; } catch {                 } if (has) top = d; const up = path.dirname(d); if (up === d) break; d = up; } return top; }
let checkoutRootsMemo = null;
function checkoutRoots() { if (checkoutRootsMemo) return checkoutRootsMemo; const roots = new Set(); for (const d of [process.cwd(), resolveProjectDir(), sessionRoot()]) { const r = checkoutRootOf(d); if (r) roots.add(r); } checkoutRootsMemo = [...roots]; return checkoutRootsMemo; }


export function insideProjectReally(p) { return reallyInsideDir(p, resolveProjectDir()) || reallyInsideDir(p, process.cwd()) || reallyInsideDir(p, sessionRoot()) || checkoutRoots().some((r) => reallyInsideDir(p, r)); }




export function insideOpenedFolder(p) { const opened = process.env.CLAUDE_TEST_OPENED_DIR; return !!opened && path.isAbsolute(opened) && reallyInsideDir(p, opened); }




export function envPathOutsideProject(name) {
  const v = process.env[name];
  if (!v || !v.trim()) return null;
  const p = path.resolve(v.trim());
  if (!insideProjectReally(p)) return p;
  process.stderr.write('[claude-test] ' + name + ' points inside the project and is ignored\\n');
  return null;
}




export function dirNotPrivateProblem(dir, had = null) {
  if (process.platform === 'win32') return null;
  let st = had; if (!st) { try { st = fs.statSync(dir); } catch { return null; } }
  if (!st.isDirectory()) return dir + ' is not a directory';
  const uid = typeof process.getuid === 'function' ? process.getuid() : null;
  if (uid !== null && st.uid !== uid && st.uid !== 0) return dir + ' is owned by another user (uid ' + st.uid + ')';
  if ((st.mode & 0o022) !== 0) return dir + ' is writable by group or other users (mode ' + (st.mode & 0o777).toString(8) + ')';
  return null;
}



export function trustedHome() { try { return os.userInfo().homedir || os.homedir(); } catch { return os.homedir(); } }
export function homeTampered() { const envHome = process.platform === 'win32' ? (process.env.USERPROFILE || '') : (process.env.HOME || ''); return !!envHome && path.resolve(envHome) !== path.resolve(trustedHome()); }




const PW_NPM_SPELLINGS = ['npm_config_playwright_browsers_path', 'npm_package_config_playwright_browsers_path'];
function platformCacheBrowsers() {
  if (process.platform === 'linux') return path.join(process.env.XDG_CACHE_HOME || path.join(os.homedir(), '.cache'), 'ms-playwright');
  if (process.platform === 'darwin') return path.join(os.homedir(), 'Library', 'Caches', 'ms-playwright');
  if (process.platform === 'win32') return path.join(process.env.LOCALAPPDATA || path.join(os.homedir(), 'AppData', 'Local'), 'ms-playwright');
  return path.join(os.homedir(), '.cache', 'ms-playwright');
}
function trustedHomeBrowsers() {
  const h = trustedHome();
  if (process.platform === 'darwin') return path.join(h, 'Library', 'Caches', 'ms-playwright');
  if (process.platform === 'win32') return path.join(h, 'AppData', 'Local', 'ms-playwright');
  return path.join(h, '.cache', 'ms-playwright');
}







let browserEnvChecked = false;


function sharedRegistryProblem(dir) { if (process.platform === 'win32') return null; try { const st = fs.statSync(dir); if (!st.isDirectory()) return dir + ' is not a directory'; if (typeof process.getuid === 'function' && st.uid !== process.getuid() && st.uid !== 0) return dir + ' is owned by another user (uid ' + st.uid + ')'; if (st.mode & 0o002) return dir + ' is writable by every user (mode ' + (st.mode & 0o777).toString(8) + ')'; return null; } catch { return null; } }






const SERVER_ENV_KEEP = new Set(['PATH', 'HOME', 'USER', 'LOGNAME', 'SHELL', 'LANG', 'LANGUAGE', 'TZ', 'TMPDIR', 'TEMP', 'TMP', 'DISPLAY', 'WAYLAND_DISPLAY', 'XAUTHORITY', 'DBUS_SESSION_BUS_ADDRESS', 'LD_LIBRARY_PATH', 'CHROME_DEVEL_SANDBOX', 'FONTCONFIG_FILE', 'FONTCONFIG_PATH', 'SSL_CERT_FILE', 'SSL_CERT_DIR', 'NODE_EXTRA_CA_CERTS', 'HTTP_PROXY', 'HTTPS_PROXY', 'NO_PROXY', 'ALL_PROXY', 'PLAYWRIGHT_BROWSERS_PATH',
  'SYSTEMROOT', 'WINDIR', 'COMSPEC', 'PATHEXT', 'USERPROFILE', 'USERNAME', 'APPDATA', 'LOCALAPPDATA', 'PROGRAMFILES', 'PROGRAMFILES(X86)', 'PROGRAMDATA', 'PROGRAMW6432', 'COMMONPROGRAMFILES', 'HOMEDRIVE', 'HOMEPATH', 'OS', 'PROCESSOR_ARCHITECTURE', 'NUMBER_OF_PROCESSORS', 'SYSTEMDRIVE']);
const SERVER_ENV_KEEP_PREFIX = ['LC_', 'XDG_', 'CLAUDE_TEST_'];
const SERVER_ENV_EXACT = new Set(['LD_LIBRARY_PATH', 'CHROME_DEVEL_SANDBOX']);
export function browserServerEnv(env = process.env) {
  const out = {};
  for (const [k, v] of Object.entries(env)) { const K = k.toUpperCase(); if (v !== undefined && v !== '' && (k === K || !SERVER_ENV_EXACT.has(K)) && (SERVER_ENV_KEEP.has(K) || SERVER_ENV_KEEP.has(k) || SERVER_ENV_KEEP_PREFIX.some((p) => K.startsWith(p)) || /^(http|https|no|all)_proxy$/.test(k))) out[k] = v; }
  return out;
}


function scrubPlaywrightEnv() {
  for (const k of Object.keys(process.env)) if ((/^(PLAYWRIGHT_|PWTEST_|PW_|PWDEBUG$)/i.test(k) && !/^PLAYWRIGHT_BROWSERS_PATH$/i.test(k)) || /^npm_(package_)?config_.*(playwright|pwdebug|pwtest)/i.test(k) && !/browsers_path$/i.test(k)) delete process.env[k];
}
export function sanitizeBrowserEnv() {
  if (browserEnvChecked) return; browserEnvChecked = true;
  scrubPlaywrightEnv();
  if (process.env.PLAYWRIGHT_BROWSERS_PATH === undefined) { for (const k of PW_NPM_SPELLINGS) if (process.env[k] !== undefined) { process.env.PLAYWRIGHT_BROWSERS_PATH = process.env[k]; break; } }
  for (const k of PW_NPM_SPELLINGS) delete process.env[k];
  const v = process.env.PLAYWRIGHT_BROWSERS_PATH;
  if (v === '0') return;
  const given = v !== undefined && v !== '' ? path.resolve(process.env.INIT_CWD || process.cwd(), v) : null;
  const candidates = [given, platformCacheBrowsers(), trustedHomeBrowsers()].filter(Boolean);




  const why = (c) => insideProjectReally(c) ? 'is inside the project' : (fs.existsSync(c) && sharedRegistryProblem(c)) ? 'is not safe to run browsers from (' + sharedRegistryProblem(c) + ')' : null;
  let pick = [...new Set(candidates)].find((c) => !why(c));
  if (!pick) {
    pick = candidates[candidates.length - 1];
    process.stderr.write('[claude-test] no safe Playwright browsers path: ' + [...new Set(candidates)].map((c) => c + ' ' + why(c)).join('; ') + ' — an installed Chrome, or "ct.mjs install chromium" (own copy under the tools folder), avoids it\\n');
  } else if (pick !== candidates[0]) process.stderr.write('[claude-test] the Playwright browsers path ' + candidates[0] + ' ' + why(candidates[0]) + ' and is ignored; using ' + pick + '\\n');
  process.env.PLAYWRIGHT_BROWSERS_PATH = pick;
}
export function playwrightRegistryDir() {
  const v = process.env.PLAYWRIGHT_BROWSERS_PATH;
  if (v === '0') return { hermetic: true };
  return { dir: v && v !== '' ? path.resolve(process.env.INIT_CWD || process.cwd(), v) : platformCacheBrowsers() };
}





const GIT_SAFE_ARGS = ['core.fsmonitor=', 'core.hooksPath=/dev/null', 'hook.post-index-change.enabled=false', 'hook.pre-auto-gc.enabled=false', 'safe.bareRepository=explicit', 'protocol.allow=never', 'submodule.recurse=false', 'gc.auto=0', 'maintenance.auto=false'].flatMap((pair) => ['-c', pair]);





const GIT_SAFE_ENV = { GIT_NO_LAZY_FETCH: '1', GIT_ALLOW_PROTOCOL: '/', GIT_NO_REPLACE_OBJECTS: '1', GIT_TERMINAL_PROMPT: '0', GIT_LFS_SKIP_SMUDGE: '1', GIT_OPTIONAL_LOCKS: '0', PYTHONSAFEPATH: '1' };
const GIT_MS = 10000;





let gitOffHere = false;
export function gitOff() { return gitOffHere || process.env.CLAUDE_TEST_NO_GIT === '1'; }

export function withoutGit(act) { const was = gitOffHere; gitOffHere = true; try { return act(); } finally { gitOffHere = was; } }












export function safeGit(dir, args, options = {}) {
  if (gitOff()) throw new Error('no git is started here');
  let from; try { from = fs.realpathSync(dir); } catch { from = path.resolve(dir); }
  let at = from; let entry;
  for (;;) {
    try { entry = fs.lstatSync(path.join(at, '.git')); break; } catch {                 }
    const up = path.dirname(at); if (up === at) throw new Error('not in a git checkout'); at = up;
  }
  const told = typeof process.getuid === 'function' && entry.uid === process.getuid() ? ['--git-dir=' + path.join(at, '.git'), '--work-tree=' + at] : [];
  for (let up = from; !told.length; ) {
    let head = false; try { fs.lstatSync(path.join(up, 'HEAD')); head = true; } catch {                 }
    if (head) throw new Error(up + ' holds a HEAD, which git could take for a repository\\'s, and the checkout belongs to another account');
    const next = path.dirname(up); if (next === up) break; up = next;
  }
  let dbHome = null; try { dbHome = os.userInfo().homedir || null; } catch {                                                                                                                   }
  const home = dbHome || trustedHome(); let below = from; while (path.dirname(below) !== below && !reallyInsideDir(home, path.dirname(below))) below = path.dirname(below);
  let topmost = null; if (dbHome) topmost = checkoutRootOf(from); else for (let d = from; ; ) { try { fs.lstatSync(path.join(d, '.git')); topmost = d; } catch {                 } const up = path.dirname(d); if (up === d) break; d = up; }
  const theirs = (file) => [from, dbHome && reallyInsideDir(home, at) && reallyInsideDir(at, home) ? below : at, topmost].some((top) => top && reallyInsideDir(file, top));
  const nothingThere = (e) => e.code === 'ENOENT' || e.code === 'ENOTDIR';
  const kernels = (p) => { try { return fs.realpathSync.native(p); } catch (e) { return nothingThere(e) ? p : null; } };
  const through = (file, depth = 0) => { for (let d = path.resolve(file); ; ) { const real = kernels(d); if (real === null || theirs(d) || theirs(real)) return true; let to = null; try { to = fs.readlinkSync(d); } catch (e) { if (e.code !== 'EINVAL' && !nothingThere(e)) return true;                       } if (to !== null && (depth > 8 || through(path.resolve(path.dirname(d), to), depth + 1))) return true;                                                                                                                                    const up = path.dirname(d); if (up === d) return false; d = up; } };
  const plain = (folder) => path.isAbsolute(folder) && !folder.split(path.sep).includes('..');
  const program = (process.env.PATH || '').split(path.delimiter).filter(plain).map((folder) => path.join(folder, process.platform === 'win32' ? 'git.exe' : 'git'))
    .find((file) => { try { fs.accessSync(file, fs.constants.X_OK); return fs.statSync(file).isFile() && !through(file) && !theirs(fs.realpathSync(file)); } catch { return false; } });
  if (!program) throw new Error('no git on PATH outside the checkout');
  const searched = ['PATH', 'PYTHONPATH', 'NODE_PATH', 'RUBYLIB', 'PERL5LIB', 'PERLLIB', 'GEM_PATH', 'CLASSPATH', 'DYLD_LIBRARY_PATH', 'DYLD_FRAMEWORK_PATH', 'LD_LIBRARY_PATH', 'LIBRARY_PATH', 'CPATH', 'C_INCLUDE_PATH', 'CPLUS_INCLUDE_PATH', 'R_LIBS', 'R_LIBS_USER', 'R_LIBS_SITE', 'DYLD_FALLBACK_LIBRARY_PATH', 'DYLD_FALLBACK_FRAMEWORK_PATH'];
  const env = Object.fromEntries(Object.entries(process.env).filter(([k]) => !/^GIT_/i.test(k) && (searched.includes(k) || !/^(LD_|DYLD_|GCONV_PATH$|BASH_ENV$|ENV$|SHELLOPTS$|BASHOPTS$|PS4$|DEVELOPER_DIR$)/.test(k))));
  for (const name of searched) {
    if (env[name] === undefined) continue;
    const kept = env[name].split(path.delimiter).filter((folder) => plain(folder) && !/[;$]/.test(folder) && !through(folder));
    if (kept.length) env[name] = kept.join(path.delimiter); else delete env[name];
  }



  const led = (folder) => !plain(folder) || through(folder);
  if (env.HOME !== undefined && led(env.HOME) && !(dbHome && plain(env.HOME) && reallyInsideDir(env.HOME, dbHome) && reallyInsideDir(dbHome, env.HOME))) env.HOME = dbHome && !led(dbHome) ? dbHome : os.devNull;
  if (env.XDG_CONFIG_HOME !== undefined && led(env.XDG_CONFIG_HOME)) delete env.XDG_CONFIG_HOME;
  let sub = 0; while (args[sub] === '-c') sub += 2;
  const closed = args[sub] === 'status' || args[sub] === 'diff' ? ['--ignore-submodules=all'] : [];
  return execFileSync(program, [...GIT_SAFE_ARGS, ...told, ...args.slice(0, sub + 1), ...closed, ...args.slice(sub + 1)], { stdio: ['ignore', 'pipe', 'ignore'], timeout: GIT_MS, killSignal: 'SIGTERM', ...options, cwd: dir, env: { ...env, ...GIT_SAFE_ENV } });
}

function gitIgnored(projectDir, file) {
  try { safeGit(projectDir, ['check-ignore', '-q', file], { stdio: 'ignore' }); return true; }
  catch (e) { return e && e.status === 1 ? false : null; }
}





function resolvePrivateFile(projectDir, rcValue, defaultName, warnings, key, envName, { carriesProject = false } = {}) {
  const defaultPath = path.join(privateDir(projectDir), defaultName);
  if (rcValue !== undefined) warnings.push(RC_FILE + ': "' + key + '" is ignored — sign-in material is per developer; put the file at ' + defaultPath);
  const envVal = process.env[envName];
  if (envVal && envVal.trim()) warnings.push(envName + ' is set (' + shown(envVal.trim(), 120) + ') and is ignored — sign-in material comes only from ' + defaultPath + '; a session variable cannot choose it');


  const refused = (why, note = key + ': ' + why) => { if (!warnings.includes(note)) warnings.push(note); return { path: null, inUse: false, source: null, defaultPath, refused: why }; };
  const dp = fs.existsSync(path.dirname(defaultPath)) ? dirNotPrivateProblem(path.dirname(defaultPath)) : null;
  if (dp) return refused(dp + ' — sign-in material is neither read from nor written to that folder until it is private again (chmod 700)');
  const isLink = (p) => { try { return fs.lstatSync(p).isSymbolicLink(); } catch { return false; } };
  if (isLink(defaultPath)) return refused(defaultPath + ' is a symbolic link and is ignored — replace the link with a copy of the file (sign-in material comes only from a regular file in the private folder)');
  const linkedDir = [path.dirname(defaultPath), path.dirname(path.dirname(defaultPath))].find(isLink);
  if (linkedDir) { const why = linkedDir + ' is a symbolic link, so the sign-in files under it are ignored — make it a real folder and copy auth.json / secrets.env to ' + path.dirname(defaultPath); return refused(why, why); }
  let st = null; try { st = fs.lstatSync(defaultPath); } catch { st = null; }
  const exists = st !== null && st.isFile();
  if (exists && insideProjectReally(defaultPath)) return refused(defaultPath + ' resolves inside the repository, so it is ignored — sign-in material must live outside it; check where HOME / XDG_CONFIG_HOME (or a link under them) point');
  const found = { path: exists ? defaultPath : null, inUse: exists, source: exists ? 'private folder' : null, defaultPath };
  if (!exists || !carriesProject) return found;
  let parsed; if (st.size <= MAX_OWN_STATE_BYTES) { try { parsed = JSON.parse(fs.readFileSync(defaultPath, 'utf8')); } catch { parsed = undefined; } }
  const why = parsed === undefined ? null : wrongProject(parsed, projectDir);
  if (why) return refused(defaultPath + ' ' + why + ', so it is not used — delete it and sign in again' + (typeof (parsed && parsed.project) === 'string' && parsed.project !== '' ? '' : ' (a session file you saved yourself needs "project": ' + JSON.stringify(shown(projectIdentityPath(projectDir), 4096)) + ' beside its cookies and origins)'));
  return { ...found, hasContent: parsed !== undefined && ((Array.isArray(parsed.cookies) && parsed.cookies.length > 0) || (Array.isArray(parsed.origins) && parsed.origins.length > 0)) };
}




export const CONSENT_FILE = 'allowed-origins.json';



export function dataRoot() { return path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..', '..', '..'); }



export function madeHereKey() {
  const file = path.join(dataRoot(), 'made-here.key');
  try {
    const st = fs.lstatSync(file);
    if (!st.isFile() || st.size !== 64 || (process.platform !== 'win32' && (st.mode & 0o077) !== 0)) return null;
    const key = fs.readFileSync(file, 'utf8'); return /^[0-9a-f]{64}$/.test(key) ? key : null;
  } catch { return null; }
}

export function madeHereMac(key, runId) { return crypto.createHmac('sha256', key).update(runId).digest('hex'); }


export function consentDir(projectDir) { return path.join(dataRoot(), 'consent', path.basename(privateDir(projectDir))); }

export function liveDir(projectDir, runId) { if (!RUN_ID.test(runId)) throw new Error('not a run id'); let real = projectDir; try { real = fs.realpathSync(projectDir); } catch {                      } return path.join(dataRoot(), 'live', projectSlug(real), runId); }


export function startTieFile(claudePid) { return path.join(dataRoot(), 'start-ties', String(claudePid) + '.json'); }

export const START_TIE_SLACK_MS = 5000;



export const isTaskOutput = (p) => typeof p === 'string' && p.length <= 4096 && path.isAbsolute(p) && path.normalize(p) === p && !/^[\\\\/]{2}/.test(p) && !/^\\/net\\//i.test(p) && !/^\\/network\\/servers\\//i.test(p) && /^[A-Za-z0-9_-]{1,80}\\.output$/.test(path.basename(p)) && path.basename(path.dirname(p)) === 'tasks';



export function processStartOf(pid, timeoutMs = 5000) {
  if (!Number.isInteger(pid) || pid <= 1 || process.platform === 'win32') return null;
  if (process.platform === 'linux') { try { const stat = fs.readFileSync('/proc/' + pid + '/stat', 'utf8'); return stat.slice(stat.lastIndexOf(')') + 2).split(' ')[19] || null; } catch { return null; } }
  try { return psStartText(execFileSync('/bin/ps', psStartArgs(pid), { encoding: 'utf8', timeout: timeoutMs, stdio: ['ignore', 'pipe', 'ignore'], env: psStartEnv() })); } catch { return null; }
}

export function processStartOfLater(pid, timeoutMs, done) {
  if (!Number.isInteger(pid) || pid <= 1 || process.platform === 'win32' || process.platform === 'linux') { done(processStartOf(pid)); return; }
  try { execFile('/bin/ps', psStartArgs(pid), { encoding: 'utf8', timeout: timeoutMs, env: psStartEnv() }, (e, text) => done(e ? null : psStartText(text))); } catch { done(null); }
}

const psStartArgs = (pid) => ['-o', 'lstart=', '-p', String(pid)];
const psStartEnv = () => ({ ...process.env, TZ: 'UTC0', LC_ALL: 'C' });
const psStartText = (text) => String(text).trim().split(/\\s+/).join(' ') || null;

const startTimeOk = (t) => (typeof t === 'string' && t.length > 0 && t.length < 64 ? t : null);

const START_TIE_KEEP_MS = 24 * 60 * 60 * 1000;

const MOST_EARLIER_STARTS = 7;

const MOST_START_TIE_BYTES = 16384;



function sweepStartTies(dir, keepPid) {
  const names = []; try { const d = fs.opendirSync(dir); try { for (let e = d.readSync(); e && names.length < 200; e = d.readSync()) names.push(e.name); } finally { d.closeSync(); } } catch { return; }
  for (const name of names) {
    const m = /^(\\d{1,10})\\.json(\\.\\d{1,10}\\.tmp)?$/.exec(name); if (!m) continue;
    const tmp = !!m[2]; const claude = Number(m[1]);
    if (!tmp && claude === keepPid) continue;
    try { const st = fs.lstatSync(path.join(dir, name)); if (!st.isFile()) continue; const age = Date.now() - st.mtimeMs; if (tmp ? age > 60000 : age > START_TIE_KEEP_MS) fs.unlinkSync(path.join(dir, name)); } catch {                    }
  }
}




export function writeStartTie(claudePid, group, output = null) {
  const file = startTieFile(claudePid); fs.mkdirSync(path.dirname(file), { recursive: true, mode: 0o700 });
  sweepStartTies(path.dirname(file), claudePid);
  const tmp = file + '.' + process.pid + '.tmp';

  const start = startTimeOk(processStartOf(group, 1000));


  const claudeStart = startTimeOk(processStartOf(claudePid, 1000)); const was = readStartTie(claudePid, 0, true);
  let earlier = was && (was.claudeStart || null) === claudeStart ? [{ group: was.group, at: was.at, ...(was.start ? { start: was.start } : {}), ...(was.output ? { output: was.output } : {}) }, ...was.earlier].filter((e) => e.group !== group).slice(0, MOST_EARLIER_STARTS) : [];
  const recordOf = () => JSON.stringify({ group, at: Date.now(), ...(start ? { start } : {}), ...(claudeStart ? { claudeStart } : {}), ...(isTaskOutput(output) ? { output } : {}), ...(earlier.length ? { earlier } : {}) });
  while (earlier.length && Buffer.byteLength(recordOf()) > MOST_START_TIE_BYTES) earlier = earlier.slice(0, -1);
  fs.writeFileSync(tmp, recordOf(), { mode: 0o600, flag: 'wx' });
  fs.renameSync(tmp, file);
}


function startEntryOf(j, anyTime = false) {
  if (!j || typeof j !== 'object' || !Number.isInteger(j.group) || j.group <= 1 || typeof j.at !== 'number' || (!anyTime && j.at > Date.now() + START_TIE_SLACK_MS)) return null;
  return { group: j.group, at: j.at, ...(startTimeOk(j.start) ? { start: j.start } : {}), ...(isTaskOutput(j.output) ? { output: j.output } : {}) };
}



export function readStartTie(claudePid, since, anyTime = false) {
  let fd;
  try {
    fd = fs.openSync(startTieFile(claudePid), fs.constants.O_RDONLY | (process.platform === 'win32' ? 0 : fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK));
    const st = fs.fstatSync(fd); if (!st.isFile() || st.size > MOST_START_TIE_BYTES) return null;
    const b = Buffer.alloc(st.size); const n = fs.readSync(fd, b, 0, st.size, 0);
    const j = JSON.parse(b.subarray(0, n).toString('utf8'));
    const newest = startEntryOf(j, anyTime); if (!newest || newest.at < since - START_TIE_SLACK_MS) return null;
    return { ...newest, ...(startTimeOk(j.claudeStart) ? { claudeStart: j.claudeStart } : {}), earlier: (Array.isArray(j.earlier) ? j.earlier.slice(0, MOST_EARLIER_STARTS) : []).map((e) => startEntryOf(e, anyTime)).filter((e) => e && Date.now() - e.at < START_TIE_KEEP_MS) };
  } catch { return null; } finally { if (fd !== undefined) try { fs.closeSync(fd); } catch {              } }
}

export function localPortOf(o) { try { const u = new URL(/^https?:\\/\\//.test(String(o)) ? String(o) : 'http://' + o); return isLocalHost(u.hostname.replace(/^\\[|\\]$/g, '')) ? Number(u.port) || (u.protocol === 'https:' ? 443 : 80) : null; } catch { return null; } }

export function consentKey(o) { const s = String(o).trim().toLowerCase(); const m = s.match(/^(https?:\\/\\/)?(\\[[0-9a-f:]+\\]|[^:/\\[\\]]+)(:\\d+)?$/); return m ? (m[1] || '') + (LOOPBACK_HOSTS.includes(m[2]) ? 'localhost' : m[2]) + (m[3] || '') : s; }
const isLink = (p) => { try { return fs.lstatSync(p).isSymbolicLink(); } catch { return false; } };


function readRecord(projectDir, name, words) {
  const file = path.join(consentDir(projectDir), name); const dir = path.dirname(file);
  const none = (why) => (why ? { file, refused: why } : { file });
  if (!fs.existsSync(dir)) return none(null);
  const dp = dirNotPrivateProblem(dir); if (dp) return none(name + ': ' + dp + ' — ' + words.what + ' are not read from that folder until it is private again (chmod 700)');
  if ([file, dir, path.dirname(dir)].some(isLink)) return none(file + ' (or its folder, or that folder\\'s parent) is a symbolic link, so the record of ' + words.what + ' is ignored — replace the link with a real folder or file');
  let st; try { st = fs.lstatSync(file); } catch { return none(null); }
  if (!st.isFile() || st.nlink > 1 || st.size > 65536) return none(file + ' is not a plain file of sane size (a hard link to another file counts) and is ignored — delete it and ' + words.again);
  if (insideProjectReally(file)) return none(file + ' resolves inside the folder Claude Code opened, so it is ignored — ' + words.what + ' are recorded outside the project (if Claude Code was opened in your home folder, open it in the project\\'s folder instead)');
  let j; try { j = JSON.parse(fs.readFileSync(file, 'utf8')); } catch { return none(file + ' is not valid JSON and is ignored — delete it and ' + words.again); }
  const foreign = wrongProject(j, projectDir); if (foreign) return none(file + ' ' + foreign + ', so it is ignored — delete it and ' + words.again);
  return { file, j };
}
const CONSENT_WORDS = { what: 'allowed addresses', again: 'allow the address again' };
export function readConsent(projectDir, warnings = []) {
  const r = readRecord(projectDir, CONSENT_FILE, CONSENT_WORDS);
  if (r.refused && !warnings.includes(r.refused)) warnings.push(r.refused);
  if (!r.j) return { file: r.file, origins: new Set(), hosts: new Set(), ...(r.refused ? { refused: r.refused } : {}) };
  const keys = (o) => (o && typeof o === 'object' && !Array.isArray(o) ? Object.keys(o).filter((k) => k.length <= 300) : []);
  return { file: r.file, origins: new Set(keys(r.j.origins).map(consentKey)), hosts: new Set(keys(r.j.hosts).map((h) => h.trim().toLowerCase())) };
}




export const START_FILE = 'allowed-starts.json';
const START_WORDS = { what: 'remembered app starts', again: 'accept the app start again when Claude asks' };
const START_KEYS = ['realPath', 'folder', 'command', 'line', 'runs'];

const START_RUNS_MAX_BYTES = 4 * 1024 * 1024;

const START_RUNS_MAX_DEPTH = 3;
const SCRIPT_RUNNERS = new Set(['npm', 'pnpm', 'yarn', 'bun']);


const RUNNER_OWN = {
  pnpm: new Set(['add', 'audit', 'bin', 'config', 'create', 'dedupe', 'deploy', 'dlx', 'env', 'exec', 'fetch', 'i', 'import', 'init', 'install', 'link', 'list', 'ls', 'outdated', 'pack', 'patch', 'prune', 'publish', 'rebuild', 'remove', 'rm', 'root', 'server', 'setup', 'store', 'unlink', 'up', 'update', 'why', 'x']),
  yarn: new Set(['add', 'audit', 'autoclean', 'bin', 'cache', 'check', 'config', 'create', 'dlx', 'exec', 'explain', 'generate-lock-entry', 'global', 'import', 'info', 'init', 'install', 'licenses', 'link', 'list', 'login', 'logout', 'node', 'npm', 'outdated', 'owner', 'pack', 'patch', 'plugin', 'policies', 'publish', 'rebuild', 'remove', 'set', 'stage', 'tag', 'team', 'unlink', 'unplug', 'up', 'upgrade', 'version', 'why', 'workspace', 'workspaces']),
  bun: new Set(['add', 'audit', 'build', 'create', 'exec', 'i', 'info', 'init', 'install', 'link', 'outdated', 'patch', 'pm', 'publish', 'remove', 'repl', 'rm', 'test', 'unlink', 'update', 'upgrade', 'why', 'x']),
};

const FILE_RUNNER = /^(node|nodejs|python|pypy|ruby|php|deno|tsx|ts-node|go)[0-9.]*$/;


const RUNS_OTHERS = new Set(['make', 'gmake', 'foreman', 'honcho', 'overmind', 'env', 'turbo', 'nx', 'lerna', 'wireit', 'run-p', 'run-s', 'npm-run-all', 'npm-run-all2', 'concurrently', 'just', 'task']);

const START_SAFE_VARS = new Set(['PORT', 'HOST', 'HOSTNAME', 'NODE_ENV', 'RAILS_ENV', 'RACK_ENV', 'APP_ENV', 'FLASK_ENV', 'FLASK_DEBUG', 'DEBUG', 'CI', 'FORCE_COLOR', 'NO_COLOR']);


const RUNNER_SETTINGS = ['.npmrc', '.yarnrc', '.yarnrc.yml', '.pnpmfile.cjs', 'pnpm-workspace.yaml', 'bunfig.toml', '.pnp.cjs', '.pnp.loader.mjs', '.pnp.data.json', '.env.yarn', '.corepack.env'];



const NPMRC_KEY = /^(registry|@[a-z0-9_.-]+:registry|\\/\\/[^\\s=[\\]]+:(_authtoken|_auth|username|_password|email|always-auth)|save-exact|save-prefix|engine-strict|fund|audit|package-lock|legacy-peer-deps|strict-peer-deps|auto-install-peers|node-linker|shamefully-hoist|link-workspace-packages|prefer-workspace-packages|loglevel|progress|update-notifier|lockfile|resolution-mode|strict-ssl|always-auth|email|dedupe-peer-dependents|save-workspace-protocol|prefer-offline|prefer-frozen-lockfile|strict-peer-dependencies|public-hoist-pattern\\[\\]|hoist-pattern\\[\\]|ignore-workspace-root-check)$/;
const YARNRC_KEY = /^(registry|@[a-z0-9_.-]+:registry|network-timeout|save-prefix|disable-self-update-check|ignore-engines|lastupdatecheck|strict-ssl|email|username|always-auth|save-exact|ignore-optional|prefer-offline)$/;
const YAML_TOP = {
  '.yarnrc.yml': /^(nodelinker|npmregistryserver|npmscopes|npmauthtoken|npmalwaysauth|npmpublishregistry|enabletelemetry|enableglobalcache|enableimmutableinstalls|enableinlinebuilds|enableprogressbars|enablecolors|enablehyperlinks|checksumbehavior|compressionlevel|defaultsemverrangeprefix|pnpmode|enablescripts|nmmode|nmhoistinglimits|enablemirror|enablestrictssl|httptimeout|httpretry|logfilters|supportedarchitectures|cachefolder|globalfolder|enablenetwork|preferinteractive)$/,
  'pnpm-workspace.yaml': /^(packages|catalog|catalogs|onlybuiltdependencies|neverbuiltdependencies|ignoredbuiltdependencies|overrides|linkworkspacepackages|preferworkspacepackages|sharedworkspacelockfile|nodelinker|shamefullyhoist|publichoistpattern|hoistpattern|autoinstallpeers|strictpeerdependencies|dedupepeerdependents|saveexact|saveprefix|enginestrict)$/,
};

const YAML_NESTED_OK = /^(npmscopes|logfilters|supportedarchitectures|packages|catalog|catalogs|onlybuiltdependencies|neverbuiltdependencies|ignoredbuiltdependencies|overrides|publichoistpattern|hoistpattern)$/;
const BUNFIG_TABLE = /^\\[(install|install\\.cache|install\\.scopes)\\]$/;
const BUNFIG_KEY = /^(registry|exact|frozenlockfile|savetextlockfile|production|optional|dev|peer|auto|linker|dir|disable|disablemanifest|telemetry|"?@[a-z0-9_.-]+"?)$/;

function settingsPlain(name, text) {
  if (name === '.env.yarn' || name === '.corepack.env') return false;
  text = text.replace(/^\\uFEFF/, '');
  if (!(name in { '.npmrc': 1, '.yarnrc': 1, '.yarnrc.yml': 1, 'pnpm-workspace.yaml': 1, 'bunfig.toml': 1 })) return true;
  if (/\\\\/.test(text) || /\\r(?!\\n)/.test(text)) return false;
  let top = null;
  for (const raw of text.split(/\\r?\\n/)) {
    const line = raw.replace(/\\s+$/, ''); const t = line.trim();
    if (!t || t.startsWith('#') || (t.startsWith(';') && !name.endsWith('.yml') && !name.endsWith('.yaml') && name !== 'bunfig.toml')) continue;
    const low = t.toLowerCase();
    if (name === '.npmrc') { if (/["']/.test(t)) return false; const m = /^([^=\\s]+)\\s*=/.exec(low); if (!m || !NPMRC_KEY.test(m[1])) return false; continue; }
    if (name === '.yarnrc') { const m = /^(?:"([^"]+)"|([a-z@][a-z0-9@:._-]*?)):?[ \\t]+(?:"[^"]*"|[0-9]+|true|false)(?:[ \\t]+#.*)?$/.exec(low); if (!m || !YARNRC_KEY.test(m[1] || m[2])) return false; continue; }
    if (name === 'bunfig.toml') { if (/[{["']/.test(t.replace(/^\\[[^\\]]*\\]$/, '').replace(/^"?@[a-z0-9_.-]+"?\\s*=/i, '').replace(/"[^"]*"\\s*$/, ''))) return false; if (t.startsWith('[')) { if (!BUNFIG_TABLE.test(low)) return false; continue; } const m = /^([^=\\s]+)\\s*=/.exec(low); if (!m || !BUNFIG_KEY.test(m[1])) return false; continue; }

    if (/^ *[^\\S ]/.test(line)) return false;
    if (/^\\s*(-\\s+)?[!&*?{]/.test(line) || /[{]/.test(t.replace(/\\$\\{[A-Za-z0-9_]+(:-[^{}]*)?\\}/g, ''))) return false;
    if (!/^\\s/.test(line)) {
      const m = /^["']?([a-z0-9_-]+)["']?\\s*:/.exec(low); if (!m || !YAML_TOP[name].test(m[1])) return false; top = m[1];
      const rest = low.slice(m[0].length).replace(/ +#.*$/, '');
      if (!/^(?: +(?:"[^"]*"|'[^']*'|[^\\s"'#][^"']*))?$/.test(rest) || /:( |$)/.test(rest.replace(/"[^"]*"|'[^']*'/g, ''))) return false;
      continue;
    }
    if (!top || !YAML_NESTED_OK.test(top)) return false;
  }
  return true;
}

const START_RUNS_BUDGET = { words: 400, files: 64, bytes: 32 * 1024 * 1024 };
let startBudget = null;

const spend = (what, n) => { if (!startBudget) return true; startBudget[what] += n; return startBudget[what] <= START_RUNS_BUDGET[what]; };
const sha256Of = (b) => crypto.createHash('sha256').update(b).digest('hex');

function smallFileBytes(p) {
  let fd;
  try {
    fd = fs.openSync(p, fs.constants.O_RDONLY | (fs.constants.O_NONBLOCK || 0));
    const st = fs.fstatSync(fd); if (!st.isFile() || st.size > START_RUNS_MAX_BYTES) return null;
    const b = Buffer.alloc(st.size); let n = 0; while (n < st.size) { const k = fs.readSync(fd, b, n, st.size - n, n); if (!k) break; n += k; }
    return b.subarray(0, n);
  } catch { return null; } finally { if (fd !== undefined) try { fs.closeSync(fd); } catch {              } }
}

function startFile(projectDir, folder, rel) {
  try {
    const p = path.resolve(folder, rel); if (!reallyInsideDir(p, projectDir)) return null;
    const b = smallFileBytes(p); if (!b || !spend('files', 1) || !spend('bytes', b.length)) return null;
    return { path: path.relative(fs.realpathSync(projectDir), fs.realpathSync(p)), sha256: sha256Of(b) };
  } catch { return null; }
}


function runnerSettings(projectDir, folder) {
  const out = []; let root; try { root = fs.realpathSync(checkoutRootOf(projectDir) || projectDir); if (!reallyInsideDir(projectDir, root)) root = fs.realpathSync(projectDir); } catch { return null; }
  for (let dir = folder; ; dir = path.dirname(dir)) {
    for (const name of RUNNER_SETTINGS) {
      const p = path.join(dir, name); try { fs.lstatSync(p); } catch { continue; }
      if (!reallyInsideDir(p, root)) return null;
      const b = smallFileBytes(p); if (!b || !spend('files', 1) || !spend('bytes', b.length)) return null;
      if (!settingsPlain(name, b.toString('utf8'))) return null;
      out.push({ path: path.relative(root, fs.realpathSync(p)), sha256: sha256Of(b) });
    }
    if (dir === root || !reallyInsideDir(path.dirname(dir), root) || path.dirname(dir) === dir) break;
  }
  return out;
}




function startRuns(projectDir, folder, command, depth, seen) {
  if (typeof command !== 'string' || !/^[A-Za-z0-9_./:@=+,-]+( [A-Za-z0-9_./:@=+,-]+)*$/.test(command.trim())) return null;
  const words = command.trim().split(' '); if (!spend('words', words.length)) return null;
  while (words.length && /^[A-Za-z_][A-Za-z0-9_]*=/.test(words[0])) { if (!START_SAFE_VARS.has(words[0].slice(0, words[0].indexOf('=')))) return null; words.shift(); }
  const [prog, ...args] = words; if (!prog) return null;
  const end = args.indexOf('--'); const opts = end < 0 ? args : args.slice(0, end);
  const one = (f) => (f ? { parts: [f] } : null);
  if (SCRIPT_RUNNERS.has(prog)) {
    if (depth >= START_RUNS_MAX_DEPTH) return null;
    const a0 = opts[0]; let name = null; let rest = [];
    if (a0 === 'run' || a0 === 'run-script') { name = opts[1]; rest = opts.slice(2); }
    else if (prog === 'npm') { name = a0 === 'start' || a0 === 'test' ? a0 : null; rest = opts.slice(1); }
    else if (a0 && !RUNNER_OWN[prog].has(a0)) { name = a0; rest = opts.slice(1); }
    if (!name || name.startsWith('-') || (prog === 'npm' && rest.some((a) => a.startsWith('-')))) return null;
    const pkgFile = path.join(folder, 'package.json'); let pkg = null;
    try { const b = reallyInsideDir(pkgFile, projectDir) ? smallFileBytes(pkgFile) : null; pkg = b ? JSON.parse(b.toString('utf8')) : null; } catch { pkg = null; }
    const scripts = pkg && pkg.scripts && typeof pkg.scripts === 'object' && !Array.isArray(pkg.scripts) ? pkg.scripts : {};
    const text = Object.prototype.hasOwnProperty.call(scripts, name) && typeof scripts[name] === 'string' ? scripts[name] : null;
    if (text === null) {
      if (prog !== 'bun' || a0 !== 'run') return null;
      const f = startFile(projectDir, folder, name); const s = f && runnerSettings(projectDir, folder); const more = s && namedFiles(projectDir, folder, [...rest, ...(end < 0 ? [] : args.slice(end + 1))]);
      return more ? { parts: [f, ...s, ...more] } : null;
    }
    if (seen.has(name)) return null; const chain = new Set([...seen, name]);
    const settings = runnerSettings(projectDir, folder); if (!settings) return null;
    const passed = namedFiles(projectDir, folder, [...rest, ...(end < 0 ? [] : args.slice(end + 1))]); if (!passed) return null;
    const parts = [{ script: name, text }, { packageManager: pkg.packageManager ?? null, workspaces: pkg.workspaces ?? null }, ...settings, ...passed];
    for (const n of ['pre' + name, name, 'post' + name]) {
      const t = n === name ? text : Object.prototype.hasOwnProperty.call(scripts, n) && typeof scripts[n] === 'string' ? scripts[n] : null; if (t === null) continue;
      if (n !== name) parts.push({ script: n, text: t });
      const inner = startRuns(projectDir, folder, t, depth + 1, chain); if (!inner) return null;
      if (inner.parts) parts.push(...inner.parts);
    }
    return { parts };
  }
  if (RUNS_OTHERS.has(prog)) return null;
  if (FILE_RUNNER.test(prog)) {
    const rest = /^(deno|go)/.test(prog) ? (args[0] === 'run' ? args.slice(1) : null) : args;
    if (!rest || !rest.length || rest[0].startsWith('-') || (prog === 'tsx' && rest[0] === 'watch')) return null;
    const f = startFile(projectDir, folder, rest[0]); const more = namedFiles(projectDir, folder, rest.slice(1));
    return f && more ? { parts: [f, ...more] } : null;
  }
  if (prog.includes('/')) { const f = startFile(projectDir, folder, prog); const more = namedFiles(projectDir, folder, args); return f && more ? { parts: [f, ...more] } : null; }
  const more = namedFiles(projectDir, folder, args); if (!more) return null;
  return more.length ? { parts: more } : { unknown: true };
}


const RESOLVED_ENDINGS = ['.js', '.cjs', '.mjs', '.ts', '.mts', '.cts', '.tsx', '.jsx', '.json', '.node', '.py', '.rb'];



function namedFiles(projectDir, folder, words) {
  const out = [];
  for (const w of words) {
    const parts = w.split('='); const cands = [];
    if (parts.length > 1) { for (const v of parts.slice(1)) if (v && !v.startsWith('-')) cands.push(v); }
    else if (!w.startsWith('-')) cands.push(w);
    else if (/^-[A-Za-z]./.test(w)) cands.push(w.slice(2));
    let root; try { root = fs.realpathSync(projectDir); } catch { return null; }
    if (cands.some((c) => /^file:/i.test(c))) return null;
    for (const v of cands.filter((c) => !/^[a-z][a-z0-9+.-]*:\\/\\//i.test(c)).flatMap((c) => c.split(/[:;]/)).filter(Boolean)) {
      const p = path.resolve(folder, v);
      if (path.isAbsolute(v) || /^[\\\\/]{2}/.test(v) || !(p === root || p.startsWith(root + path.sep))) return null;
      const dotted = /^[A-Za-z_][\\w.]*$/.test(v) && v.includes('.') ? [v.replace(/\\./g, '/') + '.py', v.replace(/\\./g, '/') + '/__init__.py'] : [];
      const there = [v, ...RESOLVED_ENDINGS.map((e) => v + e), ...dotted].filter((c) => { try { fs.lstatSync(path.resolve(folder, c)); return true; } catch { return false; } });
      for (const c of there) { const f = startFile(projectDir, folder, c); if (!f) return null; if (!out.some((o) => o.path === f.path)) out.push(f); }
    }
  }
  return out;
}




export function startRunsDigest(projectDir, folder, command) {
  startBudget = { words: 0, files: 0, bytes: 0 };
  try { const r = startRuns(projectDir, folder, command, 0, new Set()); return r && r.parts && r.parts.length ? sha256Of(JSON.stringify(r.parts)) : null; } finally { startBudget = null; }
}



export function startFacts(projectDir, cwd, command, line, source, outside) {
  try { const folder = fs.realpathSync(path.resolve(projectDir, cwd || '.')); return { realPath: fs.realpathSync(projectDir), folder, command, line, runs: startRunsDigest(projectDir, folder, command), source: typeof source === 'string' ? source : null, outside: !!outside }; } catch { return null; }
}

export function readStart(projectDir) {
  const r = readRecord(projectDir, START_FILE, START_WORDS);
  const s = r.j && r.j.start && typeof r.j.start === 'object' && !Array.isArray(r.j.start) ? r.j.start : null;
  return { file: r.file, start: s, ...(r.refused ? { refused: r.refused } : {}) };
}

export function startMatches(projectDir, facts) {
  if (!facts) return false;
  const rec = readStart(projectDir); const s = rec.start;
  return !rec.refused && !!s && START_KEYS.every((k) => typeof s[k] === 'string' && typeof facts[k] === 'string' && s[k] === facts[k]) && (s.source ?? null) === facts.source && s.outside === facts.outside;
}

export function writeStart(projectDir, facts) {
  const cur = readStart(projectDir); if (cur.refused) return cur.refused;
  if (!facts || typeof facts.runs !== 'string') { forgetStart(projectDir); return 'Claude Test did not remember this start: it could not tell which of the project\\'s files this command runs, so it could not notice if they change. It will ask again next time.'; }
  if (!START_KEYS.every((k) => typeof facts[k] === 'string' && facts[k])) { forgetStart(projectDir); return 'the start could not be described exactly, so nothing was remembered'; }
  try {
    fs.mkdirSync(path.dirname(cur.file), { recursive: true, mode: 0o700 });
    const existed = fs.existsSync(cur.file);
    const j = { project: projectIdentityPath(projectDir), start: { realPath: facts.realPath, folder: facts.folder, command: facts.command, line: facts.line, runs: facts.runs, source: facts.source, outside: !!facts.outside, at: new Date().toISOString() } };
    const tmp = cur.file + '.' + process.pid + '.tmp'; try { fs.unlinkSync(tmp); } catch {            }
    fs.writeFileSync(tmp, JSON.stringify(j, null, 1) + '\\n', { mode: 0o600, flag: 'wx' }); fs.renameSync(tmp, cur.file);
    const back = readStart(projectDir);
    if (back.refused && !existed) { try { fs.unlinkSync(cur.file); } catch {            } }
    return back.refused ? back.refused + ' \\u2014 nothing was remembered' : null;
  } catch (e) { return 'could not write ' + cur.file + ': ' + e.message + (['EPERM', 'EACCES', 'EROFS'].includes(e.code) ? ' \\u2014 a sandboxed shell (Claude Code\\'s, typically) may not write there' : ''); }
}

export function forgetStart(projectDir) {
  const file = path.join(consentDir(projectDir), START_FILE); const dir = path.dirname(file);
  if ([dir, path.dirname(dir)].some(isLink)) return { removed: false, file, why: 'the remembered app start was not removed: the folder that holds ' + file + ', or its parent, is a symbolic link. Delete ' + file + ' yourself' };
  let st; try { st = fs.lstatSync(file); } catch { return { removed: false, file }; }
  if (st.isDirectory()) return { removed: false, file, why: 'the remembered app start was not removed: ' + file + ' is a folder, not the record. Delete it yourself' };
  try { fs.unlinkSync(file); return { removed: true, file }; } catch (e) { return { removed: false, file, why: 'could not remove ' + file + ': ' + e.message + (['EPERM', 'EACCES', 'EROFS'].includes(e.code) ? ' \\u2014 a sandboxed shell (Claude Code\\'s, typically) may not write there' : '') }; }
}

export function writeConsent(projectDir, { origins = [], hosts = [], remove = false }) {
  const cur = readConsent(projectDir); if (cur.refused) return cur.refused;
  try {
    fs.mkdirSync(path.dirname(cur.file), { recursive: true, mode: 0o700 });
    const j = { project: projectIdentityPath(projectDir), origins: {}, hosts: {} }; try { const old = JSON.parse(fs.readFileSync(cur.file, 'utf8')); for (const k of ['origins', 'hosts']) if (old && old[k] && typeof old[k] === 'object' && !Array.isArray(old[k])) Object.assign(j[k], old[k]); } catch {                     }
    const now = new Date().toISOString(); const existed = fs.existsSync(cur.file);
    for (const o of origins) { for (const k of Object.keys(j.origins)) if (consentKey(k) === consentKey(o)) delete j.origins[k]; if (!remove) j.origins[consentKey(o)] = now; }
    for (const h of hosts) { const k = String(h).trim().toLowerCase(); delete j.hosts[k]; if (!remove) j.hosts[k] = now; }
    const tmp = cur.file + '.' + process.pid + '.tmp'; try { fs.unlinkSync(tmp); } catch {            }
    fs.writeFileSync(tmp, JSON.stringify(j, null, 1) + '\\n', { mode: 0o600, flag: 'wx' }); fs.renameSync(tmp, cur.file);
    const back = readConsent(projectDir);
    if (back.refused && !existed) { try { fs.unlinkSync(cur.file); } catch {            } }
    return back.refused ? back.refused + ' — nothing was allowed' : null;
  } catch (e) { return 'could not write ' + cur.file + ': ' + e.message + (['EPERM', 'EACCES', 'EROFS'].includes(e.code) ? ' — a sandboxed shell (Claude Code\\'s, typically) may not write there' : ''); }
}







export function parseDotenv(src) {
  const LINE = /(?:^|^)\\s*(?:export\\s+)?([\\w.-]+)(?:\\s*=\\s*?|:\\s+?)(\\s*'(?:\\\\'|[^'])*'|\\s*"(?:\\\\"|[^"])*"|\\s*\`(?:\\\\\`|[^\`])*\`|[^#\\r\\n]+)?\\s*(?:#.*)?(?:$|$)/mg;
  const obj = {}; let m; const lines = String(src).replace(/\\r\\n?/mg, '\\n');
  while ((m = LINE.exec(lines)) != null) { let v = (m[2] || '').trim(); const q = v[0]; v = v.replace(/^(['"\`])([\\s\\S]*)\\1$/mg, '$2'); if (q === '"') v = v.replace(/\\\\n/g, '\\n').replace(/\\\\r/g, '\\r'); obj[m[1]] = v; }
  return obj;
}







const UNSAFE_ANY = String.raw\`\\u2028\\u2029\\uFE00-\\uFE0D\\u{E0100}-\\u{E01EF}]|(?![\\u200C\\u200D])\\p{Cf}|[\\u115F\\u1160\\u3164\\uFFA0\\u2065\\uFFF0-\\uFFF8\\u{E0000}\\u{E0002}-\\u{E001F}\\u{E0080}-\\u{E00FF}\\u{E01F0}-\\u{E0FFF}]\`;
const RE_SHOWN = new RegExp('(?:[\\\\p{Cc}' + UNSAFE_ANY + ')+', 'gu');
const RE_SHOWN_TEXT = new RegExp('(?:[\\\\u0000-\\\\u0008\\\\u000B\\\\u000C\\\\u000E-\\\\u001F\\\\u007F-\\\\u009F' + UNSAFE_ANY + ')+', 'gu');
const RE_HAS_CONTROL = new RegExp('[\\\\u0000-\\\\u0008\\\\u000A-\\\\u001F\\\\u007F-\\\\u009F' + UNSAFE_ANY, 'u');
export function shown(s, max = 400) {
  let t = String(s).replace(RE_SHOWN, ' ').replace(/ {2,}/g, ' ');
  if (t !== String(s)) t = t.trim();
  return t.length > max ? t.slice(0, max - 1) + '…' : t;
}

export function shownText(s) { const t = String(s).slice(0, 1 << 20); return t.replace(RE_SHOWN_TEXT, ' '); }

export function markedText(s) { let replaced = 0; const text = String(s).replace(RE_SHOWN_TEXT, (run) => [...run].map((ch) => { replaced++; return '[U+' + ch.codePointAt(0).toString(16).toUpperCase().padStart(4, '0') + ']'; }).join('')); return { text, replaced }; }



export function draftTextFault(text) {
  const t = String(text); const shownAs = shownText(t);
  let at = 0; while (at < t.length && t[at] === shownAs[at]) at++;
  const split = /[A-Za-z0-9_$<>]\\p{Default_Ignorable_Code_Point}+[A-Za-z0-9_<>]/u.exec(t);
  const found = [at < t.length ? at : -1, t.search(/\\r(?!\\n)/), split ? split.index + 1 : -1, t.search(/[\\uD800-\\uDBFF](?![\\uDC00-\\uDFFF])|(?<![\\uD800-\\uDBFF])[\\uDC00-\\uDFFF]/)].filter((i) => i >= 0);
  return found.length ? Math.min(...found) : -1;
}



export function specNameOk(stem) { return typeof stem === 'string' && /^[a-z0-9][a-z0-9-]{0,79}$/.test(stem) && !['readme', 'claude', 'agents', 'architecture'].includes(stem) && !WIN_DEVICE.test(stem + '.md'); }

export function hasControl(s) { return RE_HAS_CONTROL.test(String(s)); }

export function shownDeep(v, max = 2000) {
  if (typeof v === 'string') return shown(v, max);
  if (Array.isArray(v)) return v.map((x) => shownDeep(x, max));
  if (v && typeof v === 'object') { const o = {}; for (const [k, x] of Object.entries(v)) o[k] = shownDeep(x, max); return o; }
  return v;
}


export function commandLineClean(s) { return !hasControl(s) && !/[\\u200c\\u200d]|\\p{Default_Ignorable_Code_Point}/u.test(String(s)); }
function startCommandEarly(rc) { return typeof rc.startCommand === 'string' && rc.startCommand.trim() && rc.startCommand.trim().length <= 400 && commandLineClean(rc.startCommand) ? rc.startCommand.trim() : null; }
export function loadConfig(projectDir) {
  const dir = path.resolve(projectDir || process.cwd());
  const rcPath = path.join(dir, RC_FILE);
  let rc = {}; let warnings = []; let rcFound = false;
  pinnedProjectDir();


  const isRegularFile = (p) => { try { return fs.lstatSync(p).isFile(); } catch { return false; } };
  if (isRegularFile(rcPath)) {
    rcFound = true;
    try { ({ data: rc, warnings } = parseRc(fs.readFileSync(rcPath, 'utf8'))); }
    catch (e) { warnings.push('could not read ' + RC_FILE + ': ' + e.message); }
  } else if (fs.existsSync(rcPath)) warnings.push(RC_FILE + ' is not a regular file (a symlink?) and is ignored');
  let baseUrl = parseBaseUrl(rc.baseUrl);
  let baseUrlSource = baseUrl ? RC_FILE : null;
  if (rc.baseUrl !== undefined && !baseUrl) warnings.push(RC_FILE + ': baseUrl ignored — it must be an http(s) URL whose host is a plain name (letters, digits, hyphens, dots), an IPv4 address or [IPv6], with no credentials');


  let launch = null;
  const launchPath = path.join(dir, '.claude', 'launch.json');
  if (isRegularFile(launchPath)) {
    try {
      const txt = fs.readFileSync(launchPath, 'utf8').replace(/\\/\\*[\\s\\S]*?\\*\\//g, '').replace(/^\\s*\\/\\/.*$/gm, '');
      const j = JSON.parse(txt);
      const c = Array.isArray(j.configurations) ? j.configurations[0] : null;
      if (c) {
        const cmd = c.program ? ['node', c.program, ...(c.args || [])] : c.runtimeExecutable ? [c.runtimeExecutable, ...(c.runtimeArgs || [])] : null;



        launch = { name: typeof c.name === 'string' ? c.name.slice(0, 60) : null, command: cmd ? cmd.join(' ') : null, port: Number(c.port) || null, url: typeof c.url === 'string' ? c.url : null, cwd: typeof c.cwd === 'string' ? c.cwd : null };
      }
    } catch { warnings.push('.claude/launch.json: not valid JSON, ignored'); }
  }

  const rejectedOrigins = [];
  const extra = [];
  const rawExtra = rc.allowedOrigins === undefined ? [] : Array.isArray(rc.allowedOrigins) ? rc.allowedOrigins : [rc.allowedOrigins];


  const printable = (e) => { const s = String(e); return /^[A-Za-z0-9.:/\\[\\]*@_-]{1,80}$/.test(s) ? s : '(an entry that is not a plain host or origin)'; };
  for (const e of rawExtra) { const n = typeof e === 'string' ? normaliseOrigin(e) : null; if (n) extra.push(n); else rejectedOrigins.push(typeof e === 'string' || typeof e === 'number' || typeof e === 'boolean' ? printable(e) : '(non-text entry)'); }
  if (rejectedOrigins.length) warnings.push(RC_FILE + ': ignored allowedOrigins entries that are not plain origins or hosts ("host:*" wildcard ports are not accepted — name the port): ' + rejectedOrigins.join(', '));




  const reachableHosts = []; const rejectedReachable = [];
  const rawReach = rc.reachableHosts === undefined ? [] : Array.isArray(rc.reachableHosts) ? rc.reachableHosts : [rc.reachableHosts];
  for (const e of rawReach.slice(0, 64)) {
    if (typeof e !== 'string') { rejectedReachable.push({ entry: '(non-text entry)', why: 'not text' }); continue; }
    let why; try { why = reachableEntryProblem(e); } catch (err) { why = 'could not be checked (' + String(err && err.message || err).slice(0, 80) + ')'; }
    if (why === null) { const t = e.trim(); if (!reachableHosts.includes(t)) reachableHosts.push(t); } else rejectedReachable.push({ entry: printable(e.trim()), why });
  }
  if (rawReach.length > 64) warnings.push(RC_FILE + ': reachableHosts takes at most 64 entries; the rest were ignored');
  if (rejectedReachable.length) warnings.push(RC_FILE + ': ignored reachableHosts entries: ' + rejectedReachable.map((r) => r.entry + ' (' + r.why + ')').join('; '));





  const twins = [];
  if (baseUrl && LOOPBACK_HOSTS.includes(baseUrl.hostname)) {
    for (const h of baseUrl.hostname === 'localhost' ? LOOPBACK_HOSTS : ['localhost', baseUrl.hostname]) twins.push(baseUrl.protocol + '//' + h + (baseUrl.port ? ':' + baseUrl.port : ''));
  }




  let devDiscovery = null; let candidates = null;
  if (!baseUrl) {
    devDiscovery = discoverDevServer({ projectDir: dir, startCommand: startCommandEarly(rc), startCommandSource: startCommandEarly(rc) ? RC_FILE : null, launch });
    candidates = candidateList({ baseUrl: null }, devDiscovery);
  }
  const candidateOrigins = candidates ? candidates.flatMap((cand) => LOOPBACK_HOSTS.map((h) => 'http://' + h + ':' + cand.port)) : [];
  const wantedOrigins = [...new Set([...(baseUrl ? [baseUrl.origin, ...twins] : candidateOrigins), ...extra])];

  const consent = readConsent(dir, warnings);
  const allowedOrigins = wantedOrigins.filter((o) => consent.origins.has(consentKey(o)));
  const pendingOrigins = [...new Set(wantedOrigins.filter((o) => !consent.origins.has(consentKey(o))).map(consentKey))];
  const pendingHosts = reachableHosts.filter((h) => !consent.hosts.has(h.toLowerCase()));
  for (const h of pendingHosts) reachableHosts.splice(reachableHosts.indexOf(h), 1);
  const startCommand = startCommandEarly(rc);


  const setupCommand = typeof rc.setupCommand === 'string' && rc.setupCommand.trim() && rc.setupCommand.trim().length <= 400 && commandLineClean(rc.setupCommand) ? rc.setupCommand.trim() : null;
  if (rc.setupCommand !== undefined && !setupCommand) warnings.push(RC_FILE + ': setupCommand must be a one-line command string of printable characters, at most 400 long (ignored)');
  if (rc.startCommand !== undefined && !startCommandEarly(rc)) warnings.push(RC_FILE + ': startCommand must be a one-line command string of printable characters, at most 400 long (ignored)');
  const storageState = resolvePrivateFile(dir, rc.storageState, 'auth.json', warnings, 'storageState', 'CLAUDE_TEST_STORAGE_STATE', { carriesProject: true });
  const secretsFile = resolvePrivateFile(dir, rc.secretsFile, 'secrets.env', warnings, 'secretsFile', 'CLAUDE_TEST_SECRETS_FILE');



  const baseIsLoopback = !!baseUrl && LOOPBACK_HOSTS.includes(baseUrl.hostname);
  for (const n of [openedNote, pinNote]) if (n && !warnings.includes(n)) warnings.push(n);
  const signInApplies = baseIsLoopback;
  const signInNote = !baseUrl ? 'sign-in withheld: set baseUrl in ' + RC_FILE + ' (a saved session / secrets file is only given to the browser when a local base URL is configured, in ' + RC_FILE + ')'
    : baseIsLoopback ? 'base URL is on this machine, so a saved session / secrets file (if present) is given to the browser'
    : 'base URL is NOT on this machine: a saved session / secrets file is withheld from the browser — sign-in works for local dev servers only (by design, for now)';
  const isLoopbackOrigin = (o) => { const h = o.replace(/^https?:\\/\\//, '').replace(/:(\\d+|\\*)$/, ''); return LOOPBACK_HOSTS.includes(h); };
  const remoteOrigins = allowedOrigins.filter((o) => !isLoopbackOrigin(o));
  const sessionHasContent = storageState.inUse && storageState.hasContent;
  if (signInApplies && (sessionHasContent || secretsFile.inUse) && extra.length) warnings.push('sign-in material is attached and the browser may also load ' + extra.join(', ') + ' (allowedOrigins): the browser server types secret values only into the page\\'s own fields on ' + baseUrl.origin + ' and checks afterwards that the value landed there, but a document from one of those hosts embedded IN such a page is inside the browser with it and can read what is typed there, and the saved session\\'s cookies go wherever the browser sends them — list only hosts you trust as much as the app itself');



  const browser = typeof rc.browser === 'string' && /^(chrome|msedge|chromium)$/.test(rc.browser.trim()) ? rc.browser.trim() : null;
  if (rc.driver !== undefined && !(typeof rc.driver === 'string' && rc.driver.trim() === 'bundled')) warnings.push(RC_FILE + ': driver can only be "bundled", so delete the line: specs still run in the Claude Test browser, which is held to the allowed addresses (ignored)');
  if (rc.browser !== undefined && !browser) warnings.push(RC_FILE + ': browser must be one of chrome, msedge, chromium: only these can be held to the allowed addresses, so the default test browser is used (ignored)');

  return {
    projectDir: dir, rcPath, rcFound, rc, warnings,
    baseUrl: baseUrl ? baseUrl.href : null, baseUrlSource, baseOrigin: baseUrl ? baseUrl.origin : null, secretOrigins: baseUrl ? [baseUrl.origin] : [],
    allowedOrigins, wantedOrigins, pendingOrigins, pendingHosts, consentFile: consent.file, rejectedOrigins, reachableHosts, rejectedReachable, candidates, devDiscovery, startCommand, startCommandSource: startCommand ? RC_FILE : null,
    browser, launch, storageState, secretsFile, setupCommand, signInApplies, signInNote,
    specsDir: path.join(dir, SPECS_DIR), runsDir: path.join(dir, RUNS_DIR),
  };
}





export function assertRunsDirInsideProject(cfg) {
  const realProject = fs.realpathSync(cfg.projectDir);
  for (const p of [path.dirname(cfg.runsDir), cfg.runsDir]) {
    let st; try { st = fs.lstatSync(p); } catch (e) { if (e.code === 'ENOENT') continue; throw e; }
    const rel = path.relative(cfg.projectDir, p);
    if (st.isSymbolicLink()) throw new Error(rel + ' is a symlink — refusing to write run artifacts through it');
    if (!st.isDirectory()) throw new Error(rel + ' is not a directory');
    if (!insideDir(fs.realpathSync(p), realProject)) throw new Error(rel + ' resolves outside the project — refusing to write run artifacts there');
  }
}








export function trackedClaudeTestSymlinks(projectDir, root) {
  const dirs = [...new Set([projectDir, ...projectsBelow(root).map((b) => path.join(root, b))])];
  const out = [];
  for (const d of dirs) {
    let listing = '';
    try { listing = safeGit(d, ['ls-files', '-s', '-z', '--', '.claude-test']).toString(); } catch { continue; }
    for (const rec of listing.split('\\0')) { if (!rec.startsWith('120000 ')) continue; const rel = rec.slice(rec.indexOf('\\t') + 1); let target = '?'; try { target = fs.readlinkSync(path.join(d, rel)); } catch {            } out.push((path.relative(root, path.join(d, rel)) || rel).replace(/[^\\x20-\\x7e]/g, '?') + ' → ' + String(target).replace(/[^\\x20-\\x7e]/g, '?').slice(0, 120)); if (out.length >= 10) return out; }
  }

  const seen = new Set(out.map((s) => s.split(' → ')[0]));
  let budget = 400;
  const walk = (base, d, depth) => { if (budget <= 0 || depth > 3 || out.length >= 10) return; let ents = []; try { ents = fs.readdirSync(d, { withFileTypes: true }); } catch { return; } for (const e of ents) { if (--budget <= 0 || out.length >= 10) return; const p = path.join(d, e.name); if (e.isSymbolicLink()) { const rel = (path.relative(root, p) || p).replace(/[^\\x20-\\x7e]/g, '?'); if (!seen.has(rel)) { let t = '?'; try { t = fs.readlinkSync(p); } catch {       } out.push(rel + ' → ' + String(t).replace(/[^\\x20-\\x7e]/g, '?').slice(0, 120) + ' (untracked)'); seen.add(rel); } } else if (e.isDirectory()) walk(base, p, depth + 1); } };
  for (const d of dirs) { const ct = path.join(d, '.claude-test'); try { if (fs.lstatSync(ct).isSymbolicLink()) { const rel = (path.relative(root, ct) || ct).replace(/[^\\x20-\\x7e]/g, '?'); if (!seen.has(rel)) { let t = '?'; try { t = fs.readlinkSync(ct); } catch {       } out.push(rel + ' → ' + String(t).replace(/[^\\x20-\\x7e]/g, '?').slice(0, 120) + ' (the folder itself)'); seen.add(rel); } continue; } } catch { continue; } walk(d, ct, 0); }
  return out;
}
function assertNoTrackedSymlinkUnderRuns(cfg) {
  let listing = '';
  let links;
  try { listing = safeGit(cfg.projectDir, ['ls-files', '-s', '--', path.relative(cfg.projectDir, cfg.runsDir)], { maxBuffer: 64 * 1024 * 1024 }).toString(); links = listing.split('\\n').filter((l) => l.startsWith('120000 ')).map((l) => String(l.split('\\t')[1]).replace(/[^\\x20-\\x7e]/g, '?')); }
  catch (e) {
    if (e && e.message === 'not in a git checkout') return;
    links = []; let budget = 20000; let unread = null;
    const walk = (d, depth) => { let ents = []; try { ents = fs.readdirSync(d, { withFileTypes: true }); } catch (err) { if (err.code !== 'ENOENT') unread = d; return; }                                                               for (const e of ents) { if (--budget < 0) return; const p = path.join(d, e.name); if (e.isSymbolicLink()) links.push(path.relative(cfg.projectDir, p).replace(/[^\\x20-\\x7e]/g, '?')); else if (e.isDirectory() && depth < 3) walk(p, depth + 1); } };
    walk(cfg.runsDir, 0);
    if (budget < 0) throw new Error(path.relative(cfg.projectDir, cfg.runsDir) + ' has too many entries to check for symlinks — remove old runs first');
    if (unread) throw new Error(path.relative(cfg.projectDir, unread).replace(/[^\\x20-\\x7e]/g, '?') + ' cannot be listed, so it cannot be checked for symlinks — remove it, or make it readable, first');
    if (links.length) throw new Error(path.relative(cfg.projectDir, cfg.runsDir) + ' contains symlinks (' + links.slice(0, 3).join(', ') + (links.length > 3 ? ', …' : '') + ') — remove them first');
    return;
  }
  if (links.length) throw new Error(path.relative(cfg.projectDir, cfg.runsDir) + ' contains symlinks committed to git (' + links.slice(0, 3).join(', ') + (links.length > 3 ? ', …' : '') + ') — remove them from the repository first');
}







const STEM_SHAPE = /^(?![.\\s])[^/\\\\$\`"':;&|<>*?\\n\\t]{1,120}$/u;




const JOINING_LETTER = /[\\p{Script=Arabic}\\p{Script=Syriac}\\p{Script=Mandaic}\\p{Script=Mongolian}\\p{Script=Devanagari}\\p{Script=Bengali}\\p{Script=Gurmukhi}\\p{Script=Gujarati}\\p{Script=Oriya}\\p{Script=Tamil}\\p{Script=Telugu}\\p{Script=Kannada}\\p{Script=Malayalam}\\p{Script=Sinhala}\\p{Script=Myanmar}\\p{Script=Khmer}\\p{Script=Tibetan}\\p{Script=Javanese}\\p{Script=Balinese}]/u;
const EMOJI_CHAR = /\\p{Emoji_Presentation}|\\p{Emoji_Modifier}|[\\u{1F000}-\\u{1FAFF}]/u;
function joinerNeighbourOk(cps, i, dir) { const c = cps[i + dir]; if (c === undefined) return false; if (EMOJI_CHAR.test(c)) return true; if (dir > 0 && /\\p{Extended_Pictographic}/u.test(c) && cps[i + 2] === '\\uFE0F') return true;                                                                                             if (c === '\\uFE0F') { const base = cps[i + 2 * dir]; return dir < 0 && base !== undefined && (EMOJI_CHAR.test(base) || /\\p{Extended_Pictographic}/u.test(base)); } if (JOINING_LETTER.test(c)) return true; if (/\\p{M}/u.test(c)) { const base = cps[i + 2 * dir]; return base !== undefined && JOINING_LETTER.test(base); } return false; }
function joinersWellPlaced(s) { const cps = [...s]; return cps.every((c, i) => (c !== '\\u200c' && c !== '\\u200d') || (joinerNeighbourOk(cps, i, -1) && joinerNeighbourOk(cps, i, +1))); }
export function safeStem(s) { return typeof s === 'string' && STEM_SHAPE.test(s) && shownText(s) === s && !hasControl(s) && joinersWellPlaced(s); }

export function stemOk(s) { if (!safeStem(s) || s.startsWith('-')) return false; try { encodeURIComponent(s); return true; } catch { return false; } }
const ARTIFACT_NAME = /^(.+)\\.(png|snapshot\\.md)$/;

const WIN_DEVICE = /^(con|prn|aux|nul|com[0-9\\u00b9\\u00b2\\u00b3]|lpt[0-9\\u00b9\\u00b2\\u00b3])(\\.|$)/i;

export const RUN_ID = /^\\d{4}-\\d{2}-\\d{2}T\\d{2}-\\d{2}-\\d{2}(-\\d+)?$/;

export const RUN_PLACEHOLDER = '{run}';

export function runStamp(runId) { const m = typeof runId === 'string' && RUN_ID.test(runId) ? runId.match(/^\\d{4}-(\\d{2})-(\\d{2})T(\\d{2})-(\\d{2})-(\\d{2})(-\\d+)?$/) : null; return m ? m[1] + m[2] + '-' + m[3] + m[4] + m[5] + (m[6] || '') : null; }

export function fillRun(text, runId) { const stamp = runStamp(runId); return stamp && typeof text === 'string' ? text.split(RUN_PLACEHOLDER).join(stamp) : text; }

export function stepsRanFor(state, stamp) {
  const since = ' since you last closed the browser or recorded a verdict';
  if (!state || state.typed !== true) return { ok: false, why: 'this run\\'s value, ' + stamp + ', has not been typed into the page' + since + ' (only browser_type and browser_fill_form count as typing, into a field of the page and never in a call that also types a secret KEY; a browser dialog\\'s text does not count)', fail: 'the steps never typed this run\\'s value' };
  return state.sent === true ? { ok: true } : { ok: false, why: 'this run\\'s value, ' + stamp + ', was typed, but no page action came after it (a click, key press, navigation, wait or more typing; snapshots and screenshots only read the page)' + since + ', so the form was never submitted', fail: 'the form was never submitted' };
}

function holdsStamp(text, stamp) { for (let i = text.indexOf(stamp); i >= 0; i = text.indexOf(stamp, i + 1)) if (!/^-?\\d/.test(text.slice(i + stamp.length, i + stamp.length + 2))) return true; return false; }
const TYPING_TOOLS = new Set(['browser_type', 'browser_fill_form', 'browser_handle_dialog']);

const PAGE_ACTIONS = new Set([...TYPING_TOOLS, 'browser_click', 'browser_press_key', 'browser_navigate', 'browser_navigate_back', 'browser_select_option', 'browser_hover', 'browser_drag', 'browser_wait_for']);





export function makeRunValueWatch() {
  const waiting = new Map();
  let seen = new Map();
  return {

    forwarded(id, name, args, stamps, secret) {
      if (secret || id === undefined || !PAGE_ACTIONS.has(name)) return;
      const a = args && typeof args === 'object' ? args : {};
      const accepted = name === 'browser_handle_dialog' && a.accept === true;
      const texts = name === 'browser_type' ? [a.text] : name === 'browser_fill_form' && Array.isArray(a.fields) ? a.fields.map((f) => f && f.value) : [];
      const held = (Array.isArray(stamps) ? stamps : []).filter((st) => typeof st === 'string' && st && texts.some((t) => typeof t === 'string' && holdsStamp(t, st)));
      waiting.set(id, { stamps: held, send: (name === 'browser_type' && a.submit === true) || accepted });
      if (waiting.size > 256) waiting.delete(waiting.keys().next().value);
    },
    waits: () => waiting.size > 0,
    waitsFor: (id) => waiting.has(id),

    answered(id, ok) {
      const w = waiting.get(id); if (!w) return; waiting.delete(id); if (!ok) return;
      for (const v of seen.values()) v.sent = true;
      for (const st of w.stamps) if (!seen.has(st)) seen.set(st, { typed: true, sent: w.send });
    },
    forget() { seen = new Map(); waiting.clear(); },
    stateOf(stamp) { const v = seen.get(stamp); return { typed: !!v, sent: !!(v && v.sent) }; },

    held() { return { waiting: [...waiting].map(([id, w]) => [id, { ...w, stamps: [...w.stamps] }]), seen: [...seen].map(([st, v]) => [st, { ...v }]) }; },
  };
}

export function snapshotStemOk(stem) { return safeStem(stem) && !WIN_DEVICE.test(stem + '.snapshot.md'); }
export function runsPathProblem(cfg, abs) {
  const rel = path.relative(cfg.projectDir, cfg.runsDir) + '/';
  if (!insideDir(abs, cfg.runsDir) || abs === cfg.runsDir) return 'must be a file under ' + rel;


  const parts = path.relative(cfg.runsDir, abs).split(path.sep);
  const am = parts.length === 2 ? parts[1].match(ARTIFACT_NAME) : null;
  if (!am || !safeStem(am[1]) || WIN_DEVICE.test(parts[1])) return 'must be <run folder>/<name>.png or <name>.snapshot.md, directly inside the run folder (no subfolders)';
  if (!RUN_ID.test(parts[0])) return 'must be inside a run folder that "ct.mjs new-run" made (its name is a date and time)';
  try { assertRunsDirInsideProject(cfg); } catch (e) { return 'cannot be written: ' + e.message; }
  if (!fs.existsSync(cfg.runsDir)) return 'cannot be written yet: ' + rel + ' does not exist (run "ct.mjs new-run" first)';
  let realRuns; try { realRuns = fs.realpathSync(cfg.runsDir); } catch { realRuns = cfg.runsDir; }
  let existing = abs; while (!fs.existsSync(existing)) existing = path.dirname(existing);
  let realExisting; try { realExisting = fs.realpathSync(existing); } catch { return 'cannot be resolved'; }
  if (!insideDir(realExisting, realRuns)) return 'must stay under ' + rel + ' (a symlink points elsewhere)';
  try { const realParent = fs.realpathSync(path.dirname(abs)); if (realParent !== path.join(realRuns, parts[0])) return 'must stay directly inside its run folder (a link points elsewhere)'; } catch { return 'cannot be written yet: the run folder does not exist'; }
  try { const st = fs.lstatSync(abs); if (st.isSymbolicLink()) return 'is a symlink'; if (st.nlink > 1) return 'is a hard link to another file — not writing through it'; } catch {                          }
  return null;
}

export function ensureRunsDir(cfg) {
  assertRunsDirInsideProject(cfg);
  assertNoTrackedSymlinkUnderRuns(cfg);
  fs.mkdirSync(cfg.runsDir, { recursive: true });






  const gi = path.join(path.dirname(cfg.runsDir), '.gitignore');
  try { fs.writeFileSync(gi, '# Claude Test run artifacts (logs, screenshots, driver state) are local evidence, not source.\\nruns/\\nfiled.*.tmp\\n', { flag: 'wx' }); return; } catch (e) { if (e.code !== 'EEXIST') throw e; }
  const ignored = gitIgnored(cfg.projectDir, path.join(cfg.runsDir, 'canary-' + crypto.randomBytes(6).toString('hex'), 'log.md'));


  const hasLine = () => { let fd; try { fd = fs.openSync(gi, fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK); } catch { return false; } try { const st = fs.fstatSync(fd); if (!st.isFile() || st.size > 256 * 1024) return false; const lines = fs.readFileSync(fd, 'utf8').split('\\n'); return lines.includes('runs/') && !lines.slice(lines.lastIndexOf('runs/')).some((line) => line.startsWith('!')); } finally { fs.closeSync(fd); } };
  if (ignored === true || (ignored === null && hasLine())) return;
  let ordinary = false; try { const st = fs.lstatSync(gi); ordinary = st.isFile() && st.nlink === 1 && st.size <= 256 * 1024; } catch {                  }

  throw new Error(path.relative(cfg.projectDir, gi) + (ordinary ? ' does not list runs/, so test results could be committed to git. Add the line runs/ to that file, then run the test again.' : ' is not an ordinary file (it may be a link to another file), so Claude Test does not use it. Delete it, then run the test again: a new one is made.'));
}


export function originAllowed(cfg, url) {
  let u; try { u = new URL(url); } catch { return false; }
  if (u.protocol !== 'http:' && u.protocol !== 'https:') return false;
  for (const o of cfg.allowedOrigins) {
    if (/^https?:\\/\\//.test(o)) { if (u.origin === o) return true; continue; }


    const mm = o.match(/^(\\[[^\\]]+\\]|[^:]+)(?::(\\d+))?$/);
    if (mm && u.hostname === mm[1] && (mm[2] ? u.port === mm[2] : u.port === '')) return true;
  }
  return false;
}



export function mintSpecId() { const A = 'abcdefghijklmnopqrstuvwxyz234567'; const b = crypto.randomBytes(8); let s = ''; for (let i = 0; i < 8; i++) s += A[b[i] & 31]; return 'ct_' + s; }


export function withSpecId(text, id) {
  let body = String(text).replace(/^\\uFEFF/, '').replace(/\\r\\n/g, '\\n');
  if (body.startsWith('---\\n')) {
    const end = body.indexOf('\\n---', 3);
    if (end > 0) { const fm = body.slice(4, end).split('\\n').filter((l) => !/^\\s*id\\s*:/.test(l)); return '---\\n' + ['id: ' + id, ...fm].join('\\n') + body.slice(end); }
  }
  return '---\\nid: ' + id + '\\n---\\n' + body;
}






export function fromComment(text) {
  const all = [...String(text).matchAll(/<!--\\s*from:\\s*([\\s\\S]*?)\\s*-->/g)];
  if (!all.length) return null;
  const files = [];
  for (const m of all) for (const tok of m[1].replace(/(^|\\s)\\([^)]*\\)/g, ' ').replace(/"[^"]*"/g, ' ').split(/,\\s*|\\s+/)) { const clean = tok.replace(/[—–].*$/, '').replace(/:[\\d,-]+$/, '').trim(); if (clean && /^[\\w/.@()[\\]$+-]+\\.\\w+$/.test(clean) && !files.includes(clean)) files.push(clean); }
  const lastM = all[all.length - 1];
  return { last: { text: lastM[1].trim(), start: lastM.index, end: lastM.index + lastM[0].length }, files, count: all.length };
}





export function joinWrappedCriteria(text) {
  const lines = String(text).split('\\n'); const out = []; let inSection = false; let afterMust = false;
  const BLOCK = /^\\s*(#{1,6}\\s|[-*+]\\s|\\d+[.)]\\s|[-*_]{3,}\\s*$|\`\`\`|~~~|>|\\||[[<]|(must not|must)\\s*:)/i;
  for (const line of lines) {
    if (/^##\\s+passes when\\s*$/i.test(line)) { inSection = true; afterMust = false; out.push(line); continue; }
    if (/^##\\s+/.test(line)) { inSection = false; afterMust = false; out.push(line); continue; }
    if (inSection && /^\\s*[-*]\\s*(must not|must)\\s*:/i.test(line)) { afterMust = true; out.push(line); continue; }
    if (inSection && afterMust && /^[ \\t]+\\S/.test(line) && !BLOCK.test(line)) { out[out.length - 1] = out[out.length - 1].replace(/\\s+$/, '') + ' ' + line.trim(); continue; }
    afterMust = false; out.push(line);
  }
  return out.join('\\n');
}
export function parseSpec(text, file) {
  const out = { file, name: null, frontMatter: {}, description: '', passesWhen: '', must: [], mustNot: [], warnings: [] };
  let body = joinWrappedCriteria(text.replace(/^\\uFEFF/, ''));
  if (body.startsWith('---')) {
    const end = body.indexOf('\\n---', 3);
    if (end < 0) out.warnings.push('front matter opened with --- but never closed; it is being read as body text');
    if (end > 0) {
      const { data, warnings } = parseRc(body.slice(3, end));
      out.frontMatter = data; out.warnings.push(...warnings.map((w) => 'front matter ' + w));
      body = body.slice(end + 4).replace(/^\\r?\\n/, '');
    }
  }
  const h1 = body.match(/^#\\s+(.+)$/m);
  if (h1) out.name = shown(h1[1].trim(), 160);
  else if (typeof out.frontMatter.name === 'string') out.name = shown(out.frontMatter.name, 160);
  else out.warnings.push('no "# name" heading');
  const pw = body.search(/^##\\s+passes when\\s*$/im);
  const afterH1 = h1 ? body.indexOf(h1[0]) + h1[0].length : 0;
  if (pw < 0) { out.warnings.push('no "## Passes when" section'); out.description = body.slice(afterH1).trim(); }
  else {
    out.description = body.slice(afterH1, pw).replace(/^##\\s+steps\\s*$/im, '').trim();
    const rest = body.slice(pw).replace(/^##.*$/m, '');
    const next = rest.search(/^##\\s+/m);
    out.passesWhen = (next >= 0 ? rest.slice(0, next) : rest).trim();
    for (const line of out.passesWhen.split(/\\r?\\n/)) {
      const m = line.match(/^\\s*[-*]\\s*(must not|must)\\s*:\\s*(.+)$/i);
      if (m) (m[1].toLowerCase() === 'must' ? out.must : out.mustNot).push(m[2].trim());
    }
    if (out.must.length + out.mustNot.length === 0) out.warnings.push('"## Passes when" has no "- Must:" / "- Must not:" lines');
    else if (out.must.length === 0) out.warnings.push('no "- Must:" line — a spec needs at least one positive criterion to pass');
  }
  if (!out.description) out.warnings.push('no steps text between the heading and "## Passes when"');
  return out;
}




export function specsDirProblem(cfg) {
  let st; try { st = fs.lstatSync(cfg.specsDir); } catch { return null; }
  const rel = path.relative(cfg.projectDir, cfg.specsDir);
  if (st.isSymbolicLink()) return rel + ' is a symlink — refusing to use it';
  if (!st.isDirectory()) return rel + ' is not a directory';
  if (!reallyInsideDir(cfg.specsDir, cfg.projectDir)) return rel + ' resolves outside the project';
  return null;
}

export function listSpecs(cfg) {
  if (!fs.existsSync(cfg.specsDir) || specsDirProblem(cfg)) return [];
  let names; try { names = fs.readdirSync(cfg.specsDir); } catch { return []; }
  return names
    .filter((f) => f.endsWith('.md') && !f.startsWith('_') && f.toLowerCase() !== 'readme.md')
    .sort()
    .map((f) => {
      const p = path.join(cfg.specsDir, f);


      try { if (!fs.lstatSync(p).isFile()) return { file: path.relative(cfg.projectDir, p), name: null, skipped: true, warnings: ['not a regular file (a symlink?) — skipped; copy the spec here instead'] }; } catch {                                      }
      try { const s = parseSpec(fs.readFileSync(p, 'utf8'), path.relative(cfg.projectDir, p)); return { file: s.file, id: typeof s.frontMatter.id === 'string' && /^ct_[a-z2-7]{8}$/.test(s.frontMatter.id) ? s.frontMatter.id : null, name: s.name, allow_navigation: s.frontMatter.allow_navigation, timeout_ms: s.frontMatter.timeout_ms, area: typeof s.frontMatter.area === 'string' && /^[a-z][a-z0-9-]{0,23}$/.test(s.frontMatter.area) ? s.frontMatter.area : undefined, tags: Array.isArray(s.frontMatter.tags) ? s.frontMatter.tags : undefined, must: s.must.length, mustNot: s.mustNot.length, warnings: s.warnings }; }
      catch (e) { return { file: path.relative(cfg.projectDir, p), name: null, warnings: ['unreadable: ' + e.message] }; }
    });
}




export const SECRET_FILE = /(^|\\/)\\.?env([.-][^/]*)?$|(^|\\/)[^/]*\\.env(\\.[^/]*)?$|(^|\\/)\\.envrc$|(^|\\/)\\.npmrc$|(^|\\/)\\.netrc$|\\.(pem|key|p12|pfx|crt|cer|jks|keystore|sqlite3?|db)$|(^|\\/)[^/]*(secrets?|credentials?|creds|passw(or)?ds?|passwd|api[-_]?keys?|keystore|private[-_.]?keys?|id_rsa|id_ed25519|service[-_]?account|tokens?|kubeconfig)[^/]*\\.(json|ya?ml|toml|txt|env|ini|cfg|conf)$|(^|\\/)(?![^/]*\\.(tsx?|jsx?|mjs|cjs|vue|svelte|css|scss|html?)$)(id_(rsa|dsa|ecdsa|ed25519)([-_.][^/]*)?|([^/]*[-_.])?kubeconfig([-_.][^/]*)?)$|(^|\\/)\\.(git-credentials|pgpass|pypirc)$|(^|\\/)(secrets?|credentials?|creds|private[-_.]?keys?|\\.ssh|\\.aws|\\.gnupg|\\.kube)\\//i;



const PLAIN_PATH = /^[\\w@+$~()[\\]-]+(\\.[\\w@+$~()[\\]-]+)*(\\/[\\w@+$~()[\\]-]+(\\.[\\w@+$~()[\\]-]+)*)*$/;
export function plainPath(file) { return typeof file === 'string' && file.length <= 160 && PLAIN_PATH.test(file) && !file.includes('$('); }


export const AFFECTED_ONLY_ABOVE = 4;








export function affectedPlan(specs, changed, { complete = true } = {}) {
  const valid = specs.filter((s) => s && typeof s.stem === 'string' && s.stem).sort((a, b) => a.stem < b.stem ? -1 : a.stem > b.stem ? 1 : 0);
  const live = valid.filter((s) => stemOk(s.stem)); const unnamedSpecs = valid.filter((s) => !stemOk(s.stem)); const unnamed = unnamedSpecs.length;
  const changedSet = new Set(changed);
  const because = (s) => { const hit = (s.files || []).find((f) => changedSet.has(f)); return hit ? (SECRET_FILE.test(hit) ? 'names a changed file whose name looks like a secrets file, so the name is not shown' : !plainPath(hit) ? 'names a changed file whose name cannot be shown' : 'names ' + hit) : s.edited ? 'was edited since it last ran' : s.failedLast ? 'did not pass the last time it ran' : s.noRecentResult ? 'has not run recently' : null; };
  const affected = live.filter((s) => because(s)); const unknown = live.filter((s) => !because(s) && !s.files); const rest = live.filter((s) => !because(s) && s.files);
  const inOrder = (parts) => [...parts.flatMap((p) => p.filter((s) => !s.data)), ...parts.flatMap((p) => p.filter((s) => s.data))].map((s) => s.stem);
  const all = inOrder([affected, unknown, rest]);
  const unnamedAffected = unnamedSpecs.filter((s) => because(s)).length;
  const why = !valid.length ? 'no-specs' : unnamedAffected || unnamedSpecs.some((s) => !s.files) ? 'unnamed-spec-must-run' : !affected.length ? 'nothing-affected' : !complete ? 'history-not-compared' : !rest.length ? 'every-spec-affected' : live.length <= AFFECTED_ONLY_ABOVE ? 'few-specs' : 'affected-only';
  const plural = (n, one, many) => n + ' ' + (n === 1 ? one : many);


  const startedWhy = () => {
    const byFile = affected.filter((s) => (s.files || []).some((f) => changedSet.has(f))).length;
    const edited = affected.filter((s) => !(s.files || []).some((f) => changedSet.has(f)) && s.edited).length;
    const failed = affected.filter((s) => !(s.files || []).some((f) => changedSet.has(f)) && !s.edited && s.failedLast).length;
    const parts = [[byFile, 'the one the changes may affect', 'the ones the changes may affect'], [edited, 'the one edited since it last ran', 'the ones edited since they last ran'], [failed, 'the one that did not pass last time', 'the ones that did not pass last time'], [affected.length - byFile - edited - failed, 'the one not run recently', 'the ones not run recently'], [unknown.length, 'the one that does not say what it covers', 'the ones that do not say what they cover']].filter(([n]) => n > 0).map(([n, one, many]) => (n === 1 ? one : many));
    return parts.length > 1 ? parts.slice(0, -1).join(', ') + ' and ' + parts[parts.length - 1] : parts[0];
  };
  const plan = { mode: why === 'affected-only' ? 'affected' : 'all', why, total: live.length + unnamed, run: why === 'affected-only' ? inOrder([affected, unknown]) : all, all, affected: affected.map((s) => ({ stem: s.stem, because: because(s) })), ...(unnamed > 0 ? { unnamed } : {}), ...(unnamedAffected > 0 ? { unnamedAffected } : {}) };
  if (plan.mode === 'affected') Object.assign(plan, { skipped: rest.length + unnamed, started: 'Started ' + plan.run.length + ' of ' + (live.length + unnamed) + ' tests: ' + startedWhy(), skippedLine: plural(rest.length + unnamed, 'other test', 'other tests') + ' skipped. Type /claude-test:run all to run every test.' });
  return plan;
}






export function fixPlan(specs, failed, touched, { local = true } = {}) {
  const failedSet = new Set(failed); const touchedSet = new Set(touched);
  const plan = affectedPlan(specs.map((s) => ({ ...s, failedLast: failedSet.has(s && s.stem), noRecentResult: false })), touched);
  const picked = new Set(plan.affected.map((a) => a.stem));
  const namesTouched = (s) => (s.files || []).some((f) => touchedSet.has(f));
  const maybeHeld = local ? [] : specs.filter((s) => s && s.data && failedSet.has(s.stem) && !namesTouched(s)).map((s) => s.stem);
  const fixWasForAnother = specs.some((s) => s && failedSet.has(s.stem) && namesTouched(s) && plan.all.includes(s.stem));
  const held = new Set(!plan.unnamedAffected && fixWasForAnother ? maybeHeld : []);
  const notRerun = plan.all.filter((s) => held.has(s));
  return { run: plan.all.filter((s) => picked.has(s) && !held.has(s)), also: plan.affected.filter((a) => !failedSet.has(a.stem)), ...(notRerun.length ? { notRerun } : {}), ...(plan.unnamedAffected ? { unnamed: plan.unnamedAffected } : {}) };
}



export function touchedSince({ uncommitted, recorded, startedAt, modifiedAt, secret }) {
  const listed = new Set(uncommitted); const after = (f) => { const t = modifiedAt(f); return t === null || t >= startedAt; };
  const now = uncommitted.filter((f) => (recorded && !recorded.has(f) && !secret(f)) || after(f));
  return [...new Set([...now, ...(recorded ? [...recorded].filter((f) => !listed.has(f) && after(f)) : [])])];
}

export function reachesOnlyThisMachine(cfg) {
  const local = (origin) => isLocalHost(String(origin).replace(/^https?:\\/\\//, '').replace(/:(\\d+|\\*)$/, ''));
  return (!cfg.baseUrl || isLocalHost(new URL(cfg.baseUrl).hostname)) && (cfg.allowedOrigins || []).every(local) && (cfg.reachableHosts || []).every(local);
}


export function appRelative(projectDir, file) {
  const s = String(file ?? '');
  if (!s || s.includes('\\0')) return null;
  const inside = (base) => { const rel = path.relative(base, path.resolve(base, s)); return rel && rel !== '..' && !rel.startsWith('..' + path.sep) && !path.isAbsolute(rel) ? rel.split(path.sep).join('/') : null; };
  let real = null; try { real = fs.realpathSync(projectDir); } catch {                                             }
  return inside(path.resolve(projectDir)) ?? (real ? inside(real) : null);
}
