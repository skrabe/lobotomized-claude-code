<!--
name: 'Data: Artifact spreadsheet HTML template'
description: >-
  Provides the bundled live-spreadsheet HTML template extracted for Claude when
  the sheet Artifact skill is activated.
ccVersion: 2.1.232
-->
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title><!-- SLOT: TITLE — the sheet's name alone, short and distinctive; never a "Name — explainer" compound -->Sheet</title>
<style>
  /* KIT:tokens:begin — identical across the productivity family; the
     keep-in-sync test asserts byte-equality of every KIT region. */
  :root {
    /* CDS-vocabulary token literals retuned to the iA Writer register:
       one continuous paper surface (no canvas/card split), near-black
       ink, and a duospace editor voice — inlined because artifacts
       render self-contained with no network access. */
    --cds-surface-0: #ffffff;            /* the paper — whole viewport */
    --cds-surface-1: #ffffff;            /* same paper: no card separation */
    --cds-surface-2: #ffffff;            /* chrome sits on the paper too */
    --cds-text-primary: #1a1a19;
    --cds-text-secondary: #55544f;
    --cds-text-muted: #767470;           /* AA on white for small text */
    --cds-border: rgba(26, 26, 25, 0.12);
    --cds-border-strong: rgba(26, 26, 25, 0.28);
    --cds-text-accent: #1565c9;
    --cds-accent-bg: rgba(21, 101, 201, 0.08);
    --cds-radius: 4px;
    /* Voice grammar: the USER'S CONTENT speaks in the brand's humanist
       sans — the same family as claude.ai itself — at reading sizes with
       generous line-height; CHROME AND ANNOTATION share the family one
       step smaller and quieter. What carries the iA spirit is not a
       typeface but the posture: one paper, typography first, chrome
       that recedes. The MONO register survives only where it earns its
       seat: formulas and references, where 0/O and = are load-bearing.
       A surface never mixes roles: content speaks, chrome whispers. */
    --cds-font-voice: var(--cds-font-sans);
    --cds-font-formula: "Anthropic Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    --cds-text-danger: #b3261e;
    --cds-font-sans: "Anthropic Sans", ui-sans-serif, -apple-system, sans-serif;
    --cds-font-mono: "Anthropic Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
    font-family: var(--cds-font-voice);
    /* Counter the artifact skeleton's :root{color-scheme:light} so UA
       chrome (scrollbars, select popups, resize grips) follows the theme. */
    color-scheme: light dark;
  }
  /* Dark mode, iA-register values. The artifacts viewer forwards the
     viewer theme into this document: it stamps
     html[data-theme="light"|"dark"] for an explicit theme, and removes
     the stamp for "system" so prefers-color-scheme takes over — these
     two rules cover both paths, and an explicit light stamp wins over a
     dark OS. Print stays light below. */
  :root[data-theme="light"] { color-scheme: light; }
  :root[data-theme="dark"] {
    color-scheme: dark;
    --cds-surface-0: #151514;
    --cds-surface-1: #151514;
    --cds-surface-2: #151514;
    --cds-text-primary: #ededea;
    --cds-text-secondary: #b5b3aa;
    --cds-text-muted: #8f8d86;
    --cds-border: rgba(237, 237, 234, 0.12);
    --cds-border-strong: rgba(237, 237, 234, 0.28);
    --cds-text-accent: #5da0f2;
    --cds-text-danger: #f2756a;
    --cds-accent-bg: rgba(93, 160, 242, 0.12);
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      color-scheme: dark;
      --cds-surface-0: #151514;
      --cds-surface-1: #151514;
      --cds-surface-2: #151514;
      --cds-text-primary: #ededea;
      --cds-text-secondary: #b5b3aa;
      --cds-text-muted: #8f8d86;
      --cds-border: rgba(237, 237, 234, 0.12);
      --cds-border-strong: rgba(237, 237, 234, 0.28);
      --cds-text-accent: #5da0f2;
      --cds-text-danger: #f2756a;
      --cds-accent-bg: rgba(93, 160, 242, 0.12);
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; background: var(--cds-surface-0); color: var(--cds-text-primary);
    /* The publish wrap declares its own body font — a direct declaration
       beats :root inheritance, so the editor voice must live here too. */
    font-family: var(--cds-font-voice);
  }
  /* KIT:tokens:end */

  /* KIT:chrome:begin — the editor chrome: toolbar band, buttons, canvas,
     comment bubble and composer. One implementation for the family. The
     chrome recedes until pointed at — the text is the interface; only
     the save status keeps full presence, since trust in it is the
     product. */
  .toolbar {
    position: sticky; top: 0; z-index: 22;
    display: flex; align-items: center; gap: 2px;
    padding: 10px 16px;
    background: var(--cds-surface-2);
    font-family: var(--cds-font-sans);
  }
  .toolbar button, .toolbar select, .tb-sep {
    opacity: 0.65; transition: opacity 0.15s ease;
  }
  @media (prefers-contrast: more) {
    .toolbar button, .toolbar select, .tb-sep { opacity: 1; transition: none; }
  }
  /* Discoverability: the toolbar greets at full presence, receding once
     the writer starts (or after a few seconds). */
  .toolbar.fresh button, .toolbar.fresh select, .toolbar.fresh .tb-sep { opacity: 1; }
  .toolbar:hover button, .toolbar:focus-within button,
  .toolbar:hover select, .toolbar:focus-within select,
  .toolbar:hover .tb-sep, .toolbar:focus-within .tb-sep { opacity: 1; }
  .toolbar button, .toolbar select {
    appearance: none; border: 1px solid transparent; background: none;
    color: var(--cds-text-secondary); font-family: var(--cds-font-sans);
    font-size: 13px; line-height: 1; padding: 6px 8px; border-radius: var(--cds-radius);
    display: inline-flex; align-items: center; gap: 4px;
    cursor: pointer; min-width: 30px;
  }
  .toolbar select { padding-right: 4px; }
  .toolbar button:hover, .toolbar select:hover { color: var(--cds-text-primary); background: var(--cds-accent-bg); }
  .toolbar button:disabled, .toolbar select:disabled { opacity: 0.25; cursor: default; background: none; }
  .toolbar button.on { color: var(--cds-text-accent); background: var(--cds-accent-bg); }
  .tb-sep { width: 1px; height: 18px; background: var(--cds-border); margin: 0 8px; }
  .tb-right { margin-left: auto; display: flex; align-items: center; gap: 10px; font-size: 12px; font-variant-numeric: tabular-nums; color: var(--cds-text-muted); }
  .tb-status { white-space: nowrap; color: var(--cds-text-secondary); opacity: 1; }
  .canvas { padding: 20px 24px 120px; }
  .cbub {
    position: absolute; z-index: 20; transform: translate(-50%, 0);
    font-family: var(--cds-font-sans); font-size: 13px;
    background: var(--cds-surface-1); border: 1px solid var(--cds-border-strong);
    border-radius: 999px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    padding: 6px 12px; cursor: pointer; white-space: nowrap;
    color: var(--cds-text-primary);
  }
  .cbub:hover { background: var(--cds-accent-bg); }
  .ccomposer {
    position: absolute; z-index: 21; width: 300px;
    background: var(--cds-surface-1); border: 1px solid var(--cds-border-strong);
    border-radius: var(--cds-radius); box-shadow: 0 6px 24px rgba(0,0,0,0.12);
    padding: 10px; font-family: var(--cds-font-sans);
  }
  .ccomposer .crow { display: flex; justify-content: flex-end; gap: 8px; margin-top: 8px; align-items: center; }
  .ccomposer .cnote { margin-right: auto; font-size: 11px; color: var(--cds-text-secondary); }
  .ccomposer button {
    font-family: var(--cds-font-sans); font-size: 13px; border-radius: var(--cds-radius); cursor: pointer;
    padding: 6px 12px; border: 1px solid var(--cds-border-strong); background: none; color: var(--cds-text-primary);
  }
  .ccomposer button.primary { background: var(--cds-text-accent); border-color: var(--cds-text-accent); color: var(--cds-surface-0); }
  .cquote { border-left: 2px solid var(--cds-text-accent); padding: 2px 8px; margin: 0 0 8px; font-size: 12px; color: var(--cds-text-secondary); max-height: 48px; overflow: hidden; }
  .cpanel {
    position: fixed; top: 0; right: 0; bottom: 0; width: 300px; z-index: 9;
    background: var(--cds-surface-1); border-left: 1px solid var(--cds-border);
    font-family: var(--cds-font-sans); font-size: 13px;
    overflow-y: auto; padding: 14px; box-shadow: -4px 0 16px rgba(0,0,0,0.06);
  }
  .cpanel h2 { font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; margin: 0 0 12px; color: var(--cds-text-secondary); }
  .cpanel .citem { border: 1px solid var(--cds-border); border-radius: var(--cds-radius); padding: 8px 10px; margin-bottom: 8px; }
  .cpanel .citem .cwho { font-weight: 600; font-size: 12px; }
  .cpanel .citem .cwhen { color: var(--cds-text-muted); font-size: 11px; margin-left: 6px; }
  .cpanel .citem .cq { color: var(--cds-text-secondary); font-size: 12px; border-left: 2px solid var(--cds-text-accent); padding-left: 6px; margin: 4px 0; overflow: hidden; max-height: 34px; }
  .cpanel .citem .cbody { margin-top: 2px; white-space: pre-wrap; }
  .cpanel .cempty { color: var(--cds-text-muted); }
  .cpanel .cact { display: flex; gap: 6px; margin-top: 6px; }
  .cpanel .cact button, .cpanel .cshowresolved, .cpanel .crow-reply button {
    appearance: none; border: 1px solid var(--cds-border); background: none;
    color: var(--cds-text-secondary); font-family: var(--cds-font-sans); font-size: 11px;
    border-radius: var(--cds-radius); padding: 3px 8px; cursor: pointer;
  }
  .cpanel .cact button:hover, .cpanel .cshowresolved:hover, .cpanel .crow-reply button:hover { border-color: var(--cds-border-strong); color: var(--cds-text-primary); }
  .cpanel .cshowresolved { margin-top: 4px; }
  .cpanel .creply { margin: 4px 0 0 10px; padding-left: 8px; border-left: 2px solid var(--cds-border); font-size: 12px; }
  .cpanel .crow-reply { display: flex; gap: 6px; margin-top: 6px; }
  .cpanel .citem.cfocus { border-color: var(--cds-text-accent); background: var(--cds-accent-bg); }
  @media (prefers-reduced-motion: no-preference) {
    [data-ccount].pulse { animation: kit-pulse 600ms ease-out; }
    @keyframes kit-pulse { 0% { transform: scale(1); } 35% { transform: scale(1.35); } 100% { transform: scale(1); } }
  }
  .toolbar button[data-cpanel-toggle] { opacity: 1; font-size: 12px; }
  .cmark { background: var(--cds-accent-bg); border-bottom: 1px solid var(--cds-text-accent); }
  /* Resting comment-anchor mark: a quiet accent underline only; the
     wash is reserved for hover and panel focus. */
  .visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
  /* The anchor mark is a change-bar in the margin, not an underline a
     reader mistakes for a rule. */
  .canchor { position: relative; }
  .canchor::before {
    content: ""; position: absolute; left: -14px; top: 2px; bottom: 2px;
    width: 3px; border-radius: 2px; background: var(--cds-text-accent); opacity: 0.5;
  }
  .canchor:hover { background: var(--cds-accent-bg); }
  .canchor:hover::before { opacity: 1; }
  :focus-visible { outline: 2px solid var(--cds-text-accent); outline-offset: 1px; }
  @media (prefers-reduced-motion: no-preference) {
    .cpanel, .ccomposer, .cbub { animation: kit-enter 140ms ease-out; }
    @keyframes kit-enter { from { opacity: 0; transform: translateY(2px); } to { opacity: 1; transform: none; } }
  }
  /* KIT:chrome:end */

  /* ── The sheet (kind-specific): a wider page holding the grid, the
     formula bar under the toolbar, generated row numbers and column
     letters, and sort affordances on the letters. ─────────────────── */
  .fbar {
    position: sticky; top: 41px; z-index: 9;
    display: flex; align-items: center; gap: 8px;
    padding: 5px 12px;
    background: var(--cds-surface-1);
    border-bottom: 1px solid var(--cds-border);
    font-family: var(--cds-font-sans); font-size: 13px;
  }
  .fbar .fref {
    min-width: 44px; text-align: center; padding: 3px 6px;
    border: 1px solid var(--cds-border); border-radius: 4px;
    color: var(--cds-text-secondary); font-variant-numeric: tabular-nums;
  }
  .fbar .fx { color: var(--cds-text-muted); font-style: italic; }
  .fbar input {
    flex: 1; border: none; outline: none; background: none;
    color: var(--cds-text-primary); font: 13px var(--cds-font-formula); padding: 3px 4px;
  }
  .page.sheet {
    /* The grid owns the viewport: no card, no page metaphor. */
    padding: 0 0 48px;
    font-size: 14px; line-height: 1.5;
  }
  .sheet-head { padding: 4px 0 10px; }
  .page.sheet h1 { font-size: 20px; line-height: 1.3; margin: 0 0 4px; font-weight: 700; }
  .purpose { margin: 0 0 18px; color: var(--cds-text-secondary); font-family: var(--cds-font-sans); }
  .docmeta { font-family: var(--cds-font-sans); font-size: 13px; color: var(--cds-text-secondary); margin: 0 0 18px; display: flex; gap: 10px; align-items: center; }
  /* One status garment family-wide: quiet letterspaced caps. */
  .status { display: inline-block; font-weight: 700; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--cds-text-secondary); white-space: nowrap; }
  .gridwrap { overflow-x: auto; }
  .sheet table {
    border-collapse: collapse;
    font-family: var(--cds-font-sans); font-variant-numeric: tabular-nums;
  }
  .sheet td.filler, .sheet th.cl-filler { min-width: 110px; }
  .sheet-head { max-width: 68ch; }
  .sortchip {
    appearance: none; border: 1px solid var(--cds-border); background: var(--cds-accent-bg);
    color: var(--cds-text-secondary); font-family: var(--cds-font-sans); font-size: 11px;
    border-radius: 999px; padding: 2px 10px; cursor: pointer; margin-top: 6px;
  }
  .sortchip:hover { border-color: var(--cds-border-strong); color: var(--cds-text-primary); }
  .sheet td.rsel, .sheet th.rsel { background: var(--cds-accent-bg); }
  .fstats { margin-left: auto; font-size: 12px; color: var(--cds-text-secondary); font-variant-numeric: tabular-nums; }
  .sheet td.local-note { position: relative; }
  .sheet td.local-note::after {
    content: "view only"; position: absolute; top: 1px; right: 3px;
    font: 9px var(--cds-font-sans); color: var(--cds-text-accent); letter-spacing: 0.04em;
  }
  .sheet tr.cl th:not(.corner):not(.cl-filler) { cursor: pointer; }
  .sheet thead tr.cl th:not(.corner):not(.cl-filler):not([aria-sort]):hover::after { content: " ▲"; font-size: 9px; color: var(--cds-text-muted); }
  .sheet th, .sheet td {
    border: 1px solid var(--cds-border);
    padding: 6px 10px; text-align: left; min-width: 84px;
  }
  .sheet td:focus, .sheet th:focus { outline: 2px solid var(--cds-text-accent); outline-offset: -2px; }
  .sheet thead tr.cl th {
    background: var(--cds-surface-2); color: var(--cds-text-muted);
    font-weight: 500; font-size: 12px; text-align: center;
    padding: 3px 6px; user-select: none; min-width: 0;
  }
  .sheet thead tr.cl th:not(.corner):not(.cl-filler):hover { color: var(--cds-text-accent); }
  .sheet thead tr.cl th[aria-sort]::after { content: " ▲"; font-size: 9px; }
  .sheet thead tr.cl th[aria-sort="descending"]::after { content: " ▼"; }
  .sheet thead tr.cols th {
    background: var(--cds-surface-2); font-weight: 600;
    border-bottom: 1px solid var(--cds-border-strong);
  }
  /* Row numbers come from the ORIGINAL-order stamps (what references
     mean), not the view order a sort creates. Totals address as Σ. */
  .sheet th.rn {
    background: var(--cds-surface-2); color: var(--cds-text-muted);
    font-weight: 500; font-size: 12px; text-align: center;
    min-width: 0; width: 40px; padding: 6px 8px; user-select: none;
  }
  .sheet tbody th.rn::before { content: attr(data-rn); }
  .sheet td.num, .sheet th.num { text-align: right; font-variant-numeric: tabular-nums; }
  .sheet td.fx { color: var(--cds-text-accent); }
  .sheet td.fxerr { color: var(--cds-text-danger); }
  .sheet tfoot td, .sheet tfoot th,
  .sheet tr.totals-row td, .sheet tr.totals-row th { font-weight: 600; border-top: 2px solid var(--cds-border-strong); }
  .notes { margin-top: 20px; font-family: var(--cds-font-sans); font-size: 13px; color: var(--cds-text-secondary); }
  .notes h2 { font-size: 13px; font-weight: 600; margin: 0 0 6px; color: var(--cds-text-primary); }
  .notes li { margin-bottom: 4px; }

  @media print {
    :root, :root[data-theme="dark"], :root:not([data-theme="light"]) {
      --cds-surface-0: #ffffff; --cds-surface-1: #ffffff; --cds-surface-2: #ffffff;
      --cds-text-primary: #0b0b0b; --cds-text-secondary: #52514e; --cds-text-muted: #898781;
      --cds-border: rgba(11, 11, 11, 0.1); --cds-border-strong: rgba(11, 11, 11, 0.2);
      --cds-text-accent: #184f95; --cds-accent-bg: transparent;
    }
    .toolbar, .fbar, .cbub, .ccomposer, .cpanel, .sortchip { display: none; }
    .sheet td.local-note::after { content: none; }
    .canvas { padding: 0; }
    .page.sheet { box-shadow: none; border: none; max-width: none; padding: 0; }
  }
