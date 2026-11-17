<!--
name: 'Data: signin.mjs'
description: Text asset signin.mjs that Claude Code loads by path from its bundle.
ccVersion: 2.1.326
-->










import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { playwrightRegistryDir, dirNotPrivateProblem, projectIdentityPath, wrongProject, MAX_OWN_STATE_BYTES } from './config.mjs';


export const SKILLS_DIR = '.claude-test/skills';
export const SKILL_BLOCK_KEY = 'claude-test';
export const STATE_FILE_NAME = 'storageState.json';
export const SKILL_NAME_RE = /^[a-z0-9][a-z0-9-]{0,63}$/;
export const CT_ENV_NAME_RE = /^CT_[A-Z0-9_]{1,61}$/;
export const CRED_NAME_RE = /^[A-Za-z][A-Za-z0-9_-]{0,63}$/;
export const MAX_SKILLS = 8, MAX_SKILL_DIRS = 64, MAX_SKILL_MD_BYTES = 16 * 1024, MAX_DESCRIPTION_CHARS = 1024;
export const DEFAULT_SKILL_TIMEOUT_S = 120, MAX_SKILL_TIMEOUT_S = 300;
export const MAX_STATE_BYTES = 1024 * 1024, MAX_STDOUT_BYTES = 64 * 1024, STDERR_TAIL_BYTES = 8192, MAX_CREDS_LINE_BYTES = 4096, MAX_CREDS = 16;
const STDIO_GRACE_MS = 1500;
export const LOOPBACK_HOSTS = ['localhost', '127.0.0.1', '[::1]', '::1'];

const printable = (s, n) => String(s).replace(/[^\\x20-\\x7e]+/g, ' ').slice(0, n);







export function storageStateShapeProblem(s) { return skillStateShapeProblem(s); }
export function skillStateShapeProblem(s) {
  if (!s || typeof s !== 'object' || !Array.isArray(s.cookies) || !Array.isArray(s.origins)) return 'not a Playwright storage state (need cookies[] and origins[])';
  const eff = (v) => (typeof v === 'string' && v !== '' ? v : undefined);
  const badCookie = s.cookies.findIndex((c) => {
    const url = eff(c?.url); const domain = eff(c?.domain); const p = eff(c?.path);
    return typeof c?.name !== 'string' || typeof c?.value !== 'string'
      || (c?.url !== undefined && typeof c?.url !== 'string') || (c?.domain !== undefined && typeof c?.domain !== 'string') || (c?.path !== undefined && typeof c?.path !== 'string')
      || !(url !== undefined || (domain !== undefined && p !== undefined)) || (url !== undefined && (domain !== undefined || p !== undefined))
      || (url !== undefined && !URL.canParse(url))
      || (c?.expires !== undefined && (typeof c?.expires !== 'number' || (c.expires !== -1 && (c.expires < 0 || c.expires > 253402300799))))
      || (c?.httpOnly !== undefined && typeof c?.httpOnly !== 'boolean') || (c?.secure !== undefined && typeof c?.secure !== 'boolean')
      || (c?.sameSite !== undefined && !['Strict', 'Lax', 'None'].includes(c.sameSite)) || c?.partitionKey !== undefined;
  });
  if (badCookie !== -1) return 'cookies[' + badCookie + '] needs a string name/value plus a parseable url or a domain/path pair (not both); expires in epoch seconds; sameSite Strict|Lax|None';
  const httpOrigin = (v) => { try { const u = new URL(v); return u.protocol === 'http:' || u.protocol === 'https:'; } catch { return false; } };
  const badIdb = (idb) => idb !== undefined && (!Array.isArray(idb) || idb.some((d) => !d || typeof d.name !== 'string' || typeof d.version !== 'number' || !Array.isArray(d.stores)));
  const badOrigin = s.origins.findIndex((o) => typeof o?.origin !== 'string' || !httpOrigin(o.origin) || !Array.isArray(o?.localStorage) || o.localStorage.some((kv) => typeof kv?.name !== 'string' || typeof kv?.value !== 'string') || badIdb(o?.indexedDB));
  if (badOrigin !== -1) return 'origins[' + badOrigin + '] is malformed (need an absolute http(s) origin, localStorage[{name,value}], and indexedDB entries {name, version, stores[]} when present)';
  return null;
}

const hostOf = (h) => h.replace(/^\\[|\\]$/g, '').toLowerCase();
const isLoopbackHost = (h) => LOOPBACK_HOSTS.includes(h.toLowerCase()) || LOOPBACK_HOSTS.includes(hostOf(h));








