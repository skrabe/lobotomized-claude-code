<!--
name: 'Skill: Whiteboard merge-state.mjs Helper'
description: >-
  The merge-state.mjs write-back helper bundled as a whiteboard-skill file,
  extracted to the skill base directory that Claude is pointed at when the
  whiteboard skill loads.
ccVersion: 2.1.238
-->
// Whiteboard write-back helper. Reads the board state the page embeds, appends
// Claude's elements, places each new element clear of everything already on
// the board, and writes the republishable page: the skill's template plus
// exactly one inserted state line. Serialization escapes every "<" the way
// the page's own serializer does, so board text can never close the
// embedded script block. Runs on node or bun, no dependencies.
//
// usage: node merge-state.mjs --state <fetched page, or a bare board state such as {"v":1,"els":[],"pingCount":0,"ping":null}>
//                             --add <file with a JSON array of elements to add>
//                             --template <path to template.html>
//                             --out <path to whiteboard.html>
//                             [--retire id1,id2]   (your own cl_ ids to remove)
//                             [--title "<topic> whiteboard"]     (name the board on first publish)

import { readFileSync, writeFileSync } from 'node:fs'

const FONT_SIZE = 17, STICKY_FONT = 15, MARGIN = 16, STEP = 24

function arg(name){
  const i = process.argv.indexOf('--' + name)
  return i === -1 ? undefined : process.argv[i + 1]
}
function fail(msg){ process.stderr.write('whiteboard merge: ' + msg + '\\n'); process.exit(1) }
function read(p, what){
  try{ return readFileSync(p, 'utf8') }
  catch(e){ fail('cannot read ' + what + ' at ' + p + ' — pass the path you wrote it to (' + e.code + ')') }
}

const statePath = arg('state'), addPath = arg('add'), tplPath = arg('template'), outPath = arg('out')
if(!statePath || !addPath || !tplPath || !outPath) fail('need --state, --add, --template and --out')
const retire = new Set((arg('retire') || '').split(',').map(s => s.trim()).filter(Boolean))

