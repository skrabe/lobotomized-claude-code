<!--
name: 'Skill: Whiteboard HTML Template'
description: >-
  The whiteboard canvas template.html bundled with the whiteboard skill,
  extracted to the skill base directory for Claude to publish and edit as the
  whiteboard artifact.
ccVersion: 2.1.228
-->
<title>Whiteboard</title>
<script>
"use strict";
const CSS = \`
  /* The board's own vars resolve through the vendored @ant/cds token sheet (the static
     style element this page carries — artifacts render self-contained, so the sheet is
     embedded rather than injected). Canvas-read vars (--ground, --grid, --ink, --muted,
     --accent) must land on plain-hex ramp stops: getComputedStyle hands the canvas the
     substituted token TEXT, and ctx.fillStyle cannot evaluate the sheet's hsl(from ...)
     alpha tokens. CSS-only vars (--panel, --shadow) may use any token. Dark mode rides
     the sheet's own data-mode/OS axes (the script mirrors the viewer's data-theme stamp
     onto data-mode), so only board-owned vars need dark overrides here. */
  :root{
    color-scheme: light dark; /* counter the skeleton's :root{color-scheme:light} so UA chrome (scrollbars, caret, overscroll) follows the board's theme */
    --ground:var(--surface-0); --panel:var(--surface-2); --ink:var(--text-primary); --muted:var(--text-secondary);
    --grid:var(--gray-100); --accent:var(--text-accent); --shadow:var(--shadow-md);
    --claude:#c2410c; --sticky:#f4e187; --sticky-ink:#3b3320;
    --claude-sticky:#fdba74; --claude-sticky-ink:#231d0d;
    --ui:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
    --hand:"Segoe Print","Bradley Hand","Marker Felt","Comic Sans MS","Chalkboard SE",cursive;
  }
  /* Dark overrides for the board-owned values only — the CDS semantic tokens the vars
     above point at flip by themselves. Both axes, mirroring the vendored block's own
     structure: the media block's :where() keeps an explicit light stamp winning over
     OS-dark, and the attribute block forces dark on an OS-light machine. */
  @media (prefers-color-scheme: dark){
    :root:where(:not([data-mode="light"])){
      color-scheme: dark;
      --ground:var(--surface-1); /* dark: the board is the lower surface, chrome floats above it */
      --grid:var(--gray-700);
      --claude:#f0a24a; --sticky:#c9b25a; --sticky-ink:#231d0d;
      --claude-sticky:#f0a24a; --claude-sticky-ink:#231d0d;
    }
  }
  :root[data-mode="dark"]{
    color-scheme: dark;
    --ground:var(--surface-1); /* dark: the board is the lower surface, chrome floats above it */
    --grid:var(--gray-700);
    --claude:#f0a24a; --sticky:#c9b25a; --sticky-ink:#231d0d;
    --claude-sticky:#f0a24a; --claude-sticky-ink:#231d0d;
  }
  :root[data-mode="light"]{
    color-scheme: light;
    /* the paper colours restate their light defaults so every theme block carries
       the sticky palette; --ground/--grid need no restating — the :where() guard
       keeps both dark axes inert under a light stamp, so the base values win */
    --claude:#c2410c; --sticky:#f4e187; --sticky-ink:#3b3320;
    --claude-sticky:#fdba74; --claude-sticky-ink:#231d0d;
  }
  *{box-sizing:border-box}
  html,body{height:100%;margin:0}
  body{background:var(--ground);color:var(--ink);font:13px/1.4 var(--ui);overflow:hidden;-webkit-font-smoothing:antialiased}
  #board{position:fixed;inset:0;width:100%;height:100%;touch-action:none;display:block}
  #board.crosshair{cursor:crosshair}
  #board.grab{cursor:grab}
  #board.grabbing{cursor:grabbing}
  #board.move{cursor:move}

  .brand{position:fixed;left:14px;top:12px;max-width:330px;background:var(--panel);border:1.5px solid var(--ink);border-radius:11px 7px 12px 8px;padding:7px 10px 8px;box-shadow:var(--shadow)}
  .brand h1{font-family:var(--hand);font-size:20px;line-height:1;margin:0 0 4px;letter-spacing:.2px}
  .brand p{margin:0;color:var(--muted);font-size:12px;max-width:40ch}
  .brand b{color:var(--ink);font-weight:600}
  .brand .lede{display:block;color:var(--ink);margin-bottom:2px}

  .toolbar{position:fixed;left:14px;top:max(calc(50% + 24px),min(356px,calc(100% - 230px)));transform:translateY(-50%);display:flex;flex-direction:column;gap:4px;background:var(--panel);border:1.5px solid var(--ink);border-radius:11px 7px 12px 8px;padding:6px;box-shadow:var(--shadow)}
  .toolbar .sep{height:1px;background:var(--grid);margin:3px 4px}
  .tb{appearance:none;border:1.5px solid transparent;background:transparent;color:var(--ink);width:38px;height:38px;border-radius:9px 6px 8px 7px;display:grid;place-items:center;cursor:pointer;position:relative}
  .tb:hover{border-color:var(--grid)}
  .tb:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .tb[aria-pressed="true"]{background:var(--ink);color:var(--ground)}
  .tb svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
  .tb .key{position:absolute;right:2px;bottom:1px;font-size:8px;font-family:var(--ui);color:var(--muted);letter-spacing:.3px}
  .tb[aria-pressed="true"] .key{color:var(--ground);opacity:.75}

  .topbar{position:fixed;top:12px;right:14px;display:flex;gap:6px;align-items:center;background:var(--panel);border:1.5px solid var(--ink);border-radius:10px 7px 11px 8px;padding:5px 6px;box-shadow:var(--shadow)}
  .topbar .sep{width:1px;height:20px;background:var(--grid);margin:0 1px}
  @media (max-width: 920px){ .brand p{display:none} }
  @media (max-width: 800px){
    .brand{display:none}
    .topbar{max-width:calc(100% - 28px);flex-wrap:wrap;justify-content:flex-end}
    .topbar .sep{display:none}
  }
  .sizer{display:inline-flex;align-items:center;gap:2px}
  .sizer .zval{min-width:26px;line-height:32px;text-align:center;font-variant-numeric:tabular-nums;color:var(--muted);font-size:12px}
  .sizer .btn{padding:0 6px}
  .btn{appearance:none;border:1.5px solid transparent;background:transparent;color:var(--ink);height:32px;padding:0 10px;border-radius:8px 6px 9px 6px;font:12px var(--ui);cursor:pointer;display:inline-flex;align-items:center;gap:6px}
  .btn:hover{border-color:var(--grid)}
  .btn:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .btn svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
  .btn[aria-pressed="true"]{background:var(--ink);color:var(--ground)}
  .btn.primary{background:var(--fill-accent);color:var(--on-accent);border-color:var(--fill-accent)}
  .btn:disabled{opacity:.4;cursor:default}
  #themeBtn svg{display:none}
  #themeBtn[data-choice="auto"] .t-auto,#themeBtn[data-choice="light"] .t-light,#themeBtn[data-choice="dark"] .t-dark{display:block}

  .zoombar{position:fixed;right:14px;bottom:12px;display:flex;gap:2px;align-items:center;background:var(--panel);border:1.5px solid var(--ink);border-radius:10px 7px 11px 8px;padding:3px;box-shadow:var(--shadow)}
  .zoombar .btn{height:26px;padding:0 8px}
  .zoombar .zval{min-width:44px;line-height:26px;text-align:center;font-variant-numeric:tabular-nums;color:var(--muted);font-size:12px}

  .status{position:fixed;left:16px;right:170px;bottom:14px;color:var(--muted);font-size:12px;pointer-events:none;display:flex;gap:14px;align-items:center} /* right clears the zoombar */
  .status kbd{font:11px/1 var(--ui);border:1px solid var(--grid);border-bottom-width:2px;border-radius:4px;padding:1px 4px;color:var(--ink);background:var(--panel)}
  .sync{display:inline-flex;align-items:center;gap:5px}
  .sync i{width:7px;height:7px;border-radius:50%;background:var(--grid);display:inline-block}
  .sync[data-s="saving"] i{background:var(--accent)}
  .sync[data-s="local"] i{background:var(--sticky)}

  .painter{position:fixed;top:58px;right:22px;display:flex;flex-direction:column;align-items:center;gap:1px;pointer-events:none;color:var(--muted);font-size:11px}
  @media (max-width: 800px){ .painter{top:112px} } /* clear a bar that has wrapped to two rows */
  .painter[hidden]{display:none}
  .painter canvas{width:64px;height:56px;image-rendering:pixelated;animation:hover 2.6s ease-in-out infinite}
  @keyframes hover{50%{transform:translateY(-4px)}}
  @media (prefers-reduced-motion: reduce){ .painter canvas{animation:none} }
  #editor{position:fixed;display:none;resize:none;transform-origin:0 0;background:transparent;color:var(--ink);border:1.5px dashed var(--accent);outline:none;padding:2px 4px;font-family:var(--hand);white-space:pre;overflow:hidden;text-align:center;border-radius:4px}

  .toast{position:fixed;left:50%;bottom:56px;transform:translateX(-50%);background:var(--ink);color:var(--ground);padding:7px 12px;border-radius:8px;font-size:12px;opacity:0;transition:opacity .18s ease;pointer-events:none}
  .toast.show{opacity:1}

  .modal{position:fixed;inset:0;background:rgba(11,11,11,.55);display:none;place-items:center;padding:24px;z-index:10}
  .modal.open{display:grid}
  .modal .card{background:var(--panel);color:var(--ink);border:1.5px solid var(--ink);border-radius:12px 8px 13px 9px;padding:14px;max-width:min(920px,100%);max-height:100%;display:flex;flex-direction:column;gap:10px;box-shadow:var(--shadow)}
  .modal .card header{display:flex;justify-content:space-between;align-items:center;gap:12px}
  .modal .card header h2{margin:0;font-family:var(--hand);font-size:17px;font-weight:normal}
  .modal .card .imgwrap{overflow:auto;border:1px solid var(--grid);border-radius:6px;background:var(--ground)}
  .modal .card img{display:block;max-width:100%;height:auto}
  .modal .card p{margin:0;color:var(--muted);font-size:12px}

  @media (prefers-reduced-motion: reduce){ .toast{transition:none} }
\`;

const MARKUP = \`
<canvas id="board" class="crosshair" aria-label="Whiteboard canvas"></canvas>
<div class="brand">
  <h1>whiteboard</h1>
  <p><span class="lede">Sketch your idea here — Claude reads this board.</span> Draw boxes, arrows, and notes, then hit <b>Send to Claude</b> to hand it over. Orange marks are Claude's — rework them as you like.</p>
</div>
<div class="toolbar" role="toolbar" aria-label="Drawing tools">
  <button class="tb" data-tool="select" aria-pressed="false" title="Select and move (V)"><svg viewBox="0 0 24 24"><path d="M6 3l12 9-5.5 1.5L11 20 6 3z"/></svg><span class="key">V</span></button>
  <div class="sep"></div>
  <button class="tb" data-tool="rect" aria-pressed="true" title="Box / service (R)"><svg viewBox="0 0 24 24"><path d="M4 6.5c4-.6 10-.4 16 0v11c-5.5.5-11 .4-16 0z"/></svg><span class="key">R</span></button>
  <button class="tb" data-tool="ellipse" aria-pressed="false" title="Ellipse (O)"><svg viewBox="0 0 24 24"><ellipse cx="12" cy="12" rx="8" ry="6"/></svg><span class="key">O</span></button>
  <button class="tb" data-tool="cylinder" aria-pressed="false" title="Database (D)"><svg viewBox="0 0 24 24"><path d="M5 7c0-2 14-2 14 0v10c0 2-14 2-14 0z"/><path d="M5 7c0 2 14 2 14 0"/></svg><span class="key">D</span></button>
  <button class="tb" data-tool="diamond" aria-pressed="false" title="Decision (Y)"><svg viewBox="0 0 24 24"><path d="M12 4l8 8-8 8-8-8z"/></svg><span class="key">Y</span></button>
  <button class="tb" data-tool="sticky" aria-pressed="false" title="Sticky note (S)"><svg viewBox="0 0 24 24"><path d="M5 5h14v10l-4 4H5z"/><path d="M15 19v-4h4"/></svg><span class="key">S</span></button>
  <div class="sep"></div>
  <button class="tb" data-tool="arrow" aria-pressed="false" title="Arrow / connection (A)"><svg viewBox="0 0 24 24"><path d="M5 19L19 5"/><path d="M11 5h8v8"/></svg><span class="key">A</span></button>
  <button class="tb" data-tool="line" aria-pressed="false" title="Line (L)"><svg viewBox="0 0 24 24"><path d="M5 19L19 5"/></svg><span class="key">L</span></button>
  <button class="tb" data-tool="pen" aria-pressed="false" title="Freehand (P)"><svg viewBox="0 0 24 24"><path d="M4 17c3-6 5 3 8-2s4 4 8-2"/></svg><span class="key">P</span></button>
  <button class="tb" data-tool="text" aria-pressed="false" title="Text (T)"><svg viewBox="0 0 24 24"><path d="M5 7V5h14v2"/><path d="M12 5v14"/><path d="M9 19h6"/></svg><span class="key">T</span></button>
</div>
<div class="topbar" role="group" aria-label="Board actions">
  <button class="btn" id="themeBtn" data-choice="auto" title="Theme"><svg class="t-auto" viewBox="0 0 24 24"><circle cx="12" cy="12" r="7.5"/><path d="M12 4.5a7.5 7.5 0 0 1 0 15z" fill="currentColor"/></svg><svg class="t-light" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M5.6 18.4l1.8-1.8M16.6 7.4l1.8-1.8"/></svg><svg class="t-dark" viewBox="0 0 24 24"><path d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5z"/></svg></button>
  <div class="sep"></div>
  <button class="btn" id="undoBtn" title="Undo (Ctrl+Z)" disabled><svg viewBox="0 0 24 24"><path d="M9 5L5 9l4 4"/><path d="M5 9h9a5 5 0 0 1 0 10h-2"/></svg></button>
  <button class="btn" id="redoBtn" title="Redo (Ctrl+Shift+Z)" disabled><svg viewBox="0 0 24 24"><path d="M15 5l4 4-4 4"/><path d="M19 9h-9a5 5 0 0 0 0 10h2"/></svg></button>
  <div class="sep"></div>
  <div class="sizer" id="sizer" title="Text size">
    <button class="btn" id="sizeDown" title="Smaller text ([)">−</button>
    <span class="zval" id="sizeVal">17</span>
    <button class="btn" id="sizeUp" title="Larger text (])">+</button>
  </div>
  <div class="sep"></div>
  <button class="btn" id="snapBtn" aria-pressed="true" title="Snap to grid">Snap</button>
  <button class="btn" id="clearBtn" title="Clear the board">Clear</button>
  <button class="btn" id="exportBtn" title="Save an image of the board"><svg viewBox="0 0 24 24"><path d="M12 4v11"/><path d="M8 11l4 4 4-4"/><path d="M5 19h14"/></svg>Image</button>
  <button class="btn" id="submitBtn" title="Save this board to the shared artifact — doesn&#39;t ask Claude">Submit</button>
  <button class="btn primary" id="pingBtn" title="Republish the board and flag it for listening Claude sessions"><svg viewBox="0 0 24 24"><path d="M4 20l16-8L4 4l3 8z"/><path d="M7 12h13"/></svg>Send to Claude</button>
</div>
<div class="zoombar">
  <button class="btn" id="zoomOut" title="Zoom out">−</button>
  <span class="zval" id="zoomVal">100%</span>
  <button class="btn" id="zoomIn" title="Zoom in">+</button>
  <button class="btn" id="zoomFit" title="Fit everything in view">Fit</button>
</div>
<div class="status">
  <span class="sync" id="sync" data-s="idle"><i></i><span id="syncText">saved</span></span>
  <span>Drag to draw · double-click to label · <kbd>V</kbd> select · box-drag or <kbd>shift</kbd>+click to multi-select · <kbd>A</kbd> arrow · <kbd>[</kbd><kbd>]</kbd> text size · <kbd>space</kbd>-drag to pan · <kbd>ctrl</kbd>+scroll to zoom</span>
</div>
<div class="painter" id="painter" hidden aria-live="polite">
  <canvas id="clawd" width="16" height="14" aria-hidden="true"></canvas>
  <span>Claude is drawing back…</span>
</div>
<textarea id="editor" spellcheck="false" aria-label="Label editor"></textarea>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<div class="modal" id="exportModal" role="dialog" aria-modal="true" aria-labelledby="exportTitle">
  <div class="card">
    <header>
      <h2 id="exportTitle">Board image</h2>
      <button class="btn" id="closeExport">Close</button>
    </header>
    <div class="imgwrap"><img id="exportImg" alt="Rendered whiteboard"></div>
    <p>This view can't hand the file over directly — right-click the image to save or copy it.</p>
  </div>
</div>
\`;

// escape every "<" so nothing a viewer types can close the JSON block or open a tag
function esc(s){ return JSON.stringify(s).replace(/</g, '\\\\u003c'); }
// the board keeps the name it was published with; re-escape the decoded title for the head
// (element content only — this does not escape single quotes, so never use it in attributes)
function escHtml(s){ return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
// The vendored CDS token sheet rides the page as a static style element (it contains
// backticks, so it cannot live inside the CSS template literal). Reading it back off the
// DOM is what lets buildPage re-emit it on every republish.
function cdsTokenCss(){
  const el = document.getElementById('cds-tokens');
  return (el && el.textContent) || '';
}
// Publish gate for the captured sheet: buildPage re-emits it raw, so an empty capture
// (sheet loss would bake into every later generation) or a "</" (would terminate the
// style element and truncate the republished page) must refuse the publish.
function tokenCssPublishable(tokenCss){
  // U+FFFD is the remaining parser-divergence signal: a NUL in the served bytes
  // reaches the DOM capture as U+FFFD (RAWTEXT tokenization replaces it), which
  // would fork the captured block from the drift-gated template bytes forever.
  // The END-marker check refuses a tail-truncated capture (a cut-off transfer
  // still boots, and its Send would bake the truncation into every generation).
  return !!tokenCss && tokenCss.indexOf('</') === -1 && tokenCss.indexOf('\\uFFFD') === -1
    && tokenCss.indexOf('===== END vendored @ant/cds tokens =====') !== -1;
}
// Pure serializer — no DOM, no closure state — so the republish round-trip (the token
// block must survive publish → reload → publish byte-identically) is testable headless.
// The JSON block comes first so a reading session finds the board state without running JS.
// Every top-level function must appear in the emission list below — one left out survives
// generation 1 and breaks only when the republished page itself republishes.
// Parse-safety: the state-block HTML comment emitted below is the page's only
// comment-open/close pair, and it must close before either script-opener literal
// that follows — a comment-open left unclosed ahead of a script-opener puts the
// WHATWG script-data tokenizer into double-escaped state, where the real end tag
// stops terminating the element and browsers swallow the rest of the page into
// the script. Never introduce comment-open bytes into any serialized function
// (including JS comments — toString() emits them); whiteboardTokens.test.ts pins
// this with a three-state tokenizer scan against the indexOf terminator.
function buildPage(state, title, tokenCss){
  // The state block stays ahead of the ~26KB sheet and the code script so a
  // reading session's head-slice fetch still captures it whole; the sheet only
  // has to parse before boot() reads colors, which scheduleBoot guarantees.
  return '<!doctype html><html><head><meta charset="utf-8">'
    + '<title>' + escHtml(title) + '</title></head><body>'
    + '<!-- whiteboard state (boxes, labels, arrows, ping marker) is the JSON block below -->'
    + '<script type="application/json" id="wb-state">' + esc(state) + '<\\/script>'
    + '<style id="cds-tokens">' + tokenCss + '</style>'
    + '<script>"use strict";const CSS=' + esc(CSS) + ';const MARKUP=' + esc(MARKUP) + ';'
    + esc.toString() + ';' + escHtml.toString() + ';' + cdsTokenCss.toString() + ';'
    + tokenCssPublishable.toString() + ';'
    + buildPage.toString() + ';' + themeMirror.toString() + ';' + scheduleBoot.toString() + ';'
    + main.toString() + ';' + boot.toString() + ';themeMirror();scheduleBoot();'
    + '<\\/script></body></html>';
}
// The viewer toggle stamps data-theme on the root element; the vendored CDS token block
// keys its toggle axis on data-mode (the CDS convention) and cannot be edited
// (provenance-tested byte-identical). Mirroring the attribute lets that block serve the
// viewer toggle with its own precedence rules — toggle beats OS in both directions.
function themeMirror(){
  const root = document.documentElement;
  const sync = () => {
    const t = root.getAttribute('data-theme');
    if(t) root.setAttribute('data-mode', t);
    else root.removeAttribute('data-mode');
  };
  sync();
  if(typeof MutationObserver !== 'undefined'){
    new MutationObserver(sync).observe(root, {attributes: true, attributeFilter: ['data-theme']});
  }
}
// The token style element sits after this script in the template, so boot must wait for
// the parser to reach it: the canvas reads its colors off the sheet at startup, and an
// immediate boot would read them before the sheet exists.
function scheduleBoot(){
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
}

function main(){
  // ---------- state ----------
  const GRID = 20;
  const CLICK_PX = 4; // a press that travels fewer screen px than this is a click, not a drag
  const board = document.getElementById('board');
  const ctx = board.getContext('2d');
  const editor = document.getElementById('editor');
  // the board rides inside the page as a JSON block so a session reading the artifact can lift
  // the boxes, labels and connections straight out without a browser
  let embedded = null, embeddedAt = 0, pingCount = 0, lastPing = null;
  try{
    const stateEl = document.getElementById('wb-state');
    const raw = stateEl ? JSON.parse(stateEl.textContent) : (window.__WB_STATE__ || null);
    const data = Array.isArray(raw) ? {els: raw} : (raw || null);
    if(data && Array.isArray(data.els)) embedded = data.els;
    if(data && typeof data.savedAt === 'number') embeddedAt = data.savedAt;
    // pingCount is carried on every version so ping.n stays monotonic across sends
    // the send marker rides in viewer-writable state like every other field here, so bound it
    // the way sanitize() bounds the rest: an integer count and a short timestamp string
    const pingN = v => Number.isFinite(v) ? Math.max(0, Math.min(1e9, Math.floor(v))) : null;
    if(data && pingN(data.pingCount) !== null) pingCount = pingN(data.pingCount);
    else if(data && data.ping && pingN(data.ping.n) !== null) pingCount = pingN(data.ping.n);
    if(data && data.ping && pingN(data.ping.n) !== null)
      lastPing = {n: pingN(data.ping.n), at: typeof data.ping.at === 'string' ? data.ping.at.slice(0, 64) : null};
  }catch(_){}

  let els = [];
  let selected = new Set(); // ids of every selected element
  let tool = 'rect';
  let snap = true;
  let view = {x: 0, y: 0, scale: 1};
  let undoStack = [], redoStack = [];
  let drag = null;
  let editing = null;
  let editAnchor = null, editScale = 1; // world-space origin + layout scale of the open editor
  let spaceHeld = false;
  let dpr = Math.max(1, window.devicePixelRatio || 1);
  let C = {};

  const uid = () => Math.random().toString(36).slice(2, 9);
  const clone = o => JSON.parse(JSON.stringify(o));
  const byClaude = e => e && (e.author === 'claude' || e.by === 'claude');
  // Claude's notes sit on orange paper, the user's on yellow; each paper carries its own readable ink
  const stickyPaper = e => byClaude(e) ? {fill: C.claudeSticky, ink: C.claudeStickyInk} : {fill: C.sticky, ink: C.stickyInk};
  // the one selected element, or null when the selection is empty or holds several
  const selOne = () => selected.size === 1 ? els.find(e => selected.has(e.id)) || null : null;

  // ---------- theme ----------
  function readTheme(){
    const cs = getComputedStyle(document.documentElement);
    const v = n => cs.getPropertyValue(n).trim();
    C = {ground: v('--ground'), grid: v('--grid'), ink: v('--ink'), muted: v('--muted'),
         accent: v('--accent'), claude: v('--claude'), sticky: v('--sticky'), stickyInk: v('--sticky-ink'),
         claudeSticky: v('--claude-sticky'), claudeStickyInk: v('--claude-sticky-ink'),
         hand: v('--hand'), ui: v('--ui')};
  }
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { readTheme(); render(); });
  new MutationObserver(() => { readTheme(); render(); syncThemeBtn(); })
    .observe(document.documentElement, {attributes: true, attributeFilter: ['data-theme']});

  // The root's data-theme stamp is the single source of truth: absent = follow the OS. The
  // button reads and cycles that stamp; localStorage only carries the choice across reloads.
  const THEME_KEY = 'wb-theme';
  const rootTheme = () => {
    const t = document.documentElement.getAttribute('data-theme');
    return t === 'light' || t === 'dark' ? t : 'auto';
  };
  function setTheme(t){
    if(t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t);
    else document.documentElement.removeAttribute('data-theme');
    try{ t === 'auto' ? localStorage.removeItem(THEME_KEY) : localStorage.setItem(THEME_KEY, t); }catch(_){}
  }
  const THEME_NEXT = {auto: 'light', light: 'dark', dark: 'auto'};
  const THEME_TITLE = {auto: 'Theme: follows your system — click for light', light: 'Theme: light — click for dark', dark: 'Theme: dark — click to follow your system'};
  function syncThemeBtn(){
    const b = document.getElementById('themeBtn'); if(!b) return;
    const t = rootTheme();
    b.title = THEME_TITLE[t]; b.setAttribute('aria-label', THEME_TITLE[t]); b.dataset.choice = t;
  }
  // a saved choice never overrides a stamp the host already set on the root
  const applyStoredTheme = () => {
    if(document.documentElement.hasAttribute('data-theme')) return;
    try{ const t = localStorage.getItem(THEME_KEY); if(t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t); }catch(_){}
  };

  // ---------- persistence & self-publish ----------
  // Ordinary edits stay on this device (localStorage). The shared artifact only gets republished
  // when the viewer hits "Send to Claude", which bakes the board in and stamps a ping marker;
  // that reload is deliberate, and pan/zoom, tool, selection and undo ride across it in
  // sessionStorage. Multiplayer merging waits for CRDTs.
  const KEY = 'wb-v0', SESSION = 'wb-session';
  const selfCap = () => (window.claude && window.claude.self) || null;
  // One-way send marker: first-party template code posts the capability envelope
  // itself (no runtime-API surface grows for it); the shell relays allowlisted
  // names to the server-side count and everything else drops silently.
  // The name must also exist in the shell broker's and the control
  // plane's page-event allowlists, or the relay drops it.
  const noteSend = () => {
    try { parent.postMessage({__frame_cap: true, cap: 'analytics', id: 'wb-send-' + Date.now(), method: 'track', args: ['frame_whiteboard_send']}, '*'); } catch (e) {}
  };
  let readOnly = false, inflight = false, unsent = false, blockedChip = '';
  const pingBtn = document.getElementById('pingBtn'), submitBtn = document.getElementById('submitBtn');
  const sync = document.getElementById('sync'), syncText = document.getElementById('syncText');
  function setSync(s, txt){ sync.dataset.s = s; syncText.textContent = txt; }

  function saveLocal(){
    try{ localStorage.setItem(KEY, JSON.stringify({els, view, at: Date.now(), unsent})); }catch(_){}
  }
  // whatever wrote the block (a viewer, or a session republishing), normalize it into shapes the
  // renderer expects: known types, finite numbers, plain strings — nothing here reaches the DOM as HTML
  function sanitize(list){
    const num = v => Number.isFinite(v) ? v : 0;
    const str = v => (typeof v === 'string' ? v : '').slice(0, 2000);
    const size = v => Number.isFinite(v) ? Math.max(8, Math.min(64, v)) : undefined;
    const out = [], seen = new Set(); // ids are unique on the board; a repeated id keeps its first kept element
    for(const e of Array.isArray(list) ? list.slice(0, 2000) : []){
      if(!e || typeof e !== 'object' || typeof e.id !== 'string') continue;
      const id = e.id.slice(0, 40);
      if(seen.has(id)) continue;
      const n = out.length, t = e.type, base = {id, type: t, seed: num(e.seed) || 1};
      if(e.author === 'claude' || e.by === 'claude') base.author = 'claude';
      if(['rect','ellipse','cylinder','diamond','sticky'].includes(t)){
        // a shape is stored by its top-left corner with a non-negative size
        const x = num(e.x), y = num(e.y), w = num(e.w), h = num(e.h);
        out.push(Object.assign(base, {x: w < 0 ? num(x + w) : x, y: h < 0 ? num(y + h) : y, w: Math.abs(w), h: Math.abs(h), label: str(e.label)}));
      } else if(t === 'text'){
        const te = {x: num(e.x), y: num(e.y), text: str(e.text)};
        const sz = size(e.size);
        if(sz) te.size = sz;
        out.push(Object.assign(base, te));
      } else if(t === 'arrow' || t === 'line'){
        out.push(Object.assign(base, {x1: num(e.x1), y1: num(e.y1), x2: num(e.x2), y2: num(e.y2),
          label: str(e.label), fromId: typeof e.fromId === 'string' ? e.fromId : null, toId: typeof e.toId === 'string' ? e.toId : null}));
      } else if(t === 'pen'){
        const pts = (Array.isArray(e.pts) ? e.pts : []).slice(0, 4000)
          .filter(p => Array.isArray(p) && Number.isFinite(p[0]) && Number.isFinite(p[1])).map(p => [p[0], p[1]]);
        if(pts.length) out.push(Object.assign(base, {pts}));
      }
      if(out.length > n) seen.add(id);
    }
    // a binding only points at a connectable element on the board, so following one never recurses
    const targets = new Set(out.filter(isConnectable).map(x => x.id));
    for(const a of out){
      if(a.type !== 'arrow' && a.type !== 'line') continue;
      if(!targets.has(a.fromId)) a.fromId = null;
      if(!targets.has(a.toId)) a.toId = null;
    }
    return out;
  }
  function loadState(){
    // Union the newer copy with the older one by id: your unsent sketching and Claude's orange
    // additions both survive, whichever side saved last. (Deletes can reappear — fine for v0.)
    let local = null;
    try{ const raw = localStorage.getItem(KEY); if(raw) local = JSON.parse(raw); }catch(_){}
    const localEls = local && Array.isArray(local.els) ? local.els : null;
    if(localEls && embedded){
      // Claude's marks only ever enter through the published version, so it is authoritative for
      // them: a Claude-authored element missing from the embedded set was retired by Claude
      // (an answered question) and must not be resurrected from an older local copy.
      const claudeLive = new Set(embedded.filter(byClaude).map(e => e.id));
      const localKept = localEls.filter(e => !byClaude(e) || claudeLive.has(e.id));
      const localNewer = local.at > embeddedAt;
      const primary = localNewer ? localKept : clone(embedded), secondary = localNewer ? embedded : localKept;
      const seen = new Set(primary.map(e => e.id));
      els = primary.concat(clone(secondary.filter(e => !seen.has(e.id))));
      if(localNewer && local.view && typeof local.view.scale === 'number') view = local.view;
      unsent = !!local.unsent;
    } else if(localEls){
      els = localEls;
      if(local.view && typeof local.view.scale === 'number') view = local.view;
      unsent = !!local.unsent;
    } else if(embedded){
      els = clone(embedded);
    }
    els = sanitize(els);
  }
  function saveSession(){
    try{ sessionStorage.setItem(SESSION, JSON.stringify({view, undoStack, redoStack, tool, snap, selectedIds: [...selected], textSize})); }catch(_){}
  }
  function loadSession(){
    try{
      const raw = sessionStorage.getItem(SESSION);
      if(!raw) return;
      const d = JSON.parse(raw);
      if(d.view && typeof d.view.scale === 'number') view = d.view;
      if(Array.isArray(d.undoStack)) undoStack = d.undoStack;
      if(Array.isArray(d.redoStack)) redoStack = d.redoStack;
      if(typeof d.tool === 'string') tool = d.tool;
      if(typeof d.snap === 'boolean') snap = d.snap;
      selected = new Set(sessionSelectedIds(d));
      if(Number.isFinite(d.textSize)) textSize = Math.max(8, Math.min(64, d.textSize));
    }catch(_){}
  }
  // the session's selection, bounded like every other stored field; reads the single-id form
  // an older page wrote as well as the id list this one writes
  function sessionSelectedIds(d){
    if(d && Array.isArray(d.selectedIds)) return d.selectedIds.filter(x => typeof x === 'string').slice(0, 500);
    if(d && typeof d.selectedId === 'string') return [d.selectedId];
    return [];
  }
  // drop selected ids whose element is gone (an undo, merge or reload replaced the board)
  function pruneSelection(){
    if(!selected.size) return;
    const live = new Set(els.map(e => e.id));
    for(const id of [...selected]) if(!live.has(id)) selected.delete(id);
  }
  function goLocal(){ readOnly = true; saveLocal(); syncStatus(); }
  function syncStatus(){
    if(inflight){ setSync('saving', 'saving to the shared board…'); return; }
    if(blockedChip){ setSync('local', blockedChip); return; } // the reason stays visible while Send is off
    if(unsent) setSync('local', readOnly ? 'saved on this device' : 'saved here · not shared yet');
    else setSync('idle', 'saved · shared board is up to date');
  }
  // the runtime can attach window.claude a beat after this script (script-order skew), so give
  // it a few seconds before concluding the permissions module is absent
  async function runtimeReady(){
    for(let i = 0; i < 20 && !(window.claude && window.claude.permissions); i++)
      await new Promise(r => setTimeout(r, 250));
  }
  // verdicts that never change for this view: a live module's answers and publish() refusals;
  // lifecycle codes (capability_disabled / _removed: a stale or re-booted runtime) stay transient
  const PERMANENT = ['denied', 'unavailable', 'consent_required', 'not_writer', 'not_granted', 'not_declared'];
  // only a live module's resolved answer is a verdict; an absent module, a rejection, or a
  // transient code is 'unknown', which leaves Send live for publish() to judge
  async function sendAccess(){
    const perms = window.claude && window.claude.permissions;
    if(!perms) return 'unknown';
    let s;
    try{ s = await perms.state('self'); }
    catch(_){ return 'unknown'; }
    return (s === 'granted' || s === 'prompt' || PERMANENT.indexOf(s) !== -1) ? s : 'unknown';
  }
  // 'denied' / 'consent_required' are the viewer's own choice; not_granted / not_declared mean the
  // board itself lacks send access; the rest can't be fixed from here, so copy stays ownership-neutral.
  function blockedMessage(state){
    if(state === 'no_runtime') return 'This view only saves on this device. Send to Claude needs the shared artifact runtime.';
    if(state === 'denied' || state === 'consent_required') return 'Sending is off for this visit. Your sketch saves on this device.';
    if(state === 'not_writer') return 'You can view this board but not send it. It belongs to someone else.';
    if(state === 'not_granted' || state === 'not_declared')
      return 'Send to Claude isn\\'t available on this board. Your sketch still saves on this device. Ask Claude to republish the board to reconnect it.';
    return 'Send to Claude isn\\'t available in this view. Your sketch still saves on this device.';
  }
  function disableSend(state){
    pingBtn.disabled = submitBtn.disabled = true;
    pingBtn.title = submitBtn.title = blockedMessage(state);
    blockedChip = (state === 'denied' || state === 'consent_required')
      ? 'Sharing is off this visit · saved on this device'
      : 'Sharing is unavailable here · saved on this device';
    if(window.console && console.warn) console.warn('whiteboard send blocked', state);
    goLocal();
    toast(pingBtn.title, 7000);
  }
  async function ensureGrant(){
    let s = await sendAccess();
    if(s === 'prompt'){
      try{ const r = await window.claude.permissions.request(['self']); s = (r && r.self) || 'unknown'; }
      catch(err){ s = (err && err.code) || 'unknown'; }
      if(s !== 'granted' && PERMANENT.indexOf(s) === -1) s = 'unknown';
    }
    return s;
  }
  // settle the button once at load: an authoritative verdict disables Send up front, while
  // 'granted', 'prompt' (asked inside the click gesture), and 'unknown' leave it live
  async function primeSend(){
    await runtimeReady();
    const s = await sendAccess();
    if(PERMANENT.indexOf(s) !== -1) disableSend(s);
  }
  // every edit lands on this device; nothing leaves the browser until Submit or Send to Claude
  function persist(){ unsent = true; saveLocal(); saveSession(); syncStatus(); }
  // Submit and Send both republish the shared artifact; only Send stamps the ping marker that
  // flags the board for this session (and puts up the waiting-for-Claude painter)
  async function publishBoard(toClaude){
    if(inflight) return;
    if(readOnly){ toast(pingBtn.title || 'This view can\\'t write to the shared artifact, so it can\\'t save there.', 7000); return; }
    if(!els.length){ toast('The board is empty — sketch something first.'); return; }
    if(editing) commitEdit();
    inflight = true; pingBtn.disabled = submitBtn.disabled = true; syncStatus(); saveSession();
    const grant = await ensureGrant();
    // ensureGrant answers 'granted', 'unknown', or a PERMANENT verdict; 'unknown' leaves the
    // call to publish(), which needs the shared artifact runtime to exist at all
    if(grant !== 'granted' && grant !== 'unknown'){ settle(); disableSend(grant); return; }
    if(!selfCap()){ settle(); syncStatus(); toast(blockedMessage('no_runtime'), 7000); return; }
    const tokenCss = cdsTokenCss();
    if(!tokenCssPublishable(tokenCss)){
      // publishing without the sheet would bake the loss into every later generation
      settle(); syncStatus();
      toast('This view lost its design tokens — reload the board, then try again.');
      return;
    }
    const ping = toClaude ? {n: pingCount + 1, at: new Date().toISOString()} : null;
    // a save carries the last send's marker forward so an unanswered ping is never erased by a Submit
    const state = {v: 1, els: els, savedAt: Date.now(), pingCount: ping ? ping.n : pingCount, ping: ping || lastPing};
    // remember which of Claude's marks we've already seen so the reply can be spotted after reload
    if(toClaude) rememberWaiting();
    selfCap().publish(buildPage(state, document.title || 'Whiteboard', tokenCss)).then(() => {
      settle(); unsent = false; saveLocal();
      // the send count rides a one-way analytics envelope, not the publish API; a shell that predates it drops the message
      if(toClaude) noteSend();
      setSync('idle', toClaude ? 'sent to Claude' : 'saved to the shared board'); // the shell reloads this view to the new version
      if(toClaude){ lastPing = ping; pingCount = ping.n; showPainter(true); }
    }).catch(err => {
      if(toClaude) clearWaiting();
      settle();
      const code = (err && err.code) || 'upstream_error';
      if(window.console && console.warn) console.warn('whiteboard publish rejected', code, err && err.message);
      if(code === 'conflict'){ return; } // a newer version won and this view reloads to it
      if(PERMANENT.indexOf(code) !== -1){ disableSend(code); return; }
      if(code === 'rate_limited'){ syncStatus(); toast('Saving too fast — give it a few seconds and try again.'); return; }
      syncStatus(); toast('Couldn\\'t save to the shared board. The board is still saved here. Try again in a moment. (error: ' + code + ')');
    });
  }
  function settle(){ inflight = false; if(!readOnly) pingBtn.disabled = submitBtn.disabled = false; }
  const sendToClaude = () => publishBoard(true);
  const submitBoard = () => publishBoard(false);

  // ---------- waiting for Claude to draw back ----------
  // After a send the corner shows Clawd painting until a version carrying new Claude-authored
  // elements lands (the shell reloads this view to it), or the wait quietly times out.
  const WAIT = 'wb-waiting', WAIT_TIMEOUT_MS = 15 * 60 * 1000;
  const painterEl = document.getElementById('painter');
  const claudeIds = () => els.filter(byClaude).map(e => e.id);
  function rememberWaiting(){
    try{ sessionStorage.setItem(WAIT, JSON.stringify({since: Date.now(), known: claudeIds()})); }catch(_){}
  }
  function clearWaiting(){ try{ sessionStorage.removeItem(WAIT); }catch(_){} showPainter(false); }
  let paintTimer = null, paintFrame = 0;
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function showPainter(on){
    painterEl.hidden = !on;
    clearInterval(paintTimer); paintTimer = null;
    if(on){ drawClawd(0); if(!reduceMotion) paintTimer = setInterval(() => { paintFrame ^= 1; drawClawd(paintFrame); }, 420); }
  }
  function checkWaiting(){
    let w = null;
    try{ const raw = sessionStorage.getItem(WAIT); if(raw) w = JSON.parse(raw); }catch(_){}
    if(!w) return;
    const known = new Set(w.known || []);
    const fresh = claudeIds().filter(id => !known.has(id));
    if(fresh.length){
      clearWaiting();
      toast(fresh.length === 1 ? 'Claude drew back on the board (in orange).' : 'Claude drew back — ' + fresh.length + ' orange marks on the board.');
      return;
    }
    if(Date.now() - (w.since || 0) > WAIT_TIMEOUT_MS){ clearWaiting(); return; }
    showPainter(true);
  }
  // two frames of Clawd waving a paintbrush; the bristles carry the same orange he draws in
  const CLAWD_FRAMES = [[
    '................',
    '................',
    '................',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '..OODOODOO......',
    '..OODOODOO....B.',
    '..OOOOOOOOOHHFB.',
    '..OOOOOOOO....B.',
    '..OOOOOOOO......',
    '...OO..OO......b',
    '...OO..OO.......',
    '................',
    '................'],[
    '..............b.',
    '..............BB',
    '.............B..',
    '..OOOOOOOO..F...',
    '..OOOOOOOO.H....',
    '..OODOODOOH.....',
    '..OODOODOOO.....',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '...OO..OO.......',
    '...OO..OO.......',
    '................',
    '................']];
  function drawClawd(frame){
    const c = document.getElementById('clawd').getContext('2d');
    const PAL = {O: '#D97757', D: '#2A1F1B', H: '#8B5E34', F: '#7D848A', B: C.claude, b: C.claude};
    c.clearRect(0, 0, 16, 14);
    CLAWD_FRAMES[frame % 2].forEach((row, y) => Array.from(row).forEach((ch, x) => {
      if(PAL[ch]){ c.globalAlpha = ch === 'b' ? .55 : 1; c.fillStyle = PAL[ch]; c.fillRect(x, y, 1, 1); }
    }));
    c.globalAlpha = 1;
  }

  // ---------- keep Claude's marks off the rest of the board ----------
  // A writing session can't measure rendered hand-written text, so the page reflows any
  // Claude-authored mark that collides: step it down the grid until it sits in clear space.
  function deconflict(){
    const pad = 8, ignore = t => t === 'arrow' || t === 'line' || t === 'pen';
    const clash = (a, b) => a.x < b.x + b.w + pad && a.x + a.w + pad > b.x && a.y < b.y + b.h + pad && a.y + a.h + pad > b.y;
    els.forEach((e, i) => {
      if(!byClaude(e) || ignore(e.type)) return;
      if(e.type === 'text'){ const m = measureText(e.text, textPx(e)); e.w = m.w; e.h = m.h; }
      for(let tries = 0; tries < 40; tries++){
        const b = bbox(e);
        const hit = els.some((o, j) => j < i && !ignore(o.type) && clash(b, bbox(o)));
        if(!hit) break;
        moveElement(e, clone(e), 0, GRID);
      }
    });
  }

  // ---------- history ----------
  let pending = null;
  function beginChange(){ pending = JSON.stringify(els); }
  function endChange(){
    if(pending == null) return;
    if(pending !== JSON.stringify(els)){
      undoStack.push(pending);
      if(undoStack.length > 150) undoStack.shift();
      redoStack = [];
      persist();
    }
    pending = null;
    updateButtons();
  }
  function mutate(fn){ beginChange(); fn(); endChange(); render(); }
  function undo(){
    if(!undoStack.length) return;
    redoStack.push(JSON.stringify(els));
    els = sanitize(JSON.parse(undoStack.pop()));
    selected.clear(); updateButtons(); render(); persist();
  }
  function redo(){
    if(!redoStack.length) return;
    undoStack.push(JSON.stringify(els));
    els = sanitize(JSON.parse(redoStack.pop()));
    selected.clear(); updateButtons(); render(); persist();
  }
  function updateButtons(){
    document.getElementById('undoBtn').disabled = !undoStack.length;
    document.getElementById('redoBtn').disabled = !redoStack.length;
  }

  // ---------- geometry helpers ----------
  const snapv = v => snap ? Math.round(v / GRID) * GRID : v;
  const screenToWorld = (sx, sy) => ({x: (sx - view.x) / view.scale, y: (sy - view.y) / view.scale});
  const worldToScreen = (x, y) => ({x: x * view.scale + view.x, y: y * view.scale + view.y});

  function normRect(e){ // handle negative w/h from dragging up-left
    const x = e.w < 0 ? e.x + e.w : e.x, y = e.h < 0 ? e.y + e.h : e.y;
    return {x, y, w: Math.abs(e.w), h: Math.abs(e.h)};
  }
  function bbox(e){
    switch(e.type){
      case 'arrow': case 'line': {
        const {p1, p2} = e.type === 'arrow' ? arrowEndpoints(e) : {p1: {x: e.x1, y: e.y1}, p2: {x: e.x2, y: e.y2}};
        return {x: Math.min(p1.x, p2.x), y: Math.min(p1.y, p2.y), w: Math.abs(p1.x - p2.x), h: Math.abs(p1.y - p2.y)};
      }
      case 'pen': {
        let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
        for(const p of e.pts){ x0 = Math.min(x0, p[0]); y0 = Math.min(y0, p[1]); x1 = Math.max(x1, p[0]); y1 = Math.max(y1, p[1]); }
        return {x: x0, y: y0, w: x1 - x0, h: y1 - y0};
      }
      case 'text': return {x: e.x, y: e.y, w: e.w || 80, h: e.h || 24};
      default: return normRect(e);
    }
  }
  const center = e => { const b = bbox(e); return {x: b.x + b.w / 2, y: b.y + b.h / 2}; };
  function boundsOfAll(list = els){
    if(!list.length) return null;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for(const e of list){ const b = bbox(e); x0 = Math.min(x0, b.x); y0 = Math.min(y0, b.y); x1 = Math.max(x1, b.x + b.w); y1 = Math.max(y1, b.y + b.h); }
    return {x: x0, y: y0, w: Math.max(1, x1 - x0), h: Math.max(1, y1 - y0)};
  }
  // rectangles overlap (touching edges counts); either may carry a negative w/h
  function rectsIntersect(a, b){
    const ax0 = Math.min(a.x, a.x + a.w), ax1 = Math.max(a.x, a.x + a.w), ay0 = Math.min(a.y, a.y + a.h), ay1 = Math.max(a.y, a.y + a.h);
    const bx0 = Math.min(b.x, b.x + b.w), bx1 = Math.max(b.x, b.x + b.w), by0 = Math.min(b.y, b.y + b.h), by1 = Math.max(b.y, b.y + b.h);
    return ax0 <= bx1 && ax1 >= bx0 && ay0 <= by1 && ay1 >= by0;
  }
  // the selection a rubber band yields: its base (what was selected, kept with a modifier) XOR the hits
  function resolveMarquee(base, hitIds){
    const out = new Set(base);
    for(const id of hitIds) out.has(id) ? out.delete(id) : out.add(id);
    return out;
  }
  function clipToBox(target, from, shape){ // point on shape's box edge facing \`from\`
    const b = bbox(shape); const cx = b.x + b.w / 2, cy = b.y + b.h / 2;
    const dx = from.x - cx, dy = from.y - cy;
    if(!dx && !dy) return {x: cx, y: cy};
    const hw = b.w / 2 + 6, hh = b.h / 2 + 6;
    let t = Infinity;
    if(dx) t = Math.min(t, hw / Math.abs(dx));
    if(dy) t = Math.min(t, hh / Math.abs(dy));
    if(shape.type === 'ellipse'){
      t = 1 / Math.sqrt((dx*dx)/(hw*hw) + (dy*dy)/(hh*hh));
    }
    return {x: cx + dx * t, y: cy + dy * t};
  }
  function arrowEndpoints(a){
    let p1 = {x: a.x1, y: a.y1}, p2 = {x: a.x2, y: a.y2};
    const f = a.fromId ? els.find(e => e.id === a.fromId) : null;
    const t = a.toId ? els.find(e => e.id === a.toId) : null;
    if(f) p1 = center(f);
    if(t) p2 = center(t);
    if(f) p1 = clipToBox(p1, p2, f);
    if(t) p2 = clipToBox(p2, p1, t);
    return {p1, p2};
  }
  function distToSeg(p, a, b){
    const l2 = (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y);
    if(l2 === 0) return Math.hypot(p.x-a.x, p.y-a.y);
    let t = ((p.x-a.x)*(b.x-a.x) + (p.y-a.y)*(b.y-a.y)) / l2;
    t = Math.max(0, Math.min(1, t));
    return Math.hypot(p.x - (a.x + t*(b.x-a.x)), p.y - (a.y + t*(b.y-a.y)));
  }
  const isShape = e => ['rect','ellipse','cylinder','diamond','sticky'].includes(e.type);
  const isConnectable = e => isShape(e) || e.type === 'text';

  function hit(p, tol = 6 / view.scale){
    for(let i = els.length - 1; i >= 0; i--){
      const e = els[i];
      if(e.type === 'arrow' || e.type === 'line'){
        const {p1, p2} = e.type === 'arrow' ? arrowEndpoints(e) : {p1: {x: e.x1, y: e.y1}, p2: {x: e.x2, y: e.y2}};
        if(distToSeg(p, p1, p2) < tol + 4) return e;
      } else if(e.type === 'pen'){
        for(let j = 1; j < e.pts.length; j++){
          if(distToSeg(p, {x: e.pts[j-1][0], y: e.pts[j-1][1]}, {x: e.pts[j][0], y: e.pts[j][1]}) < tol + 4) return e;
        }
      } else {
        const b = bbox(e);
        if(p.x >= b.x - 2 && p.x <= b.x + b.w + 2 && p.y >= b.y - 2 && p.y <= b.y + b.h + 2) return e;
      }
    }
    return null;
  }
  function shapeAt(p, excludeId){
    for(let i = els.length - 1; i >= 0; i--){
      const e = els[i];
      if(e.id === excludeId || !isConnectable(e)) continue;
      const b = bbox(e);
      if(p.x >= b.x && p.x <= b.x + b.w && p.y >= b.y && p.y <= b.y + b.h) return e;
    }
    return null;
  }
  function handles(e){ // interactive handles for the selected element
    if(!e) return [];
    if(e.type === 'arrow' || e.type === 'line'){
      const {p1, p2} = e.type === 'arrow' ? arrowEndpoints(e) : {p1: {x: e.x1, y: e.y1}, p2: {x: e.x2, y: e.y2}};
      return [{kind: 'p1', x: p1.x, y: p1.y}, {kind: 'p2', x: p2.x, y: p2.y}];
    }
    if(isShape(e)){
      const b = normRect(e), mx = b.x + b.w/2, my = b.y + b.h/2;
      return [ // corners before edges, so a corner wins when a small shape's handles overlap
        {kind: 'resize', corner: 'nw', x: b.x, y: b.y}, {kind: 'resize', corner: 'ne', x: b.x + b.w, y: b.y},
        {kind: 'resize', corner: 'sw', x: b.x, y: b.y + b.h}, {kind: 'resize', corner: 'se', x: b.x + b.w, y: b.y + b.h},
        {kind: 'resize', corner: 'n', x: mx, y: b.y}, {kind: 'resize', corner: 's', x: mx, y: b.y + b.h},
        {kind: 'resize', corner: 'w', x: b.x, y: my}, {kind: 'resize', corner: 'e', x: b.x + b.w, y: my},
      ];
    }
    return [];
  }
  // the grab handle under a world point on the selected element, or null
  function handleAt(p, e){
    if(!e) return null;
    // a small shape's eight zones are capped so they can't tile its interior; arrows and lines
    // keep the full tolerance (their box is often zero-height or zero-width)
    const b = bbox(e);
    const hs = isShape(e) ? Math.min(8 / view.scale, b.w / 6, b.h / 6) : 8 / view.scale;
    for(const h of handles(e)) if(Math.abs(p.x - h.x) < hs && Math.abs(p.y - h.y) < hs) return h;
    return null;
  }
  const RESIZE_CURSOR = {nw: 'nwse-resize', se: 'nwse-resize', ne: 'nesw-resize', sw: 'nesw-resize', n: 'ns-resize', s: 'ns-resize', e: 'ew-resize', w: 'ew-resize'};
  const handleCursor = h => h.kind !== 'resize' ? 'pointer' : RESIZE_CURSOR[h.corner];

  // ---------- sketchy drawing primitives ----------
  function rng(seed){ let s = (seed | 0) || 1; return () => { s = (s * 1664525 + 1013904223) | 0; return ((s >>> 0) / 4294967296); }; }
  const WOB = 1.6;
  function skLine(c, r, x1, y1, x2, y2, passes = 2){
    // bow the stroke in proportion to its length so long edges read as hand-drawn too
    const len = Math.hypot(x2 - x1, y2 - y1), bow = Math.min(9, len * 0.018);
    const nx = len ? -(y2 - y1) / len : 0, ny = len ? (x2 - x1) / len : 0;
    for(let i = 0; i < passes; i++){
      const off = (r() - .5) * 2 * bow;
      const t = .35 + r() * .3;
      const mx = x1 + (x2 - x1) * t + nx * off, my = y1 + (y2 - y1) * t + ny * off;
      c.beginPath();
      c.moveTo(x1 + (r() - .5) * WOB * 2, y1 + (r() - .5) * WOB * 2);
      c.quadraticCurveTo(mx, my, x2 + (r() - .5) * WOB * 2, y2 + (r() - .5) * WOB * 2);
      c.stroke();
    }
  }
  function skRect(c, r, x, y, w, h){
    skLine(c, r, x, y, x + w, y); skLine(c, r, x + w, y, x + w, y + h);
    skLine(c, r, x + w, y + h, x, y + h); skLine(c, r, x, y + h, x, y);
  }
  function skEllipse(c, r, cx, cy, rx, ry, passes = 2){
    for(let p = 0; p < passes; p++){
      c.beginPath();
      const n = 26, off = r() * Math.PI * 2;
      for(let i = 0; i <= n; i++){
        const a = off + (i / n) * Math.PI * 2;
        const jr = 1 + (r() - .5) * .03;
        const x = cx + Math.cos(a) * rx * jr + (r() - .5) * WOB * .6, y = cy + Math.sin(a) * ry * jr + (r() - .5) * WOB * .6;
        if(i === 0) c.moveTo(x, y); else c.lineTo(x, y);
      }
      c.closePath(); c.stroke();
    }
  }
  function skHalfEllipse(c, r, cx, cy, rx, ry){ // bottom half arc
    for(let p = 0; p < 2; p++){
      c.beginPath();
      const n = 14;
      for(let i = 0; i <= n; i++){
        const a = (i / n) * Math.PI;
        const x = cx + Math.cos(a) * rx + (r() - .5) * WOB * .6, y = cy + Math.sin(a) * ry + (r() - .5) * WOB * .6;
        if(i === 0) c.moveTo(x, y); else c.lineTo(x, y);
      }
      c.stroke();
    }
  }

  // ---------- text ----------
  const FONT_SIZE = 17, STICKY_FONT = 15, MIN_FIT = 9;
  const TEXT_SIZES = [12, 14, 17, 20, 24, 32, 40, 48];
  let textSize = FONT_SIZE; // size the next free-text label is placed at
  const textPx = e => (e && e.type === 'text' && Number.isFinite(e.size)) ? e.size : FONT_SIZE;
  function handFont(px){ return px + 'px ' + C.hand; }
  function measureText(txt, px){
    ctx.save(); ctx.font = handFont(px);
    const lines = (txt || '').split('\\n');
    let w = 0; for(const l of lines) w = Math.max(w, ctx.measureText(l).width);
    ctx.restore();
    return {w: Math.ceil(w) + 8, h: Math.ceil(lines.length * px * 1.35) + 6};
  }
  function drawMultiline(c, txt, cx, cy, px, color, align = 'center'){
    if(!txt) return;
    c.save(); c.font = handFont(px); c.fillStyle = color; c.textAlign = align; c.textBaseline = 'middle';
    const lines = txt.split('\\n'), lh = px * 1.35, start = cy - (lines.length - 1) * lh / 2;
    lines.forEach((l, i) => c.fillText(l, cx, start + i * lh));
    c.restore();
  }
  // split a word wider than the box at the longest prefix that fits (binary search, so a long
  // unbroken label never becomes a character-by-character scan)
  function splitWord(c, w, maxW){
    const parts = [];
    while(c.measureText(w).width > maxW && w.length > 1){
      let lo = 1, hi = w.length - 1;
      while(lo < hi){
        const mid = (lo + hi + 1) >> 1;
        if(c.measureText(w.slice(0, mid)).width <= maxW) lo = mid; else hi = mid - 1;
      }
      parts.push(w.slice(0, lo)); w = w.slice(lo);
    }
    parts.push(w);
    return parts;
  }
  // greedy word-wrap of one paragraph to maxW at the canvas's current font
  function wrapPara(c, para, maxW){
    const lines = [];
    let cur = '';
    for(const word of para.split(' ')){
      for(const w of splitWord(c, word, maxW)){
        const test = cur ? cur + ' ' + w : w;
        if(cur && c.measureText(test).width > maxW){ lines.push(cur); cur = w; }
        else cur = test;
      }
    }
    lines.push(cur);
    return lines;
  }
  // the largest font at which the wrapped label fits the box; the floor size if nothing does.
  // Fits are cached per (box, text) so drag/pan redraws don't re-measure every label, and only
  // the first FIT_CHARS of a label are laid out — more than any shape can show at the floor size.
  const fitCache = new Map(), FIT_CHARS = 600;
  function fitText(c, txt, maxW, maxH, maxPx){
    const key = Math.round(maxW) + '|' + Math.round(maxH) + '|' + maxPx + '|' + txt;
    const hit = fitCache.get(key);
    if(hit) return hit;
    let best = null;
    for(let px = maxPx; px >= MIN_FIT; px--){
      c.font = handFont(px);
      // cap by code point so the ellipsis can't land inside a surrogate pair
      const cps = Array.from(String(txt || '')), capped = cps.length > FIT_CHARS ? cps.slice(0, FIT_CHARS).join('') + '\\u2026' : cps.join('');
      const lines = capped.split('\\n').reduce((a, para) => a.concat(wrapPara(c, para, maxW)), []);
      best = {px, lines};
      if(lines.length * px * 1.35 <= maxH) break;
    }
    if(fitCache.size > 500) fitCache.clear();
    fitCache.set(key, best);
    return best;
  }
  // the region of a shape that reads as "inside" it, for label fitting
  function innerBox(e){
    const b = normRect(e), pad = 8;
    switch(e.type){
      case 'ellipse': return {cx: b.x + b.w/2, cy: b.y + b.h/2, w: b.w/Math.SQRT2 - pad, h: b.h/Math.SQRT2 - pad};
      case 'diamond': return {cx: b.x + b.w/2, cy: b.y + b.h/2, w: b.w/2 - pad, h: b.h/2 - pad};
      case 'cylinder': { const ry = Math.min(14, b.h * .18); return {cx: b.x + b.w/2, cy: b.y + b.h/2 + ry/2, w: b.w - 2*pad, h: b.h - ry - 2*pad}; } // below the top rim
      case 'sticky': return {cx: b.x + b.w/2, cy: b.y + b.h/2, w: b.w - 20, h: b.h - 14}; // the note's top-left writing inset
      default: return {cx: b.x + b.w/2, cy: b.y + b.h/2, w: b.w - 2*pad, h: b.h - 2*pad};
    }
  }
  // draw a shape's label shrunk and wrapped to stay inside it, clipped as a last resort
  function drawFitted(c, e, txt, maxPx, color){
    if(!txt) return;
    const ib = innerBox(e);
    const w = Math.max(12, ib.w), h = Math.max(12, ib.h);
    c.save();
    const f = fitText(c, txt, w, h, maxPx);
    c.beginPath(); c.rect(ib.cx - w/2 - 2, ib.cy - h/2 - 2, w + 4, h + 4); c.clip();
    c.font = handFont(f.px); c.fillStyle = color; c.textAlign = 'center'; c.textBaseline = 'middle';
    const lh = f.px * 1.35, start = ib.cy - (f.lines.length - 1) * lh / 2;
    f.lines.forEach((l, i) => c.fillText(l, ib.cx, start + i * lh));
    c.restore();
  }

  // ---------- element rendering ----------
  function drawElement(c, e){
    const r = rng(e.seed);
    const ink = byClaude(e) ? C.claude : C.ink; // Claude's strokes read in orange marker
    const lbl = e === editing ? '' : e.label; // the open editor shows the label being typed, so the canvas doesn't double it
    c.lineWidth = 1.6; c.strokeStyle = ink; c.lineCap = 'round'; c.lineJoin = 'round';
    switch(e.type){
      case 'rect': {
        const b = normRect(e); skRect(c, r, b.x, b.y, b.w, b.h);
        drawFitted(c, e, lbl, FONT_SIZE, ink);
        break;
      }
      case 'ellipse': {
        const b = normRect(e); skEllipse(c, r, b.x + b.w/2, b.y + b.h/2, b.w/2, b.h/2);
        drawFitted(c, e, lbl, FONT_SIZE, ink);
        break;
      }
      case 'cylinder': {
        const b = normRect(e); const ry = Math.min(14, b.h * .18);
        skEllipse(c, r, b.x + b.w/2, b.y + ry, b.w/2, ry);
        skLine(c, r, b.x, b.y + ry, b.x, b.y + b.h - ry);
        skLine(c, r, b.x + b.w, b.y + ry, b.x + b.w, b.y + b.h - ry);
        skHalfEllipse(c, r, b.x + b.w/2, b.y + b.h - ry, b.w/2, ry);
        drawFitted(c, e, lbl, FONT_SIZE, ink);
        break;
      }
      case 'diamond': {
        const b = normRect(e), cx = b.x + b.w/2, cy = b.y + b.h/2;
        skLine(c, r, cx, b.y, b.x + b.w, cy); skLine(c, r, b.x + b.w, cy, cx, b.y + b.h);
        skLine(c, r, cx, b.y + b.h, b.x, cy); skLine(c, r, b.x, cy, cx, b.y);
        drawFitted(c, e, lbl, FONT_SIZE, ink);
        break;
      }
      case 'sticky': {
        const b = normRect(e), paper = stickyPaper(e);
        c.save(); c.fillStyle = paper.fill;
        c.beginPath(); c.moveTo(b.x + 1, b.y + 2); c.lineTo(b.x + b.w - 2, b.y); c.lineTo(b.x + b.w, b.y + b.h - 1); c.lineTo(b.x, b.y + b.h); c.closePath(); c.fill();
        c.restore();
        c.strokeStyle = paper.ink; c.globalAlpha = .45; skRect(c, r, b.x, b.y, b.w, b.h); c.globalAlpha = 1; c.strokeStyle = ink;
        if(lbl){
          c.save();
          const ib = innerBox(e), f = fitText(c, lbl, Math.max(12, ib.w), Math.max(12, ib.h), STICKY_FONT);
          c.beginPath(); c.rect(b.x + 4, b.y + 4, b.w - 8, b.h - 8); c.clip();
          c.font = handFont(f.px); c.fillStyle = paper.ink; c.textBaseline = 'top';
          f.lines.forEach((l, i) => c.fillText(l, b.x + 10, b.y + 9 + i * f.px * 1.35));
          c.restore();
        }
        break;
      }
      case 'text': {
        const px = textPx(e), m = measureText(e.text, px);
        e.w = m.w; e.h = m.h;
        if(e !== editing){
          c.save(); c.font = handFont(px); c.fillStyle = ink; c.textBaseline = 'top';
          (e.text || '').split('\\n').forEach((l, i) => c.fillText(l, e.x + 4, e.y + 4 + i * px * 1.35));
          c.restore();
        }
        break;
      }
      case 'line': {
        skLine(c, r, e.x1, e.y1, e.x2, e.y2);
        break;
      }
      case 'arrow': {
        const {p1, p2} = arrowEndpoints(e);
        skLine(c, r, p1.x, p1.y, p2.x, p2.y);
        const ang = Math.atan2(p2.y - p1.y, p2.x - p1.x), L = 12;
        skLine(c, r, p2.x, p2.y, p2.x - L * Math.cos(ang - .45), p2.y - L * Math.sin(ang - .45), 1);
        skLine(c, r, p2.x, p2.y, p2.x - L * Math.cos(ang + .45), p2.y - L * Math.sin(ang + .45), 1);
        if(lbl){
          const mx = (p1.x + p2.x) / 2, my = (p1.y + p2.y) / 2;
          const m = measureText(lbl, 14);
          c.save(); c.fillStyle = C.ground; c.fillRect(mx - m.w/2, my - m.h/2, m.w, m.h); c.restore();
          drawMultiline(c, lbl, mx, my, 14, ink);
        }
        break;
      }
      case 'pen': {
        if(e.pts.length < 2){
          c.beginPath(); c.fillStyle = ink; c.arc(e.pts[0][0], e.pts[0][1], 1, 0, 7); c.fill();
          break;
        }
        c.beginPath(); c.moveTo(e.pts[0][0], e.pts[0][1]);
        for(let i = 1; i < e.pts.length - 1; i++){
          const x0 = e.pts[i][0], y0 = e.pts[i][1], x1 = e.pts[i+1][0], y1 = e.pts[i+1][1];
          c.quadraticCurveTo(x0, y0, (x0 + x1) / 2, (y0 + y1) / 2);
        }
        const last = e.pts[e.pts.length - 1]; c.lineTo(last[0], last[1]);
        c.stroke();
        break;
      }
    }
  }

  function drawSelection(c){
    if(!selected.size) return;
    const pad = 6 / view.scale;
    c.save();
    c.strokeStyle = C.accent; c.lineWidth = 1 / view.scale; c.setLineDash([5 / view.scale, 4 / view.scale]);
    for(const e of els){
      if(!selected.has(e.id)) continue;
      const b = bbox(e);
      c.strokeRect(b.x - pad, b.y - pad, b.w + pad * 2, b.h + pad * 2);
    }
    c.setLineDash([]);
    const e = selOne(); // handles only apply to a single element
    if(e){
      const b = bbox(e);
      c.fillStyle = C.ground; c.strokeStyle = C.accent; c.lineWidth = 1.5 / view.scale;
      // the drawn handle never exceeds its clickable zone, which is capped on small shapes
      const hs = isShape(e) ? Math.min(5 / view.scale, b.w / 6, b.h / 6) : 5 / view.scale;
      for(const h of handles(e)){
        c.beginPath(); c.rect(h.x - hs, h.y - hs, hs * 2, hs * 2); c.fill(); c.stroke();
      }
    }
    c.restore();
  }

  function drawMarquee(c){
    if(!drag || drag.mode !== 'marquee' || !drag.moved) return;
    const r = marqueeRect();
    c.save();
    c.strokeStyle = C.accent; c.fillStyle = C.accent; c.lineWidth = 1 / view.scale;
    c.setLineDash([4 / view.scale, 3 / view.scale]);
    c.globalAlpha = .08; c.fillRect(r.x, r.y, r.w, r.h);
    c.globalAlpha = 1; c.strokeRect(r.x, r.y, r.w, r.h);
    c.restore();
  }

  function drawGrid(c, w, h){
    const s = view.scale, step = GRID * (s < .5 ? 4 : s < .9 ? 2 : 1);
    const x0 = -view.x / s, y0 = -view.y / s, x1 = x0 + w / s, y1 = y0 + h / s;
    if(step * s < 6) return;
    c.fillStyle = C.grid;
    const r = Math.max(.9, 1.1 / s);
    for(let x = Math.floor(x0 / step) * step; x < x1; x += step){
      for(let y = Math.floor(y0 / step) * step; y < y1; y += step){
        c.fillRect(x - r/2, y - r/2, r, r);
      }
    }
  }

  // ---------- main render ----------
  function render(){
    const w = board.clientWidth, h = board.clientHeight;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);
    ctx.setTransform(dpr * view.scale, 0, 0, dpr * view.scale, dpr * view.x, dpr * view.y);
    drawGrid(ctx, w, h);
    for(const e of els) drawElement(ctx, e);
    drawSelection(ctx);
    drawMarquee(ctx);
    if(!els.length){
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.textAlign = 'center'; ctx.fillStyle = C.muted; ctx.font = handFont(19);
      ctx.fillText('drag anywhere to sketch a box, then add arrows between things', w / 2, h / 2 - 10);
      ctx.font = '12px ' + C.ui; ctx.fillStyle = C.muted;
      ctx.fillText('saves in this browser as you go · Submit shares it · Send to Claude hands it over — Claude answers in orange', w / 2, h / 2 + 18);
      ctx.textAlign = 'start';
    }
    document.getElementById('zoomVal').textContent = Math.round(view.scale * 100) + '%';
    syncEditor();
    updateSizer();
  }

  function resize(){
    dpr = Math.max(1, window.devicePixelRatio || 1);
    board.width = Math.round(board.clientWidth * dpr);
    board.height = Math.round(board.clientHeight * dpr);
    render();
  }
  window.addEventListener('resize', resize);

  // ---------- tools & toolbar ----------
  const toolKeys = {v: 'select', r: 'rect', o: 'ellipse', d: 'cylinder', y: 'diamond', s: 'sticky', a: 'arrow', l: 'line', p: 'pen', t: 'text'};
  function setTool(t){
    tool = t;
    document.querySelectorAll('.tb').forEach(b => b.setAttribute('aria-pressed', b.dataset.tool === t ? 'true' : 'false'));
    board.className = t === 'select' ? '' : 'crosshair';
    board.style.cursor = '';
    saveSession();
  }
  document.querySelectorAll('.tb').forEach(b => b.addEventListener('click', () => setTool(b.dataset.tool)));

  // ---------- pointer interaction ----------
  function evtPoint(ev){
    const r = board.getBoundingClientRect();
    return {sx: ev.clientX - r.left, sy: ev.clientY - r.top};
  }
  board.addEventListener('contextmenu', ev => ev.preventDefault());
  board.addEventListener('dblclick', ev => {
    const {sx, sy} = evtPoint(ev); const p = screenToWorld(sx, sy);
    const e = hit(p);
    if(e && e.type !== 'pen' && e.type !== 'line') startEdit(e);
  });

  board.addEventListener('pointerdown', ev => {
    if(editing) return;
    board.setPointerCapture(ev.pointerId);
    const {sx, sy} = evtPoint(ev); const p = screenToWorld(sx, sy);
    const panIntent = ev.button === 1 || spaceHeld || ev.button === 2;
    if(panIntent){ startPan(sx, sy); return; }
    if(ev.button !== 0) return;

    if(tool === 'select'){
      const toggle = ev.shiftKey || ev.ctrlKey || ev.metaKey; // shift/ctrl/cmd grow or shrink the selection
      const sel = selOne();
      const h = toggle ? null : handleAt(p, sel);
      if(h){
        beginChange();
        drag = {mode: h.kind, id: sel.id, sx, sy, moved: false};
        if(h.kind === 'resize'){
          // the opposite side stays put while this handle follows the pointer; an edge handle moves one axis
          const b = normRect(sel);
          sel.x = b.x; sel.y = b.y; sel.w = b.w; sel.h = b.h;
          drag.ax = h.corner.includes('w') ? b.x + b.w : h.corner.includes('e') ? b.x : null;
          drag.ay = h.corner.includes('n') ? b.y + b.h : h.corner.includes('s') ? b.y : null;
        }
        board.classList.add('move');
        return;
      }
      const e = hit(p);
      if(e && toggle){
        selected.has(e.id) ? selected.delete(e.id) : selected.add(e.id);
        saveSession(); render();
      } else if(e){
        if(!selected.has(e.id)) selected = new Set([e.id]);
        beginChange();
        // every selected element moves by the grabbed one's snapped delta, measured from its
        // starting corner captured once here (a bound arrow's box would shift as its shapes move)
        const b = bbox(e);
        drag = {mode: 'move', id: e.id, offX: p.x - b.x, offY: p.y - b.y, ax0: b.x, ay0: b.y, sx, sy, origs: new Map(), moved: false};
        for(const x of els) if(selected.has(x.id)) drag.origs.set(x.id, clone(x));
        board.classList.add('move');
        saveSession(); render();
      } else if(ev.pointerType === 'touch'){
        selected.clear(); saveSession(); render(); startPan(sx, sy); // no marquee on touch: a drag is the only pan gesture
      } else {
        // empty canvas: a drag rubber-bands a selection (kept and toggled when a modifier is held)
        drag = {mode: 'marquee', start: p, end: p, sx, sy, base: toggle ? new Set(selected) : new Set(), moved: false};
        render();
      }
      return;
    }

    // drawing tools
    selected.clear();
    beginChange();
    const seed = 1 + Math.floor(Math.random() * 1e9);
    if(tool === 'text'){
      // stop the browser's mousedown focus shuffle so the editor keeps focus once it opens
      ev.preventDefault(); pending = null; // history handled when the text commits
      const over = hit(p);
      if(over && over.type !== 'pen' && over.type !== 'line'){ setTimeout(() => startEdit(over), 0); return; }
      const el = {id: uid(), type: 'text', x: snapv(p.x), y: snapv(p.y), text: '', size: textSize, seed};
      els.push(el); render();
      setTimeout(() => startEdit(el, true), 0);
      return;
    }
    const startedOn = hit(p);
    if(tool === 'arrow' || tool === 'line'){
      const el = {id: uid(), type: tool, x1: snapv(p.x), y1: snapv(p.y), x2: snapv(p.x), y2: snapv(p.y), seed, label: '',
                  fromId: tool === 'arrow' ? (shapeAt(p) || {}).id || null : null, toId: null};
      els.push(el); drag = {mode: 'create-line', id: el.id};
    } else if(tool === 'pen'){
      const el = {id: uid(), type: 'pen', pts: [[p.x, p.y]], seed};
      els.push(el); drag = {mode: 'create-pen', id: el.id};
    } else {
      const el = {id: uid(), type: tool, x: snapv(p.x), y: snapv(p.y), w: 0, h: 0, seed, label: ''};
      els.push(el); drag = {mode: 'create-shape', id: el.id, start: p, startedOn: startedOn ? startedOn.id : null};
    }
    render();
  });

  function startPan(sx, sy){
    drag = {mode: 'pan', sx, sy, vx: view.x, vy: view.y};
    board.style.cursor = ''; // the grabbing class carries the pan cursor; a leftover hover cursor would override it
    board.classList.add('grabbing');
  }

  board.addEventListener('pointermove', ev => {
    const {sx, sy} = evtPoint(ev); const p = screenToWorld(sx, sy);
    if(!drag){
      // cursor feedback in select mode: resize arrows over a handle, move over a shape
      if(tool !== 'select' || spaceHeld) return;
      const sel = selOne(), h = handleAt(p, sel);
      const cur = h ? handleCursor(h) : hit(p) ? 'move' : '';
      if(cur !== board.style.cursor) board.style.cursor = cur;
      return;
    }
    const e = drag.id ? els.find(x => x.id === drag.id) : null;
    switch(drag.mode){
      case 'pan':
        view.x = drag.vx + (sx - drag.sx); view.y = drag.vy + (sy - drag.sy); break;
      case 'move': {
        if(!drag.moved && Math.hypot(sx - drag.sx, sy - drag.sy) < CLICK_PX) break;
        drag.moved = true;
        const {dx, dy} = moveDelta(p, drag);
        for(const el of els){ const o = drag.origs.get(el.id); if(o) moveElement(el, o, dx, dy); }
        break;
      }
      case 'marquee': {
        drag.end = p;
        if(!drag.moved && Math.hypot(sx - drag.sx, sy - drag.sy) < CLICK_PX) break;
        drag.moved = true;
        const r = marqueeRect();
        selected = resolveMarquee(drag.base, els.filter(x => rectsIntersect(r, bbox(x))).map(x => x.id));
        break;
      }
      case 'resize': {
        if(!drag.moved && Math.hypot(sx - drag.sx, sy - drag.sy) < CLICK_PX) break;
        drag.moved = true;
        // the dragged side follows the pointer, the anchored side never moves; crossing it flips the box
        if(drag.ax != null){
          let px = snapv(p.x);
          if(Math.abs(px - drag.ax) < 20) px = drag.ax + (px >= drag.ax ? 20 : -20);
          e.x = Math.min(drag.ax, px); e.w = Math.abs(px - drag.ax);
        }
        if(drag.ay != null){
          let py = snapv(p.y);
          if(Math.abs(py - drag.ay) < 20) py = drag.ay + (py >= drag.ay ? 20 : -20);
          e.y = Math.min(drag.ay, py); e.h = Math.abs(py - drag.ay);
        }
        break;
      }
      case 'p1': case 'p2': {
        // a click on an endpoint handle leaves the endpoint and its binding untouched
        if(!drag.moved && Math.hypot(sx - drag.sx, sy - drag.sy) < CLICK_PX) break;
        drag.moved = true;
        const k = drag.mode === 'p1' ? 1 : 2;
        e['x' + k] = snapv(p.x); e['y' + k] = snapv(p.y);
        if(e.type === 'arrow'){
          const over = shapeAt(p, null);
          e[k === 1 ? 'fromId' : 'toId'] = over ? over.id : null;
        }
        break;
      }
      case 'create-shape':
        e.w = snapv(p.x) - e.x; e.h = snapv(p.y) - e.y; break;
      case 'create-line':
        e.x2 = snapv(p.x); e.y2 = snapv(p.y);
        if(e.type === 'arrow'){ const over = shapeAt(p, null); e.toId = over && over.id !== e.fromId ? over.id : null; }
        break;
      case 'create-pen': {
        const last = e.pts[e.pts.length - 1];
        if(Math.hypot(p.x - last[0], p.y - last[1]) > 2 / view.scale) e.pts.push([p.x, p.y]);
        break;
      }
    }
    render();
  });

  board.addEventListener('pointerup', () => finishDrag());
  board.addEventListener('pointercancel', () => finishDrag());

  function marqueeRect(){
    return {x: Math.min(drag.start.x, drag.end.x), y: Math.min(drag.start.y, drag.end.y),
            w: Math.abs(drag.end.x - drag.start.x), h: Math.abs(drag.end.y - drag.start.y)};
  }

  function finishDrag(){
    if(!drag) return;
    const e = drag.id ? els.find(x => x.id === drag.id) : null;
    board.classList.remove('grabbing', 'move');
    if(drag.mode === 'pan'){ saveSession(); drag = null; render(); return; }
    if(drag.mode === 'marquee'){
      if(!drag.moved) selected = drag.base; // a click on empty canvas clears (or, with a modifier, keeps) the selection
      saveSession(); drag = null; render(); return;
    }
    // a click that moved nothing, on one of several selected elements, narrows the selection to it
    if(drag.mode === 'move' && !drag.moved && selected.size > 1) selected = new Set([drag.id]);
    if(drag.mode === 'create-shape'){
      const b = normRect(e);
      if(b.w < 8 && b.h < 8){
        // a plain click: on an existing thing it selects, on empty space it drops a default box
        if(drag.startedOn){ els = els.filter(x => x.id !== e.id); selected = new Set([drag.startedOn]); }
        else { e.x -= 60; e.y -= 30; e.w = 120; e.h = 60; selected = new Set([e.id]); }
      } else { e.x = b.x; e.y = b.y; e.w = Math.max(20, b.w); e.h = Math.max(20, b.h); selected = new Set([e.id]); }
      setTool('select'); // back to the pointer after each shape so the next drag moves rather than draws
    }
    if(drag.mode === 'create-line'){
      if(Math.hypot(e.x2 - e.x1, e.y2 - e.y1) < 6){ els = els.filter(x => x.id !== e.id); }
      else selected = new Set([e.id]);
    }
    endChange();
    drag = null;
    saveSession();
    render();
  }

  // the group-move delta: pointer offset from the grab anchor captured at pointerdown, snapped;
  // never re-measured from the grabbed element, whose box can depend on shapes in motion
  function moveDelta(p, grab){
    return {dx: snapv(p.x - grab.offX) - grab.ax0, dy: snapv(p.y - grab.offY) - grab.ay0};
  }
  function moveElement(e, orig, dx, dy){
    switch(e.type){
      case 'arrow': case 'line':
        e.x1 = orig.x1 + dx; e.y1 = orig.y1 + dy; e.x2 = orig.x2 + dx; e.y2 = orig.y2 + dy; break;
      case 'pen':
        e.pts = orig.pts.map(([x, y]) => [x + dx, y + dy]); break;
      case 'text': e.x = orig.x + dx; e.y = orig.y + dy; break;
      default: { const b = normRect(orig); e.x = b.x + dx; e.y = b.y + dy; e.w = b.w; e.h = b.h; }
    }
  }

  // ---------- wheel: pan / zoom ----------
  board.addEventListener('wheel', ev => {
    ev.preventDefault();
    const {sx, sy} = evtPoint(ev);
    if(ev.ctrlKey || ev.metaKey) zoomAt(sx, sy, Math.exp(-ev.deltaY * 0.01));
    else { view.x -= ev.deltaX; view.y -= ev.deltaY; }
    render(); saveSession();
  }, {passive: false});

  function zoomAt(sx, sy, factor){
    const before = screenToWorld(sx, sy);
    view.scale = Math.min(4, Math.max(0.15, view.scale * factor));
    view.x = sx - before.x * view.scale;
    view.y = sy - before.y * view.scale;
  }
  function zoomFit(){
    const b = boundsOfAll();
    const w = board.clientWidth, h = board.clientHeight;
    if(!b){ view = {x: 0, y: 0, scale: 1}; render(); saveSession(); return; }
    const pad = 80;
    const s = Math.min(2, Math.min((w - pad*2) / b.w, (h - pad*2) / b.h));
    view.scale = Math.max(0.15, s);
    view.x = (w - b.w * view.scale) / 2 - b.x * view.scale;
    view.y = (h - b.h * view.scale) / 2 - b.y * view.scale;
    render(); saveSession();
  }
  document.getElementById('zoomIn').onclick = () => { zoomAt(board.clientWidth/2, board.clientHeight/2, 1.25); render(); saveSession(); };
  document.getElementById('zoomOut').onclick = () => { zoomAt(board.clientWidth/2, board.clientHeight/2, 0.8); render(); saveSession(); };
  document.getElementById('zoomFit').onclick = zoomFit;

  // ---------- label editing ----------
  function startEdit(e, fresh = false){
    if(editing && editing !== e) commitEdit();
    editing = e; selected = new Set([e.id]); editAnchor = null; render();
    const isSticky = e.type === 'sticky', isText = e.type === 'text', isArrow = e.type === 'arrow';
    const px = (isSticky ? STICKY_FONT : isArrow ? 14 : isText ? textPx(e) : FONT_SIZE) * view.scale;
    const tw = isText ? measureText(e.text || '', textPx(e)).w : isArrow ? measureText(e.label || '', 14).w : 0;
    const b = isText || isArrow ? {w: Math.max(120, tw + 16), h: 30} : normRect(e);
    // resolve the final on-screen width first so a centered editor is centered on that width
    const sw = Math.max(90, (isText || isArrow || isSticky ? b.w : Math.max(12, innerBox(e).w)) * view.scale);
    let left, top;
    if(isText){ const s = worldToScreen(e.x, e.y); left = s.x; top = s.y; }
    else if(isArrow){ const {p1, p2} = arrowEndpoints(e); const s = worldToScreen((p1.x+p2.x)/2, (p1.y+p2.y)/2 - 14); left = s.x - sw / 2; top = s.y; }
    else if(isSticky){ const s = worldToScreen(b.x, b.y); left = s.x; top = s.y; }
    else { const s = worldToScreen(innerBox(e).cx, b.y); left = s.x - sw / 2; top = s.y; }
    editor.value = isText ? (e.text || '') : (e.label || '');
    editor.style.left = left + 'px'; editor.style.top = top + 'px';
    editor.style.transform = '';
    editAnchor = screenToWorld(left, top); editScale = view.scale;
    editor.style.width = sw + 'px';
    const lines = Math.max(1, editor.value.split('\\n').length);
    editor.style.height = Math.max(30, (isText ? textPx(e) * 1.35 * lines : isArrow ? 30 : b.h) * view.scale) + 'px';
    editor.style.fontSize = px + 'px';
    editor.style.lineHeight = (isText ? textPx(e) * 1.35 : (isArrow ? 30 : b.h) / lines) * view.scale + 'px';
    editor.style.textAlign = isText || isSticky ? 'left' : 'center';
    editor.style.color = isSticky ? stickyPaper(e).ink : C.ink;
    editor.style.display = 'block';
    editor.focus(); editor.select();
    editor.dataset.fresh = fresh ? '1' : '';
    editor.dataset.fit = isText || isArrow ? '' : '1';
    // a shape's editor wraps and stays the size of the shape; free text grows as you type
    editor.style.whiteSpace = editor.dataset.fit ? 'pre-wrap' : 'pre';
    editor.style.paddingTop = '';
    if(editor.dataset.fit) fitEditor();
  }
  // the editor is laid out at editScale and pinned to a world point, so a pan or zoom mid-edit
  // carries it with the canvas: re-project its origin and let transform supply the zoom delta
  function syncEditor(){
    if(!editing || !editAnchor) return;
    const s = worldToScreen(editAnchor.x, editAnchor.y);
    editor.style.left = s.x + 'px'; editor.style.top = s.y + 'px';
    editor.style.transform = view.scale === editScale ? '' : 'scale(' + view.scale / editScale + ')';
  }
  // keep the label editor's font matched to what the shape will render as the label changes
  function fitEditor(){
    const e = editing; if(!e) return;
    const maxPx = e.type === 'sticky' ? STICKY_FONT : FONT_SIZE, ib = innerBox(e);
    const f = fitText(ctx, editor.value || ' ', Math.max(12, ib.w), Math.max(12, ib.h), maxPx);
    const lh = f.px * 1.35 * editScale, boxH = parseFloat(editor.style.height) || 0;
    editor.style.fontSize = f.px * editScale + 'px';
    editor.style.lineHeight = lh + 'px';
    editor.style.paddingTop = e.type === 'sticky' ? '' : Math.max(2, (boxH - f.lines.length * lh) / 2) + 'px';
  }
  function commitEdit(cancel = false){
    if(!editing) return;
    const e = editing; editing = null;
    editor.style.display = 'none';
    editor.blur();
    const val = editor.value.replace(/\\s+$/,'');
    beginChange();
    if(e.type === 'text'){
      if(cancel && editor.dataset.fresh) els = els.filter(x => x.id !== e.id);
      else if(!val) els = els.filter(x => x.id !== e.id);
      else e.text = val;
      if(tool === 'text') setTool('select');
    } else if(!cancel){
      e.label = val;
    }
    endChange();
    render();
  }
  editor.addEventListener('keydown', ev => {
    if(ev.key === 'Enter' && !ev.shiftKey){ ev.preventDefault(); commitEdit(); }
    else if(ev.key === 'Escape'){ ev.preventDefault(); commitEdit(true); }
    ev.stopPropagation();
  });
  editor.addEventListener('input', () => {
    if(editor.dataset.fit){ fitEditor(); return; } // shape labels shrink to fit; free text grows the box instead
    const lines = editor.value.split('\\n').length;
    const px = parseFloat(editor.style.fontSize) || 16;
    editor.style.height = Math.max(parseFloat(editor.style.height) || 30, lines * px * 1.5 + 8) + 'px';
    const longest = editor.value.split('\\n').reduce((m, l) => Math.max(m, l.length), 0);
    editor.style.width = Math.max(parseFloat(editor.style.width) || 90, longest * px * .62 + 24) + 'px';
  });
  editor.addEventListener('blur', () => commitEdit());

  // ---------- keyboard ----------
  window.addEventListener('keydown', ev => {
    if(editing) return;
    if(ev.target.tagName === 'TEXTAREA' || ev.target.tagName === 'INPUT') return;
    if(drag) return; // a gesture is in flight; keys wait until it finishes
    const mod = ev.ctrlKey || ev.metaKey;
    if(mod && ev.key.toLowerCase() === 'z'){ ev.preventDefault(); ev.shiftKey ? redo() : undo(); return; }
    if(mod && ev.key.toLowerCase() === 'y'){ ev.preventDefault(); redo(); return; }
    if(ev.key === ' '){ spaceHeld = true; board.style.cursor = ''; board.classList.add('grab'); ev.preventDefault(); return; }
    if(ev.key === 'Escape'){ selected.clear(); saveSession(); render(); return; }
    if((ev.key === 'Delete' || ev.key === 'Backspace') && selected.size){
      ev.preventDefault(); deleteSelected(); return;
    }
    if((ev.key === '[' || ev.key === ']') && !mod){ ev.preventDefault(); stepSize(ev.key === ']' ? 1 : -1); return; }
    const t = toolKeys[ev.key.toLowerCase()];
    if(t && !mod && !ev.altKey) setTool(t);
  });
  window.addEventListener('keyup', ev => {
    if(ev.key === ' '){ spaceHeld = false; board.classList.remove('grab'); }
  });

  function deleteSelected(){
    if(!selected.size) return;
    const gone = new Set(selected);
    mutate(() => {
      // arrows that survive detach from any deleted shape, keeping their visual position
      for(const g of els){
        if(!gone.has(g.id) || !isConnectable(g)) continue;
        const c = center(g);
        for(const a of els){
          if(a.type !== 'arrow' || gone.has(a.id)) continue;
          if(a.fromId === g.id){ a.x1 = c.x; a.y1 = c.y; a.fromId = null; }
          if(a.toId === g.id){ a.x2 = c.x; a.y2 = c.y; a.toId = null; }
        }
      }
      els = els.filter(e => !gone.has(e.id));
      selected.clear();
    });
  }

  // ---------- text size ----------
  // the stepper shows the selected text's size, else the size the next text will be drawn at;
  // stepping always moves that default, and re-sizes a selected text as an undoable edit
  const selectedText = () => { const e = selOne(); return e && e.type === 'text' ? e : null; };
  const sizeVal = document.getElementById('sizeVal');
  function shownSize(){ const t = selectedText(); return t ? textPx(t) : textSize; }
  function updateSizer(){
    const v = String(shownSize());
    if(sizeVal.textContent !== v) sizeVal.textContent = v;
  }
  function stepSize(dir){
    const cur = shownSize();
    // a size off the ladder (e.g. one Claude wrote) steps to its nearest rung in that direction
    let i = TEXT_SIZES.findIndex(s => s >= cur);
    if(i === -1) i = TEXT_SIZES.length;
    const up = TEXT_SIZES[i] > cur ? TEXT_SIZES[i] : TEXT_SIZES[i + 1];
    const next = dir > 0 ? (up || cur) : (TEXT_SIZES[i - 1] || Math.min(cur, TEXT_SIZES[0]));
    textSize = next;
    const t = selectedText();
    if(t && textPx(t) !== next) mutate(() => { t.size = next; });
    else { saveSession(); render(); }
  }
  document.getElementById('sizeDown').onclick = () => stepSize(-1);
  document.getElementById('sizeUp').onclick = () => stepSize(1);

  // ---------- top bar ----------
  document.getElementById('undoBtn').onclick = undo;
  document.getElementById('redoBtn').onclick = redo;
  document.getElementById('snapBtn').onclick = ev => {
    snap = !snap; ev.currentTarget.setAttribute('aria-pressed', String(snap)); saveSession();
  };
  document.getElementById('clearBtn').onclick = () => {
    if(!els.length) return;
    mutate(() => { els = []; selected.clear(); });
    toast('Board cleared — undo brings it back.');
  };

  // ---------- toast ----------
  let toastTimer = null;
  function toast(msg, ms){
    const t = document.getElementById('toast');
    t.textContent = msg; t.classList.add('show');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => t.classList.remove('show'), ms || 2600);
  }

  // ---------- export ----------
  const modal = document.getElementById('exportModal');
  document.getElementById('exportBtn').onclick = exportPNG;
  document.getElementById('pingBtn').onclick = sendToClaude;
  document.getElementById('submitBtn').onclick = submitBoard;
  document.getElementById('closeExport').onclick = () => modal.classList.remove('open');
  modal.addEventListener('click', ev => { if(ev.target === modal) modal.classList.remove('open'); });
  // the root's data-theme observer re-reads the tokens and repaints; the button only flips the stamp
  document.getElementById('themeBtn').onclick = () => setTheme(THEME_NEXT[rootTheme()]);

  async function exportPNG(){
    const b = boundsOfAll();
    if(!b){ toast('The board is empty — sketch something first.'); return; }
    const pad = 48, s = 2;
    const off = document.createElement('canvas');
    off.width = Math.ceil((b.w + pad * 2) * s); off.height = Math.ceil((b.h + pad * 2) * s);
    const oc = off.getContext('2d');
    oc.scale(s, s); oc.translate(pad - b.x, pad - b.y);
    oc.fillStyle = C.ground; oc.fillRect(b.x - pad, b.y - pad, b.w + pad * 2, b.h + pad * 2);
    for(const e of els) drawElement(oc, e);
    const blob = await new Promise(res => off.toBlob(res, 'image/png'));
    // the viewer runtime offers real file saves; the frame itself can't start downloads
    const dl = window.claude && window.claude.downloads;
    if(dl && blob){
      try{ await dl.save({filename: 'whiteboard.png', data: blob}); toast('Saved whiteboard.png'); return; }
      catch(err){ if(err && err.code === 'declined') return; }
    }
    if(navigator.clipboard && window.ClipboardItem && blob){
      try{ await navigator.clipboard.write([new ClipboardItem({'image/png': blob})]); toast('Board image copied — paste it wherever you like.'); return; }
      catch(_){}
    }
    // last resort: show the image so it can be right-clicked and saved
    document.getElementById('exportImg').src = off.toDataURL('image/png');
    modal.classList.add('open');
  }

  // ---------- tiny API for future integrations ----------
  window.whiteboard = {
    toJSON: () => clone(els),
    toPNG: () => exportPNG(),
    load: data => { mutate(() => { els = sanitize(clone(data)); selected.clear(); }); zoomFit(); }
  };

  // ---------- boot ----------
  applyStoredTheme(); // stamp the saved light/dark choice before the tokens are read, so the first paint matches
  readTheme();
  syncThemeBtn();
  loadState();
  loadSession();
  deconflict();
  pruneSelection();
  setTool(tool);
  document.getElementById('snapBtn').setAttribute('aria-pressed', String(snap));
  updateButtons();
  syncStatus();
  drawClawd(0);
  checkWaiting();
  primeSend();
  resize();
}

function boot(){
  const st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
  document.body.insertAdjacentHTML('beforeend', MARKUP);
  main();
}
themeMirror();
scheduleBoot();
</script>
<!-- The sheet sits AFTER the script so the template keeps the exact two-line head
     merge-state.mjs pins (<title>, <script>); scheduleBoot compensates by waiting for
     the parser to reach it before the canvas reads colors. -->
<style id="cds-tokens">
  /* ===== BEGIN vendored @ant/cds tokens (src/frame/cdsTokens.vanilla.generated.css) =====
     Byte-identical to that file (drift-tested in test/frame/planArtifactHtml.test.ts).
     Do not edit this block: refresh the vendored file from @ant/cds and re-embed. */
/*
 * VENDORED — verbatim copy of @ant/cds tokens.vanilla.css (the CDS team's
 * framework-agnostic token export) from anthropics/apps@230786b7e9757b07527ac4283db9b19676a8ae91
 * (packages/cds/src/generated/tokens.vanilla.css).
 * upstream-sha256: 94f136cf38cc5f54c1b6dda76677c466b122f6b7e6f8702ef18774cbc7643152
 *   (sha256 of everything below this header comment, i.e. of the raw
 *   upstream file — recomputed and asserted by the "provenance hash"
 *   test, so a refresh that swaps bytes without updating this line
 *   fails CI rather than shipping a lying header.)
 *
 * Browser floor: the export uses hsl(from …) and color-mix() — ~Chrome 119 /
 * Safari 16.4. On older viewers the consuming declarations are dropped
 * SILENTLY (no error, no telemetry): borders, the alpha ramp, and dark
 * surfaces degrade. This line is the triage breadcrumb for "published
 * artifact looks broken" reports — ask the browser version first.
 *
 * The plan-artifact, workshop, and whiteboard templates embed this file
 * byte-for-byte between BEGIN/END markers; drift tests assert the copies
 * stay identical. To refresh: copy the upstream generated file below this
 * header, update the commit hash and upstream-sha256 above, run
 * \`bun scripts/embed-cds-tokens.ts\`, then \`bun test
 * test/frame/planArtifactHtml.test.ts test/skills/bundled/whiteboardTokens.test.ts\`.
 */

/**
 * GENERATED — do not edit. Run \`yarn workspace @ant/cds gen:tokens\`.
 *
 * Framework-agnostic CDS token export: unprefixed \`--*\` custom
 * properties under \`:root\`, with dark-mode overrides under
 * \`[data-mode="dark"]\` and \`@media (prefers-color-scheme: dark)\`.
 * No \`.cds-root\` scoping, density steps, or component-private tokens.
 *
 * Source: \`packages/cds/tokens/\`. For the full React/Tailwind build
 * (scoped under \`.cds-root\`), see \`tokens.css\`.
 */

:root {
  --radius: 8px;
  --h-control: 32px;
  --h-control-nested: 22px;
  --icon: 20px;
  --pad-sm: 8px;
  --pad-md: 12px;
  --pad-lg: 16px;
  --pad-xl: 24px;
  --gap-xs: 8px;
  --gap-sm: 12px;
  --gap-md: 16px;
  --gap-lg: 28px;
  --gap-xl: 40px;
  --outset-x: 0px;
  --outset-y: 0px;
  --border: var(--alpha-2);
  --border-accent: var(--blue-250);
  --border-danger: var(--red-250);
  --border-success: var(--green-250);
  --border-warning: var(--yellow-250);
  --border-pro: var(--violet-250);
  --border-git-added: color-mix(in srgb, var(--text-git-added) 40%, transparent);
  --border-git-removed: color-mix(in srgb, var(--text-git-removed) 40%, transparent);
  --border-git-modified: color-mix(in srgb, var(--text-git-modified) 40%, transparent);
  --border-git-merged: color-mix(in srgb, var(--text-git-merged) 40%, transparent);
  --border-git-closed: color-mix(in srgb, var(--text-git-closed) 40%, transparent);
  --border-git-conflicting: color-mix(in srgb, var(--text-git-conflicting) 40%, transparent);
  --border-git-draft: color-mix(in srgb, var(--text-git-draft) 40%, transparent);
  --border-git-opened: var(--border-git-added);
  --border-git-queued: var(--border-git-modified);
  --border-strong: var(--alpha-3);
  --border-stronger: hsl(from var(--neutral-900) h s l / 40%);
  --shadow-sm: 0 1px 2px 0 hsl(from var(--gray-900) h s l / 6%), 0 2px 8px 0 var(--shadow-color);
  --shadow-md: 0 2px 4px 0 hsl(from var(--gray-900) h s l / 7%), 0 6px 16px 0 var(--shadow-color);
  --shadow-lg: 0 4px 8px 0 hsl(from var(--gray-900) h s l / 8%), 0 12px 28px -2px var(--shadow-color);
  --shadow-color: hsl(from var(--gray-900) h s l / 8%);
  --shadow-popover: 0 8px 24px rgb(0 0 0 / 0.12), 0 2px 6px rgb(0 0 0 / 0.08);
  --ring-outer: 1px;
  --ring-inner: 0px;
  --ring-color: var(--border);
  --focus-shadow: inset 0 0 0 1px var(--page-bg), 0 0 0 1px var(--fill-accent), 0 0 6px 1px var(--bg-accent);
  --font-mono: var(--font-anthropic-mono, "Anthropic Mono Variable"), "Anthropic Mono", "SF Mono", ui-monospace, Menlo, Consolas, monospace;
  --font-system: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-sans: var(--font-anthropic-sans, "Anthropic Sans Variable", "Anthropic Sans"), var(--font-system);
  --font-voice: var(--font-anthropic-serif, "Anthropic Serif Variable", "Anthropic Serif"), ui-serif, Georgia, "Times New Roman", serif;
  --ease-out: cubic-bezier(0.165, 0.84, 0.44, 1);
  --ease-snap: cubic-bezier(0.32, 0.72, 0, 1);
  --ease-overshoot: cubic-bezier(0.34, 1.3, 0.64, 1);
  --dur-fast: 60ms;
  --dur-snap: 120ms;
  --dur-base: 200ms;
  --dur-slow: 450ms;
  --btn-spring: linear(0, 0.2459, 0.6526, 0.9468, 1.0764, 1.0915, 1.0585, 1.0219, 0.9993, 0.9914, 0.9921, 0.9957, 0.9988, 1.0004, 1);
  --black: #000000;
  --oncolor-200: hsl(60 6.7% 97.1% / 0.75);
  --oncolor-300: hsl(60 6.7% 97.1% / 0.5);
  --clay: #d97757;
  --clay-emphasized: #c6613f;
  --heather: #cbcadb;
  --plum: #827dbd;
  --cactus: #bcd1ca;
  --mineral: #629987;
  --peach: #ebc9b7;
  --gray-0: #ffffff;
  --gray-10: #fcfcfb;
  --gray-20: #f9f9f7;
  --gray-30: #f6f6f4;
  --gray-40: #f3f3f0;
  --gray-50: #f0efec;
  --gray-60: #edece8;
  --gray-70: #eae9e4;
  --gray-80: #e7e6e1;
  --gray-90: #e4e3dd;
  --gray-100: #e1e0d9;
  --gray-150: #d2d1c7;
  --gray-200: #c3c2b7;
  --gray-250: #b4b3a8;
  --gray-300: #a5a49a;
  --gray-350: #97958d;
  --gray-400: #898781;
  --gray-450: #7b7974;
  --gray-500: #6d6b67;
  --gray-550: #5f5e5a;
  --gray-600: #52514e;
  --gray-650: #454442;
  --gray-700: #383835;
  --gray-750: #2c2c2a;
  --gray-800: #20201f;
  --gray-810: #1e1e1d;
  --gray-820: #1c1c1b;
  --gray-830: #1a1a19;
  --gray-840: #181817;
  --gray-850: #151515;
  --gray-860: #131313;
  --gray-870: #111111;
  --gray-880: #0f0f0f;
  --gray-890: #0d0d0d;
  --gray-900: #0b0b0b;
  --red-0: #ffffff;
  --red-10: #fffbfb;
  --red-20: #fef7f7;
  --red-30: #fef3f3;
  --red-40: #fdefef;
  --red-50: #fbebeb;
  --red-60: #fae7e7;
  --red-70: #fae3e3;
  --red-80: #fadfdf;
  --red-90: #fadada;
  --red-100: #fad6d6;
  --red-150: #f7c1c1;
  --red-200: #f4abab;
  --red-250: #f09595;
  --red-300: #ec7e7e;
  --red-350: #e66767;
  --red-400: #e34948;
  --red-450: #d03b3b;
  --red-500: #b93535;
  --red-550: #a32c2c;
  --red-600: #8e2626;
  --red-650: #791e1e;
  --red-700: #641919;
  --red-750: #511212;
  --red-800: #3c0e0e;
  --red-810: #380d0d;
  --red-820: #340c0c;
  --red-830: #310b0b;
  --red-840: #2d0a0a;
  --red-850: #280a0a;
  --red-860: #230b0a;
  --red-870: #1d0b0a;
  --red-880: #170c0b;
  --red-890: #110c0b;
  --red-900: #0b0b0b;
  --orange-0: #ffffff;
  --orange-10: #fefbfa;
  --orange-20: #fdf7f5;
  --orange-30: #fcf4f0;
  --orange-40: #faf0ec;
  --orange-50: #f9ece7;
  --orange-60: #f8e9e2;
  --orange-70: #f7e5dd;
  --orange-80: #f7e1d7;
  --orange-90: #f7dcd1;
  --orange-100: #f7d8cb;
  --orange-150: #f3c5b2;
  --orange-200: #f4ae94;
  --orange-250: #f09978;
  --orange-300: #ec835a;
  --orange-350: #eb6834;
  --orange-400: #d95926;
  --orange-450: #c25124;
  --orange-500: #ae461c;
  --orange-550: #993d19;
  --orange-600: #863311;
  --orange-650: #712b0f;
  --orange-700: #5d230b;
  --orange-750: #4b1b08;
  --orange-800: #371407;
  --orange-810: #341307;
  --orange-820: #301106;
  --orange-830: #2d1006;
  --orange-840: #290f06;
  --orange-850: #240e07;
  --orange-860: #1f0e08;
  --orange-870: #1a0e09;
  --orange-880: #150d0a;
  --orange-890: #100c0b;
  --orange-900: #0b0b0b;
  --yellow-0: #ffffff;
  --yellow-10: #fefcf8;
  --yellow-20: #fcf8f1;
  --yellow-30: #fbf5ea;
  --yellow-40: #f9f2e4;
  --yellow-50: #f9eeda;
  --yellow-60: #faebce;
  --yellow-70: #fae7c2;
  --yellow-80: #fae3b8;
  --yellow-90: #f9e0b0;
  --yellow-100: #f9dca4;
  --yellow-150: #f9c868;
  --yellow-200: #fab219;
  --yellow-250: #eda100;
  --yellow-300: #db9300;
  --yellow-350: #c98500;
  --yellow-400: #b77700;
  --yellow-450: #a66a00;
  --yellow-500: #945d00;
  --yellow-550: #835100;
  --yellow-600: #734500;
  --yellow-650: #623900;
  --yellow-700: #512e00;
  --yellow-750: #412400;
  --yellow-800: #311a00;
  --yellow-810: #2e1800;
  --yellow-820: #2b1700;
  --yellow-830: #271500;
  --yellow-840: #231402;
  --yellow-850: #1f1204;
  --yellow-860: #1b1106;
  --yellow-870: #171007;
  --yellow-880: #130e09;
  --yellow-890: #0f0d0a;
  --yellow-900: #0b0b0b;
  --green-0: #ffffff;
  --green-10: #fafdfa;
  --green-20: #f5fbf4;
  --green-30: #f0f9ef;
  --green-40: #ebf7e9;
  --green-50: #e5f4e4;
  --green-60: #e0f2de;
  --green-70: #dbf0d8;
  --green-80: #d5eed3;
  --green-90: #d0eccd;
  --green-100: #caeac7;
  --green-150: #aee0a9;
  --green-200: #91d68b;
  --green-250: #73cb6d;
  --green-300: #55bf50;
  --green-350: #35b231;
  --green-400: #0ca30c;
  --green-450: #009300;
  --green-500: #008300;
  --green-550: #007300;
  --green-600: #006300;
  --green-650: #005400;
  --green-700: #074506;
  --green-750: #0f350d;
  --green-800: #11260f;
  --green-810: #10230f;
  --green-820: #10210f;
  --green-830: #101e0f;
  --green-840: #101b0f;
  --green-850: #0f180e;
  --green-860: #0e160e;
  --green-870: #0e130d;
  --green-880: #0d100d;
  --green-890: #0c0e0c;
  --green-900: #0b0b0b;
  --aqua-0: #ffffff;
  --aqua-10: #f9fdfb;
  --aqua-20: #f3fbf8;
  --aqua-30: #edf9f4;
  --aqua-40: #e8f7f1;
  --aqua-50: #e2f4ed;
  --aqua-60: #dcf2ea;
  --aqua-70: #d5f0e6;
  --aqua-80: #ceefe2;
  --aqua-90: #c7eddf;
  --aqua-100: #bfebdb;
  --aqua-150: #a0e1c9;
  --aqua-200: #7ad7b4;
  --aqua-250: #5acba0;
  --aqua-300: #3bbd8c;
  --aqua-350: #1baf7a;
  --aqua-400: #199e70;
  --aqua-450: #138e65;
  --aqua-500: #0f7e5c;
  --aqua-550: #0e6e53;
  --aqua-600: #065f49;
  --aqua-650: #095040;
  --aqua-700: #034235;
  --aqua-750: #02342b;
  --aqua-800: #022720;
  --aqua-810: #02241e;
  --aqua-820: #02221c;
  --aqua-830: #021f1a;
  --aqua-840: #031c18;
  --aqua-850: #051a16;
  --aqua-860: #071713;
  --aqua-870: #081411;
  --aqua-880: #0a110f;
  --aqua-890: #0b0e0d;
  --aqua-900: #0b0b0b;
  --blue-0: #ffffff;
  --blue-10: #fafcff;
  --blue-20: #f5f9fe;
  --blue-30: #f0f7fe;
  --blue-40: #ebf4fc;
  --blue-50: #e7f1fb;
  --blue-60: #e2eefa;
  --blue-70: #ddebfa;
  --blue-80: #d7e8fa;
  --blue-90: #d2e5fa;
  --blue-100: #cde2fb;
  --blue-150: #b7d3f6;
  --blue-200: #9ec5f4;
  --blue-250: #86b6ef;
  --blue-300: #6da7ec;
  --blue-350: #5598e7;
  --blue-400: #3987e5;
  --blue-450: #2a78d6;
  --blue-500: #256abf;
  --blue-550: #1c5cab;
  --blue-600: #184f95;
  --blue-650: #104281;
  --blue-700: #0d366b;
  --blue-750: #062b57;
  --blue-800: #032042;
  --blue-810: #031e3d;
  --blue-820: #021c39;
  --blue-830: #021a36;
  --blue-840: #021831;
  --blue-850: #03162c;
  --blue-860: #051426;
  --blue-870: #07121f;
  --blue-880: #091018;
  --blue-890: #0a0d11;
  --blue-900: #0b0b0b;
  --violet-0: #ffffff;
  --violet-10: #fcfbff;
  --violet-20: #f8f8ff;
  --violet-30: #f5f4ff;
  --violet-40: #f2f1ff;
  --violet-50: #efedff;
  --violet-60: #ebeafe;
  --violet-70: #e8e6fe;
  --violet-80: #e5e2fd;
  --violet-90: #e2dffd;
  --violet-100: #dfdbfd;
  --violet-150: #cfcafb;
  --violet-200: #bfb9f5;
  --violet-250: #b0a7f2;
  --violet-300: #a096eb;
  --violet-350: #9085e9;
  --violet-400: #8173e3;
  --violet-450: #7161e0;
  --violet-500: #6250d6;
  --violet-550: #5645be;
  --violet-600: #4a3aa7;
  --violet-650: #3e318e;
  --violet-700: #322777;
  --violet-750: #271e60;
  --violet-800: #1d1649;
  --violet-810: #1b1544;
  --violet-820: #19133f;
  --violet-830: #17123b;
  --violet-840: #151036;
  --violet-850: #130f32;
  --violet-860: #110e2b;
  --violet-870: #0f0e23;
  --violet-880: #0e0d1b;
  --violet-890: #0c0c13;
  --violet-900: #0b0b0b;
  --magenta-0: #ffffff;
  --magenta-10: #fefbfc;
  --magenta-20: #fef6f9;
  --magenta-30: #fdf2f6;
  --magenta-40: #fbeff3;
  --magenta-50: #faebf0;
  --magenta-60: #f9e6ed;
  --magenta-70: #f9e2eb;
  --magenta-80: #f9dee8;
  --magenta-90: #f9d9e5;
  --magenta-100: #f9d4e2;
  --magenta-150: #f3c0d3;
  --magenta-200: #f3a8c3;
  --magenta-250: #ed93b4;
  --magenta-300: #e87ba4;
  --magenta-350: #e46191;
  --magenta-400: #d55181;
  --magenta-450: #c04873;
  --magenta-500: #ad3d66;
  --magenta-550: #993458;
  --magenta-600: #862a4c;
  --magenta-650: #722340;
  --magenta-700: #5e1c34;
  --magenta-750: #4c1429;
  --magenta-800: #390f1f;
  --magenta-810: #360d1c;
  --magenta-820: #320c1a;
  --magenta-830: #2f0b18;
  --magenta-840: #2b0a16;
  --magenta-850: #270a14;
  --magenta-860: #220a12;
  --magenta-870: #1c0b11;
  --magenta-880: #170b0f;
  --magenta-890: #110b0d;
  --magenta-900: #0b0b0b;
  --pictogram-highlight-default: var(--gray-80);
  --pictogram-highlight-heather: var(--heather);
  --pictogram-highlight-cactus: var(--cactus);
  --pictogram-highlight-peach: var(--peach);
  --cursor-interactive: pointer;
  --neutral-0: var(--gray-0);
  --neutral-10: var(--gray-10);
  --neutral-20: var(--gray-20);
  --neutral-30: var(--gray-30);
  --neutral-40: var(--gray-40);
  --neutral-50: var(--gray-50);
  --neutral-60: var(--gray-60);
  --neutral-70: var(--gray-70);
  --neutral-80: var(--gray-80);
  --neutral-90: var(--gray-90);
  --neutral-100: var(--gray-100);
  --neutral-150: var(--gray-150);
  --neutral-200: var(--gray-200);
  --neutral-250: var(--gray-250);
  --neutral-300: var(--gray-300);
  --neutral-350: var(--gray-350);
  --neutral-400: var(--gray-400);
  --neutral-450: var(--gray-450);
  --neutral-500: var(--gray-500);
  --neutral-550: var(--gray-550);
  --neutral-600: var(--gray-600);
  --neutral-650: var(--gray-650);
  --neutral-700: var(--gray-700);
  --neutral-750: var(--gray-750);
  --neutral-800: var(--gray-800);
  --neutral-810: var(--gray-810);
  --neutral-820: var(--gray-820);
  --neutral-830: var(--gray-830);
  --neutral-840: var(--gray-840);
  --neutral-850: var(--gray-850);
  --neutral-860: var(--gray-860);
  --neutral-870: var(--gray-870);
  --neutral-880: var(--gray-880);
  --neutral-890: var(--gray-890);
  --neutral-900: var(--gray-900);
  --alpha-0: hsl(from var(--neutral-900) h s l / 0%);
  --alpha-1: hsl(from var(--neutral-900) h s l / 5%);
  --alpha-2: hsl(from var(--neutral-900) h s l / 10%);
  --alpha-3: hsl(from var(--neutral-900) h s l / 20%);
  --alpha-4: hsl(from var(--neutral-900) h s l / 35%);
  --alpha-5: hsl(from var(--neutral-900) h s l / 50%);
  --alpha-6: hsl(from var(--neutral-900) h s l / 60%);
  --alpha-7: hsl(from var(--neutral-900) h s l / 70%);
  --alpha-8: hsl(from var(--neutral-900) h s l / 85%);
  --alpha-9: hsl(from var(--neutral-900) h s l / 95%);
  --surface-0: var(--gray-20);
  --surface-1: var(--gray-10);
  --surface-2: var(--gray-0);
  --surface-3: var(--gray-0);
  --surface-popover: var(--surface-3);
  --surface-panel: var(--surface-2);
  --page-bg: var(--surface-0);
  --fill-accent: var(--blue-450);
  --fill-accent-hover: var(--blue-400);
  --fill-danger: var(--red-450);
  --fill-danger-hover: var(--red-400);
  --fill-success: var(--green-450);
  --fill-success-hover: var(--green-400);
  --fill-warning: var(--yellow-200);
  --fill-warning-hover: var(--yellow-250);
  --fill-pro: var(--violet-450);
  --fill-pro-hover: var(--violet-400);
  --fill-git-added: #1a8633;
  --fill-git-added-hover: #1e9b3b;
  --fill-git-removed: var(--text-git-removed);
  --fill-git-removed-hover: #de295f;
  --fill-git-modified: #8b751c;
  --fill-git-modified-hover: #a08720;
  --fill-git-merged: #855fd6;
  --fill-git-merged-hover: #9473db;
  --fill-git-closed: #ed0b00;
  --fill-git-closed-hover: #ff1307;
  --fill-git-conflicting: #b85b19;
  --fill-git-conflicting-hover: #c5621b;
  --fill-git-draft: var(--text-git-draft);
  --fill-git-draft-hover: #808080;
  --fill-git-opened: var(--fill-git-added);
  --fill-git-opened-hover: var(--fill-git-added-hover);
  --fill-git-queued: var(--fill-git-modified);
  --fill-git-queued-hover: var(--fill-git-modified-hover);
  --fill-brand: var(--clay-emphasized);
  --fill-brand-hover: var(--clay);
  --fill-primary: var(--neutral-900);
  --fill-primary-hover: var(--neutral-750);
  --fill-secondary: hsl(0 0% 100% / 0.1);
  --fill-secondary-hover: var(--alpha-1);
  --fill-secondary-ring: var(--border);
  --fill-field: hsl(0 0% 100% / 0.5);
  --fill-ghost-hover: var(--alpha-1);
  --fill-disabled: var(--alpha-1);
  --fill-control: var(--alpha-2);
  --fill-control-hover: var(--alpha-3);
  --bg-accent: var(--blue-100);
  --bg-danger: var(--red-100);
  --bg-success: var(--green-100);
  --bg-warning: var(--yellow-100);
  --bg-pro: var(--violet-100);
  --bg-git-added: color-mix(in srgb, var(--text-git-added) 20%, transparent);
  --bg-git-removed: color-mix(in srgb, var(--text-git-removed) 20%, transparent);
  --bg-git-modified: color-mix(in srgb, var(--text-git-modified) 20%, transparent);
  --bg-git-merged: color-mix(in srgb, var(--text-git-merged) 20%, transparent);
  --bg-git-closed: color-mix(in srgb, var(--text-git-closed) 20%, transparent);
  --bg-git-conflicting: color-mix(in srgb, var(--text-git-conflicting) 20%, transparent);
  --bg-git-draft: color-mix(in srgb, var(--text-git-draft) 20%, transparent);
  --bg-git-opened: var(--bg-git-added);
  --bg-git-queued: var(--bg-git-modified);
  --bg-neutral: var(--alpha-1);
  --bg-neutral-hover: var(--alpha-2);
  --backdrop: rgb(0 0 0 / 0.4);
  --text-accent: var(--blue-600);
  --text-danger: var(--red-600);
  --text-success: var(--green-600);
  --text-warning: var(--yellow-600);
  --text-pro: var(--violet-600);
  --text-git-added: #1e9e3c;
  --text-git-removed: #cd2054;
  --text-git-modified: #98801f;
  --text-git-merged: #8e6bd9;
  --text-git-closed: #ff3a30;
  --text-git-conflicting: #c5621b;
  --text-git-draft: #737373;
  --text-git-opened: var(--text-git-added);
  --text-git-queued: var(--text-git-modified);
  --text-primary: var(--neutral-900);
  --text-secondary: var(--neutral-600);
  --text-muted: var(--neutral-400);
  --text-disabled: var(--alpha-4);
  --font-size-caption: 12px;
  --font-size-footnote: 13px;
  --font-size-code: 13px;
  --font-size-body: 14px;
  --font-size-heading: 15px;
  --font-size-title: 22px;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --leading-caption: 14px;
  --leading-footnote: 16px;
  --leading-code: 19px;
  --leading-body: 20px;
  --leading-heading: 20px;
  --leading-title: 26px;
  --on-primary: var(--neutral-0);
  --on-accent: var(--gray-0);
  --on-danger: var(--gray-0);
  --on-success: var(--gray-900);
  --on-warning: var(--gray-900);
  --on-pro: var(--gray-0);
  --on-git-added: var(--gray-0);
  --on-git-removed: var(--gray-0);
  --on-git-modified: var(--gray-0);
  --on-git-merged: var(--gray-0);
  --on-git-closed: var(--gray-0);
  --on-git-conflicting: var(--gray-0);
  --on-git-draft: var(--gray-0);
  --on-git-opened: var(--on-git-added);
  --on-git-queued: var(--on-git-modified);
  --on-brand: var(--gray-0);
  --z-modal: 40;
  --z-coachmark: 35;
  --z-popover: 50;
  --z-tooltip: 50;
  --z-toast: 60;
}

[data-mode="dark"] {
  --border-accent: var(--blue-700);
  --border-danger: var(--red-700);
  --border-success: var(--green-700);
  --border-warning: var(--yellow-700);
  --border-pro: var(--violet-700);
  --shadow-color: hsl(0 0% 0% / 0.24);
  --shadow-popover: 0 8px 24px rgb(0 0 0 / 0.32), 0 2px 6px rgb(0 0 0 / 0.2);
  --ring-outer: 0px;
  --ring-inner: 1px;
  --ring-color: var(--alpha-2);
  --focus-shadow: inset 0 0 0 1px var(--page-bg), 0 0 0 1px var(--fill-accent), 0 0 6px 1px hsl(from var(--blue-600) h s l / 60%);
  --pictogram-highlight-default: var(--gray-650);
  --pictogram-highlight-heather: var(--plum);
  --pictogram-highlight-cactus: var(--mineral);
  --pictogram-highlight-peach: var(--clay-emphasized);
  --neutral-0: var(--gray-900);
  --neutral-10: var(--gray-890);
  --neutral-20: var(--gray-880);
  --neutral-30: var(--gray-870);
  --neutral-40: var(--gray-860);
  --neutral-50: var(--gray-850);
  --neutral-60: var(--gray-840);
  --neutral-70: var(--gray-830);
  --neutral-80: var(--gray-820);
  --neutral-90: var(--gray-810);
  --neutral-100: var(--gray-800);
  --neutral-150: var(--gray-750);
  --neutral-200: var(--gray-700);
  --neutral-250: var(--gray-650);
  --neutral-300: var(--gray-600);
  --neutral-350: var(--gray-550);
  --neutral-400: var(--gray-500);
  --neutral-450: var(--gray-450);
  --neutral-500: var(--gray-400);
  --neutral-550: var(--gray-350);
  --neutral-600: var(--gray-300);
  --neutral-650: var(--gray-250);
  --neutral-700: var(--gray-200);
  --neutral-750: var(--gray-150);
  --neutral-800: var(--gray-100);
  --neutral-810: var(--gray-90);
  --neutral-820: var(--gray-80);
  --neutral-830: var(--gray-70);
  --neutral-840: var(--gray-60);
  --neutral-850: var(--gray-50);
  --neutral-860: var(--gray-40);
  --neutral-870: var(--gray-30);
  --neutral-880: var(--gray-20);
  --neutral-890: var(--gray-10);
  --neutral-900: var(--gray-0);
  --surface-0: var(--gray-890);
  --surface-1: var(--gray-830);
  --surface-2: var(--gray-750);
  --surface-3: var(--gray-700);
  --fill-git-added: var(--text-git-added);
  --fill-git-added-hover: #27c840;
  --fill-git-removed-hover: #ff1342;
  --fill-git-modified: var(--text-git-modified);
  --fill-git-modified-hover: #fac800;
  --fill-git-merged: var(--text-git-merged);
  --fill-git-merged-hover: #a67dff;
  --fill-git-closed: var(--text-git-closed);
  --fill-git-closed-hover: #ff4940;
  --fill-git-conflicting: var(--text-git-conflicting);
  --fill-git-conflicting-hover: #f97a1f;
  --fill-git-draft-hover: #999999;
  --fill-primary-hover: var(--gray-100);
  --fill-secondary: var(--alpha-2);
  --fill-secondary-hover: hsl(0 0% 100% / 0.14);
  --fill-secondary-ring: transparent;
  --fill-field: var(--fill-secondary);
  --bg-accent: var(--blue-800);
  --bg-danger: var(--red-800);
  --bg-success: var(--green-800);
  --bg-warning: var(--yellow-800);
  --bg-pro: var(--violet-800);
  --backdrop: rgb(0 0 0 / 0.5);
  --text-accent: var(--blue-300);
  --text-danger: var(--red-300);
  --text-success: var(--green-400);
  --text-warning: var(--yellow-300);
  --text-pro: var(--violet-300);
  --text-git-added: #32d74b;
  --text-git-removed: #ff2c56;
  --text-git-modified: #ffd014;
  --text-git-merged: #b796ff;
  --text-git-closed: #ff6159;
  --text-git-conflicting: #fa832e;
  --text-git-draft: #a6a6a6;
  --text-secondary: var(--gray-200);
  --text-muted: var(--gray-400);
  --on-git-added: var(--gray-900);
  --on-git-removed: var(--gray-900);
  --on-git-modified: var(--gray-900);
  --on-git-merged: var(--gray-900);
  --on-git-closed: var(--gray-900);
  --on-git-conflicting: var(--gray-900);
  --on-git-draft: var(--gray-900);
}

@media (prefers-color-scheme: dark) {
  :root:where(:not([data-mode="light"])) {
    --border-accent: var(--blue-700);
    --border-danger: var(--red-700);
    --border-success: var(--green-700);
    --border-warning: var(--yellow-700);
    --border-pro: var(--violet-700);
    --shadow-color: hsl(0 0% 0% / 0.24);
    --shadow-popover: 0 8px 24px rgb(0 0 0 / 0.32), 0 2px 6px rgb(0 0 0 / 0.2);
    --ring-outer: 0px;
    --ring-inner: 1px;
    --ring-color: var(--alpha-2);
    --focus-shadow: inset 0 0 0 1px var(--page-bg), 0 0 0 1px var(--fill-accent), 0 0 6px 1px hsl(from var(--blue-600) h s l / 60%);
    --pictogram-highlight-default: var(--gray-650);
    --pictogram-highlight-heather: var(--plum);
    --pictogram-highlight-cactus: var(--mineral);
    --pictogram-highlight-peach: var(--clay-emphasized);
    --neutral-0: var(--gray-900);
    --neutral-10: var(--gray-890);
    --neutral-20: var(--gray-880);
    --neutral-30: var(--gray-870);
    --neutral-40: var(--gray-860);
    --neutral-50: var(--gray-850);
    --neutral-60: var(--gray-840);
    --neutral-70: var(--gray-830);
    --neutral-80: var(--gray-820);
    --neutral-90: var(--gray-810);
    --neutral-100: var(--gray-800);
    --neutral-150: var(--gray-750);
    --neutral-200: var(--gray-700);
    --neutral-250: var(--gray-650);
    --neutral-300: var(--gray-600);
    --neutral-350: var(--gray-550);
    --neutral-400: var(--gray-500);
    --neutral-450: var(--gray-450);
    --neutral-500: var(--gray-400);
    --neutral-550: var(--gray-350);
    --neutral-600: var(--gray-300);
    --neutral-650: var(--gray-250);
    --neutral-700: var(--gray-200);
    --neutral-750: var(--gray-150);
    --neutral-800: var(--gray-100);
    --neutral-810: var(--gray-90);
    --neutral-820: var(--gray-80);
    --neutral-830: var(--gray-70);
    --neutral-840: var(--gray-60);
    --neutral-850: var(--gray-50);
    --neutral-860: var(--gray-40);
    --neutral-870: var(--gray-30);
    --neutral-880: var(--gray-20);
    --neutral-890: var(--gray-10);
    --neutral-900: var(--gray-0);
    --surface-0: var(--gray-890);
    --surface-1: var(--gray-830);
    --surface-2: var(--gray-750);
    --surface-3: var(--gray-700);
    --fill-git-added: var(--text-git-added);
    --fill-git-added-hover: #27c840;
    --fill-git-removed-hover: #ff1342;
    --fill-git-modified: var(--text-git-modified);
    --fill-git-modified-hover: #fac800;
    --fill-git-merged: var(--text-git-merged);
    --fill-git-merged-hover: #a67dff;
    --fill-git-closed: var(--text-git-closed);
    --fill-git-closed-hover: #ff4940;
    --fill-git-conflicting: var(--text-git-conflicting);
    --fill-git-conflicting-hover: #f97a1f;
    --fill-git-draft-hover: #999999;
    --fill-primary-hover: var(--gray-100);
    --fill-secondary: var(--alpha-2);
    --fill-secondary-hover: hsl(0 0% 100% / 0.14);
    --fill-secondary-ring: transparent;
    --fill-field: var(--fill-secondary);
    --bg-accent: var(--blue-800);
    --bg-danger: var(--red-800);
    --bg-success: var(--green-800);
    --bg-warning: var(--yellow-800);
    --bg-pro: var(--violet-800);
    --backdrop: rgb(0 0 0 / 0.5);
    --text-accent: var(--blue-300);
    --text-danger: var(--red-300);
    --text-success: var(--green-400);
    --text-warning: var(--yellow-300);
    --text-pro: var(--violet-300);
    --text-git-added: #32d74b;
    --text-git-removed: #ff2c56;
    --text-git-modified: #ffd014;
    --text-git-merged: #b796ff;
    --text-git-closed: #ff6159;
    --text-git-conflicting: #fa832e;
    --text-git-draft: #a6a6a6;
    --text-secondary: var(--gray-200);
    --text-muted: var(--gray-400);
    --on-git-added: var(--gray-900);
    --on-git-removed: var(--gray-900);
    --on-git-modified: var(--gray-900);
    --on-git-merged: var(--gray-900);
    --on-git-closed: var(--gray-900);
    --on-git-conflicting: var(--gray-900);
    --on-git-draft: var(--gray-900);
  }
}

  /* ===== END vendored @ant/cds tokens ===== */
</style>