function strictCookie(c) {
  let { name, value, domain, path: p, expires, httpOnly, secure, sameSite } = c;
  if (typeof c.url === 'string' && c.url !== '') { const u = new URL(c.url); domain = u.hostname; p = '/'; if (secure === undefined) secure = u.protocol === 'https:'; }
  return { name, value, domain, path: p || '/', expires: typeof expires === 'number' ? expires : -1, httpOnly: httpOnly === true, secure: secure === true, sameSite: sameSite || 'Lax' };
}
export function filterStateToLoopback(state, baseUrl = null) {
  let basePort = null; try { if (baseUrl) { const b = new URL(baseUrl); basePort = b.port || (b.protocol === 'https:' ? '443' : '80'); } } catch {                                 }
  const otherPorts = new Set();
  const cookies = state.cookies.filter((c) => {
    if (!c || typeof c !== 'object' || typeof c.name !== 'string' || typeof c.value !== 'string') return false;
    if (typeof c.url === 'string' && c.url !== '') { try { return isLoopbackHost(new URL(c.url).hostname); } catch { return false; } }
    return typeof c.domain === 'string' && isLoopbackHost(c.domain.replace(/^\\./, ''));
  }).map(strictCookie);
  const origins = state.origins
    .filter((o) => { try { if (!o || !Array.isArray(o.localStorage)) return false; const u = new URL(o.origin); if (!((u.protocol === 'http:' || u.protocol === 'https:') && isLoopbackHost(u.hostname))) return false; const port = u.port || (u.protocol === 'https:' ? '443' : '80'); if (basePort && port !== basePort) { otherPorts.add(port); return false; } return true; } catch { return false; } })
    .map((o) => ({ origin: o.origin, localStorage: o.localStorage.map((kv) => ({ name: kv.name, value: kv.value })), ...(Array.isArray(o.indexedDB) ? { indexedDB: o.indexedDB } : {}) }));
  for (const c of state.cookies) { try { if (c && typeof c.url === 'string' && c.url) { const u = new URL(c.url); const port = u.port || (u.protocol === 'https:' ? '443' : '80'); if (isLoopbackHost(u.hostname) && basePort && port !== basePort) otherPorts.add(port); } } catch {       } }
  return { state: { cookies, origins }, kept: { cookies: cookies.length, origins: origins.length }, dropped: { cookies: state.cookies.length - cookies.length, origins: state.origins.length - origins.length }, otherLoopbackPorts: [...otherPorts] };
}

export const EMPTY_STATE = Object.freeze({ cookies: [], origins: [] });



export function writePrivateFile(p, data, { privateFolder = true } = {}) {
  const linkAt = [p, path.dirname(p), path.dirname(path.dirname(p))].find((q) => { try { return fs.lstatSync(q).isSymbolicLink(); } catch (e) { if (e.code !== 'ENOENT') throw e; return false; } });
  if (linkAt) throw new Error(linkAt + ' is a symbolic link — refusing to write sign-in material through it (sign-in files live in a real private folder; remove the link)');
  fs.mkdirSync(path.dirname(p), { recursive: true, mode: 0o700 });
  if (privateFolder) { try { fs.chmodSync(path.dirname(p), 0o700); } catch {                   } }
  const tmp = p + '.' + process.pid + '.' + Date.now() + '.tmp';
  fs.writeFileSync(tmp, data, { mode: 0o600, flag: 'wx' });
  fs.renameSync(tmp, p);
  try { fs.chmodSync(p, 0o600); } catch {                   }
}
const mib = (n) => (n / 1048576).toFixed(1) + ' MiB';



export function writeAuthState(authPath, state, opts = {}) {
  if (typeof opts.projectDir !== 'string' || opts.projectDir === '') throw new Error('the project folder this session belongs to was not given — not saved');
  const data = JSON.stringify({ project: projectIdentityPath(opts.projectDir), cookies: state.cookies, origins: state.origins }, null, 2) + '\\n';
  if (Buffer.byteLength(data) > MAX_OWN_STATE_BYTES) throw new Error('the session to save is ' + mib(Buffer.byteLength(data)) + ', over the ' + mib(MAX_OWN_STATE_BYTES) + ' this tool keeps — not saved (the app stores more in the browser than a test session should carry)');
  writePrivateFile(authPath, data, opts);
}