</style>

<!-- TOOLBAR (sheet variant): undo/redo + save status. Toolbar markup is
     per kind; the shared kit styles (KIT:chrome) and wires (KIT:editor)
     whatever controls a kind carries. -->
<div class="toolbar" role="toolbar" aria-label="Formatting">
  <button data-cmd="undo" title="Undo" aria-label="Undo"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5.5 3 2.5 6l3 3"/><path d="M2.5 6h7a4 4 0 0 1 0 8H6"/></svg></button>
  <button data-cmd="redo" title="Redo" aria-label="Redo"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.5 3l3 3-3 3"/><path d="M13.5 6h-7a4 4 0 0 0 0 8H10"/></svg></button>
  <button data-cpanel-toggle title="All comments" aria-label="All comments" aria-expanded="false"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 3.5h11v7h-6l-3 3v-3h-2z"/></svg> <span data-ccount>0</span></button>
  <span class="tb-right">
    <span class="tb-status" data-status role="status">Saved</span>
  </span>
</div>
<!-- /TOOLBAR -->
<div class="fbar">
  <span class="fref" data-ref>—</span>
  <span class="fx">fx</span>
  <input data-finput placeholder="Select a cell — type = to start a formula (SUM, AVERAGE, IF…)" aria-label="Cell value or formula">
</div>

<div class="canvas">
<article class="page sheet" data-comment-empty="No comments yet — select cell text, or press Ctrl+Alt+M (Cmd+Alt+M) on any cell">

  <div class="sheet-head">
  <p class="docmeta" contenteditable="false">
    <span class="status"><!-- SLOT: STATUS — where the sheet is right now: Draft, In review, Decided, or Final -->Draft</span>
    <span><!-- SLOT: SHEET_META — owner and date, e.g. "Riley Chen · June 2026" -->Owner · Month Year</span>
  </p>

  <h1><!-- SLOT: TITLE_H1 — same name as the tab title -->Sheet title</h1>

  <p class="purpose"><!-- SLOT: PURPOSE — one sentence: what this sheet tracks and what a reader should do with it -->What this sheet tracks, in one sentence.</p>
  </div>

  <div class="gridwrap">
  <table>
    <thead>
      <!-- The column-letter row and row numbers are generated at load;
           author only the named columns and the data. -->
      <tr class="cols">
        <th class="rn corner" contenteditable="false"></th>
        <!-- SLOT: COLUMNS
             One <th> per attribute. Units and currency go in the header
             ("Cost (USD)"), not in every cell; numeric columns get
             class="num" on the <th> and every cell below it. -->
        <th>First column</th>
        <th class="num">Numeric column</th>
      </tr>
    </thead>
    <tbody>
      <!-- SLOT: ROWS
           One tr per record: a leading th class="rn" (left empty — the
           row number is generated), then cells in column order,
           class="num" matching the column. Keep cells plain values —
           one fact per cell, no prose paragraphs. -->
      <tr><th class="rn"></th><td>First record</td><td class="num">1,200</td></tr>
      <tr><th class="rn"></th><td>Second record</td><td class="num">800</td></tr>
    </tbody>
    <!-- SLOT: TOTALS (optional) — a tfoot row of editable cells: a
         label, then per-column figures. A cell whose text starts with
         '=' is a live formula (e.g. =SUM(B1:B2)) — it recomputes as the
         data changes, shows its source while being edited, and persists
         as the formula. Omit when totals add nothing. -->
    <tfoot>
      <tr><th class="rn corner" contenteditable="false"></th><td>Total</td><td class="num">2,000</td></tr>
    </tfoot>
  </table>
  </div>

  <!-- SLOT: NOTES (optional) — assumptions and caveats behind the
       numbers, as a short list. Omit when there are none. -->
  <section class="notes">
    <h2>Notes</h2>
    <ul>
      <li>First assumption behind the numbers.</li>
    </ul>
  </section>

  <p class="cstore" hidden aria-hidden="true" contenteditable="false"><!-- SLOT: COMMENTS_STORE — leave as an empty JSON array; readers comments accumulate here -->[]</p>

</article>
</div>