// --- the page title: an explicit --title, else the one the board carries, else the default.
// titleFrom is the ONE place a candidate becomes a name: NFC-normalize; replace every DENIED code
// point (controls, invisible format chars except the ZWJ/ZWNJ a name can need, bidi overrides,
// LS/PS) with a space; collapse whitespace; cap by code point; strip BLANK runs (whitespace and
// joiners) from both edges; then a name exists only if some code point actually renders
// (VISIBLE) — the same emptiness test the rename guard relies on, so display and refusal agree
// (standalone sibling of sanitizeArtifactTitle in src/tools/ArtifactTool/constants.ts) ---
const DEFAULT_TITLE = 'Whiteboard'
const escHtml = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
// reads back what escHtml writes and what the server's re-serialization writes (&#34; &#39; &#13;)
const unescHtml = s => s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;|&#34;/g, '"')
  .replace(/&#39;/g, "'").replace(/&#13;/g, '\\r').replace(/&amp;/g, '&')
// The server stores a published page with \` data-id="<16 chars>"\` added to every open tag (last,
// on the tags read here): the one extra attribute a read-back page may carry (KEEP-IN-SYNC:
// dataIdAttrLen in the CLI)
const DATA_ID = '(?: data-id="(?!-)(?:(?!--)[A-Za-z0-9_-]){16}")?'
const DENIED = /(?![\\u200c\\u200d])[\\p{C}\\u202a-\\u202e\\u2066-\\u2069\\u2028\\u2029]/gu
const EDGE_BLANK = /^[\\s\\u200c\\u200d]+|[\\s\\u200c\\u200d]+$/gu
// blank to the eye: whitespace, joiners, combining marks without a base, and the fillers and
// blank glyphs that render as nothing — a name needs at least one code point outside all of it
const VISIBLE = /[^\\s\\u200c\\u200d\\p{M}\\u2800\\u3164\\uffa0\\u115f\\u1160]/u
function titleFrom(plain){
  const t = String(plain || '').normalize('NFC').replace(DENIED, ' ').replace(/\\s+/g, ' ')
  const capped = Array.from(t).slice(0, 120).join('') // cap by code point so no surrogate pair splits
  const name = capped.replace(EDGE_BLANK, '')
  return VISIBLE.test(name) ? escHtml(name) : ''
}

// --- read the state: either a bare JSON object or the page carrying the wb-state block ---
// The block is matched only where a real board carries it — after the page's body comment
// (a sent board), after the title line (a page this helper wrote), or on its own — so the
// opener string inside the page's own script source can never be mistaken for it.
const raw = read(statePath, 'the --state board')
let stateText = raw.trim()
const bareState = stateText[0] === '{'
let stateAt = -1
if(!bareState){
  const anchor = '(?:^\\\\s*|<body' + DATA_ID + '>\\\\s*|-->\\\\s*|<\\\\/title>\\\\s*)<script type="application\\\\/json" id="wb-state"'
  const m = raw.match(new RegExp(anchor + DATA_ID + '>(\\\\{[\\\\s\\\\S]*?\\\\})<\\\\/script>'))
  // a page that ends before any script closes, or an anchored opener with no closer (or cut
  // inside its own tag), is a sent board whose read was cut off; an opener carrying anything but
  // the server's attribute is a board this helper cannot read — neither is an unsent board
  const headOnly = !/<\\/(?:script|body|html)>/i.test(raw) && /^\\s*<(?:!doctype|html|head|meta|title)[\\s>]/i.test(raw)
  if(!m) fail(headOnly || new RegExp(anchor + '(?:' + DATA_ID + '>(?:\\\\{|$)|[^>]*$)').test(raw)
    ? 'the wb-state block in ' + statePath + ' is cut off — the board read is incomplete; read the full saved HTML by path and run again'
    : new RegExp(anchor + '[\\\\s/]').test(raw)
    ? 'the wb-state block in ' + statePath + ' carries attributes this helper does not read — the board cannot be written back safely; stop and tell the user'
    : 'no wb-state block in ' + statePath + ' — a board that has never been sent has no state to write back to; ask the user to hit Send to Claude first')
  stateText = m[1]; stateAt = m.index + m[0].indexOf('<script')
}
// a fetched PAGE names the board in the FIRST <title> of its head — the head is the content before
// the wb-state block, so a <title> literal later in the page's script source is never a name
let carried = ''
if(!bareState){
  const head = raw.slice(0, stateAt), t = new RegExp('<title' + DATA_ID + '>').exec(head)
  const textAt = t ? t.index + t[0].length : -1
  const closeAt = t ? head.indexOf('</title>', textAt) : -1
  if(closeAt !== -1) carried = titleFrom(unescHtml(head.slice(textAt, closeAt)))
}
let state
try{ state = JSON.parse(stateText) }
catch(e){ fail('the wb-state block does not parse — the board read is incomplete; stop and tell the user (' + e.message + ')') }
if(!state || !Array.isArray(state.els)) fail('state has no els array')

// --- read the additions and enforce the authorship rules ---
let additions
try{ additions = JSON.parse(read(addPath, 'the --add additions file')) }
catch(e){ fail('additions file is not valid JSON (' + e.message + ')') }
if(!Array.isArray(additions)) fail('additions must be a JSON array of elements')
// the page identifies an element by the first 40 characters of its id, so uniqueness is
// checked on that same key
const idKey = id => typeof id === 'string' ? id.slice(0, 40) : id
const existingIds = new Set(state.els.map(e => e && idKey(e.id)))
for(const id of retire){
  const el = state.els.find(e => e && e.id === id)
  if(!el) continue
  if(el.author !== 'claude' && el.by !== 'claude') fail('refusing to retire ' + id + ': not authored by claude')
}
const ADDABLE = new Set(['text', 'rect', 'ellipse', 'cylinder', 'diamond', 'sticky', 'arrow'])
for(const e of additions){
  if(!e || typeof e !== 'object' || !ADDABLE.has(e.type)) fail('additions must be text, rect, ellipse, cylinder, diamond, sticky or arrow (got ' + JSON.stringify(e && e.type) + ')')
  e.author = 'claude'
  if(typeof e.id !== 'string' || !e.id.startsWith('cl_')) fail('every addition needs an id starting with cl_ (got ' + JSON.stringify(e.id) + ')')
  // the page keeps ids to 40 characters, so a longer one would no longer be unique on the board
  if(e.id.length > 40) fail('addition id ' + JSON.stringify(e.id.slice(0, 40)) + '… is over 40 characters — shorten it')
  if(existingIds.has(e.id)) fail('addition id ' + e.id + ' already exists on the board or earlier in this batch')
  existingIds.add(e.id)
  if(!Number.isInteger(e.seed)) e.seed = 1 + Math.floor(Math.random() * 1e9)
  // a text node may carry its font size; clamp it to the range the page itself accepts
  if(e.type === 'text'){
    if(Number.isFinite(e.size)) e.size = Math.max(8, Math.min(64, e.size))
    else delete e.size
  }
}
// --- an arrow binds only to a box, sticky or text node on the board; the page clears anything else ---
const CONNECTABLE = new Set(['text', 'rect', 'ellipse', 'cylinder', 'diamond', 'sticky'])
const bindable = new Set(state.els.concat(additions)
  .filter(e => e && !retire.has(e.id) && CONNECTABLE.has(e.type)).map(e => idKey(e.id)))
for(const e of additions){
  if(e.type !== 'arrow') continue
  for(const k of ['fromId', 'toId']){
    if(e[k] == null) continue
    if(!bindable.has(e[k])) fail(e.id + ': ' + k + ' must name a box, sticky or text node on the board (got ' + JSON.stringify(String(e[k]).slice(0, 40)) + ')')
  }
}

// --- geometry: the same boxes the page uses, with an estimate for unmeasured text ---
function textSize(txt, px){
  const lines = String(txt || '').split('\\n')
  const w = Math.max(...lines.map(l => l.length)) * px * 0.62 + 12
  return {w: Math.ceil(w), h: Math.ceil(lines.length * px * 1.35) + 8}
}
function bbox(e){
  switch(e.type){
    case 'arrow': case 'line':
      return {x: Math.min(e.x1, e.x2), y: Math.min(e.y1, e.y2), w: Math.abs(e.x1 - e.x2), h: Math.abs(e.y1 - e.y2)}
    case 'pen': {
      let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity
      for(const p of e.pts || []){ x0 = Math.min(x0, p[0]); y0 = Math.min(y0, p[1]); x1 = Math.max(x1, p[0]); y1 = Math.max(y1, p[1]) }
      return {x: x0, y: y0, w: Math.max(1, x1 - x0), h: Math.max(1, y1 - y0)}
    }
    case 'text': {
      const m = textSize(e.text, Number.isFinite(e.size) ? e.size : FONT_SIZE)
      return {x: e.x, y: e.y, w: e.w || m.w, h: e.h || m.h}
    }
    case 'sticky': {
      const m = textSize(e.label, STICKY_FONT)
      return {x: e.x, y: e.y, w: e.w || Math.max(120, m.w + 16), h: e.h || Math.max(70, m.h + 18)}
    }
    default: return {x: e.x, y: e.y, w: e.w || 120, h: e.h || 60}
  }
}
const intersects = (a, b, m) =>
  a.x < b.x + b.w + m && a.x + a.w + m > b.x && a.y < b.y + b.h + m && a.y + a.h + m > b.y

// --- place each non-connector addition clear of the board and of each other ---
const finite = (...ns) => ns.every(n => Number.isFinite(n))
const occupied = state.els.filter(e => e && !retire.has(e.id) && e.type !== 'arrow' && e.type !== 'line').map(bbox)
for(const e of additions){
  if(e.type === 'arrow'){ // connectors ride their endpoints; they still need real coordinates
    if(!finite(e.x1, e.y1, e.x2, e.y2)) fail(e.id + ': arrows need finite x1,y1,x2,y2')
    continue
  }
  if(!finite(e.x, e.y)) fail(e.id + ': needs finite x and y')
  let box = bbox(e)
  if(!finite(box.w, box.h) || box.w <= 0 || box.h <= 0) fail(e.id + ': needs a positive width and height')
  // the estimated size is written back so the published element renders the way it was placed
  e.w = box.w; e.h = box.h
  let placed = box, found = false
  // scan down-then-right from the requested spot until the box is clear of everything occupied
  outer: for(let ring = 0; ring < 40; ring++){
    for(let dx = 0; dx <= ring; dx++){
      const dy = ring - dx
      const cand = {x: box.x + dx * STEP, y: box.y + dy * STEP, w: box.w, h: box.h}
      if(!occupied.some(o => intersects(cand, o, MARGIN))){ placed = cand; found = true; break outer }
    }
  }
  if(!found) fail('no clear spot near (' + box.x + ',' + box.y + ') for ' + e.id + ' — move it to open space')
  e.x = placed.x; e.y = placed.y
  occupied.push(placed)
}

// --- the send marker is carried forward bounded the same way the page bounds it: an integer
// count in 0..1e9 and a short timestamp string, so a write-back never re-emits a malformed one ---
// captured before bounding: the rename guard must judge the marker as the board carried it,
// and bounding normalizes a present-but-unparseable marker (string count, ping with no
// numeric n) to absent/null — any truthy marker, parseable or not, means the board was sent
const everSent = Boolean(state.pingCount || state.ping)
const pingN = v => Number.isFinite(v) ? Math.max(0, Math.min(1e9, Math.floor(v))) : null
// derive the count the way the page does — the explicit field, else the marker's n — and never
// write a count the board didn't carry, so an older board keyed only by ping.n keeps its place
const markN = state.ping ? pingN(state.ping.n) : null
const countN = pingN(state.pingCount)
if(countN !== null) state.pingCount = countN
else if(markN !== null) state.pingCount = markN
else delete state.pingCount
state.ping = markN === null ? null
  : {n: markN, at: typeof state.ping.at === 'string' ? state.ping.at.slice(0, 64) : null}

// --- merge: fetched state verbatim, minus retired own elements, plus additions ---
state.els = state.els.filter(e => e && !retire.has(e.id)).concat(additions)

// --- write the page: template + one state line after its <title>, "<" escaped as the page does ---
const esc = s => JSON.stringify(s).replace(/</g, '\\\\u003c')
const line = '<script type="application/json" id="wb-state">' + esc(state) + '</script>'
// The page code comes ONLY from the skill's own template: refuse anything that is not its
// exact two-line head, so a fetched or foreign page can never be laundered into the publish.
// line endings normalized — a CRLF checkout of the template must still match its own head
const tpl = read(tplPath, 'the --template').replace(/\\r\\n/g, '\\n').split('\\n')
if(tpl[0] !== '<title>' + DEFAULT_TITLE + '</title>' || tpl[1] !== '<script>')
  fail('that is not the skill template — pass template.html from the skill directory')
// the only template line the output varies is its <title>: explicit name, else the board's own, else the default
let explicit = arg('title')
if(explicit !== undefined && (/^\\s*--/.test(explicit) || /<topic>/i.test(explicit)))
  fail('--title needs the board\\'s name (e.g. "Ingest pipeline whiteboard"), got ' + JSON.stringify(explicit))
const explicitTitle = titleFrom(explicit)
const title = explicitTitle || carried || DEFAULT_TITLE
if(!explicitTitle && !carried){
  // a sent board is named where the user can see it; with no --title and nothing to carry,
  // writing the default would silently rename it, so refuse unless the board was never
  // sent — judged on the pre-bounding marker (everSent above), never the bounded one
  if(everSent){
    // bounding already ran: only a marker that bounded to a positive send count evidences
    // a send — anything that bounds to zero (unparseable, negative, sub-1 fractional) does not
    const evidenced = (state.pingCount || 0) > 0 || Boolean(state.ping && state.ping.n > 0)
    fail((evidenced
      ? 'this board has been sent but --state carries no <title> to keep'
      : 'this board carries a send marker that could not be read as a send count, so it may have been sent, and --state carries no <title> to keep')
      + ' — pass the saved page (head included) so the board keeps its name, or pass --title')
  }
  process.stderr.write('whiteboard merge: no --title and the board carries no name — using the default title\\n')
}
writeFileSync(outPath, ['<title>' + title + '</title>', line].concat(tpl.slice(1)).join('\\n'))
process.stdout.write('wrote ' + outPath + ' — ' + additions.length + ' added, ' + retire.size + ' retired, ' + state.els.length + ' elements total\\n')