export function ensureAuthFile(authPath, opts = {}) {
  if (typeof opts.projectDir !== 'string' || opts.projectDir === '') throw new Error('the project folder this session belongs to was not given');
  const own = opts.privateFolder !== false;
  if (own) { const why = fs.existsSync(path.dirname(authPath)) ? dirNotPrivateProblem(path.dirname(authPath)) : null; if (why) return { usable: false, reason: why }; }
  let st; try { st = fs.statSync(authPath); } catch (e) { if (e.code !== 'ENOENT') throw e; writeAuthState(authPath, EMPTY_STATE, opts); return { usable: true, created: true }; }
  if (!st.isFile()) return { usable: false, reason: authPath + ' is not a regular file' };
  if (st.size === 0) { writeAuthState(authPath, EMPTY_STATE, opts); return { usable: true, repaired: 'empty file initialised' }; }
  if (st.size > MAX_OWN_STATE_BYTES) return { usable: false, reason: authPath + ' is ' + mib(st.size) + ', over the ' + mib(MAX_OWN_STATE_BYTES) + ' this tool loads — not given to the browser; run "ct-auth.mjs logout" and sign in again' };
  let j; try { j = JSON.parse(fs.readFileSync(authPath, 'utf8')); } catch { j = undefined; }
  const foreign = j === undefined ? null : wrongProject(j, opts.projectDir);
  if (foreign) return { usable: false, reason: authPath + ' ' + foreign + ' — not given to the browser and left as it is; delete it and sign in again' };
  const problem = j === undefined ? 'is not valid JSON' : storageStateShapeProblem(j);
  if (!problem) {


    const f = filterStateToLoopback(j, opts.baseUrl || null);
    if (!f.dropped.cookies && !f.dropped.origins) return { usable: true };
    if (own) { writeAuthState(authPath, f.state, opts); return { usable: true, repaired: 'dropped ' + f.dropped.cookies + ' cookie(s) and ' + f.dropped.origins + ' origin(s) that are not this machine\\'s app (kept ' + f.kept.cookies + '/' + f.kept.origins + ')' }; }
    return { usable: false, reason: authPath + ' holds ' + f.dropped.cookies + ' cookie(s) / ' + f.dropped.origins + ' origin(s) for hosts that are not this machine (left untouched)' };
  }
  if (own) { writeAuthState(authPath, EMPTY_STATE, opts); return { usable: true, repaired: 'unreadable state replaced by an empty one (' + problem + ')' }; }
  return { usable: false, reason: authPath + ' ' + problem + ' (left untouched)' };
}


export function stateHasContent(p) { try { const j = JSON.parse(fs.readFileSync(p, 'utf8')); return (Array.isArray(j.cookies) && j.cookies.length > 0) || (Array.isArray(j.origins) && j.origins.length > 0); } catch { return false; } }


export function savedSessionCheckable(authPath) { const i = authFileInfo(authPath); return i.present && !i.empty && !i.problem; }

export function authFileInfo(authPath) {
  let st; try { st = fs.statSync(authPath); } catch { return { present: false }; }
  if (!st.isFile()) return { present: true, problem: 'not a regular file' };
  if (st.size > MAX_OWN_STATE_BYTES) return { present: true, problem: mib(st.size) + ', over the ' + mib(MAX_OWN_STATE_BYTES) + ' this tool loads (not given to the browser)' };
  let j; try { j = JSON.parse(fs.readFileSync(authPath, 'utf8')); } catch { return { present: true, problem: 'not valid JSON' }; }
  const shape = storageStateShapeProblem(j);
  if (shape) return { present: true, problem: shape };
  const exp = j.cookies.map((c) => c.expires).filter((e) => typeof e === 'number' && e > 0);
  const earliest = exp.length ? Math.min(...exp) : null;
  return {
    present: true, empty: j.cookies.length === 0 && j.origins.length === 0,
    cookies: j.cookies.length, origins: j.origins.length,
    savedMinutesAgo: Math.round((Date.now() - st.mtimeMs) / 60000),
    earliestCookieExpiry: earliest ? new Date(earliest * 1000).toISOString() : null,
    expired: exp.length > 0 && Math.max(...exp) * 1000 < Date.now() && !j.cookies.some((c) => !(typeof c.expires === 'number' && c.expires > 0)) && j.origins.length === 0,
    mode: '0' + (st.mode & 0o777).toString(8),
  };
}





const ENV_KEY_RE = /^\\s*(?:export\\s+)?([A-Za-z_][\\w.-]*)\\s*(?:=|:\\s)/;
export function readEnvFile(p) {
  const out = {};
  let t; try { t = fs.readFileSync(p, 'utf8'); } catch { return out; }
  let below = false; const above = new Set();
  for (const line of t.split(/\\r?\\n/)) {
    if (/^# --- (written by ct(-auth)?\\.mjs sign-in|typed credentials written by ct\\.mjs sign-in)/.test(line)) { below = true; continue; }
    const m = line.match(/^\\s*(?:export\\s+)?([A-Za-z_][\\w.-]*)\\s*(?:=|:\\s)\\s*(.*)$/);
    if (!m || line.trim().startsWith('#')) continue;
    let v = m[2].trim();
    if (v.startsWith("'") && v.endsWith("'") && v.length >= 2) v = v.slice(1, -1);
    else if (v.startsWith('"') && v.endsWith('"') && v.length >= 2) v = v.slice(1, -1).replace(/\\\\n/g, '\\n');
    else v = v.replace(/\\s+#.*$/, '');
    if (below && above.has(m[1])) continue;
    if (!below) above.add(m[1]);
    out[m[1]] = v;
  }
  return out;
}




export const SKILL_CREDS_MARKER = '# --- written by ct-auth.mjs sign-in: lines BELOW this marker belong to the sign-in skill and are updated by each run; put your own lines ABOVE it ---';
export function mergeEnvFile(p, pairs, opts = { privateFolder: false }) {
  let lines = []; try { lines = fs.readFileSync(p, 'utf8').split(/\\r?\\n/); if (lines[lines.length - 1] === '') lines.pop(); } catch {                }
  const keyOf = (line) => { const m = line.match(ENV_KEY_RE); return m ? m[1] : null; };
  let mark = lines.findIndex((l) => /^# --- (written by ct(-auth)?\\.mjs sign-in|typed credentials written by ct\\.mjs sign-in)/.test(l));
  if (mark !== -1) lines[mark] = SKILL_CREDS_MARKER;
  const userKeys = new Set((mark === -1 ? lines : lines.slice(0, mark)).map(keyOf).filter(Boolean));
  const refused = {}; const accepted = {};
  for (const [k, v] of Object.entries(pairs)) {
    if (userKeys.has(k)) refused[k] = 'a line you wrote already sets it';
    else if (/[\\r\\n]/.test(v) || (v.includes("'") && v.includes('"')) || (v.includes("'") && v.includes('\\\\'))) refused[k] = 'value has a newline, both quote kinds, or a quote plus a backslash (would not round-trip)';
    else accepted[k] = v;
  }
  const fmt = (k, v) => k + '=' + (v.includes("'") ? '"' + v + '"' : /[\\s#"\\\\]/.test(v) ? "'" + v + "'" : v);
  const stale = mark === -1 ? 0 : lines.slice(mark + 1).filter((l) => userKeys.has(keyOf(l))).length;
  if (Object.keys(accepted).length || stale) {
    if (mark === -1) { lines.push(SKILL_CREDS_MARKER); mark = lines.length - 1; }
    const below = lines.slice(mark + 1).filter((l) => !Object.prototype.hasOwnProperty.call(accepted, keyOf(l)) && !userKeys.has(keyOf(l)));
    lines = [...lines.slice(0, mark + 1), ...below, ...Object.entries(accepted).map(([k, v]) => fmt(k, v))];
    writePrivateFile(p, lines.join('\\n') + '\\n', opts);
  }
  return { keysInFile: Object.keys(readEnvFile(p)).length, written: Object.keys(accepted), refused };
}



export function tidySkillCreds(p, opts = { privateFolder: false }) {
  let lines; try { lines = fs.readFileSync(p, 'utf8').split(/\\r?\\n/); } catch { return 0; }
  if (lines[lines.length - 1] === '') lines.pop();
  const keyOf = (line) => { const m = line.match(ENV_KEY_RE); return m ? m[1] : null; };
  const mark = lines.findIndex((l) => /^# --- (written by ct(-auth)?\\.mjs sign-in|typed credentials written by ct\\.mjs sign-in)/.test(l));
  if (mark === -1) return 0;
  const aboveKeys = new Set(lines.slice(0, mark).map(keyOf).filter(Boolean));
  const kept = lines.slice(mark + 1).filter((l) => !aboveKeys.has(keyOf(l)));
  const dropped = lines.length - (mark + 1) - kept.length;
  if (dropped) writePrivateFile(p, [...lines.slice(0, mark + 1), ...kept].join('\\n') + '\\n', opts);
  return dropped;
}



export function scrub(text, secrets = []) {
  let t = String(text);
  for (const s of secrets) if (s && s.length >= 3) t = t.split(s).join('***');
  return t.replace(/\\b(?=[A-Za-z0-9_\\-+/=.]{24,})(?=[^\\s]*[A-Za-z])(?=[^\\s]*\\d)[A-Za-z0-9_\\-+/=.]{24,}/g, '<redacted>');
}







function parseFrontMatter(fmText) {
  const out = {}; let block = null;
  for (const raw of fmText.split('\\n')) {
    if (!raw.trim() || raw.trim().startsWith('#')) continue;
    const nested = raw.match(/^  +([A-Za-z0-9_-]+):\\s*(.*)$/);
    if (nested && block) { out[block][nested[1]] = unquote(nested[2]); continue; }
    const top = raw.match(/^([A-Za-z0-9_-]+):\\s*(.*)$/);
    if (!top) return { why: 'front matter line not understood: ' + printable(raw, 60) };
    if (top[2] === '') { block = top[1]; out[block] = {}; } else { block = null; out[top[1]] = unquote(top[2]); }
  }
  return { data: out };
}
function unquote(v) { v = v.trim(); if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) return v.slice(1, -1); if (/^-?\\d+$/.test(v)) return Number(v); return v; }


export function parseSkillMd(text, dirName) {
  const src = text.replace(/^\\uFEFF/, '').replace(/\\r\\n/g, '\\n');
  if (!src.startsWith('---\\n')) return { why: 'SKILL.md must start with a "---" frontmatter line' };
  const end = src.indexOf('\\n---', 4);
  if (end === -1) return { why: 'SKILL.md frontmatter has no closing "---" line' };
  const fm = parseFrontMatter(src.slice(4, end));
  if (fm.why) return { why: fm.why };
  const m = fm.data;
  const after = src.indexOf('\\n', end + 4);
  const body = after === -1 ? '' : src.slice(after + 1);
  if (m.name !== dirName) return { why: "frontmatter name must equal the directory name '" + dirName + "'" };
  if (typeof m.description !== 'string' || m.description.trim() === '') return { why: 'frontmatter description is required' };
  const description = m.description.trim();
  if (description.length > MAX_DESCRIPTION_CHARS) return { why: 'description is ' + description.length + ' characters; the limit is ' + MAX_DESCRIPTION_CHARS };
  const raw = m[SKILL_BLOCK_KEY];
  const block = { timeoutS: DEFAULT_SKILL_TIMEOUT_S };
  if (raw !== undefined && raw !== null) {
    if (typeof raw !== 'object' || Array.isArray(raw)) return { why: "'" + SKILL_BLOCK_KEY + "' must be a mapping (run, check, timeout_s)" };
    for (const k of Object.keys(raw)) if (!['run', 'check', 'timeout_s'].includes(k)) return { why: "'" + SKILL_BLOCK_KEY + "' has an unknown key '" + printable(k, 40) + "' (known: run, check, timeout_s)" };
    if (raw.run !== undefined) { if (typeof raw.run !== 'string' || !raw.run.trim()) return { why: "'" + SKILL_BLOCK_KEY + ".run' must be a relative path string" }; block.run = raw.run.trim(); }
    if (raw.check !== undefined) { if (typeof raw.check !== 'string' || !raw.check.trim()) return { why: "'" + SKILL_BLOCK_KEY + ".check' must be a relative path string" }; block.check = raw.check.trim(); }
    if (raw.timeout_s !== undefined) { if (typeof raw.timeout_s !== 'number' || !Number.isInteger(raw.timeout_s) || raw.timeout_s < 1 || raw.timeout_s > MAX_SKILL_TIMEOUT_S) return { why: "'" + SKILL_BLOCK_KEY + ".timeout_s' must be a whole number of seconds, 1-" + MAX_SKILL_TIMEOUT_S }; block.timeoutS = raw.timeout_s; }
  }
  return { description, body, block };
}

const within = (p, dir) => p === dir || p.startsWith(dir + path.sep);


export function resolveScript(dir, declared) {
  const shown = printable(declared, 80);
  if (path.isAbsolute(declared) || /^[A-Za-z]:/.test(declared) || declared.includes('\\\\')) return { why: "'" + shown + "' must be a relative path inside the skill directory" };
  if (declared.split('/').some((seg) => seg === '..' || seg === '')) return { why: "'" + shown + "' may not contain empty or '..' segments" };
  const lexical = path.resolve(dir, declared);
  if (!within(lexical, dir)) return { why: "'" + shown + "' points outside the skill directory" };
  let real; try { real = fs.realpathSync(lexical); } catch { return { why: "'" + shown + "' does not exist" }; }
  if (!within(real, dir)) return { why: "'" + shown + "' resolves (through a link) outside the skill directory" };
  let st; try { st = fs.statSync(real); } catch { st = null; }
  if (!st?.isFile()) return { why: "'" + shown + "' is not a regular file" };
  const via = ['.mjs', '.js', '.cjs'].includes(path.extname(real).toLowerCase()) ? 'node' : 'exec';
  if (via === 'exec' && (st.mode & 0o111) === 0) return { why: "'" + shown + "' is not a .mjs/.js/.cjs file and is not executable" };
  return { path: real, declared, via };
}



export function listSkills(projectDir) {
  const root = path.join(projectDir, SKILLS_DIR);
  const out = [];
  try { if (fs.realpathSync(root) !== path.join(fs.realpathSync(projectDir), SKILLS_DIR)) return [{ name: '(all)', problem: SKILLS_DIR + ' (or a directory above it) is a symlink — skills are not read through links' }]; } catch { return out; }
  let names; try { names = fs.readdirSync(root).sort(); } catch { return out; }
  for (const name of names.slice(0, MAX_SKILL_DIRS)) {
    const dir = path.join(root, name);
    let st; try { st = fs.lstatSync(dir); } catch { continue; }
    if (!st.isDirectory()) { if (st.isSymbolicLink()) out.push({ name, problem: 'is a symlink — skipped' }); continue; }
    if (!SKILL_NAME_RE.test(name)) { out.push({ name, problem: 'directory name must match ' + SKILL_NAME_RE }); continue; }
    const mdPath = path.join(dir, 'SKILL.md');
    let mst; try { mst = fs.lstatSync(mdPath); } catch { continue; }
    if (!mst.isFile()) { out.push({ name, problem: 'SKILL.md is not a regular file' }); continue; }
    if (mst.size > MAX_SKILL_MD_BYTES) { out.push({ name, problem: 'SKILL.md is over ' + MAX_SKILL_MD_BYTES + ' bytes' }); continue; }
    let mdText; try { mdText = fs.readFileSync(mdPath, 'utf8'); } catch (e) { out.push({ name, problem: 'SKILL.md cannot be read (' + (e.code || e.message) + ')' }); continue; }
    const parsed = parseSkillMd(mdText, name);
    if (parsed.why) { out.push({ name, problem: parsed.why }); continue; }
    if (!parsed.block.run && !parsed.block.check) continue;
    let realDir; try { realDir = fs.realpathSync(dir); } catch (e) { out.push({ name, problem: 'cannot resolve the skill folder (' + (e.code || e.message) + ')' }); continue; }
    const run = parsed.block.run ? resolveScript(realDir, parsed.block.run) : null;
    const check = parsed.block.check ? resolveScript(realDir, parsed.block.check) : null;
    const problem = run?.why || check?.why || (!parsed.block.run ? 'has a check script but no run script' : null);
    out.push({ name, dir: realDir, description: parsed.description, run: run && !run.why ? run : null, check: check && !check.why ? check : null, timeoutS: parsed.block.timeoutS, problem: problem || null });
    if (out.length >= MAX_SKILLS) break;
  }
  return out;
}


export function parseCredsLine(stdout) {
  const lines = stdout.split('\\n').map((l) => l.trim()).filter((l) => l !== '');
  const last = lines[lines.length - 1];
  if (last === undefined || !last.startsWith('{')) return { creds: {} };
  let j; try { j = JSON.parse(last); } catch { return { problem: 'the last stdout line starts with "{" but is not valid JSON', salvage: [] }; }
  const salvage = j !== null && typeof j === 'object' ? Object.values(j).filter((v) => typeof v === 'string' && v !== '').slice(0, 64) : [];
  if (Buffer.byteLength(last, 'utf8') > MAX_CREDS_LINE_BYTES) return { problem: 'the credentials line is over ' + MAX_CREDS_LINE_BYTES + ' bytes', salvage };
  if (j === null || typeof j !== 'object' || Array.isArray(j)) return { problem: 'the credentials line must be a JSON object', salvage };
  const entries = Object.entries(j);
  if (entries.length > MAX_CREDS) return { problem: 'the credentials line has ' + entries.length + ' keys; at most ' + MAX_CREDS, salvage };
  const creds = {};
  for (const [k, v] of entries) {
    if (!CRED_NAME_RE.test(k)) return { problem: 'credential names must be 1-64 letters, digits, "_" or "-", starting with a letter', salvage };
    if (typeof v !== 'string') return { problem: "credential '" + k + "' must be a string", salvage };
    if (v !== '') creds[k] = v;
  }
  return { creds };
}




export function defaultBrowsersPath() {
  const r = playwrightRegistryDir();
  return r.hermetic ? '0' : r.dir;
}




const COPY_LIMITS = { bytes: 32 * 1024 * 1024, entries: 2048, depth: 12 };
function copyTree(src, dst, budget = { bytes: 0, entries: 0 }, depth = 0) {
  if (depth > COPY_LIMITS.depth) throw new Error('skill directory is nested deeper than ' + COPY_LIMITS.depth + ' levels');
  fs.mkdirSync(dst, { recursive: true, mode: 0o700 });
  for (const ent of fs.readdirSync(src, { withFileTypes: true })) {
    if (ent.name === 'node_modules') continue;
    if (++budget.entries > COPY_LIMITS.entries) throw new Error('skill directory has more than ' + COPY_LIMITS.entries + ' entries');
    const s = path.join(src, ent.name), d = path.join(dst, ent.name);
    if (ent.isDirectory()) copyTree(s, d, budget, depth + 1);
    else if (ent.isFile()) { const st = fs.statSync(s); budget.bytes += st.size; if (budget.bytes > COPY_LIMITS.bytes) throw new Error('skill directory is larger than 32 MiB'); fs.copyFileSync(s, d); try { fs.chmodSync(d, st.mode & 0o777); } catch {       } }
  }
}









export function runSkillScript({ skill, phase, cfg, toolsDir, browserExecutable, ctVars, prepare, scratchRoot }) {
  const script = phase === 'check' ? skill.check : skill.run;
  if (!script) return Promise.resolve({ exitCode: null, spawnError: 'skill has no ' + phase + ' script', stdout: '', stderrTail: '', stdoutTruncated: false, stderrTruncated: false, timedOut: false, durationMs: 0, outDir: null, scratch: null });



  const root = scratchRoot || path.join(os.homedir(), '.cache', 'claude-test', 'scratch');
  fs.mkdirSync(root, { recursive: true, mode: 0o700 }); try { fs.chmodSync(root, 0o700); } catch {       }
  try { const rs = fs.lstatSync(root); if (!rs.isDirectory() || rs.isSymbolicLink() || (typeof process.getuid === 'function' && rs.uid !== process.getuid()) || (rs.mode & 0o022) !== 0) throw new Error('scratch root ' + root + ' is not a private directory of yours'); }
  catch (e) { return Promise.resolve({ exitCode: null, spawnError: e.message, stdout: '', stderrTail: '', stdoutTruncated: false, stderrTruncated: false, timedOut: false, durationMs: 0, outDir: null, scratch: null }); }
  const scratch = fs.mkdtempSync(path.join(root, 'ct-skill-'));
  fs.chmodSync(scratch, 0o700);
  const home = path.join(scratch, 'home'), outDir = path.join(scratch, 'out'), skillDir = path.join(scratch, 'skill');
  fs.mkdirSync(home, { mode: 0o700 }); fs.mkdirSync(outDir, { mode: 0o700 });
  try { copyTree(skill.dir, skillDir); } catch (e) { rmScratch(scratch); return Promise.resolve({ exitCode: null, spawnError: e.message, stdout: '', stderrTail: '', stdoutTruncated: false, stderrTruncated: false, timedOut: false, durationMs: 0, outDir: null, scratch: null }); }

  const nm = path.join(skillDir, 'node_modules'); fs.mkdirSync(nm, { recursive: true });
  for (const pkg of ['playwright', 'playwright-core']) {
    const from = path.join(toolsDir, 'node_modules', pkg);
    try { if (!fs.existsSync(from)) throw new Error('not in the tools folder'); fs.symlinkSync(from, path.join(nm, pkg), process.platform === 'win32' ? 'junction' : 'dir'); }
    catch (e) { rmScratch(scratch); return Promise.resolve({ exitCode: null, spawnError: 'cannot provide ' + pkg + ' to the skill (' + e.message + ') — run "ct.mjs install" first', stdout: '', stderrTail: '', stdoutTruncated: false, stderrTruncated: false, timedOut: false, durationMs: 0, outDir: null, scratch: null }); }
  }
  if (prepare) prepare(outDir);
  const rel = path.relative(skill.dir, script.path);
  const scriptCopy = path.join(skillDir, rel);
  const env = { PATH: process.env.PATH && process.env.PATH.trim() ? process.env.PATH : '/usr/local/bin:/usr/bin:/bin', HOME: home, TMPDIR: home, LANG: process.env.LANG || 'C.UTF-8', CLAUDE_TEST_TARGET_ORIGIN: new URL(cfg.baseUrl).origin, CLAUDE_TEST_OUTPUT: outDir, CLAUDE_TEST_SKILL: skill.name, CLAUDE_TEST_PHASE: phase };
  if (browserExecutable) env.CLAUDE_TEST_BROWSER_EXECUTABLE = browserExecutable;


  env.PLAYWRIGHT_BROWSERS_PATH = process.env.PLAYWRIGHT_BROWSERS_PATH || defaultBrowsersPath();
  if (process.platform === 'win32') { for (const k of ['SystemRoot', 'SystemDrive', 'windir', 'COMSPEC', 'PATHEXT']) if (process.env[k]) env[k] = process.env[k]; env.USERPROFILE = home; env.TEMP = home; env.TMP = home; }
  for (const [k, v] of Object.entries(ctVars)) if (CT_ENV_NAME_RE.test(k)) env[k] = v;
  const [cmd, args] = script.via === 'node' ? [process.execPath, [scriptCopy]] : [scriptCopy, []];
  const started = Date.now();
  const timeoutMs = skill.timeoutS * 1000;
  return new Promise((resolveP) => {
    let stdoutBuf = Buffer.alloc(0), stderrBuf = Buffer.alloc(0), stdoutTruncated = false, stderrTruncated = false, timedOut = false, settled = false, spawnError, child;
    const killGroup = () => { if (!child?.pid) return; try { process.kill(-child.pid, 'SIGKILL'); } catch {            } try { child.kill('SIGKILL'); } catch {            } };
    const finish = (exitCode, signal) => {
      if (settled) return; settled = true; clearTimeout(timer); killGroup(); for (const sig of ['SIGINT', 'SIGTERM', 'SIGHUP']) process.removeListener(sig, onSignal);
      const errText = stderrBuf.toString('utf8');
      resolveP({ exitCode, signal, timedOut, spawnError, stdout: stdoutBuf.toString('utf8'), stdoutTruncated, stderrTail: stderrTruncated ? (errText.includes('\\n') ? errText.slice(errText.indexOf('\\n') + 1) : '') : errText, stderrTruncated, durationMs: Date.now() - started, outDir, scratch });
    };
    const timer = setTimeout(() => { timedOut = true; killGroup(); }, timeoutMs);
    const onSignal = () => { killGroup(); if (!rmScratch(scratch).removed) process.stderr.write(scratchLeftWarning(scratch)); process.exit(130); };
    for (const sig of ['SIGINT', 'SIGTERM', 'SIGHUP']) process.once(sig, onSignal);
    try { child = spawn(cmd, args, { cwd: skillDir, env, stdio: ['pipe', 'pipe', 'pipe'], detached: true }); }
    catch (e) { spawnError = e.message; finish(null, null); return; }
    child.on('error', (e) => { spawnError = e.message; killGroup(); finish(null, null); });
    child.stdout.on('data', (b) => { stdoutBuf = Buffer.concat([stdoutBuf, b]); if (stdoutBuf.length > MAX_STDOUT_BYTES) { stdoutBuf = stdoutBuf.subarray(stdoutBuf.length - MAX_STDOUT_BYTES); stdoutTruncated = true; } });
    child.stderr.on('data', (b) => { stderrBuf = Buffer.concat([stderrBuf, b]); if (stderrBuf.length > STDERR_TAIL_BYTES) { stderrBuf = stderrBuf.subarray(stderrBuf.length - STDERR_TAIL_BYTES); stderrTruncated = true; } });
    child.on('close', (code, sig) => finish(code, sig));
    child.on('exit', (code, sig) => { clearTimeout(timer); setTimeout(() => { child.stdout?.destroy(); child.stderr?.destroy(); finish(code, sig); }, STDIO_GRACE_MS); });
    child.stdin.on('error', () => {});
    try { child.stdin.end('{}'); } catch {                    }
  });
}


export function readSkillState(outDir) {
  const p = path.join(outDir, STATE_FILE_NAME);
  let st; try { st = fs.lstatSync(p); } catch { return {}; }
  if (!st.isFile()) return { problem: STATE_FILE_NAME + ' is not a regular file' };
  if (st.size > MAX_STATE_BYTES) return { problem: STATE_FILE_NAME + ' is ' + st.size + ' bytes; the limit is ' + MAX_STATE_BYTES };
  try { return { state: JSON.parse(fs.readFileSync(p, 'utf8')) }; }
  catch { return { problem: STATE_FILE_NAME + ' is not valid JSON' }; }
  finally { try { fs.rmSync(p, { force: true }); } catch {       } }
}


export function scratchLeftWarning(folder) { return '[claude-test] could not delete the temporary folder ' + folder + '. It can hold a signed-in browser session or test credentials. Close any sign-in browser that is still open, then delete the folder if it is still there.\\n'; }



export function rmScratch(dir) {
  if (!dir) return { removed: true };
  let code;
  for (const pauseMs of [0, 100, 200, 300]) {
    if (pauseMs) Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, pauseMs);
    try { fs.rmSync(dir, { recursive: true, force: true }); return { removed: true }; }
    catch (e) { code = e.code; }
  }
  return { removed: false, folder: dir, why: 'deleting it failed (' + (code || 'no error code given') + ')' };
}



const HINT_FILES = ['README.md', 'CLAUDE.md', 'AGENTS.md', 'CONTRIBUTING.md', '.env.example', '.env.sample', '.env.template', '.env.development', '.env.test', 'package.json', 'Makefile', 'Procfile', 'docs/dev.md', 'docs/development.md', 'docs/local.md', 'docs/setup.md', 'docs/auth.md', 'docs/testing.md'];
const HINT_RES = [
  /\\b(?:[A-Z][A-Z0-9_]*?_)?(?:SKIP|BYPASS|DISABLE|FAKE|MOCK|STUB|NO)_?[A-Z0-9_]*(?:AUTH|LOGIN|SSO|OAUTH|IAP|SESSION)[A-Z0-9_]*\\b/,
  /\\b(?:[A-Z0-9_]*DEV_USER|TEST_USER(?:_EMAIL)?|AUTH_DISABLED|DISABLE_AUTH|MOCK_AUTH)\\b/,
  /dev[ -]login|auth\\w* (?:is )?(?:stubbed|mocked|bypass)|impersonat|login as any user|magic link.{0,40}(?:console|log)/i,
  /\\/(?:__)?dev[-_/]?(?:login|auth|session)\\b/,
];



export function bypassHints(projectDir) {
  const hints = [];
  for (const rel of HINT_FILES) {
    let t; try { const p = path.join(projectDir, rel); const st = fs.lstatSync(p); if (!st.isFile() || st.size > 512 * 1024) continue; const real = fs.realpathSync(p); const root = fs.realpathSync(projectDir); if (!(real === root || real.startsWith(root + path.sep))) continue;                                                                        t = fs.readFileSync(real, 'utf8').slice(0, 65536); } catch { continue; }
    const lines = t.split('\\n');
    for (let i = 0; i < lines.length && hints.length < 10; i++) {
      const line = lines[i];
      if (line.length > 300) continue;


      const shown = /^\\.env/.test(path.basename(rel)) ? line.replace(/^(\\s*#?\\s*(?:export\\s+)?[A-Za-z_][A-Za-z0-9_]*\\s*=)(.*)$/, (m0, k, rest) => { const cm = rest.match(/\\s+#.*$/); const val = (cm ? rest.slice(0, cm.index) : rest).trim(); return k + (/^["']?(0|1|true|false|yes|no|on|off)["']?$/i.test(val) ? val : '<value hidden>') + (cm ? cm[0] : ''); }) : line;
      for (const re of HINT_RES) { const m = shown.match(re); if (m) { hints.push({ match: printable(m[0], 60), file: rel, line: i + 1, text: printable(shown.trim(), 160) }); break; } }
    }
    if (hints.length >= 10) break;
  }
  return hints;
}





export function secretsMergeTarget(cfg) {
  const p = cfg.secretsFile.defaultPath;
  try { const st = fs.lstatSync(p); if (st.isSymbolicLink() || !st.isFile()) return null; } catch {                                      }
  const isLink = (q) => { try { return fs.lstatSync(q).isSymbolicLink(); } catch { return false; } };
  if (isLink(path.dirname(p)) || isLink(path.dirname(path.dirname(p)))) return null;
  return p;
}