<script>
  // KIT:editor:begin — toolbar wiring: the page is the editing surface,
  // the toolbar drives the live selection; word count and a save status
  // ride the right side. Toolbar markup is per kind; this wiring is
  // byte-shared and treats every control as optional.
  (() => {
    const page = document.querySelector('.page')
    const toolbar = document.querySelector('.toolbar')
    if (!page || !toolbar) return
    toolbar.addEventListener('mousedown', ev => {
      // Everything but the select — its native picker is its mousedown default action.
      if (!ev.target.closest('select')) ev.preventDefault()
    })
    // Run an editing command. The live-edit op vocabulary cannot express
    // structure — a formatBlock or list toggle could destroy server-annotated
    // elements no commit can ever restore — so structural commands refuse
    // outright on annotated docs. Everything works on classic pages.
    // \`structural\` must name every block-replacing command a family toolbar ships.
    const structural = ['formatBlock', 'insertUnorderedList', 'insertOrderedList']
    // Firefox removed script-triggered undo/redo (execCommand returns
    // false there) — disable the buttons up front with the chord as the
    // pointer, instead of a click that reports success and does nothing.
    if (!(document.queryCommandSupported && document.queryCommandSupported('undo'))) {
      for (const b of toolbar.querySelectorAll('button[data-cmd]')) {
        if (b.dataset.cmd === 'undo' || b.dataset.cmd === 'redo') {
          b.disabled = true
          b.title = 'Use Ctrl+Z / Cmd+Z'
        }
      }
    }
    // Annotation is decided at publish, so the controls that can never
    // work on a live doc are disabled up front instead of dying silently.
    if (page.querySelector('[data-id]')) {
      for (const b of toolbar.querySelectorAll('button[data-cmd]')) {
        if (structural.includes(b.dataset.cmd)) {
          b.disabled = true
          b.title = 'Not available on live docs yet'
        }
      }
      const bs = toolbar.querySelector('select[data-block]')
      if (bs) {
        bs.disabled = true
        bs.title = 'Not available on live docs yet'
      }
    }
    const runCmd = (cmd, arg) => {
      const sel = document.getSelection()
      if (!sel || !sel.rangeCount) return false
      if (!page.contains(sel.getRangeAt(0).commonAncestorContainer)) return false
      if (structural.includes(cmd) && page.querySelector('[data-id]')) return false
      return document.execCommand(cmd, false, arg)
    }
    // One predicate for "a reply draft is live": the toolbar and the
    // style picker must never disagree about what counts as a draft.
    const anyReplyDrafting = () => [...document.querySelectorAll('.cpanel .crow-reply iframe')].some(f => {
      const d = f.contentDocument
      const ins0 = d ? d.querySelectorAll('input') : []
      // A typed byline is a draft too — same predicate as the panel's
      // close guard.
      return ins0.length && (ins0[0].value.trim() !== '' ||
        (ins0[1] && ins0[1].value.trim() !== (ins0[1].dataset.prefill || '').trim()))
    })
    toolbar.addEventListener('click', ev => {
      const btn = ev.target.closest('button[data-cmd]')
      if (!btn) return
      // Clicks land while the composer keeps focus (mousedown is prevented):
      // commands must not touch the page selection mid-draft. The composer
      // hosts its textarea in its own iframe (own document, own undo
      // stack on Blink and Gecko; WebKit's is per-page — a recorded
      // limitation), so undo/redo need no mid-draft handling here — the
      // selection-targeted commands still must not fire from outside the
      // page while a draft is live (.has-draft is the composer's signal).
      const ae = document.activeElement
      // A focused reply draft (an iframe under the comments panel) is
      // mid-typing like the composer's fields: commands must not run.
      if (ae && (ae.tagName === 'TEXTAREA' || (ae.closest && (ae.closest('.ccomposer') || (ae.tagName === 'IFRAME' && ae.closest('.cpanel')))))) return
      // A parked reply draft carries the composer's has-draft weight.
      if ((document.querySelector('.ccomposer.has-draft') || anyReplyDrafting()) && !(ae && ae.closest && ae.closest('.page'))) return
      // The callout is a TOGGLE: inside a blockquote it unwraps back to
      // a paragraph instead of nesting quote-in-quote.
      let cmd2 = btn.dataset.cmd
      let arg2 = btn.dataset.arg ?? undefined
      if (cmd2 === 'formatBlock' && arg2 === 'blockquote') {
        const sel2 = document.getSelection()
        const n2 = sel2 && sel2.anchorNode
        if (n2 && (n2.nodeType === 1 ? n2 : n2.parentElement).closest('blockquote')) arg2 = 'p'
      }
      if (runCmd(cmd2, arg2)) page.focus()
      refresh()
    })
    const blockSel = toolbar.querySelector('select[data-block]')
    // Disabled at init on live docs and never re-enabled — the tracker
    // would maintain state its only consumer can never read.
    if (blockSel && !blockSel.disabled) {
      // The select steals focus — track the page's last selection live, so
      // the picked style lands on the block the user was in.
      let lastRange = null, lastEl = null, lastTag = 'p'
      document.addEventListener('selectionchange', () => {
        // Composer keystrokes pin the page selection — the tracker would
        // recompute values it already holds.
        const tae = document.activeElement
        if (tae && tae.closest && tae.closest('.ccomposer')) return
        const sel = document.getSelection()
        if (!sel || !sel.rangeCount) return
        const r = sel.getRangeAt(0)
        if (!page.contains(r.commonAncestorContainer)) return
        lastRange = r.cloneRange()
        const n = r.commonAncestorContainer
        const el = n.nodeType === 1 ? n : n.parentElement
        lastEl = el && el.closest('[data-id], h1, h2, h3, p, blockquote, li') || el
        const b = el && el.closest('h1, h2, h3')
        lastTag = b ? b.tagName.toLowerCase() : 'p'
      })
      blockSel.addEventListener('change', () => {
        // The select exempts itself from mousedown-prevent, so a mid-draft
        // pick steals focus: a live draft outranks restyling the page.
        const aeSel = document.activeElement
        if (aeSel && aeSel.tagName === 'IFRAME' && aeSel.closest && aeSel.closest('.cpanel')) { blockSel.value = lastTag; return }
        if (document.querySelector('.ccomposer.has-draft') || anyReplyDrafting()) { blockSel.value = lastTag; return }
        const sel = document.getSelection()
        const preInPage = sel && sel.rangeCount &&
          page.contains(sel.getRangeAt(0).commonAncestorContainer)
        const restorable = lastRange && lastEl && lastEl !== page && lastEl.isConnected
        // A focus-seeded caret is not user intent: decide trust before focusing.
        if (!preInPage && !restorable) { blockSel.value = lastTag; return }
        page.focus()
        if (restorable) {
          sel.removeAllRanges(); sel.addRange(lastRange.cloneRange())
        }
        if (!runCmd('formatBlock', blockSel.value)) blockSel.value = lastTag
      })
    }
    const words = toolbar.querySelector('[data-words]')
    // The O(document) word walk stays off the selectionchange path —
    // caret moves can't change the count.
    let wordsRaf = 0
    const refreshWords = () => {
      // innerText forces layout, so the keystroke path pays at most one
      // post-layout read per frame, not a reflow per input event.
      if (!words || wordsRaf) return
      wordsRaf = requestAnimationFrame(() => {
        wordsRaf = 0
        // innerText separates blocks and skips the hidden store; textContent
        // fuses Enter-split block boundaries, so it is only the fallback.
        const it = page.innerText
        let n
        if (typeof it === 'string') n = (it.trim().match(/\\S+/g) || []).length
        else {
          const store = page.querySelector('.cstore')
          const storeWords = store ? (store.textContent.trim().match(/\\S+/g) || []).length : 0
          n = (page.textContent.trim().match(/\\S+/g) || []).length - storeWords
        }
        words.textContent = n === 1 ? '1 word' : n + ' words'
      })
    }
    const refresh = () => {
      for (const b of toolbar.querySelectorAll('button[data-cmd]')) {
        const c = b.dataset.cmd
        if (['bold', 'italic', 'underline', 'strikeThrough'].includes(c)) {
          const on = document.queryCommandState(c)
          b.classList.toggle('on', on)
          b.setAttribute('aria-pressed', on ? 'true' : 'false')
        } else if (c === 'formatBlock' && b.dataset.arg === 'blockquote') {
          const sel2 = document.getSelection()
          const n2 = sel2 && sel2.anchorNode
          const inQuote = !!(n2 && (n2.nodeType === 1 ? n2 : n2.parentElement).closest('blockquote'))
          b.classList.toggle('on', inQuote)
          b.setAttribute('aria-pressed', inQuote ? 'true' : 'false')
        }
      }
      const sel = document.getSelection()
      if (blockSel && sel && sel.anchorNode && page.contains(sel.anchorNode)) {
        const el = sel.anchorNode.nodeType === 1 ? sel.anchorNode : sel.anchorNode.parentElement
        const block = el && el.closest('h1, h2, h3, p, blockquote, li')
        if (block) {
          const tag = block.tagName.toLowerCase()
          blockSel.value = ['h1', 'h2', 'h3'].includes(tag) ? tag : 'p'
        }
      }
    }
    document.addEventListener('selectionchange', () => {
      // Composer keystrokes fire selectionchange while the page selection
      // is pinned — toolbar state provably cannot change there.
      const ae = document.activeElement
      if (ae && ae.closest && ae.closest('.ccomposer')) return
      refresh()
    })
    page.addEventListener('input', () => { refresh(); refreshWords() })
    // First-run presence: full toolbar until the writer starts.
    {
      const tb = document.querySelector('.toolbar')
      if (tb) {
        tb.classList.add('fresh')
        const settle = () => tb.classList.remove('fresh')
        setTimeout(settle, 6000)
        page.addEventListener('input', settle, { once: true })
      }
    }
    refresh()
    refreshWords()
  })();
  // KIT:editor:end

  // KIT:comment:begin — select-to-comment: a selection raises a Comment
  // bubble (and Ctrl/Cmd+Alt+M opens the composer — the editable surface
  // swallows bare shortcuts, so keyboard commenting needs a chord); the
  // composer files into the document's OWN comment store (the hidden
  // .cstore block) over the same set-text path as every edit, so every
  // viewer sees every comment with no external capability involved.
  // Point anchor at the selection start.
  (() => {
    const page = document.querySelector('.page')
    if (!page) return
    let bubble = null
    let composer = null
    let bubbleDelay = null
    let bubbleSettled = false
    let panelOpenSilent = false
    // Captured drafts whose items are not in the rendered set (a
    // just-resolved thread, an unreadable store) park here until their
    // item renders again — a re-render must never eat typed text. A
    // parked capture drops its focused flag: it describes an iframe
    // the rebuild destroyed, and a parked draft never steals focus.
    const draftStash = new Map()
    const clear = el => { if (el && el.parentNode) el.parentNode.removeChild(el) }
    // Comments live IN the document: one hidden annotated block (.cstore)
    // holds the serialized list, and appends ride the same set-text
    // vocabulary as every other edit — durable on live docs, view-local
    // on classic ones, no external capability involved. Every stored
    // string is other people's input: rendered with textContent, never
    // markup. IDENTITY SEAM (documented, not active): the entry schema
    // reserves an author id field for the user capability's opaque
    // per-organization tokens (resolved live, per viewer, via
    // profiles()); writing such a token into doc content is a mint site
    // in that program's enumeration, so activation is coordinated there
    // — shipped code stores only commenter-typed bylines or nothing.
    const storeEl = () => page.querySelector('.cstore')
    const isLiveEntry = e => e && typeof e === 'object' && !e.resolved
    const cLive = document.createElement('span')
    cLive.className = 'visually-hidden'
    cLive.setAttribute('aria-live', 'polite')
    document.body.appendChild(cLive)
    const announceComment = msg => { cLive.textContent = ''; setTimeout(() => { cLive.textContent = msg }, 30) }
    const readStore = () => {
      const el = storeEl()
      if (!el) return null
      try {
        const arr = JSON.parse(el.textContent)
        if (!Array.isArray(arr)) return null
        // Foreign-written entries can lack ids — or carry duplicate or
        // non-string ones. Every verb keys on a unique string, so anything
        // else re-mints (first occurrence keeps a duplicated id) — and a
        // mint may never take an id ANY entry carries, or it would steal
        // a later entry's persisted id.
        const carried = new Set()
        for (const e of arr) {
          if (e && typeof e === 'object' && typeof e.id === 'string' && e.id) carried.add(e.id)
        }
        const seen = new Set()
        arr.forEach((e, i) => {
          if (!e || typeof e !== 'object') return
          if (typeof e.id !== 'string' || !e.id || seen.has(e.id)) {
            let id = 'cpos' + i
            while (carried.has(id) || seen.has(id)) id += 'x'
            e.id = id
          }
          seen.add(e.id)
        })
        return arr
      } catch { return null }
    }
    const appendComment = entry => {
      const el = storeEl()
      if (!el) return false
      // Read at the moment of the write: the freshest local truth is
      // the DOM the observer keeps current, so a remote append observed
      // since load survives the rewrite. The whole list still recommits
      // as one set-text, so two appends inside one sync window can
      // last-write-win (a documented limit until comments get
      // per-entry blocks).
      const arr = readStore()
      if (arr === null) return false
      arr.push(entry)
      el.textContent = JSON.stringify(arr)
      // One notification channel: the textContent write above fires the
      // store observer, which refreshes the count, panel, and marks.
      el.dispatchEvent(new CustomEvent('kit-commit', { bubbles: true }))
      return true
    }
    let lastByline = ''
    document.addEventListener('keydown', e => {
      // Physical key — with Alt held, layouts compose e.key (Option+M → 'µ').
      if (!(e.altKey && (e.ctrlKey || e.metaKey) && (e.code === 'KeyM' || e.key === 'm' || e.key === 'M'))) return
      // AltGr reports ctrl+alt, indistinguishable from the chord: off the
      // page (composer, per-kind inputs) typing µ wins; on it the chord does.
      if (e.getModifierState && e.getModifierState('AltGraph') &&
          !(e.target && e.target.closest && e.target.closest('.page'))) return
      const sel = document.getSelection()
      if (!sel || !sel.rangeCount) return
      const range = sel.getRangeAt(0)
      if (!page.contains(range.commonAncestorContainer)) return
      if (sel.isCollapsed) {
        // A collapsed caret inside an anchored block: the chord opens
        // that block's conversation instead of a new composer.
        const node = range.startContainer
        const holder = (node.nodeType === 1 ? node : node.parentElement)
        const anchorEl = holder && holder.closest ? holder.closest('.canchor') : null
        if (anchorEl && anchorEl.dataset.canchorId) {
          e.preventDefault()
          if (!panel && ptoggle) ptoggle.click()
          requestAnimationFrame(() => {
            const item = document.getElementById('cpanel-' + anchorEl.dataset.canchorId)
            if (item) {
              item.scrollIntoView({ block: 'nearest' })
              const go = item.querySelector('.cact button')
              if (go) go.focus()
            }
          })
        }
        return
      }
      e.preventDefault()
      openComposer(range.cloneRange(), sel.toString())
    })
    let bubbleRange = null
    let bubbleText = ''
    const sameRange = (a, b) => a && b &&
      a.compareBoundaryPoints(Range.START_TO_START, b) === 0 &&
      a.compareBoundaryPoints(Range.END_TO_END, b) === 0
    document.addEventListener('selectionchange', () => {
      const sel = document.getSelection()
      const range = sel && !sel.isCollapsed && sel.rangeCount ? sel.getRangeAt(0) : null
      if (!range || !page.contains(range.commonAncestorContainer)) {
        // Any bail must disarm a pending settle: its late re-dispatch
        // would land back here and strand the settled flag true.
        clearTimeout(bubbleDelay); bubbleSettled = false
        clear(bubble); bubble = null; bubbleRange = null; return
      }
      // While a composer is open the bubble stays retired — bail before
      // getBoundingClientRect forces a layout per keystroke.
      if (composer) { clearTimeout(bubbleDelay); bubbleSettled = false; return }
      // Composer keystrokes and drag steps land here constantly — an
      // unchanged selection reuses the bubble untouched; a changed one
      // repositions the same node instead of rebuilding it.
      if (bubble && sameRange(range, bubbleRange)) return
      // Programmatic roving selections are navigation, not intent.
      if (page.dataset.rovingSelect) { clearTimeout(bubbleDelay); bubbleSettled = false; return }
      // A TRUE settling delay: every real event while no pill exists
      // re-arms the timer and returns; only the timer's own settled
      // re-dispatch may create the pill.
      if (!bubble) {
        if (!bubbleSettled) {
          clearTimeout(bubbleDelay)
          bubbleDelay = setTimeout(() => {
            bubbleSettled = true
            document.dispatchEvent(new Event('selectionchange'))
          }, 300)
          return
        }
        bubbleSettled = false
      }
      const rect = range.getBoundingClientRect()
      if (rect.width === 0 && rect.height === 0) {
        clear(bubble); bubble = null; bubbleRange = null; return
      }
      if (!bubble) {
        bubble = document.createElement('button')
        bubble.className = 'cbub'
        bubble.textContent = 'Comment'
        bubble.title = 'Comment on this selection (Ctrl+Alt+M / Cmd+Alt+M)'
        bubble.setAttribute('aria-keyshortcuts', 'Control+Alt+M Meta+Alt+M')
        bubble.contentEditable = 'false'
        // Prevented mousedown protects the page selection and does not
        // cancel the click — which is also what keyboard and assistive
        // tech dispatch, so one activation listener serves all three.
        bubble.addEventListener('mousedown', ev => ev.preventDefault())
        bubble.addEventListener('click', () => {
          openComposer(bubbleRange.cloneRange(), bubbleText)
        })
        document.body.appendChild(bubble)
      }
      bubbleRange = range.cloneRange()
      bubbleText = sel.toString()
      // style.left positions the pill's CENTER (translate(-50%)): clamp
      // against half the measured width so neither edge can clip.
      const half = (bubble.offsetWidth / 2) || 55
      bubble.style.left = Math.max(scrollX + 8 + half, Math.min(rect.left + rect.width / 2 + scrollX,
        scrollX + document.documentElement.clientWidth - 8 - half)) + 'px'
      bubble.style.top = rect.bottom + 6 + scrollY + 'px'
    })
    const ANCHOR_BLOCK_TAGS = /^(P|H1|H2|H3|H4|H5|H6|LI|UL|OL|BLOCKQUOTE|ASIDE|SECTION|ARTICLE|DIV|TABLE|TR|TD|TH|DT|DD|FIGCAPTION|CAPTION|PRE|FIGURE|DL|MAIN|HEADER|FOOTER|NAV|SUMMARY|DETAILS|ADDRESS|HGROUP|FIELDSET|FORM|HR)$/
    const anchorFor = range => {
      // A kind may know a more durable space for this selection (the
      // sheet's stamp-space cells): its builder gets first claim, so
      // the bubble path and the chord path file identical anchors.
      if (page.kitAnchorBuilder) {
        const built = page.kitAnchorBuilder(range)
        if (built !== undefined) return built
      }
      let el = range.startContainer
      if (el.nodeType !== 1) el = el.parentElement
      // Anchors must outlive the edit vocabulary: set-text flattens
      // inline marks, so a hop through one dies on the block's first
      // commit. Climb to the nearest block-level element (mirroring
      // KIT:persist's BLOCK_TAGS classification) before recording hops.
      while (el && el !== page && !ANCHOR_BLOCK_TAGS.test(el.tagName)) el = el.parentElement
      // A select-all puts the boundary on the page itself — descend to
      // the first block the range touches, or the path records empty.
      if (el === page) el = [...page.children].find(c => range.intersectsNode(c)) || page.children[0] || el
      const hops = []
      for (let n = el; n && n !== page; n = n.parentElement) {
        const parent = n.parentElement
        if (!parent) break
        hops.unshift(n.tagName.toLowerCase() + ':' + [...parent.children].indexOf(n))
      }
      const r = range.getBoundingClientRect()
      const p = page.getBoundingClientRect()
      return {
        path: hops.join('/'),
        x: Math.min(1, Math.max(0, (r.left - p.left) / p.width)),
        y: Math.min(1, Math.max(0, (r.top - p.top) / p.height)),
      }
    }
    // Per-kind chrome (a slide rail, a cell affordance) requests a
    // composer through this event — ranges are the one comment anchor
    // vocabulary, so kinds never reach into this region's scope.
    // An anchored block is an invitation: clicking it opens the panel
    // scrolled to its conversation (modifier-free click on the mark's
    // block, only when no text is being selected).
    page.addEventListener('click', e => {
      const el = e.target && e.target.closest ? e.target.closest('.canchor') : null
      if (!el) return
      const sel = document.getSelection()
      if (sel && !sel.isCollapsed) return
      // renderMarks materializes the entry id on the mark itself — the
      // same read the chord path uses, so every route opens one answer.
      const id = el.dataset.canchorId
      if (!id) return
      if (!panel && ptoggle) {
        // The reader was placing a caret: the panel opens for context,
        // but the keyboard stays where they clicked.
        panelOpenSilent = true
        ptoggle.click()
        panelOpenSilent = false
      }
      requestAnimationFrame(() => {
        const item = document.getElementById('cpanel-' + id)
        if (item) {
          item.scrollIntoView({ block: 'nearest' })
          item.classList.add('cfocus')
          setTimeout(() => item.classList.remove('cfocus'), 1600)
        }
      })
    })
    // The page side of the copy-forcing drag contract: one permanent
    // listener, keyed on the draft marker type, so a draft-originated
    // drop onto the page copies instead of moving text out of the draft.
    page.addEventListener('dragover', ev => {
      if (ev.dataTransfer && ev.dataTransfer.types && ev.dataTransfer.types.includes('application/x-cdraft')) {
        ev.preventDefault()
        ev.dataTransfer.dropEffect = 'copy'
      }
    })
    document.addEventListener('kit-comment-on', e => {
      const d = e.detail
      if (d && d.range) openComposer(d.range.cloneRange(), String(d.quote || d.range.toString()), d.anchor)
    })
    // The all-comments panel: renders the store, live count in the
    // toolbar, click-through to each comment's anchor. Text lands via
    // textContent only — every stored string is other people's input.
    const ptoggle = document.querySelector('[data-cpanel-toggle]')
    const pcount = document.querySelector('[data-ccount]')
    let panel = null
    // One anchor resolver: walk the stored path, verify each hop's
    // recorded tag, return the element or null.
    const resolveAnchor = a => {
      // Per-kind anchor spaces first: a kind may install a resolver for
      // anchors that outlive DOM order (the sheet's original-row cells).
      if (page.kitAnchorResolver && a) {
        const el = page.kitAnchorResolver(a)
        if (el !== undefined) return el
      }
      if (!a || typeof a.path !== 'string' || !a.path) return null
      let el = page
      for (const hop of a.path.split('/')) {
        const [tag, idxStr] = hop.split(':')
        const idx = Number(idxStr)
        el = el && el.children && Number.isInteger(idx) ? el.children[idx] : null
        if (!el || el.tagName.toLowerCase() !== tag) return null
      }
      return el === page ? null : el
    }
    const fmtWhen = iso => {
      const d = new Date(iso)
      return Number.isNaN(d.getTime()) ? '' : d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' })
    }
    const flashAnchor = entry => {
      const el = resolveAnchor(entry && entry.anchor)
      if (!el) return false
      // A kind may need to surface the anchor first (the slides select
      // the owning slide) — announce before scrolling.
      document.dispatchEvent(new CustomEvent('kit-reveal-anchor', { detail: { element: el } }))
      el.scrollIntoView({ block: 'center', behavior: 'smooth' })
      el.classList.add('cmark')
      setTimeout(() => el.classList.remove('cmark'), 1600)
      return true
    }
    // Anchor marks: display-layer decoration only — resolved at render
    // from the stored paths, never written back. aria-details ties the
    // block to the panel for assistive tech.
    const renderMarks = () => {
      for (const el of page.querySelectorAll('.canchor')) {
        el.classList.remove('canchor')
        el.removeAttribute('aria-details')
        el.removeAttribute('aria-description')
        delete el.dataset.canchorId
      }
      const arr = readStore()
      if (!arr) return
      for (const entry of arr) {
        if (!isLiveEntry(entry)) continue
        const el = resolveAnchor(entry.anchor)
        if (el) {
          el.classList.add('canchor')
          // Always-on AT visibility, panel open or closed; aria-details
          // only while its IDREF target (the panel item) exists.
          el.setAttribute('aria-description', 'Has a comment — press Ctrl+Alt+M to open the conversation')
          if (panel && entry.id) el.setAttribute('aria-details', 'cpanel-' + entry.id)
          el.dataset.canchorId = entry.id || ''
        }
      }
    }
    let showResolved = false
    const renderPanel = () => {
      if (!panel) return
      // A re-render preserves what the reader holds: every open reply
      // draft (by entry id, both fields, and caret) and the focused
      // control (by entry id + a stable key) come back after the rebuild.
      const draftStates = [...panel.querySelectorAll('.crow-reply iframe')].map(fr2 => {
        const d0 = fr2.contentDocument
        const ins0 = d0 ? d0.querySelectorAll('input') : []
        if (!ins0.length) return null
        return {
          id: (fr2.closest('.citem') || {}).id || '',
          fp: ((fr2.closest('.citem') || {}).dataset || {}).cfp || '',
          value: ins0[0].value,
          byline: ins0[1] ? ins0[1].value : '',
          prefill: ins0[1] ? (ins0[1].dataset.prefill || '') : '',
          selStart: ins0[0].selectionStart, selEnd: ins0[0].selectionEnd,
          focused: document.activeElement === fr2
            ? (d0.activeElement === ins0[1] ? 2 : 1) : 0,
        }
      }).filter(Boolean)
      for (const [sid, ds] of draftStash) {
        if (!draftStates.some(d => d.id === sid)) draftStates.push(ds)
      }
      draftStash.clear()
      const draftFocused = draftStates.some(d => d.focused)
      const af = document.activeElement
      const focusState = af && panel.contains(af) && !(af.tagName === 'IFRAME' && af.closest('.crow-reply')) ? {
        itemId: (af.closest('.citem') || {}).id || '',
        label: (af.dataset && af.dataset.act) || af.textContent || af.getAttribute('aria-label') || '',
      } : null
      panel.textContent = ''
      const h = document.createElement('h2')
      h.textContent = 'Comments'
      panel.appendChild(h)
      const arr = readStore()
      if (arr === null) {
        for (const ds of draftStates) draftStash.set(ds.id, { ...ds, focused: 0 })
        const em = document.createElement('p')
        em.className = 'cempty'
        em.textContent = storeEl() ? 'Comments are unreadable in this document' : 'This document has no comment store'
        panel.appendChild(em)
        // The focused control just got wiped: keep the keyboard in the
        // panel rather than dropping it to the page body.
        if (focusState || draftFocused) { em.setAttribute('tabindex', '-1'); em.focus() }
        return
      }
      const live = arr.filter(isLiveEntry)
      const renderable = arr.filter(e => e && typeof e === 'object')
      if (!renderable.length) {
        for (const ds of draftStates) draftStash.set(ds.id, { ...ds, focused: 0 })
        const em = document.createElement('p')
        em.className = 'cempty'
        em.textContent = page.dataset.commentEmpty || 'No comments yet — select some text to add one'
        panel.appendChild(em)
        if (focusState || draftFocused) { em.setAttribute('tabindex', '-1'); em.focus() }
        return
      }
      const done = arr.filter(e => e && typeof e === 'object' && e.resolved)
      // Reply rows open through a per-item opener so the restore path can
      // reopen one WITHOUT focus — a parked draft must never steal the
      // keyboard from the control the reader was on.
      const replyOpeners = new Map()
      const renderItem = entry => {
        const item = document.createElement('div')
        item.className = 'citem'
        item.id = 'cpanel-' + String(entry.id || '')
        // The restore path verifies this before re-attaching a parked
        // draft: positional ids can move, entry content does not.
        item.dataset.cfp = JSON.stringify([entry.text, entry.name, entry.at].map(x => x == null ? null : String(x)))
        const whoRow = document.createElement('div')
        const whoEl = document.createElement('span')
        whoEl.className = 'cwho'
        whoEl.textContent = typeof entry.name === 'string' && entry.name ? entry.name : 'Anonymous'
        const whenEl = document.createElement('span')
        whenEl.className = 'cwhen'
        whenEl.textContent = fmtWhen(String(entry.at || ''))
        whoRow.append(whoEl, whenEl)
        const qEl = document.createElement('p')
        qEl.className = 'cq'
        qEl.textContent = String(entry.quote || '')
        const bodyEl = document.createElement('p')
        bodyEl.className = 'cbody'
        bodyEl.textContent = String(entry.text || '')
        // One level of replies, collected now and attached BELOW the
        // comment body — a thread reads downward.
        const replyEls = []
        if (Array.isArray(entry.replies)) {
          for (const rep of entry.replies) {
            if (!rep || typeof rep !== 'object') continue
            const rEl = document.createElement('p')
            rEl.className = 'creply'
            const rw = document.createElement('span')
            rw.className = 'cwho'
            rw.textContent = typeof rep.name === 'string' && rep.name ? rep.name : 'Anonymous'
            rEl.appendChild(rw)
            rEl.appendChild(document.createTextNode(' ' + String(rep.text || '')))
            replyEls.push(rEl)
          }
        }
        const act = document.createElement('div')
        act.className = 'cact'
        const go = document.createElement('button')
        go.type = 'button'
        go.dataset.act = 'goto'
        go.textContent = 'Go to'
        go.setAttribute('aria-label', 'Go to this comment in the document')
        go.addEventListener('click', () => {
          if (!focusAnchor(entry)) {
            qEl.textContent = "Can’t find this spot anymore — the text may have changed"
          }
        })
        const rs = document.createElement('button')
        rs.type = 'button'
        // The focus key must survive the Resolve↔Reopen label flip.
        rs.dataset.act = 'resolve'
        rs.textContent = entry.resolved ? 'Reopen' : 'Resolve'
        rs.addEventListener('click', () => setResolved(entry.id, !entry.resolved, entry.text))
        const rp = document.createElement('button')
        rp.type = 'button'
        rp.dataset.act = 'reply'
        rp.textContent = 'Reply'
        const openReply = focus => {
          const have = item.querySelector('.crow-reply')
          if (have) {
            if (focus) {
              const d0 = have.querySelector('iframe').contentDocument
              const i0 = d0 && d0.querySelector('input')
              if (i0) i0.focus()
            }
            return have
          }
          const row = document.createElement('div')
          row.className = 'crow-reply'
          // The reply draft gets the composer's isolation: its own
          // document keeps page and draft undo histories apart, and
          // cross-boundary drags copy instead of moving.
          const fr = document.createElement('iframe')
          fr.setAttribute('title', 'Reply draft')
          fr.style.cssText = 'display:block;flex:1;min-width:0;height:64px;border:0'
          const send = document.createElement('button')
          send.type = 'button'
          send.textContent = 'Send'
          row.append(fr, send)
          item.appendChild(row)
          const fdoc = fr.contentDocument
          fdoc.addEventListener('dragstart', ev => {
            if (ev.dataTransfer) ev.dataTransfer.setData('application/x-cdraft', '1')
          })
          fdoc.addEventListener('dragover', ev => {
            if (!ev.dataTransfer) return
            if (ev.dataTransfer.types && ev.dataTransfer.types.includes('application/x-cdraft')) return
            ev.preventDefault()
            ev.dataTransfer.dropEffect = 'copy'
          })
          const root = getComputedStyle(document.documentElement)
          fdoc.head.appendChild(Object.assign(fdoc.createElement('style'), {textContent:
            ':root{color-scheme:' + (root.colorScheme || 'light dark') + '}' +
            'body{margin:0}input{display:block;width:100%;box-sizing:border-box;' +
            'font:12px ' + root.getPropertyValue('--cds-font-sans') + ';' +
            'color:' + root.getPropertyValue('--cds-text-primary') + ';' +
            'background:' + root.getPropertyValue('--cds-surface-0') + ';' +
            'border:1px solid ' + root.getPropertyValue('--cds-border') + ';' +
            'border-radius:4px;padding:4px 7px}input+input{margin-top:4px}'}))
          const inp = fdoc.createElement('input')
          inp.placeholder = 'Reply…'
          inp.setAttribute('aria-label', 'Reply to this comment')
          fdoc.body.appendChild(inp)
          // The byline is visible, prefilled, and clearable: the stored
          // name is exactly the field's text — cleared posts anonymously.
          const who = fdoc.createElement('input')
          who.placeholder = 'Your name (optional)'
          who.value = lastByline
          // The prefill is a convenience, not a draft: only user-modified
          // byline text counts for the close guard below.
          who.dataset.prefill = who.value
          who.setAttribute('aria-label', 'Your name')
          fdoc.body.appendChild(who)
          send.addEventListener('click', () => {
            const t = inp.value.trim()
            if (!t) return
            // The same read-append-recommit path appends ride — and the
            // same one-window last-write-wins caveat applies.
            const el2 = storeEl()
            const arr2 = readStore()
            if (!el2 || !arr2) return
            const target = arr2.find(x => x && typeof x === 'object' && x.id === entry.id)
            // A backfilled id is positional: if the store shifted since
            // render, the text check turns a wrong-thread write into a no-op.
            if (!target || (String(entry.id).indexOf('cpos') === 0 && target.text !== entry.text)) return
            if (!Array.isArray(target.replies)) target.replies = []
            const typed = who.value.trim()
            if (typed) lastByline = typed
            target.replies.push({ text: [...t].slice(0, 500).join(''), name: typed ? [...typed].slice(0, 60).join('') : undefined, at: new Date().toISOString() })
            // Retire the draft before the store write: the re-render
            // must not resurrect sent text as a pending draft, and the
            // typed byline becomes the row's clean baseline.
            inp.value = ''
            who.dataset.prefill = who.value
            el2.textContent = JSON.stringify(arr2)
            el2.dispatchEvent(new CustomEvent('kit-commit', { bubbles: true }))
            announceComment('Reply added')
          })
          fdoc.addEventListener('keydown', ev => {
            // IME composition Enters pick a candidate, never send.
            if (ev.isComposing || ev.keyCode === 229) return
            if (ev.key === 'Enter') { ev.preventDefault(); send.click() }
            // Keys never cross the iframe boundary: Escape parks the
            // draft from inside — the keyboard lands back on Reply.
            if (ev.key === 'Escape') { ev.preventDefault(); rp.focus() }
          })
          if (focus) inp.focus()
          return row
        }
        rp.addEventListener('click', () => { openReply(true) })
        replyOpeners.set(item.id, openReply)
        act.append(go, rs, rp)
        item.append(whoRow, qEl, bodyEl, ...replyEls, act)
        panel.appendChild(item)
      }
      live.forEach(renderItem)
      if (done.length) {
        const tg = document.createElement('button')
        tg.type = 'button'
        tg.dataset.act = 'showresolved'
        tg.className = 'cshowresolved'
        tg.textContent = (showResolved ? 'Hide' : 'Show') + ' resolved (' + done.length + ')'
        tg.addEventListener('click', () => { showResolved = !showResolved; renderPanel() })
        panel.appendChild(tg)
        if (showResolved) done.forEach(renderItem)
      }
      // Restore the reply drafts and focus captured above — after BOTH
      // sections render, so drafts and controls on resolved items restore too.
      for (const ds of draftStates) {
        const opener = replyOpeners.get(ds.id)
        // A positional id can change owners mid-draft (a foreign insert or
        // delete): a fingerprint mismatch stashes the draft rather than
        // transplanting it into a different conversation.
        const tgt = ds.id ? panel.querySelector('#' + CSS.escape(ds.id)) : null
        if (!opener || (ds.fp && tgt && tgt.dataset.cfp !== ds.fp)) { draftStash.set(ds.id, { ...ds, focused: 0 }); continue }
        const row = opener(false)
        const d1 = row && row.querySelector('iframe').contentDocument
        const ins = d1 ? d1.querySelectorAll('input') : []
        if (!ins.length) continue
        ins[0].value = ds.value
        if (ins[1]) {
          ins[1].value = ds.byline
          // The dirty baseline travels with the draft: a restored row must
          // not inherit a NEW prefill, or the close guard false-positives.
          if (ds.prefill !== undefined) ins[1].dataset.prefill = ds.prefill
        }
        if (ds.focused === 2 && ins[1]) ins[1].focus()
        else if (ds.focused === 1) {
          ins[0].focus()
          try { ins[0].setSelectionRange(ds.selStart, ds.selEnd) } catch {}
        }
      }
      // A parked draft and a focused control can coexist: the drafts come
      // back silently, the keyboard goes back to the control.
      if (focusState && !draftFocused) {
        const item = focusState.itemId ? panel.querySelector('#' + CSS.escape(focusState.itemId)) : null
        const btn = item
          ? [...item.querySelectorAll('button')].find(b => ((b.dataset && b.dataset.act) || b.textContent || b.getAttribute('aria-label') || '') === focusState.label)
          : [...panel.querySelectorAll('button')].find(b => !b.closest('.citem') && ((b.dataset && b.dataset.act) || b.textContent || '') === focusState.label)
        if (btn) btn.focus()
        else if (focusState.itemId && !item) {
          // Resolving can move the item out of the live list: keep the
          // keyboard in the panel, on the toggle that still reaches it.
          const tg2 = panel.querySelector('.cshowresolved')
          if (tg2) tg2.focus()
        }
        // The heading (and a deleted item with nothing resolved) has no
        // button to return to: the fresh heading keeps the keyboard in.
        if (!panel.contains(document.activeElement)) {
          const h2f = panel.querySelector('h2')
          if (h2f) { h2f.setAttribute('tabindex', '-1'); h2f.focus() }
        }
      }
    }
    // Resolve/reopen rewrites the one entry and recommits the store —
    // the same wholesale set-text path appends ride.
    const setResolved = (id, val, expectText) => {
      if (!id) return
      const el = storeEl()
      if (!el) return
      const arr = readStore()
      if (!arr) return
      const e = arr.find(x => x && typeof x === 'object' && x.id === id)
      if (!e) return
      // Same positional-id caveat as the reply path: verify before writing.
      if (String(id).indexOf('cpos') === 0 && e.text !== expectText) return
      if (val) e.resolved = true
      else delete e.resolved
      announceComment(val ? 'Comment resolved' : 'Comment reopened')
      el.textContent = JSON.stringify(arr)
      el.dispatchEvent(new CustomEvent('kit-commit', { bubbles: true }))
    }
    // Panel activation moves FOCUS to the anchor block (not just scroll):
    // the keyboard lands where the conversation is.
    const focusAnchor = entry => {
      const ok = flashAnchor(entry)
      const el = resolveAnchor(entry && entry.anchor)
      if (el && typeof el.focus === 'function') {
        if (!el.hasAttribute('tabindex')) el.setAttribute('tabindex', '-1')
        el.focus({ preventScroll: true })
      }
      return ok
    }
    const refreshCount = () => {
      if (!pcount) return
      const arr = readStore()
      const n = arr ? arr.filter(isLiveEntry).length : 0
      pcount.textContent = String(n)
      if (ptoggle) ptoggle.setAttribute('aria-label', 'All comments (' + n + ')')
    }
    if (ptoggle) {
      ptoggle.addEventListener('click', () => {
        if (panel) {
          // Mirrors the composer's has-draft guard: closing must not eat
          // a typed reply — the draft gets the keyboard instead.
          const fr2 = [...panel.querySelectorAll('.crow-reply iframe')].find(f => {
            const d0 = f.contentDocument
            const ins0 = d0 ? d0.querySelectorAll('input') : []
            // A typed byline is a draft too — compared against its own
            // prefill, so the convenience text alone never blocks a close.
            return ins0.length && (ins0[0].value.trim() !== '' ||
              (ins0[1] && ins0[1].value.trim() !== (ins0[1].dataset.prefill || '').trim()))
          })
          if (fr2) {
            // Land the keyboard on the field that blocks the close — a
            // byline-only draft otherwise points at an empty text field.
            const ins1 = fr2.contentDocument.querySelectorAll('input')
            const tgt = ins1[0].value.trim() ? ins1[0] : ins1[1] || ins1[0]
            tgt.focus()
            announceComment('A reply draft is open — send or clear it first')
            return
          }
          clear(panel); panel = null
          renderMarks()
          ptoggle.setAttribute('aria-expanded', 'false')
        } else {
          panel = document.createElement('aside')
          panel.className = 'cpanel'
          panel.setAttribute('aria-label', 'All comments')
          panel.addEventListener('keydown', ev => {
            // An IME Escape cancels the candidate, not the conversation —
            // without the bail it would close the panel and kill the draft.
            if (ev.isComposing || ev.keyCode === 229) return
            if (ev.key === 'Escape') {
              ev.preventDefault()
              ptoggle.click()
              // The close can bail into a draft: only a real close hands
              // the keyboard back to the toggle.
              if (!panel) ptoggle.focus()
            }
          })
          // Below the sticky toolbar: its opaque band keeps the save
          // status and word count visible while the panel is open.
          const tb = document.querySelector('.toolbar')
          if (tb) panel.style.top = tb.getBoundingClientRect().height + 'px'
          document.body.appendChild(panel)
          renderPanel()
          renderMarks()
          ptoggle.setAttribute('aria-expanded', 'true')
          const h0 = panel.querySelector('h2')
          // A live composer draft keeps the keyboard: the panel still
          // opens, silently, like the anchor-click path.
          if (h0 && !panelOpenSilent && !document.querySelector('.ccomposer.has-draft')) { h0.setAttribute('tabindex', '-1'); h0.focus() }
        }
      })
    }
    // A collaborator's comment arrives as a server-applied write to the
    // store block, not a local event — observe the block so the count
    // and an open panel track remote appends too.
    {
      const st = storeEl()
      if (st) new MutationObserver(() => {
        refreshCount(); renderMarks()
        // Drafts and focus survive the rebuild (renderPanel captures
        // and restores them), so the panel can always follow the store.
        renderPanel()
        if (pcount && !document.body.classList.contains('present')) {
          pcount.classList.remove('pulse')
          void pcount.offsetWidth
          pcount.classList.add('pulse')
        }
      }).observe(st, { childList: true, characterData: true, subtree: true })
    }
    refreshCount()
    renderMarks()
    // The textarea lives in the composer's own iframe: on Blink and
    // Gecko its document carries its own undo stack, so page and draft
    // history never interleave there (WebKit's undo manager is
    // per-page — a recorded limitation). The .has-draft class on the
    // host div is the cross-region signal for a non-empty draft.
    const openComposer = (range, quoted, anchorOverride) => {
      // A mid-draft re-trigger focuses the draft instead of destroying it.
      // One predicate for "is there a draft": the .has-draft class the
      // signal maintains — the re-trigger guard and the mid-draft guards
      // must never disagree about what counts.
      if (composer && composer.classList.contains('has-draft')) {
        const fr0 = composer.querySelector('iframe')
        const d0 = fr0 && fr0.contentDocument
        const draft = d0 && d0.querySelector('textarea')
        const byline = d0 && d0.querySelector('input')
        const target = draft && draft.value.trim() ? draft : byline || draft
        if (target) target.focus()
        return
      }
      clear(composer); clear(bubble); bubble = null
      composer = document.createElement('div')
      composer.className = 'ccomposer'
      composer.setAttribute('role', 'dialog')
      composer.setAttribute('aria-label', 'New comment')
      composer.contentEditable = 'false'
      const rect = range.getBoundingClientRect()
      composer.style.left = Math.max(scrollX + 8, Math.min(rect.left + scrollX,
        scrollX + document.documentElement.clientWidth - 308)) + 'px'
      composer.style.top = rect.bottom + 8 + scrollY + 'px'
      const q = document.createElement('p')
      q.className = 'cquote'
      q.textContent = [...quoted].slice(0, 140).join('')
      const fr = document.createElement('iframe')
      fr.setAttribute('title', 'Comment draft')
      fr.style.cssText = 'display:block;width:100%;height:122px;border:0'
      composer.append(fr)
      document.body.appendChild(composer)
      const fdoc = fr.contentDocument
      // Engine note: Blink and Gecko give this document its own undo
      // stack, which is the isolation this design rests on. WebKit's
      // undo manager is per-page, so on Safari a parked draft and page
      // edits can still interleave under Cmd+Z — a known limitation
      // recorded in the PR until a WebKit-scoped treatment ships.
      // A text drag BETWEEN the page and the draft must never MOVE: the
      // source-side deletion would be attributed and committed like any
      // edit. Drags that stay inside the draft keep native move
      // semantics — the guards are origin-aware via a marker type.
      fdoc.addEventListener('dragstart', ev => {
        if (ev.dataTransfer) ev.dataTransfer.setData('application/x-cdraft', '1')
      })
      fdoc.addEventListener('dragover', ev => {
        if (!ev.dataTransfer) return
        if (ev.dataTransfer.types && ev.dataTransfer.types.includes('application/x-cdraft')) return
        ev.preventDefault()
        ev.dataTransfer.dropEffect = 'copy'
      })
      const root = getComputedStyle(document.documentElement)
      fdoc.head.appendChild(Object.assign(fdoc.createElement('style'), {textContent:
        ':root{color-scheme:' + (root.colorScheme || 'light dark') + '}' +
        'body{margin:0}textarea{width:100%;height:80px;resize:none;box-sizing:border-box;' +
        'margin-bottom:6px;' +
        'font:14px ' + root.getPropertyValue('--cds-font-sans') + ';' +
        'color:' + root.getPropertyValue('--cds-text-primary') + ';' +
        'background:' + root.getPropertyValue('--cds-surface-0') + ';' +
        'border:1px solid ' + root.getPropertyValue('--cds-border') + ';' +
        'border-radius:4px;padding:8px}'}))
      const ta = fdoc.createElement('textarea')
      ta.placeholder = 'Comment on this selection…'
      fdoc.body.appendChild(ta)
      // The byline shares the textarea's document: ANY parent-document
      // text entry would rejoin the page's undo stack and accept
      // move-semantics drops — the isolation must cover every field.
      const who = fdoc.createElement('input')
      who.placeholder = 'Your name (optional)'
      // The prefill is a convenience, not a draft: only user-modified
      // byline text counts for the draft predicates below.
      who.value = lastByline
      const bylinePrefill = who.value
      who.setAttribute('aria-label', 'Your name')
      who.style.cssText = 'width:100%;box-sizing:border-box;font:12px ' +
        root.getPropertyValue('--cds-font-sans') + ';color:' + root.getPropertyValue('--cds-text-primary') +
        ';background:' + root.getPropertyValue('--cds-surface-0') + ';border:1px solid ' +
        root.getPropertyValue('--cds-border') + ';border-radius:4px;padding:5px 7px'
      fdoc.body.appendChild(who)
      // A typed byline is a draft too: the re-trigger guard and the
      // mid-draft signals must protect it like body text.
      const own0 = composer
      const draftSignal = () => {
        if (own0.isConnected) own0.classList.toggle('has-draft', ta.value.trim() !== '' || who.value.trim() !== bylinePrefill.trim())
      }
      ta.addEventListener('input', draftSignal)
      who.addEventListener('input', draftSignal)
      const row = document.createElement('div')
      row.className = 'crow'
      const note = document.createElement('span')
      note.className = 'cnote'
      note.setAttribute('role', 'status')
      note.textContent = !storeEl() ? 'This document has no comment store'
        : readStore() === null ? 'Comments are unreadable in this document' : ''
      const cancel = document.createElement('button')
      cancel.textContent = 'Cancel'
      cancel.addEventListener('click', () => {
        clear(composer); composer = null
        // Focus returns to the conversation's place, not the void.
        const back = resolveAnchor(anchorOverride || anchorFor(range))
        if (back) {
          if (!back.hasAttribute('tabindex')) back.setAttribute('tabindex', '-1')
          back.focus({ preventScroll: true })
        }
      })
      const post = document.createElement('button')
      post.className = 'primary'
      post.textContent = 'Comment'
      post.addEventListener('click', () => {
        const textVal = ta.value.trim()
        if (textVal === '') return
        const entry = {
          id: 'c' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
          quote: [...String(quoted)].slice(0, 140).join(''),
          text: [...textVal].slice(0, 500).join(''),
          at: new Date().toISOString(),
          anchor: anchorOverride || anchorFor(range),
        }
        const typed = who.value.trim()
        if (typed) { entry.name = [...typed].slice(0, 60).join(''); lastByline = typed }
        if (appendComment(entry)) {
          clear(composer); composer = null
          announceComment('Comment added')
          const back = resolveAnchor(entry.anchor)
          if (back) {
            if (!back.hasAttribute('tabindex')) back.setAttribute('tabindex', '-1')
            back.focus({ preventScroll: true })
          }
        } else {
          note.textContent = storeEl() ? 'Comments are unreadable in this document' : 'This document has no comment store'
        }
      })
      // Document-level: the dialog shortcuts serve BOTH fields. IME
      // composition keys (Escape cancels the candidate, not the draft)
      // must never reach them.
      fdoc.addEventListener('keydown', e => {
        if (e.isComposing || e.keyCode === 229) return
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') { e.preventDefault(); post.click() }
        // A live draft outranks a reflexive Escape: the keyboard goes to
        // the draft; Cancel stays one click away.
        if (e.key === 'Escape') { e.preventDefault(); if (composer.classList.contains('has-draft')) ta.focus(); else cancel.click() }
      })
      // Keyboard events never cross the iframe boundary, so the dialog's
      // parent-document action row needs the same shortcuts host-side.
      composer.addEventListener('keydown', e => {
        if (e.isComposing || e.keyCode === 229) return
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') { e.preventDefault(); post.click() }
        if (e.key === 'Escape') { e.preventDefault(); if (composer.classList.contains('has-draft')) ta.focus(); else cancel.click() }
      })
      row.append(note, cancel, post)
      composer.prepend(q)
      composer.append(row)
      ta.focus()
    }
  })();
  // KIT:comment:end

  // KIT:persist:begin — live persistence, live docs only: self.edit is the
  // live-doc write surface, so anywhere it is absent or refused (no runtime, classic
  // artifact, read-only viewer) edits stay local to this view. The
  // capability is read lazily at each use — the runtime can attach
  // window.claude a beat after inline scripts run — and presence alone
  // does not prove a live doc (a declared self-write capability mounts a
  // rejecting edit on a non-live doc), so the save status reports
  // persistence only after a first server-accepted commit.
  (() => {
    const page = document.querySelector('.page')
    const status = document.querySelector('[data-status]')
    if (!page) return
    const selfCap = () => {
      const api = window.claude && (window.claude.artifact || window.claude.self)
      return api && typeof api.edit === 'function' ? api : null
    }
    // A collaborator's commit lands as a server-applied write to a
    // block's DOM — with no local event. A baseline pinned at load would
    // then call a local revert-to-baseline a no-op and skip its commit
    // under "Saved" — the one silent drop path. Observing the blocks and
    // dropping the baseline for foreign writes makes the next flush
    // commit instead of skip: the fail-safe direction.
    // (Registered after baseline/dirty/inflight exist — see init below.)

    // Commit unit: the nearest server-annotated BLOCK (data-id). Blocks
    // edited since their last commit are flushed on blur and when the
    // caret leaves them. Plain text is what the op vocabulary carries —
    // a committed block's published bytes keep only its text.
    const dirty = new Set()
    const inflight = new Set()
    // Flatten-safe marks: a commit unit may contain these and nothing
    // else — set-text drops them from the published bytes (the op
    // vocabulary is plain text), which is the accepted degradation.
    const marks = new Set(['B', 'I', 'EM', 'STRONG', 'U', 'S', 'STRIKE', 'FONT',
      'A', 'SPAN', 'CODE', 'SUB', 'SUP', 'MARK', 'SMALL', 'ABBR', 'TIME',
      'KBD', 'CITE', 'DFN', 'VAR', 'SAMP', 'DEL', 'INS', 'BDI', 'BDO', 'DATA',
      'WBR'])
    // Block-level tags — the commit-unit and roster vocabulary.
    // Anything unenumerated (inline marks, media, foreign namespaces)
    // defaults to INLINE, so an exotic deletion can never brick commits.
    const BLOCK_TAGS = /^(P|H1|H2|H3|H4|H5|H6|LI|UL|OL|BLOCKQUOTE|ASIDE|SECTION|ARTICLE|DIV|TABLE|TR|TD|TH|DT|DD|FIGCAPTION|CAPTION|PRE|FIGURE|DL|MAIN|HEADER|FOOTER|NAV|SUMMARY|DETAILS|ADDRESS|HGROUP|FIELDSET|FORM|HR)$/
    // Block-level commit units the server knows about: committing after
    // one vanishes would publish a local merge the op vocabulary cannot
    // express. Inline ids are excluded — inline removal is already the
    // accepted set-text degradation, not structural divergence.
    // Baseline holds the server-known text per id: a flush whose text
    // matches is a no-op — sending it could revert a collaborator's
    // newer commit. The roster derives from the same walk, so the two
    // classifications can never drift apart.
    const baseline = new Map()
    for (const el of page.querySelectorAll('[data-id]')) {
      // Leaf commit units only: a container's aggregate text goes stale
      // the moment a child commits, and a stale container baseline
      // false-dirties on the next history sweep.
      if (BLOCK_TAGS.test(el.tagName) && !el.querySelector('[data-id]')) baseline.set(el.dataset.id, el.dataset.fxSrc !== undefined ? el.dataset.fxSrc : el.textContent)
    }
    const roster = [...baseline.keys()]
    const rosterIntact = () =>
      roster.every(id => page.querySelector('[data-id="' + CSS.escape(id) + '"]'))
    // Foreign-write coherence (see the note above the commit-unit rules):
    // a mutated block with no local dirty or inflight claim was written
    // by someone else — its baseline no longer describes server state.
    new MutationObserver(muts => {
      for (const m of muts) {
        const n = m.target.nodeType === 1 ? m.target : m.target.parentElement
        const holder = n && n.closest ? n.closest('[data-id]') : null
        const id = holder && holder.dataset.id
        // Formatting-only mutations leave textContent equal to the
        // baseline — only a real text divergence is a foreign write.
        // Engine-managed cells (data-fx-src) compare their SOURCE: the
        // display swap is presentation, not an edit.
        const cur = holder && holder.dataset && holder.dataset.fxSrc !== undefined ? holder.dataset.fxSrc : holder ? holder.textContent : ''
        if (id && !dirty.has(holder) && !inflight.has(id) && baseline.has(id) &&
            cur !== baseline.get(id)) {
          baseline.delete(id)
          // The live layer shows itself: a colleague's change flashes
          // where it landed (never while presenting).
          if (!document.body.classList.contains('present')) {
            holder.classList.add('cmark')
            setTimeout(() => holder.classList.remove('cmark'), 1600)
          }
        }
      }
    }).observe(page, { childList: true, characterData: true, subtree: true })
    let proven = false
    let disabled = false
    let fmtNoticeShown = false
    // Sticky once an edit lands in an untrackable block — the top-line
    // Saved claim would be false for the rest of the session.
    let degraded = false
    const say = s => { if (status) status.textContent = s }
    const rawBlockOf = node => {
      let el = node
      if (el && el.nodeType !== 1) el = el.parentElement
      // The commit unit is the nearest annotated BLOCK: climb past
      // annotated inline elements — their ids are not commit targets.
      let cand = el && el.closest('[data-id]')
      while (cand && !BLOCK_TAGS.test(cand.tagName)) {
        cand = cand.parentElement && cand.parentElement.closest('[data-id]')
      }
      return cand || null
    }
    const blockOf = node => {
      const cand = rawBlockOf(node)
      return cand && unitOk(cand) ? cand : null
    }
    // Anything beyond marks inside a unit — child blocks, images,
    // controls — would be destroyed by its set-text: degrade to Local
    // only instead. Same for a split block whose id is no longer
    // unique: committing either half would clobber the other. Checked
    // again at flush time — a block can go bad after it was dirtied.
    const unitOk = el => {
      for (const d of el.querySelectorAll('*')) {
        if (!marks.has(d.tagName)) return false
      }
      return page.querySelectorAll('[data-id="' + CSS.escape(el.dataset.id) + '"]').length === 1
    }
    let lastBlock = null
    let lastRaw = null
    // A mutation can span TWO commit units (cross-block delete, type-over,
    // drag) while the post-mutation selection names only one — resolve
    // BOTH boundary blocks of each pre-mutation target range, and degrade
    // per unresolvable boundary rather than letting the other side's
    // success mask it. Formatting inputTypes stay excluded: their
    // textContent is unchanged, and an eager dirty there could commit a
    // stale snapshot over newer collaborator text.
    page.addEventListener('beforeinput', e => {
      const t = e.inputType || ''
      if (t.startsWith('format') || t === 'insertOrderedList' || t === 'insertUnorderedList') return
      // The collapsed caret's own block is claimed here, PRE-mutation:
      // the foreign-write observer's microtask can run between this
      // event's listeners, and an unclaimed first keystroke in a clean
      // block would read as a foreign write and drop its baseline.
      {
        const sel0 = document.getSelection()
        const cand0 = sel0 && sel0.anchorNode && page.contains(sel0.anchorNode) ? rawBlockOf(sel0.anchorNode) : null
        if (cand0 && !dirty.has(cand0) && unitOk(cand0)) dirty.add(cand0)
      }
      const ranges = typeof e.getTargetRanges === 'function' ? e.getTargetRanges() : []
      for (const r of ranges) {
        if (r.collapsed && t !== 'insertFromDrop') continue
        for (const node of [r.startContainer, r.endContainer]) {
          // An already-dirty candidate skips the O(page) validation:
          // the add would be a no-op, and flush re-validates at commit.
          const cand = rawBlockOf(node)
          if (cand && dirty.has(cand)) continue
          const block = cand && unitOk(cand) ? cand : null
          if (block) dirty.add(block)
          else if (page.querySelector('[data-id]') && selfCap()) degraded = true
        }
      }
    })
    page.addEventListener('input', e => {
      const sel = document.getSelection()
      const block = sel && sel.anchorNode ? blockOf(sel.anchorNode) : null
      // A formatting-only input leaves textContent unchanged — marking
      // the block dirty would commit a stale snapshot over newer
      // collaborator text.
      const fmtInput = typeof e.inputType === 'string' &&
        (e.inputType.startsWith('format') ||
         e.inputType === 'insertOrderedList' || e.inputType === 'insertUnorderedList')
      // Formatting renders locally but never reaches other viewers on a
      // live doc — say so once, at the moment it first happens.
      if (fmtInput && selfCap() && !fmtNoticeShown &&
          !disabled && !degraded && !dirty.size && !inflight.size) {
        fmtNoticeShown = true
        say('Saved — formatting shows only in your view')
        setTimeout(() => {
          if (!dirty.size && !inflight.size) say(disabled || degraded ? 'Some edits local only' : 'Saved')
        }, 4000)
      }
      if (block && !fmtInput) {
        dirty.add(block)
        if (lastBlock && lastBlock !== block) flush(lastBlock)
        lastBlock = block
      }
      // History inputs dispatch with empty target ranges, and a composite
      // (a reverted drag) can revert TWO blocks while the selection names
      // one — sweep every block whose text differs from its baseline.
      if (e.inputType === 'historyUndo' || e.inputType === 'historyRedo') {
        for (const el of page.querySelectorAll('[data-id]')) {
          if (!BLOCK_TAGS.test(el.tagName) || el.querySelector('[data-id]')) continue
          const id = el.dataset.id
          // A missing baseline means a foreign write was observed — the
          // block must commit on the next flush regardless, so a
          // composite revert can never hide behind the dropped entry.
          const cur2 = el.dataset.fxSrc !== undefined ? el.dataset.fxSrc : el.textContent
          if (!baseline.has(id) || cur2 !== baseline.get(id)) dirty.add(el)
        }
      }
      // A block that can never flush (no data-id, or no live-doc api)
      // must resolve the status, not leave 'Editing…' frozen on screen.
      // The latch fires only when CONTENT landed — a formatting-only
      // input never makes the Saved claim false — and re-resolves after
      // the task so same-task DOM settling is seen.
      if (!block && selfCap() && !fmtInput) {
        const n = sel && sel.anchorNode
        queueMicrotask(() => {
          const live = document.getSelection()
          const probe = n && n.isConnected ? n : live && live.anchorNode
          if (!(probe && blockOf(probe))) degraded = true
        })
      }
      if (!disabled && !fmtInput) say(block && selfCap() ? 'Editing…' : 'Local only')
    })
    document.addEventListener('selectionchange', () => {
      const sel = document.getSelection()
      const cand = sel && sel.anchorNode && page.contains(sel.anchorNode)
        ? rawBlockOf(sel.anchorNode)
        : null
      // unitOk is O(page); with the caret still in the same block — valid
      // (lastBlock) or never-valid (lastRaw; its flush fired on entry and
      // flush re-validates) — both effects below are no-ops, so same-block
      // events skip the scan entirely.
      if (cand === lastBlock) { lastRaw = cand; return }
      if (cand && cand === lastRaw) return
      lastRaw = cand
      const block = cand && unitOk(cand) ? cand : null
      if (lastBlock && block !== lastBlock && dirty.has(lastBlock)) flush(lastBlock)
      if (block) lastBlock = block
    })
    const sweep = () => { for (const b of [...dirty]) flush(b) }
    page.addEventListener('blur', sweep, true)
    // Tab close and artifact switch dispatch neither blur nor a caret
    // move — the teardown sweep is the last chance to commit.
    addEventListener('pagehide', sweep)
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') sweep()
    })
    // Programmatic commits (a formula bar, a slide control) dispatch
    // 'kit-commit' on the edited element after writing its text.
    // Capture-phase — a non-bubbling dispatch must still reach this hook.
    page.addEventListener('kit-commit', e => {
      const block = blockOf(e.target)
      if (block) { dirty.add(block); flush(block) }
      else {
        if (selfCap()) degraded = true
        if (!disabled) say('Local only')
      }
    }, true)
    const flush = el => {
      const key = el.dataset.id
      if (disabled || inflight.has(key) || !dirty.has(el)) return
      const api = selfCap()
      if (api === null) { say('Local only'); return }
      if (!el.isConnected || key === undefined) {
        dirty.delete(el)
        // A corpse whose id has no connected holder is lost text.
        if (key === undefined ||
            !page.querySelector('[data-id="' + CSS.escape(key) + '"]')) degraded = true
        return
      }
      if (!unitOk(el) || !rosterIntact()) {
        // A real edit is being dropped — reaching here requires a live
        // capability, so the session's Saved claim is now false.
        degraded = true
        dirty.delete(el)
        if (!disabled) say('Local only')
        return
      }
      dirty.delete(el)
      // A kind may maintain the cell's PERSISTENT truth apart from its
      // display (the sheet's raw formulas live in data-fx-src) — commit
      // that truth, never the computed presentation.
      const text = el.dataset.fxSrc !== undefined ? el.dataset.fxSrc : el.textContent
      if (baseline.get(key) === text) {
        if (!disabled && !dirty.size && !inflight.size) {
          say(degraded ? 'Some edits local only' : 'Saved')
        }
        return
      }
      inflight.add(key)
      say('Editing…')
      // The id's current holder: native editing can replace or detach
      // the element between send and settle.
      const holderOf = () => [...dirty].find(d => d.isConnected && d.dataset.id === key) ||
        page.querySelector('[data-id="' + CSS.escape(key) + '"]')
      const onAccept = () => {
        inflight.delete(key)
        // A collaborator's write can land during the flight: if the
        // holder's text moved and no local keystroke claims it, the
        // baseline must drop (fail-safe) rather than pin the pre-await
        // snapshot over the foreign write.
        {
          const h = holderOf()
          const hcur = h && h.dataset && h.dataset.fxSrc !== undefined ? h.dataset.fxSrc : h ? h.textContent : null
          if (h && !dirty.has(h) && hcur !== text) baseline.delete(key)
          else baseline.set(key, text)
        }
        proven = true
        // An accept only comes from a live doc, so it overrides a latch
        // set by a concurrent refusal that settled while liveness was
        // unproven.
        disabled = false
        // A keystroke during the flight re-dirtied this id's block —
        // commit whichever element now holds the id. A degraded re-flush
        // already said Local only; let that stand.
        const holder = holderOf()
        if (holder && dirty.has(holder)) {
          flush(holder)
          if (!inflight.has(key) && !dirty.has(holder)) return
        }
        // Disconnected corpses left by native splits and replacements
        // would hold 'Editing…' forever; text with no surviving holder
        // is a real degrade.
        for (const d of [...dirty]) {
          if (d.isConnected) continue
          dirty.delete(d)
          const id = d.dataset.id
          if (id === undefined ||
              !page.querySelector('[data-id="' + CSS.escape(id) + '"]')) degraded = true
        }
        say(dirty.size || inflight.size ? 'Editing…'
          : degraded ? 'Some edits local only' : 'Saved')
      }
      const onReject = () => {
        inflight.delete(key)
        const holder = holderOf() || el
        if (!proven) {
          disabled = true
          // Stays dirty so a concurrent accept's latch override can
          // retry it — flush is a no-op while disabled holds.
          dirty.add(holder)
          say('Local only')
        } else {
          // Stays dirty; the next interaction retries the commit.
          dirty.add(holder)
          say('Not saved')
        }
      }
      // A host-bridged edit can throw synchronously or return a
      // non-thenable; both are refusals — only a settled accept may
      // prove liveness, or the latch leaks and saving silently stops.
      try {
        const res = api.edit([{ target: el.dataset.id, op: 'set-text', text }])
        if (res && typeof res.then === 'function') {
          Promise.resolve(res).then(onAccept, onReject)
        } else {
          onReject()
        }
      } catch {
        onReject()
      }
    }
  })();
  // KIT:persist:end

  // Sheet grid (kind-specific): generated column letters and sort, cell
  // editability, and the formula bar bound to the focused cell.
  (() => {
    const page = document.querySelector('.page')
    const table = document.querySelector('.sheet table')
    if (!page || !table || !table.tBodies[0]) return
    const colsRow = table.tHead && table.tHead.querySelector('tr.cols')
    if (!colsRow) return

    // Editable surface: column names, data cells, and totals cells are
    // plain values (plaintext-only keeps them honest with set-text);
    // generated chrome (letters, row numbers) stays inert.
    const editable = []
    for (const th of colsRow.cells) if (!th.classList.contains('rn')) editable.push(th)
    for (const row of table.tBodies[0].rows) for (const c of row.cells) if (!c.classList.contains('rn')) editable.push(c)
    if (table.tFoot) for (const row of table.tFoot.rows) for (const c of row.cells) if (!c.classList.contains('rn')) editable.push(c)
    for (const el of page.querySelectorAll('h1, .purpose, .notes h2, .notes li')) editable.push(el)
    for (const el of editable) {
      try { el.contentEditable = 'plaintext-only' } catch { el.contentEditable = 'true' }
    }

    // Column letters: one generated header row above the named columns;
    // clicking a letter sorts by that column (ascending, then
    // descending), numeric-aware, tbody only — totals stay pinned.
    // Sorting reorders the live DOM — the view, print, and the comment
    // surface all see the sorted order; the stored row order is
    // unchanged, so each viewer sorts independently.
    const letter = i => {
      let s = ''
      for (let n = i; n >= 0; n = Math.floor(n / 26) - 1) s = String.fromCharCode(65 + (n % 26)) + s
      return s
    }
    const nCols = colsRow.cells.length - 1
    const cl = document.createElement('tr')
    cl.className = 'cl'
    const corner = document.createElement('th')
    corner.className = 'corner'
    corner.contentEditable = 'false'
    cl.appendChild(corner)
    // Mirrors the engine's numeric reading: what sorts as a number is
    // exactly what computes as one.
    const numeric = text => {
      let c = String(text).trim().replace(/,/g, '')
      if (c.startsWith('$')) c = c.slice(1)
      let scale = 1
      if (c.endsWith('%')) { c = c.slice(0, -1); scale = 0.01 }
      if (c.trim() === '') return null
      const n = Number(c)
      return Number.isNaN(n) ? null : n * scale
    }
    // Grid comment anchors live in ORIGINAL-ORDER space: a sort cannot
    // point a mark at the wrong cell, and a comment filed while sorted
    // is right for every viewer. The kit calls this resolver first.
    // The inverse hook: ANY anchor built from a selection inside a grid
    // cell lands in stamp space — bubble path and chord path agree.
    page.kitAnchorBuilder = range => {
      const n = range && range.startContainer
      const holder = n && (n.nodeType === 1 ? n : n.parentElement)
      const cell = holder && holder.closest ? holder.closest('td, th') : null
      const row = cell && cell.parentElement
      if (cell && row && row.dataset.orow !== undefined) return { cell: { orow: Number(row.dataset.orow), col: cell.cellIndex } }
      return undefined
    }
    page.kitAnchorResolver = a => {
      if (!a || !a.cell) return undefined
      const tr = table.tBodies[0].querySelector('tr[data-orow="' + String(a.cell.orow) + '"]')
      return (tr && tr.cells[a.cell.col]) || null
    }

    // The sorted-state chip: the one visible record that the view is
    // reordered (view-only — the stored order is untouched).
    const sortChip = document.createElement('button')
    sortChip.type = 'button'
    sortChip.className = 'sortchip'
    sortChip.hidden = true
    sortChip.setAttribute('aria-label', 'Clear the sort and restore original order')
    const head = page.querySelector('.sheet-head')
    if (head) head.appendChild(sortChip)
    let clearSort = null
    sortChip.addEventListener('click', () => { if (clearSort) clearSort() })
    const updateSortChip = (col, dir) => {
      if (!col) { sortChip.hidden = true; clearSort = null; return }
      sortChip.hidden = false
      sortChip.textContent = 'sorted by ' + col + ' ' + (dir === 'descending' ? '↓' : '↑') + ' — view only · clear'
    }
    // Polite announcements for sort state — a dedicated live region so
    // the save-status chip keeps its own voice.
    const sr = document.createElement('span')
    sr.className = 'visually-hidden'
    sr.setAttribute('aria-live', 'polite')
    document.body.appendChild(sr)
    const announce = msg => { sr.textContent = ''; setTimeout(() => { sr.textContent = msg }, 30) }
    for (let i = 0; i < nCols; i++) {
      const th = document.createElement('th')
      th.textContent = letter(i)
      th.contentEditable = 'false'
      th.tabIndex = -1
      th.title = 'Sort by this column'
      th.setAttribute('aria-label', letter(i))
      th.setAttribute('aria-description', 'Sorts the sheet by this column')
      const sortBy = () => {
        // Three states: ascending → descending → original order.
        const cur = th.getAttribute('aria-sort')
        const next = cur === 'ascending' ? 'descending' : cur === 'descending' ? null : 'ascending'
        for (const h of cl.cells) h.removeAttribute('aria-sort')
        for (const h of colsRow.cells) h.removeAttribute('aria-sort')
        if (next) {
          th.setAttribute('aria-sort', next)
          // Browse-mode truth: the NAMED header carries the state too.
          const named = colsRow.cells[i + 1]
          if (named) named.setAttribute('aria-sort', next)
        }
        const dir = next === 'descending' ? -1 : 1
        const body = table.tBodies[0]
        const all = Array.from(body.rows)
        const rows = all.filter(r => !r.classList.contains('filler-row') && !r.classList.contains('totals-row'))
        const totals = all.filter(r => r.classList.contains('totals-row'))
        const fillers = all.filter(r => r.classList.contains('filler-row'))
        const col = i + 1
        if (next === null) {
          rows.sort((a, b) => Number(a.dataset.orow || 0) - Number(b.dataset.orow || 0))
        } else {
          rows.sort((a, b) => {
            const ta = (a.cells[col] ? a.cells[col].textContent : '').trim()
            const tb = (b.cells[col] ? b.cells[col].textContent : '').trim()
            const na = numeric(ta)
            const nb = numeric(tb)
            if (na !== null && nb !== null) return (na - nb) * dir
            return ta.localeCompare(tb) * dir
          })
        }
        for (const r of rows) body.appendChild(r)
        for (const r of totals) body.appendChild(r)
        for (const r of fillers) body.appendChild(r)
        table.dispatchEvent(new CustomEvent('kit-sorted'))
        updateSortChip(next ? letter(i) : null, next)
        clearSort = next ? () => { th.setAttribute('aria-sort', 'descending'); sortBy() } : null
        announce(next ? 'Sorted by column ' + letter(i) + ', ' + next : 'Original order restored')
      }
      th.addEventListener('click', sortBy)
      th.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sortBy() }
      })
      cl.appendChild(th)
    }
    table.tHead.insertBefore(cl, colsRow)

    // Totals hug the data: tfoot renders below every tbody row by
    // table-layout rule, so its rows relocate into the tbody tail at
    // init (data-ids ride along — element identity is what the persist
    // baseline keys on) and stay pinned between data and filler rows.
    if (table.tFoot) {
      for (const tr of [...table.tFoot.rows]) {
        tr.classList.add('totals-row')
        table.tBodies[0].appendChild(tr)
      }
      table.tFoot.remove()
    }

    // A spreadsheet is a continuous surface: pad generated empty columns
    // and rows out past the data, like any sheet app. Filler cells are
    // editable scratch space but live outside the authored data — they
    // regenerate on each load (on live docs, edits there read Local
    // only, the persistence model's standard answer for untracked cells).
    const FILL_COLS = Math.max(0, 8 - nCols)
    const FILL_ROWS = Math.max(0, 30 - table.tBodies[0].rows.length)
    for (let i = 0; i < FILL_COLS; i++) {
      const th = document.createElement('th')
      th.textContent = letter(nCols + i)
      th.contentEditable = 'false'
      th.className = 'cl-filler'
      cl.appendChild(th)
      const fh = Object.assign(document.createElement('th'), {className: 'filler'})
      try { fh.contentEditable = 'plaintext-only' } catch { fh.contentEditable = 'true' }
      colsRow.appendChild(fh)
    }
    const totalCols = nCols + FILL_COLS
    for (const tr of table.tBodies[0].rows) {
      for (let i = 0; i < FILL_COLS; i++) {
        const td = document.createElement('td')
        td.className = 'filler'
        try { td.contentEditable = 'plaintext-only' } catch { td.contentEditable = 'true' }
        tr.appendChild(td)
      }
    }
    for (let r = 0; r < FILL_ROWS; r++) {
      const tr = document.createElement('tr')
      tr.className = 'filler-row'
      const rn = document.createElement('th')
      rn.className = 'rn'
      tr.appendChild(rn)
      for (let c = 0; c < totalCols; c++) {
        const td = document.createElement('td')
        td.className = 'filler'
        try { td.contentEditable = 'plaintext-only' } catch { td.contentEditable = 'true' }
        tr.appendChild(td)
      }
      table.tBodies[0].appendChild(tr)
    }

    // ── The keyboard contract ──────────────────────────────────────
    // The grid is ONE tab stop: a roving tabindex keeps exactly one
    // cell tabbable; inside, Enter commits and moves down (Shift+Enter
    // keeps its newline), Tab moves across, Escape reverts the cell,
    // and arrows move cell focus from the text boundaries. Keyboard
    // arrival selects the cell's text, so typing replaces — F2 or a
    // click gives a caret instead.
    // The roving set includes the sort headers: one tab stop covers the
    // whole grid, arrows reach the letters, Enter/Space sorts there.
    const cells = () => [...table.querySelectorAll('td, th')].filter(c =>
      !c.classList.contains('rn') && !c.classList.contains('corner') &&
      (c.isContentEditable || (c.parentElement && c.parentElement.classList.contains('cl'))))
    const rove = active => {
      for (const c of cells()) c.tabIndex = -1
      if (active) active.tabIndex = 0
    }
    rove(cells()[0] || null)
    const entryValue = new Map()
    // Range selection lives in STAMP SPACE-adjacent display state: an
    // anchor cell plus the focused extent; Shift+arrows grow it,
    // Ctrl/Cmd+C copies it out as TSV, Delete clears it, and a live
    // SUM · COUNT reads beside the cell address. The .rsel wash is
    // navigation state, never stored.
    let rangeAnchor = null
    // Script writes (range clear, row clear, paste, fill) sit outside
    // the native undo stack — a small journal catches Cmd+Z when its
    // newest entry postdates the last native edit.
    const journal = []
    let lastNativeEdit = 0
    const journalPush = cells2 => {
      journal.push({ at: Date.now(), entries: cells2.map(c => ({ cell: c, text: c.textContent, fx: c.dataset.fxSrc })) })
      if (journal.length > 20) journal.shift()
    }
    const journalPop = () => {
      const j = journal[journal.length - 1]
      if (!j || j.at < lastNativeEdit) return false
      journal.pop()
      for (const en of j.entries) {
        if (!en.cell.isConnected) continue
        // Formula cells restore in SOURCE mode: a cleared cell lost its
        // engine entry, so adopt must re-parse — display text would flatten.
        en.cell.textContent = en.fx !== undefined ? en.fx : en.text
        if (en.fx !== undefined) en.cell.dataset.fxSrc = en.fx
        else delete en.cell.dataset.fxSrc
        en.cell.dispatchEvent(new Event('input', { bubbles: true }))
        en.cell.dispatchEvent(new CustomEvent('kit-commit', { bubbles: true }))
      }
      announce('Undid ' + j.entries.length + ' cells')
      return true
    }
    table.addEventListener('input', e => { if (e.isTrusted) lastNativeEdit = Date.now() })
    table.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && !e.shiftKey && (e.key === 'z' || e.key === 'Z')) {
        if (journalPop()) e.preventDefault()
      }
    })
    const clearRange = () => {
      for (const c of table.querySelectorAll('.rsel')) c.classList.remove('rsel')
      rangeAnchor = null
      updateRangeStats()
    }
    const rangeCells = () => [...table.querySelectorAll('.rsel')]
    const paintRange = (a, b) => {
      for (const c of table.querySelectorAll('.rsel')) c.classList.remove('rsel')
      const rows = [...table.rows]
      const r1 = rows.indexOf(a.parentElement), r2 = rows.indexOf(b.parentElement)
      const c1 = a.cellIndex, c2 = b.cellIndex
      for (let r = Math.min(r1, r2); r <= Math.max(r1, r2); r++) {
        for (let c = Math.min(c1, c2); c <= Math.max(c1, c2); c++) {
          const cell = rows[r] && rows[r].cells[c]
          if (cell && cell.isContentEditable) cell.classList.add('rsel')
        }
      }
      updateRangeStats()
    }
    const statsEl = document.createElement('span')
    statsEl.className = 'fstats'
    const fbarEl = document.querySelector('.fbar')
    if (fbarEl) fbarEl.appendChild(statsEl)
    const updateRangeStats = () => {
      const sel = rangeCells()
      if (sel.length < 2) { statsEl.textContent = ''; return }
      let sum = 0, count = 0
      for (const c of sel) {
        // The sheet's one numeric reading — the readout must agree with
        // sorting and the engine on what counts as a number.
        const n = numeric(c.textContent)
        if (n !== null) { sum += n; count++ }
      }
      statsEl.textContent = count
        ? 'SUM ' + (Math.round(sum * 100) / 100).toLocaleString('en-US') +
          ' · AVG ' + (Math.round((sum / count) * 100) / 100).toLocaleString('en-US') +
          ' · COUNT ' + count
        : ''
    }
    const moveFocus = (cell, dr, dc, selectAll, edge) => {
      const row = cell.parentElement
      let target = null
      if (dr !== 0 && edge) {
        // Wrap: land on the first/last editable cell of the next row.
        const rows = [...table.rows]
        let r = rows.indexOf(row) + dr
        while (r >= 0 && r < rows.length && !target) {
          const cands = [...rows[r].cells].filter(c => c.isContentEditable)
          target = edge === 'first' ? cands[0] : cands[cands.length - 1]
          r += dr
        }
        if (!target) return false
        rove(target)
        target.focus()
        if (selectAll) {
          // A roving selection is navigation, not intent — the comment
          // pill must not chase it (the kit reads this flag).
          page.dataset.rovingSelect = '1'
          const sel = document.getSelection()
          sel.removeAllRanges()
          const rg = document.createRange()
          rg.selectNodeContents(target)
          sel.addRange(rg)
          setTimeout(() => { delete page.dataset.rovingSelect }, 350)
        }
        return true
      }
      if (dr === 0) {
        const rovable = x => x.isContentEditable || (x.parentElement && x.parentElement.classList.contains('cl') && !x.classList.contains('corner'))
        let c = cell.cellIndex + dc
        while (c >= 0 && c < row.cells.length) {
          const cand = row.cells[c]
          if (rovable(cand)) { target = cand; break }
          c += dc
        }
      } else {
        const rows = [...table.rows]
        let r = rows.indexOf(row) + dr
        while (r >= 0 && r < rows.length) {
          const tr2 = rows[r]
          const cand = tr2 && tr2.cells[cell.cellIndex]
          const ok = cand && (cand.isContentEditable || (tr2.classList.contains('cl') && !cand.classList.contains('corner')))
          if (ok) { target = cand; break }
          r += dr
        }
      }
      if (!target) return false
      rove(target)
      target.focus()
      if (selectAll) {
        // A roving selection is navigation, not intent — the comment
        // pill must not chase it (the kit reads this flag).
        page.dataset.rovingSelect = '1'
        const sel = document.getSelection()
        sel.removeAllRanges()
        const rg = document.createRange()
        rg.selectNodeContents(target)
        sel.addRange(rg)
        setTimeout(() => { delete page.dataset.rovingSelect }, 350)
      }
      return true
    }
    const caretAtEdge = (cell, side) => {
      const sel = document.getSelection()
      if (!sel || !sel.isCollapsed || !sel.rangeCount) return false
      const r = sel.getRangeAt(0)
      const probe = document.createRange()
      probe.selectNodeContents(cell)
      probe.setEnd(r.startContainer, r.startOffset)
      const beforeLen = probe.toString().length
      if (side === 'start') return beforeLen === 0
      return beforeLen >= cell.textContent.length
    }
    table.addEventListener('focusin', e => {
      const cell = e.target.closest('td, th')
      if (cell && cell.isContentEditable) {
        rove(cell)
        // Identity on arrival: address · column name · value.
        {
          const row = cell.parentElement
          const addr = row.classList.contains('totals-row') ? '\\u03a3' + letter(cell.cellIndex - 1)
            : row.dataset.orow !== undefined ? letter(cell.cellIndex - 1) + (Number(row.dataset.orow) + 1)
            : letter(cell.cellIndex - 1)
          const name = colsRow.cells[cell.cellIndex] ? colsRow.cells[cell.cellIndex].textContent.trim() : ''
          announce(addr + (name ? ' \\u00b7 ' + name : '') + ' \\u00b7 ' + (cell.textContent.trim() || 'empty'))
        }
        // The engine's focusin (registered after this one) swaps a
        // formula cell's display to its SOURCE — snapshot after that
        // swap, or Escape would revert a formula to its computed
        // number and destroy it.
        setTimeout(() => { if (document.activeElement === cell || cell.contains(document.activeElement)) entryValue.set(cell, cell.textContent) }, 0)
      }
    })
    table.addEventListener('keydown', e => {
      const cell = e.target.closest('td, th')
      if (!cell) return
      // Sort headers own their keys (Enter/Space sorts); arrows still rove.
      if (cell.parentElement && cell.parentElement.classList.contains('cl')) {
        if (e.key === 'ArrowDown') { e.preventDefault(); moveFocus(cell, 1, 0, true) }
        if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
          e.preventDefault(); moveFocus(cell, 0, e.key === 'ArrowRight' ? 1 : -1, false)
        }
        return
      }
      if (!cell.isContentEditable) return
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault()
        cell.blur()
        if (!moveFocus(cell, 1, 0, true)) cell.focus()
      } else if (e.key === 'Tab') {
        // Horizontal first; at a row edge wrap to the next/previous row;
        // at the grid's true corners release the native Tab so the page
        // beyond stays reachable — a grid must never be a keyboard trap.
        const moved = moveFocus(cell, 0, e.shiftKey ? -1 : 1, true) ||
          moveFocus(cell, e.shiftKey ? -1 : 1, 0, true, e.shiftKey ? 'last' : 'first')
        if (moved) e.preventDefault()
      } else if (e.key === 'Escape') {
        e.preventDefault()
        const v = entryValue.get(cell)
        if (v !== undefined) {
          cell.textContent = v
          cell.dispatchEvent(new Event('input', { bubbles: true }))
        }
      } else if (e.key === 'F2') {
        e.preventDefault()
        const sel = document.getSelection()
        sel.removeAllRanges()
        const rg = document.createRange()
        rg.selectNodeContents(cell)
        rg.collapse(false)
        sel.addRange(rg)
      } else if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        if (e.shiftKey) {
          e.preventDefault()
          if (!rangeAnchor) rangeAnchor = cell
          const rows = [...table.rows]
          const nr = rows[rows.indexOf(cell.parentElement) + (e.key === 'ArrowDown' ? 1 : -1)]
          const next = nr && nr.cells[cell.cellIndex]
          if (next && next.isContentEditable) {
            rove(next); next.focus(); paintRange(rangeAnchor, next)
            announce(rangeCells().length + ' cells · ' + statsEl.textContent)
          }
          return
        }
        const sel = document.getSelection()
        if (sel && !sel.isCollapsed) return
        e.preventDefault()
        clearRange()
        moveFocus(cell, e.key === 'ArrowDown' ? 1 : -1, 0, true)
      } else if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
        if (e.shiftKey && rangeAnchor) {
          e.preventDefault()
          const next = cell.parentElement.cells[cell.cellIndex + (e.key === 'ArrowRight' ? 1 : -1)]
          if (next && next.isContentEditable) { rove(next); next.focus(); paintRange(rangeAnchor, next) }
          return
        }
        const side = e.key === 'ArrowRight' ? 'end' : 'start'
        if (caretAtEdge(cell, side)) {
          e.preventDefault()
          clearRange()
          moveFocus(cell, 0, e.key === 'ArrowRight' ? 1 : -1, true)
        }
      } else if ((e.ctrlKey || e.metaKey) && (e.key === 'c' || e.key === 'C') && rangeCells().length > 1) {
        // Copy OUT: the selection leaves as TSV — the other half of the
        // round-2 clipboard. Formula cells export their source.
        e.preventDefault()
        const sel = rangeCells()
        const byRow = new Map()
        for (const c of sel) {
          const r = c.parentElement
          if (!byRow.has(r)) byRow.set(r, [])
          byRow.get(r).push(c.dataset.fxSrc || c.textContent)
        }
        const tsv = [...byRow.values()].map(cols => cols.join('\\t')).join('\\n')
        if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(tsv).catch(() => {})
        announce('Copied ' + sel.length + ' cells')
      } else if ((e.key === 'Delete' || e.key === 'Backspace') && !e.ctrlKey && !e.metaKey && rangeCells().length > 1 && document.getSelection().isCollapsed) {
        e.preventDefault()
        const toClear = rangeCells()
        journalPush(toClear)
        for (const c of toClear) {
          c.textContent = ''
          c.dispatchEvent(new Event('input', { bubbles: true }))
          c.dispatchEvent(new CustomEvent('kit-commit', { bubbles: true }))
        }
        announce('Cleared ' + toClear.length + ' cells')
        clearRange()
      } else if ((e.ctrlKey || e.metaKey) && e.altKey && (e.code === 'KeyM' || e.key === 'm' || e.key === 'M')) {
        // Comment on the focused CELL — empty cells included: the
        // anchor is the cell itself, the quote its address and text.
        e.preventDefault()
        const rg = document.createRange()
        rg.selectNodeContents(cell)
        const row = cell.parentElement
        const inGrid = row.dataset.orow !== undefined
        const label = (inGrid ? letter(cell.cellIndex - 1) + String(Number(row.dataset.orow) + 1) : letter(cell.cellIndex - 1)) + ': ' + (cell.textContent.trim() || '(empty)')
        document.dispatchEvent(new CustomEvent('kit-comment-on', {
          detail: inGrid
            ? { range: rg, quote: label, anchor: { cell: { orow: Number(row.dataset.orow), col: cell.cellIndex } } }
            : { range: rg, quote: label },
        }))
      }
    })

    // Multi-cell paste: tab-separated columns, newline-separated rows,
    // spreading from the focused cell — the universal spreadsheet
    // clipboard shape. Plain text only; each landing cell gets a real
    // input event so the engine, fbar, and promotion all see it.
    table.addEventListener('paste', e => {
      const cell = e.target.closest && e.target.closest('td, th')
      if (!cell || !cell.isContentEditable) return
      const text = e.clipboardData ? e.clipboardData.getData('text/plain') : ''
      if (!text || (!text.includes('\\t') && !text.includes('\\n'))) return
      e.preventDefault()
      const rows = text.replace(/\\r/g, '').split('\\n')
      if (rows[rows.length - 1] === '') rows.pop()
      const tableRows = [...table.rows]
      let r0 = tableRows.indexOf(cell.parentElement)
      // Landing rows skip the totals row (a paste must never overwrite
      // computed totals); the writes are journaled so Cmd+Z restores them.
      const targets = tableRows.slice(r0).filter(tr2 => !tr2.classList.contains('totals-row'))
      const writes = []
      for (let dr = 0; dr < rows.length; dr++) {
        const tr = targets[dr]
        if (!tr) break
        const cols = rows[dr].split('\\t')
        for (let dc = 0; dc < cols.length; dc++) {
          const c = tr.cells[cell.cellIndex + dc]
          if (!c || !c.isContentEditable) continue
          writes.push([c, cols[dc]])
        }
      }
      if (!writes.length) return
      journalPush(writes.map(w => w[0]))
      for (const [c, v] of writes) {
        c.textContent = v
        c.dispatchEvent(new Event('input', { bubbles: true }))
        c.dispatchEvent(new CustomEvent('kit-commit', { bubbles: true }))
      }
      announce('Pasted into ' + writes.length + ' cells')
    })

    // Fill down: Ctrl/Cmd+D copies the cell above into the focused cell,
    // adjusting RELATIVE references one row down — token rewriting on
    // the raw text, never evaluation.
    // Reference rewrites never reach inside quoted strings — a criterion
    // like "Q1" is data, not an address.
    const outsideStrings = (src, rewrite) =>
      src.split(/("[^"]*")/).map((seg, i) => (i % 2 ? seg : rewrite(seg))).join('')
    const shiftRefs = (src, dr) => outsideStrings(src, seg =>
      seg.replace(/(\\$?)([A-Za-z]{1,3})(\\$?)(\\d+)/g,
        (m, cd, col, rd, row) => cd + col + rd + (rd === '$' ? row : String(Number(row) + dr))))
    table.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'Backspace') {
        // Clear the row's contents — content-level, so it works and
        // persists exactly like typing empties into each cell.
        const cell0 = e.target.closest && e.target.closest('td, th')
        if (!cell0 || !cell0.isContentEditable) return
        e.preventDefault()
        const row0 = cell0.parentElement
        journalPush([...row0.cells].filter(c => c.isContentEditable))
        let cleared = 0
        for (const c of row0.cells) {
          if (!c.isContentEditable || !c.textContent.trim()) continue
          c.textContent = ''
          c.dispatchEvent(new Event('input', { bubbles: true }))
          c.dispatchEvent(new CustomEvent('kit-commit', { bubbles: true }))
          cleared++
        }
        announce('Cleared row — ' + cleared + ' cells emptied')
        return
      }
      if ((e.ctrlKey || e.metaKey) && (e.key === 'd' || e.key === 'D')) {
        const cell = e.target.closest && e.target.closest('td, th')
        if (!cell || !cell.isContentEditable) return
        e.preventDefault()
        const row = cell.parentElement
        const tableRows = [...table.rows]
        const above = tableRows[tableRows.indexOf(row) - 1]
        const src = above && above.cells[cell.cellIndex]
        if (!src || !src.isContentEditable) return
        // References shift by the ORIGINAL-order distance — the visual
        // neighbor under a sort is not one stamp away, and a formula
        // must mean the same thing for every viewer.
        const o1 = above.dataset.orow, o2 = row.dataset.orow
        const txt = (src.dataset.fxSrc || src.textContent).trim()
        if (txt.startsWith('=') && (o1 === undefined || o2 === undefined)) { announce('Fill down needs data rows'); return }
        // A script write like paste: journaled so Cmd+Z restores it.
        journalPush([cell])
        if (txt.startsWith('=')) cell.textContent = '=' + shiftRefs(txt.slice(1), Number(o2) - Number(o1))
        else cell.textContent = txt
        cell.dispatchEvent(new Event('input', { bubbles: true }))
        cell.dispatchEvent(new CustomEvent('kit-commit', { bubbles: true }))
      }
    })

    // The sheet grows: first input in a scratch row PROMOTES it to a
    // real row — spliced above any totals, stamped into the original
    // order so references and ranges see it, numbered like its
    // neighbors. On live docs the row still cannot persist (it has no
    // server annotation), so the at-the-cell marker stays — honest
    // about reach, never about existence.
    table.addEventListener('input', e => {
      const cell = e.target.closest('td, th')
      if (!cell) return
      const row = cell.closest('tr')
      if (row && row.classList.contains('filler-row') && cell.textContent.trim() !== '') {
        const body = table.tBodies[0]
        const totals = body.querySelector('tr.totals-row')
        if (totals) body.insertBefore(row, totals)
        row.classList.remove('filler-row')
        const stamped = [...body.querySelectorAll('tr[data-orow]')]
        const next = stamped.length
        row.dataset.orow = String(next)
        const rn = row.querySelector('th.rn')
        if (rn) rn.dataset.rn = String(next + 1)
        for (const c of row.cells) c.classList.remove('filler')
        if (page.querySelector('[data-id]')) {
          for (const c of row.cells) if (!c.classList.contains('rn')) c.classList.add('local-note')
        }
        // Totals follow growth: any formula range ending at what was the
        // last stamped row extends to cover the newcomer — token
        // rewriting on the stored source, announced when it happens.
        {
          const prevLast = next // 1-based address of the previous last row
          let extended = 0
          for (const cell of table.querySelectorAll('[data-fx-src], td, th')) {
            const src = cell.dataset && cell.dataset.fxSrc
            if (!src) continue
            const re = new RegExp('([A-Za-z]{1,3})(\\\\d+):([A-Za-z]{1,3})' + prevLast + '(?![0-9])', 'g')
            const next2 = outsideStrings(src, seg =>
              seg.replace(re, (m, c1, r1, c2) => c1 + r1 + ':' + c2 + (prevLast + 1)))
            if (next2 !== src) {
              // The engine must SEE the new source: write it as the
              // cell's text (source mode) so adopt re-parses — the
              // display swap follows from recompute as usual.
              cell.dataset.fxSrc = next2
              cell.textContent = next2
              cell.dispatchEvent(new Event('input', { bubbles: true }))
              cell.dispatchEvent(new CustomEvent('kit-commit', { bubbles: true }))
              extended++
            }
          }
          if (extended) announce('New row ' + (next + 1) + ' — ' + extended + ' total' + (extended > 1 ? 's' : '') + ' extended to cover it')
        }
        table.dispatchEvent(new CustomEvent('kit-sorted'))
      } else if (cell.classList.contains('filler') && page.querySelector('[data-id]')) {
        cell.classList.add('local-note')
      }
    })

    // Formula bar: shows the focused cell's address and value; typing
    // mirrors into the cell, Enter or leaving the bar commits (the
    // 'kit-commit' event hands the write to the shared persist layer),
    // Escape restores.
    const fref = document.querySelector('[data-ref]')
    const finput = document.querySelector('[data-finput]')
    if (!fref || !finput) return
    let bound = null
    let before = null
    const refOf = cell => {
      const row = cell.parentElement
      if (row === colsRow) return letter(cell.cellIndex - 1)
      if (row.classList.contains('totals-row')) return '\\u03a3' + letter(cell.cellIndex - 1)
      if (row.dataset.orow !== undefined) return letter(cell.cellIndex - 1) + (Number(row.dataset.orow) + 1)
      return letter(cell.cellIndex - 1)
    }
    table.addEventListener('focusin', e => {
      const cell = e.target.closest('td, th')
      if (!cell || cell.classList.contains('rn') || !cell.isContentEditable) return
      if (bound && bound !== cell) delete bound.dataset.fxEditing
      bound = cell
      before = cell.textContent
      fref.textContent = refOf(cell)
      finput.value = cell.textContent
    })
    table.addEventListener('input', e => {
      const cell = e.target.closest('td, th')
      if (cell && cell === bound) finput.value = cell.textContent
    })
    finput.addEventListener('input', () => {
      if (!bound) return
      // Bar-editing a formula cell must not be display-swapped mid-keystroke.
      bound.dataset.fxEditing = '1'
      bound.textContent = finput.value
      // A real input event: the formula engine adopts and recomputes
      // through the same path as in-cell typing.
      bound.dispatchEvent(new Event('input', { bubbles: true }))
    })
    const commit = () => {
      if (!bound) return
      before = bound.textContent
      delete bound.dataset.fxEditing
      bound.dispatchEvent(new CustomEvent('kit-commit', { bubbles: true }))
      bound.dispatchEvent(new Event('input', { bubbles: true }))
    }
    finput.addEventListener('keydown', e => {
      if (e.key === 'Enter') { e.preventDefault(); commit() }
      if (e.key === 'Escape') {
        e.preventDefault()
        if (bound && before !== null) {
          // A formula cell restores its SOURCE (like journalPop): the
          // display snapshot goes stale the moment a dependency moves.
          const back = bound.dataset.fxSrc !== undefined ? bound.dataset.fxSrc : before
          bound.textContent = back
          finput.value = back
          delete bound.dataset.fxEditing
          bound.dispatchEvent(new Event('input', { bubbles: true }))
        }
      }
    })
    finput.addEventListener('blur', commit)
  })();

  // Formula engine (sheet-specific): a cell whose text starts with '='
  // is a live formula. The RAW formula is the cell's persistent text —
  // visible whenever the cell is being edited (focus) and committed by
  // the shared persist layer's caret-leave flush, which runs before the
  // deferred display swap below; every load recomputes from source. No
  // eval/new Function anywhere: a tokenizer and recursive-descent parser
  // over a whitelisted grammar, because author≠viewer — formula text is
  // untrusted input.
  (() => {
    const page = document.querySelector('.page.sheet')
    const table = page && page.querySelector('table')
    if (!table || !table.tBodies[0]) return
    // Aggregates follow spreadsheet convention: text and blanks are
    // SKIPPED, never coerced to zero — a label in a summed range must
    // not silently change the total. COUNT counts numbers alone.
    const nums = vs => vs.filter(v => typeof v === 'number')
    // SUMIF/COUNTIF criteria are PARSED, never executed: a criterion
    // string like ">100" or "Quoted" tokenizes into comparator + operand
    // through the same tokenizer as everything else, and the comparison
    // runs through matchCriterion — the no-eval invariant holds here too.
    const matchCriterion = (v, crit) => {
      const s = typeof crit === 'string' ? crit.trim() : String(crit)
      const m = s.match(/^(<=|>=|<>|=|<|>)?([\\s\\S]*)$/)
      const op = m[1] || '='
      const rawOperand = m[2].trim()
      const numOp = valOf(rawOperand)
      const both = typeof v === 'number' && typeof numOp === 'number'
      switch (op) {
        case '=': return both ? v === numOp : String(v).toLowerCase() === String(rawOperand).toLowerCase()
        case '<>': return both ? v !== numOp : String(v).toLowerCase() !== String(rawOperand).toLowerCase()
        case '<': return both && v < numOp
        case '>': return both && v > numOp
        case '<=': return both && v <= numOp
        case '>=': return both && v >= numOp
      }
      return false
    }
    const FN = {
      SUM: vs => nums(vs).reduce((a, b) => a + b, 0),
      AVERAGE: vs => { const n = nums(vs); if (!n.length) throw {code: '#DIV/0!'}; return n.reduce((a, b) => a + b, 0) / n.length },
      MIN: vs => { const n = nums(vs); return n.length ? Math.min(...n) : 0 },
      MAX: vs => { const n = nums(vs); return n.length ? Math.max(...n) : 0 },
      COUNT: vs => nums(vs).length,
      ROUND: vs => { const m = 10 ** Math.trunc(numArg(vs[1] ?? 0)); return Math.round(numArg(vs[0]) * m) / m },
      ABS: vs => Math.abs(numArg(vs[0])),
      // IF lives in evalAst, not here — it must evaluate lazily so its
      // guards guard (=IF(D2=0,0,C2/D2)).
      // SUMIF(range, criterion[, sumRange]) / COUNTIF(range, criterion):
      // the budget questions. Arguments arrive as PAIRED arrays via the
      // special-cased evaluator below (groupVals).
    }
    const numArg = v => {
      if (typeof v === 'number') return v
      throw {code: '#VALUE!'}
    }
    const tokenize = src => {
      const out = []
      let i = 0
      while (i < src.length) {
        const c = src[i]
        if (c === ' ' || c === '\\t') { i++; continue }
        const two = src.slice(i, i + 2)
        if (two === '<=' || two === '>=' || two === '<>') { out.push({t: 'op', v: two}); i += 2; continue }
        if (c === '"') {
          const m = src.slice(i + 1).match(/^[^"]*/)
          out.push({t: 'str', v: m[0]})
          i += m[0].length + 2
          if (src[i - 1] !== '"') throw {code: '#NAME?'}
          continue
        }
        if ('+-*/^%(),<>=&'.includes(c)) { out.push({t: 'op', v: c}); i++; continue }
        if (c >= '0' && c <= '9' || c === '.') {
          const m = src.slice(i).match(/^\\d*\\.?\\d+/)
          let v = Number(m[0])
          i += m[0].length
          out.push({t: 'num', v}); continue
        }
        if (/[A-Za-z$]/.test(c)) {
          const m = src.slice(i).match(/^[$]?[A-Za-z]{1,3}[$]?\\d+(:[$]?[A-Za-z]{1,3}[$]?\\d+)?|^[A-Za-z]+/)
          const s = m[0]
          if (/\\d/.test(s)) out.push({t: 'ref', v: s.replace(/[$]/g, '').toUpperCase()})
          else out.push({t: 'name', v: s.toUpperCase()})
          i += s.length; continue
        }
        throw {code: '#NAME?'}
      }
      return out
    }
    const parse = tokens => {
      let p = 0
      const peek = () => tokens[p]
      const eat = v => { const t = tokens[p]; if (!t || (v && t.v !== v)) throw {code: '#NAME?'}; p++; return t }
      const prim = () => {
        const t = peek()
        if (!t) throw {code: '#NAME?'}
        if (t.t === 'num') { p++; return {k: 'n', v: t.v} }
        if (t.t === 'str') { p++; return {k: 's', v: t.v} }
        if (t.t === 'ref') { p++; return t.v.includes(':') ? {k: 'range', v: t.v} : {k: 'ref', v: t.v} }
        if (t.t === 'name') {
          p++
          if (peek() && peek().v === '(') {
            eat('(')
            const args = []
            if (peek() && peek().v !== ')') { args.push(expr()); while (peek() && peek().v === ',') { eat(','); args.push(expr()) } }
            eat(')')
            return {k: 'fn', f: t.v, args}
          }
          throw {code: '#NAME?'}
        }
        if (t.v === '(') { eat('('); const e = expr(); eat(')'); return e }
        if (t.v === '-') { eat('-'); return {k: 'neg', a: prim()} }
        if (t.v === '+') { eat('+'); return prim() }
        throw {code: '#NAME?'}
      }
      // Postfix percent binds tightest: =A1% reads A1/100, the same
      // reading a 5% literal gets; '%' is never a binary operator.
      const unit = () => { let a = prim(); while (peek() && peek().v === '%') { eat('%'); a = {k: 'pct', a} } return a }
      const pow = () => { let a = unit(); while (peek() && peek().v === '^') { eat('^'); a = {k: 'op', o: '^', a, b: unit()} } return a }
      const mul = () => { let a = pow(); while (peek() && (peek().v === '*' || peek().v === '/')) { const o = eat().v; a = {k: 'op', o, a, b: pow()} } return a }
      const add = () => { let a = mul(); while (peek() && (peek().v === '+' || peek().v === '-')) { const o = eat().v; a = {k: 'op', o, a, b: mul()} } return a }
      const cat = () => { let a = add(); while (peek() && peek().v === '&') { eat('&'); a = {k: 'op', o: '&', a, b: add()} } return a }
      const expr = () => {
        let a = cat()
        while (peek() && ['=', '<', '>', '<=', '>=', '<>'].includes(peek().v)) { const o = eat().v; a = {k: 'op', o, a, b: cat()} }
        return a
      }
      const e = expr()
      if (p !== tokens.length) throw {code: '#NAME?'}
      return e
    }
    const colIdx = c => [...c].reduce((a, ch) => a * 26 + ch.charCodeAt(0) - 64, 0)
    const colName = i => { let s = ''; while (i > 0) { s = String.fromCharCode(65 + (i - 1) % 26) + s; i = Math.trunc((i - 1) / 26) } return s }
    const expand = range => {
      const [a, b] = range.split(':')
      const co = r => r.match(/^[A-Z]+/)[0], ro = r => Number(r.match(/\\d+$/)[0])
      const c1 = colIdx(co(a)), c2 = colIdx(co(b)), r1 = ro(a), r2 = ro(b)
      // Cap by arithmetic BEFORE materializing: a fat-fingered end row
      // must throw, not allocate the range.
      if ((Math.abs(r2 - r1) + 1) * (Math.abs(c2 - c1) + 1) > 4096) throw {code: '#REF!'}
      const out = []
      for (let r = Math.min(r1, r2); r <= Math.max(r1, r2); r++)
        for (let c = Math.min(c1, c2); c <= Math.max(c1, c2); c++) out.push(colName(c) + r)
      return out
    }
    // A leaf keeps its type: numeric text (commas allowed) becomes a
    // number; anything else stays a string, for the aggregates'
    // skip-non-numeric rule and string comparisons to act on.
    // ONE numeric reading for the whole sheet: commas stripped, a
    // leading $ allowed, a trailing % divides by 100. What sorts as a
    // number computes as a number — no silent disagreement.
    const valOf = s => {
      const t = String(s).trim()
      if (t === '') return ''
      let c = t.replace(/,/g, '')
      let scale = 1
      if (c.startsWith('$')) c = c.slice(1)
      if (c.endsWith('%')) { c = c.slice(0, -1); scale = 0.01 }
      if (c.trim() === '') return t
      const n = Number(c)
      return Number.isNaN(n) ? t : n * scale
    }
    // References name rows by their ORIGINAL order — sorting reorders
    // the view, never what A1 means. Rows are stamped once at init
    // (before any sort can run) and looked up by stamp.
    {
      let n = 0
      for (const tr of table.tBodies[0].rows) {
        const rn = tr.querySelector('th.rn')
        if (tr.classList.contains('totals-row')) { if (rn) rn.dataset.rn = '\\u03a3'; continue }
        if (tr.classList.contains('filler-row')) continue
        tr.dataset.orow = String(n++)
        if (rn) rn.dataset.rn = String(n)
      }
    }
    const BLANK_CELL = { blank: true }
    const cellAt = ref => {
      const col = colIdx(ref.match(/^[A-Z]+/)[0])
      const row = Number(ref.match(/\\d+$/)[0])
      const tr = table.tBodies[0].querySelector('tr[data-orow="' + (row - 1) + '"]')
      if (tr) return tr.cells[col] || null
      // =SUM(C1:C20) over a sheet with 8 data rows is the universal
      // habit: rows that EXIST on screen but hold no data read as
      // blank; truly out-of-range stays #REF!.
      const visibleRows = table.tBodies[0].rows.length
      if (row >= 1 && row <= visibleRows) return BLANK_CELL
      return null
    }
    // Element-keyed: tfoot cells hold formulas too, but only tbody data
    // cells are referenceable.
    const formulas = new Map()
    const adopt = cell => {
      // The bar mirrors per-keystroke: mid-edit text is not a commit, and
      // adopting it would flatten the formula before Escape can restore.
      if (cell.dataset && cell.dataset.fxEditing) return
      const t = String(cell.textContent).trim()
      // A computed display is not an edit: if this formula cell's text
      // is exactly its computed value (or an error code), the engine put
      // it there — adopting it would flatten the formula.
      if (cell.dataset.fxSrc && !t.startsWith('=')) {
        if (/^#/.test(t)) return
        const f = formulas.get(cell)
        if (f) {
          let shown
          try { shown = fmt(evalCell(cell, new Set(), new Map())) } catch (e2) { shown = (e2 && e2.code) || '' }
          if (t === shown) return
        }
      }
      if (t.startsWith('=')) {
        try { formulas.set(cell, {src: t, ast: parse(tokenize(t.slice(1)))}) }
        catch (err) { formulas.set(cell, {src: t, err: (err && err.code) || '#NAME?'}) }
        // The RAW formula is the cell's persistent truth: the persist
        // layer commits dataset.fxSrc wherever it exists, so a display
        // swap can never flatten a formula server-side.
        cell.dataset.fxSrc = t
      } else {
        formulas.delete(cell)
        delete cell.dataset.fxSrc
      }
    }
    const evalCell = (cell, seen, cache) => {
      if (cell === BLANK_CELL) return ''
      if (cache.has(cell)) return cache.get(cell)
      const f = formulas.get(cell)
      if (!f) return valOf(cell.textContent)
      if (f.err) throw {code: f.err}
      if (seen.has(cell)) throw {code: '#CYCLE!'}
      seen.add(cell)
      const v = evalAst(f.ast, seen, cache)
      seen.delete(cell)
      cache.set(cell, v)
      return v
    }
    const evalAst = (n, seen, cache) => {
      switch (n.k) {
        case 'n': return n.v
        case 's': return n.v
        case 'ref': { const c = cellAt(n.v); if (!c) throw {code: '#REF!'}; return evalCell(c, seen, cache) }
        case 'range': throw {code: '#NAME?'}
        case 'neg': return -numArg(evalAst(n.a, seen, cache))
        case 'pct': return numArg(evalAst(n.a, seen, cache)) / 100
        case 'fn': {
          if (n.f === 'IF') {
            // Lazy by design: =IF(D2=0,0,C2/D2) must never evaluate the
            // division it guards against.
            if (n.args.length < 2) throw {code: '#NAME?'}
            const cond = evalAst(n.args[0], seen, cache)
            return cond ? evalAst(n.args[1], seen, cache) : (n.args[2] !== undefined ? evalAst(n.args[2], seen, cache) : 0)
          }
          if (n.f === 'SUMIF' || n.f === 'COUNTIF') {
            if (n.args.length < 2) throw {code: '#NAME?'}
            const groupVals = a => a.k === 'range'
              ? expand(a.v).map(r => { const c = cellAt(r); if (!c) throw {code: '#REF!'}; return evalCell(c, seen, cache) })
              : [evalAst(a, seen, cache)]
            const test = groupVals(n.args[0])
            const crit = evalAst(n.args[1], seen, cache)
            if (n.f === 'COUNTIF') return test.filter(v => matchCriterion(v, crit)).length
            const sums = n.args[2] ? groupVals(n.args[2]) : test
            let acc = 0
            test.forEach((v, i2) => {
              if (matchCriterion(v, crit) && typeof sums[i2] === 'number') acc += sums[i2]
            })
            return acc
          }
          const fn = FN[n.f]
          if (!fn) throw {code: '#NAME?'}
          const vs = []
          for (const a of n.args) {
            if (a.k === 'range') expand(a.v).forEach(r => { const c = cellAt(r); if (!c) throw {code: '#REF!'}; vs.push(evalCell(c, seen, cache)) })
            else vs.push(evalAst(a, seen, cache))
          }
          return fn(vs)
        }
        case 'op': {
          const a = evalAst(n.a, seen, cache), b = evalAst(n.b, seen, cache)
          switch (n.o) {
            // Arithmetic on text is an error, never a silent zero.
            case '+': return numArg(a) + numArg(b)
            case '-': return numArg(a) - numArg(b)
            case '*': return numArg(a) * numArg(b)
            case '/': if (numArg(b) === 0) throw {code: '#DIV/0!'}; return numArg(a) / numArg(b)
            case '^': return numArg(a) ** numArg(b)
            case '&': return String(a) + String(b)
            case '=': return a === b ? 1 : 0
            case '<': return a < b ? 1 : 0
            case '>': return a > b ? 1 : 0
            case '<=': return a <= b ? 1 : 0
            case '>=': return a >= b ? 1 : 0
            case '<>': return a !== b ? 1 : 0
          }
        }
      }
    }
    const fmt = v => typeof v === 'number' && Number.isFinite(v)
      ? (Math.abs(v) >= 1000 ? v.toLocaleString('en-US', {maximumFractionDigits: 2}) : String(Math.round(v * 100) / 100))
      : String(v)
    // Sorting re-parents rows but never changes what refs mean (the
    // orow stamps travel with the rows) — still, recompute after a sort
    // so any dependent display refreshes.
    table.addEventListener('kit-sorted', () => recompute())
    let editing = null
    // Display writes the engine makes must not read as edits — matched
    // by VALUE (cell→written text): batched observer records interleave
    // with user and collaborator writes, so per-record identity
    // mis-attributes them (the persist layer never needs to know).
    const engineWrites = new Map()
    // A collaborator's write lands in the DOM with no local event: the
    // engine re-adopts the cell and recomputes, so B's grid follows A's
    // formula edit.
    new MutationObserver(muts => {
      let foreign = false
      for (const m of muts) {
        const n = m.target.nodeType === 1 ? m.target : m.target.parentElement
        const cell = n && n.closest ? n.closest('td, th') : null
        if (!cell) continue
        if (engineWrites.get(cell) === cell.textContent) continue
        if (cell === editing || cell.dataset.fxEditing) continue
        const t = String(cell.textContent).trim()
        const f = formulas.get(cell)
        const known = f ? (t === f.src || t === fmt((() => { try { return evalCell(cell, new Set(), new Map()) } catch (e) { return (e && e.code) || '' } })())) : false
        if (!known) {
          // A value change is as foreign as a formula change: every
          // dependent total must follow a colleague's edit.
          if (t.startsWith('=') || f) adopt(cell)
          foreign = true
        }
      }
      if (foreign) recompute()
    }).observe(table, { childList: true, characterData: true, subtree: true })
    const recompute = () => {
      const cache = new Map()
      for (const [cell, f] of formulas) {
        if (!cell.isConnected) { formulas.delete(cell); continue }
        if (cell === editing || cell.dataset.fxEditing) continue
        let shown
        try { shown = fmt(evalCell(cell, new Set(), cache)) }
        catch (err) { shown = (err && err.code) || '#NAME?' }
        cell.classList.add('fx')
        cell.classList.toggle('fxerr', /^#/.test(shown))
        if (cell.textContent !== shown) {
          engineWrites.set(cell, shown)
          cell.textContent = shown
        }
        cell.title = /^#/.test(shown)
          ? ({'#CYCLE!': 'This formula refers to itself (directly or through another cell)',
              '#DIV/0!': 'Division by zero, or an average over no numbers',
              '#NAME?': 'Unknown function or unreadable formula',
              '#REF!': 'A reference points outside the sheet',
              '#VALUE!': 'Arithmetic on text — aggregates skip text, operators cannot'})[shown] || 'Formula error'
          : (formulas.get(cell) ? formulas.get(cell).src : '')
      }
    }
    for (const sect of [table.tBodies[0], table.tFoot]) {
      if (!sect) continue
      for (const tr of sect.rows) for (const cell of tr.cells) {
        if (!cell.classList.contains('rn') && String(cell.textContent).trim().startsWith('=')) adopt(cell)
      }
    }
    recompute()
    table.addEventListener('focusin', e => {
      const cell = e.target.closest('td, th')
      if (!cell || cell.classList.contains('rn') || !cell.isContentEditable) return
      // Track the focused cell unconditionally: a formula typed into a
      // previously plain cell must not be display-swapped mid-edit.
      editing = cell
      const f = formulas.get(cell)
      if (f && cell.textContent !== f.src) cell.textContent = f.src
      // The formula bar binds on the same focusin, one registration
      // earlier — re-point it at the source text, like any sheet app.
      const fi = document.querySelector('[data-finput]')
      if (f && fi) fi.value = f.src
    })
    table.addEventListener('focusout', e => {
      const cell = e.target.closest('td, th')
      if (!cell) return
      if (cell === editing) editing = null
      adopt(cell)
      // Deferred a macrotask: the persist layer's caret-leave flush must
      // read the raw formula text, not the computed display.
      setTimeout(recompute, 0)
    })
    table.addEventListener('input', e => {
      const cell = e.target.closest('td, th')
      if (!cell) return
      adopt(cell)
      // Numbers align like numbers wherever they're typed.
      if (cell.tagName === 'TD' && !cell.classList.contains('num')) {
        const v = valOf(cell.textContent)
        if (typeof v === 'number') cell.classList.add('num')
      }
      recompute()
    })
  })()
</script>
