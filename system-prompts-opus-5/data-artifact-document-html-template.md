<!--
name: 'Data: Artifact document HTML template'
description: >-
  Provides the bundled live-document HTML template extracted for Claude when the
  document Artifact skill is activated.
ccVersion: 2.1.238
-->
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title><!-- SLOT: TITLE — the document's name alone, short and distinctive; never a "Name — explainer" compound -->Document title</title>
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
    --cds-surface-2: #f7f6f2;            /* the toolbar band, one step off the paper */
    --cds-control-hover: rgba(26, 26, 25, 0.06);
    --cds-control-active: rgba(26, 26, 25, 0.1);
    --cds-clay: #bb5a38;                 /* CDS clay, deepened so a white label reads AA */
    --cds-clay-emphasized: #ad4f2e;
    --cds-text-on-clay: #ffffff;
    --cds-text-primary: #1a1a19;
    --cds-text-secondary: #55544f;
    --cds-text-muted: #6c6a66;           /* AA at 12px on the band and the paper */
    --cds-text-body: var(--cds-text-primary);
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
    --cds-text-warning: #b84b20;
    --cds-font-sans: "Anthropic Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
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
    --cds-surface-2: #1c1c1b;
    --cds-control-hover: rgba(237, 237, 234, 0.08);
    --cds-control-active: rgba(237, 237, 234, 0.14);
    --cds-text-primary: #ededea;
    --cds-text-secondary: #b5b3aa;
    --cds-text-muted: #8f8d86;
    --cds-border: rgba(237, 237, 234, 0.12);
    --cds-border-strong: rgba(237, 237, 234, 0.28);
    --cds-text-accent: #5da0f2;
    --cds-text-danger: #f2756a;
    --cds-text-warning: #ec835a;
    --cds-accent-bg: rgba(93, 160, 242, 0.12);
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      color-scheme: dark;
      --cds-surface-0: #151514;
      --cds-surface-1: #151514;
      --cds-surface-2: #1c1c1b;
      --cds-control-hover: rgba(237, 237, 234, 0.08);
      --cds-control-active: rgba(237, 237, 234, 0.14);
      --cds-text-primary: #ededea;
      --cds-text-secondary: #b5b3aa;
      --cds-text-muted: #8f8d86;
      --cds-border: rgba(237, 237, 234, 0.12);
      --cds-border-strong: rgba(237, 237, 234, 0.28);
      --cds-text-accent: #5da0f2;
      --cds-text-danger: #f2756a;
      --cds-text-warning: #ec835a;
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

  /* KIT:chrome:begin — the editor chrome: toolbar band, buttons, menus,
     canvas, status. One implementation for the family. A defined band
     with full-presence controls; the save button is the CDS primary
     action, since trust in it is the product. */
  .toolbar {
    position: sticky; top: 0; z-index: 22;
    display: flex; align-items: center; gap: 4px;
    padding: 8px 12px; line-height: 1.25;
    background: var(--cds-surface-2);
    border-bottom: 1px solid var(--cds-border);
    font-family: var(--cds-font-sans);
  }
  .toolbar button {
    appearance: none; border: 1px solid transparent; background: none;
    color: var(--cds-text-primary); font-family: var(--cds-font-sans);
    font-size: 13px; font-weight: 400; line-height: 1;
    height: 32px; min-width: 32px; padding: 0 8px; border-radius: var(--cds-radius);
    display: inline-flex; align-items: center; justify-content: center; gap: 4px;
    cursor: pointer;
  }
  .toolbar button:hover { background: var(--cds-control-hover); }
  .toolbar button:active { background: var(--cds-control-active); }
  .toolbar button:disabled { color: var(--cds-text-muted); cursor: default; background: none; }
  .toolbar button.on { color: var(--cds-text-accent); background: var(--cds-accent-bg); }
  .toolbar button svg { flex: none; }
  .tb-sep { width: 1px; height: 20px; background: var(--cds-border); margin: 0 4px; }
  /* A styled dropdown: the toggle reads as a control, the list renders
     each choice in its own voice, so the picker shows the style itself. */
  .tb-menu { position: relative; display: inline-flex; }
  .tb-menu > button { padding: 0 8px 0 12px; min-width: 108px; justify-content: space-between; }
  .tb-menu > button[aria-expanded="true"] { background: var(--cds-control-active); }
  .tb-menu-list {
    position: absolute; top: calc(100% + 4px); left: 0; z-index: 30;
    min-width: 200px; padding: 4px; margin: 0;
    background: var(--cds-surface-1); color: var(--cds-text-primary);
    border: 1px solid var(--cds-border); border-radius: 8px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12), 0 1px 3px rgba(0, 0, 0, 0.08);
  }
  .tb-menu-list[hidden] { display: none; }
  .toolbar .tb-menu-list button {
    display: flex; width: 100%; height: auto; min-height: 32px;
    padding: 8px 12px; border-radius: var(--cds-radius); justify-content: flex-start;
    font-weight: 400; line-height: 1.25; text-align: left;
  }
  .toolbar .tb-menu-list button[aria-selected="true"] { background: var(--cds-accent-bg); }
  .tb-right { margin-left: auto; display: flex; align-items: center; gap: 8px; font-size: 12px; font-variant-numeric: tabular-nums; color: var(--cds-text-muted); }
  .tb-status { white-space: nowrap; color: var(--cds-text-secondary); }
  .tb-status[data-tone="warning"] { color: var(--cds-text-warning); }
  .tb-status[data-tone="error"] { color: var(--cds-text-danger); }
  .tb-right [data-words] { margin-left: 16px; }
  .tb-status[data-tone="busy"], .tb-status[data-tone="muted"] { color: var(--cds-text-muted); }
  /* Save is the CDS primary button: clay, white label, 8px radius. */
  .toolbar .tb-save {
    height: 32px; padding: 0 12px; border-radius: calc(2 * var(--cds-radius));
    background: var(--cds-clay); color: var(--cds-text-on-clay); border-color: transparent;
    font-size: 13px; font-weight: 700;
  }
  .toolbar .tb-save:hover:not(:disabled), .toolbar .tb-save:active:not(:disabled) { background: var(--cds-clay-emphasized); }
  .toolbar .tb-save:disabled { opacity: 1; background: var(--cds-control-hover); color: var(--cds-text-muted); }
  /* Discard is the secondary: outlined, same shape. */
  .toolbar .tb-save[data-discard]:not(:disabled) { background: none; color: var(--cds-text-primary); border-color: var(--cds-border-strong); }
  .toolbar .tb-save[data-discard]:hover:not(:disabled) { background: var(--cds-control-hover); }
  .toolbar [hidden] { display: none; }
  .canvas { padding: 20px 24px 120px; }
  /* Page content stacks below the chrome whatever it declares. */
  .page { isolation: isolate; }
  .visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
  :focus-visible { outline: 2px solid var(--cds-text-accent); outline-offset: 1px; }
  @media (prefers-reduced-motion: no-preference) {
    .toolbar button { transition: background-color 0.12s ease; }
  }
  /* KIT:chrome:end */

  /* ── The page (doc-specific) ───────────────────────────────────── */
  /* One system, stated once:
       scale   17 × 1.25ⁿ → 14 / 17 / 21 / 27 / 34  (lede 19 = 17 × 1.125, the one half-step)
       line    28px (17/28 = 1.65); every block sits on 14px half-lines
       space   14 / 28 / 42 / 56 / 70 / 112  (½ 1 1½ 2 2½ 4 lines)
       indent  28px — lists, callout, one inner margin for everything set off
       weight  400 / 700 only — the two every fallback face carries honestly
       measure 34em (578px at 17px → ≈68 chars in SF/Segoe, ≈61 in DejaVu) */
  .page {
    max-width: 34em; margin: 0 auto;
    padding: 50px 0 112px;                 /* with the canvas's 20px: 2½ lines above the title, 4 lines past the end */
    font-size: 17px; line-height: 28px;
    font-weight: 400;
    color: var(--cds-text-body, var(--cds-text-primary));
    font-synthesis: none;                  /* a roman-only brand font falls through, never fakes */
    font-kerning: normal;
    hyphens: manual;                       /* an editor: words must not re-break under the caret as they are typed */
    overflow-wrap: break-word;
  }
  .page:focus { outline: none; }
  .page h1, .page h2, .page h3 { color: var(--cds-text-primary); hyphens: manual; }
  /* balance/pretty re-break earlier lines as the text grows — under the caret
     that violates the hyphens: manual invariant above, so restrict them to the
     read-only view (the data-kit-mode hook render() sets on the root); the
     writer surface keeps greedy wrap and readers still get balanced lines. */
  :root[data-kit-mode="reader"] .page { text-wrap: pretty; }
  :root[data-kit-mode="reader"] .page h1, :root[data-kit-mode="reader"] .page h2, :root[data-kit-mode="reader"] .page h3 { text-wrap: balance; }
  .page h1 { font-size: 34px; line-height: 42px; margin: 0 0 14px; font-weight: 700; letter-spacing: -0.015em; }
  /* The lede: the paragraph after the title is the standfirst — one half-step up,
     one ink step down, a full two lines before the document proper begins. */
  .page h1 + p { font-size: 19px; line-height: 28px; color: var(--cds-text-secondary); margin: 0 0 56px; }
  .page h2 { font-size: 21px; line-height: 28px; margin: 42px 0 14px; font-weight: 700; }
  .page h3 { font-size: 14px; line-height: 20px; padding-top: 8px; margin: 28px 0 0; font-weight: 700; letter-spacing: 0.09em; text-transform: uppercase; }
  .page p, .page ul, .page ol { margin: 0 0 14px; }
  .page ul, .page ol { padding-inline-start: 28px; }
  .page li { margin-bottom: 0; }
  .page li + li { margin-top: 14px; }      /* items wrap; a half-line says where one ends */
  .page li > p { margin: 0; }
  /* The callout answers what precedes it: close above, a full line below,
     a clay rule as its second signal so it is not body copy with a hairline. */
  .page blockquote { margin: 14px 0 28px; padding: 0 0 0 25px; border-left: 3px solid var(--cds-clay); }
  .page blockquote > :last-child { margin-bottom: 0; }
  .page strong { font-weight: 700; }
  .page em { font-style: italic; }
  .page a { color: var(--cds-text-accent); text-decoration-thickness: 1px; text-underline-offset: 0.14em; }
  /* Inline code: the mono token, sized so its x-height meets the sans, and a
     line-height that keeps its inline box inside the 28px line so the grid holds. */
  .page code { font-family: var(--cds-font-mono); font-size: 0.85em; line-height: 1; hyphens: none; overflow-wrap: anywhere; }
  .page kbd { font: inherit; font-size: 0.85em; padding: 0 0.3em; border: 1px solid var(--cds-border); border-radius: var(--cds-radius); }
  @media (max-width: 480px) {
    .page { font-size: 16px; line-height: 26px; padding-top: 32px; }
    .page h1 { font-size: 30px; line-height: 39px; }
    .page h1 + p { font-size: 18px; line-height: 26px; margin-bottom: 52px; }
    .page h2 { font-size: 20px; line-height: 26px; margin: 39px 0 13px; }
    .page p, .page ul, .page ol { margin-bottom: 13px; }
    .page li + li { margin-top: 13px; }
    .page ul, .page ol { padding-inline-start: 26px; }
  }
  /* Dark: light-on-dark halates at 17px/400, so the running text drops one
     step of ink while headings keep the full primary; the rule keeps its clay. */
  :root[data-theme="dark"] { --cds-text-body: #dcdbd6; }
  @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --cds-text-body: #dcdbd6; } }
  /* The style picker shows each style in its own voice — the page scale × 0.8,
     the title capped at 22px so the row stays 32px. */
  .toolbar .tb-menu-list button[data-block-value="p"] { font-size: 14px; }
  .toolbar .tb-menu-list button[data-block-value="h1"] { font-size: 22px; font-weight: 700; letter-spacing: -0.015em; }
  .toolbar .tb-menu-list button[data-block-value="h2"] { font-size: 17px; font-weight: 700; }
  .toolbar .tb-menu-list button[data-block-value="h3"] { font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; }

  @media print {
    :root, :root[data-theme="dark"], :root:not([data-theme="light"]) {
      color-scheme: light;
      --cds-surface-0: #ffffff; --cds-surface-1: #ffffff; --cds-surface-2: #ffffff;
      --cds-text-primary: #0b0b0b; --cds-text-secondary: #52514e; --cds-text-muted: #898781;
      --cds-text-body: #0b0b0b;
      --cds-border: rgba(11, 11, 11, 0.1); --cds-border-strong: rgba(11, 11, 11, 0.2);
      --cds-text-accent: #184f95; --cds-accent-bg: transparent; --cds-text-danger: #b3261e; --cds-text-warning: #c25124;
    }
    .toolbar { display: none; }
    .canvas { padding: 0; }
    .page { max-width: 34em; margin: 0 auto; padding: 0; }   /* the same measure on paper as on screen */
    .page p, .page li { widows: 2; orphans: 2; }
    .page h1, .page h2, .page h3 { break-after: avoid; }
    .page blockquote, .page li { break-inside: avoid; }
    .page a { color: inherit; text-decoration: underline; }
  }
</style>

<!-- TOOLBAR (doc variant): block styles + inline marks + lists. Toolbar
     markup is per kind; the shared kit styles (KIT:chrome) and wires
     (KIT:editor) whatever controls a kind carries. -->
<div class="toolbar" role="toolbar" aria-label="Formatting">
  <div class="tb-menu" data-block-menu>
    <button type="button" data-block-toggle title="Paragraph style" aria-label="Paragraph style" aria-haspopup="listbox" aria-expanded="false"><span data-block-label>Body</span><svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6.5 8 10.5l4-4"/></svg></button>
    <div class="tb-menu-list" role="listbox" aria-label="Paragraph style" hidden>
      <button type="button" role="option" data-block-value="p" aria-label="Body" aria-selected="true">Body</button>
      <button type="button" role="option" data-block-value="h1" aria-label="Title" aria-selected="false">Title</button>
      <button type="button" role="option" data-block-value="h2" aria-label="Heading" aria-selected="false">Heading</button>
      <button type="button" role="option" data-block-value="h3" aria-label="Subheading" aria-selected="false">Subheading</button>
    </div>
  </div>
  <span class="tb-sep"></span>
  <button data-cmd="bold" title="Bold" aria-label="Bold"><b>B</b></button>
  <button data-cmd="italic" title="Italic" aria-label="Italic"><i>I</i></button>
  <button data-cmd="underline" title="Underline" aria-label="Underline"><u>U</u></button>
  <button data-cmd="strikeThrough" title="Strikethrough" aria-label="Strikethrough"><s>S</s></button>
  <span class="tb-sep"></span>
  <button data-cmd="insertUnorderedList" title="Bulleted list" aria-label="Bulleted list"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="2.5" cy="3.5" r="0.8" fill="currentColor" stroke="none"/><circle cx="2.5" cy="8" r="0.8" fill="currentColor" stroke="none"/><circle cx="2.5" cy="12.5" r="0.8" fill="currentColor" stroke="none"/><path d="M6 3.5h8M6 8h8M6 12.5h8"/></svg></button>
  <button data-cmd="insertOrderedList" title="Numbered list" aria-label="Numbered list"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 2.5h1.2v3M2 5.5h2.4M6.5 3.5h7.5M6.5 8h7.5M6.5 12.5h7.5M2.2 9.5h1.8l-1.8 2.5h1.8"/></svg></button>
  <button data-cmd="formatBlock" data-arg="blockquote" title="Callout" aria-label="Callout quote"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3.5v9M6.5 5h7M6.5 8h7M6.5 11h5"/></svg></button>
  <span class="tb-sep"></span>
  <button data-cmd="undo" title="Undo" aria-label="Undo"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5.5 3 2.5 6l3 3"/><path d="M2.5 6h7a4 4 0 0 1 0 8H6"/></svg></button>
  <button data-cmd="redo" title="Redo" aria-label="Redo"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.5 3l3 3-3 3"/><path d="M13.5 6h-7a4 4 0 0 0 0 8H10"/></svg></button>
  <span class="tb-right">
    <button class="tb-save" data-save hidden disabled title="Save (Ctrl+S / Cmd+S)" aria-label="Save">Save</button>
    <button class="tb-save" data-restore hidden title="Save the recovered edits as a new version" aria-label="Save recovered edits">Save</button>
    <button class="tb-save" data-discard hidden title="Discard the recovered edits and reload the saved version" aria-label="Discard recovered edits">Discard</button>
    <span class="tb-status" data-status role="status">Saved</span>
    <span data-words></span>
  </span>
</div>
<!-- /TOOLBAR -->

<div class="canvas">
  <article class="page doc" contenteditable="true" spellcheck="true">


    <h1><!-- SLOT: TITLE_H1 — same name as the tab title -->Document title</h1>

    <p><!-- SLOT: PURPOSE — one sentence: what this document is for and what a reader should do with it -->What this document is for, in one sentence.</p>

    <!-- SLOT: BODY — the document itself. Keep the working-document
         discipline: h2 section headings a reader can scan; short
         paragraphs; bulleted lists where structure helps; a blockquote
         for the one decision or callout a skimmer must not miss; bold
         for the few load-bearing phrases. Name owners and dates for
         anything open. Cut this starter structure to fit. -->
    <h2>First section</h2>
    <p>First point, in working prose.</p>
    <ul>
      <li>First supporting item.</li>
      <li>Second supporting item.</li>
    </ul>
    <blockquote><p>The one-line decision or callout a skimmer must not miss.</p></blockquote>
    <h2>Open questions</h2>
    <ol>
      <li>First open question — who owns it, and by when.</li>
    </ol>

  </article>
</div>

<script>
  // DOC:anchors:begin — every block a reader can point at keeps a short id,
  // so a viewer comment stays on its block through edits, saves and reloads.
  (() => {
    const page = document.querySelector('.page')
    if (!page) return
    const BLOCK = /^(P|H1|H2|H3|H4|H5|H6|LI|UL|OL|BLOCKQUOTE|ASIDE|SECTION|DIV|TABLE|TR|TD|TH|DL|DT|DD|FIGURE|FIGCAPTION|CAPTION|PRE|HEADER|FOOTER|NAV|SUMMARY|DETAILS|ADDRESS|HGROUP|HR)$/
    const fnv = s => {
      let h = 2166136261
      for (let i = 0; i < s.length; i++) h = Math.imul(h ^ s.charCodeAt(i), 16777619)
      return (h >>> 0).toString(36)
    }
    // A pasted form's named fields can shadow its own members: read through the prototypes.
    const { getAttribute, setAttribute, removeAttribute } = Element.prototype
    const tagOf = Object.getOwnPropertyDescriptor(Element.prototype, 'tagName').get
    const textOf = Object.getOwnPropertyDescriptor(Node.prototype, 'textContent').get
    const idOf = el => getAttribute.call(el, 'id') ?? ''
    const stateOf = Object.getOwnPropertyDescriptor(Document.prototype, 'readyState').get
    // A block that arrives without an id gets the same one in every viewer
    // of this version, so a thread resolves before any save has written it.
    const derive = (el, taken, suffix) => {
      const stem = 'b-' + fnv(tagOf.call(el) + '\\n' + textOf.call(el))
      if (!taken.has(stem)) return stem
      let n = suffix.get(stem) || 2
      while (taken.has(stem + '-' + n)) n++
      suffix.set(stem, n + 1)
      return stem + '-' + n
    }
    // A block made while editing lives only in this tab until a save.
    const fresh = taken => {
      let id = ''
      while (id.length < 4 || taken.has(id)) id = 'b-' + Math.random().toString(36).slice(2, 9)
      return id
    }
    // A repeated id (split, paste, any copy) leaves the newcomer, so a thread
    // never answers to two elements; a pasted id comments can't address is shed.
    const ID = /^[A-Za-z_-][A-Za-z0-9_-]{0,31}$/
    // Ids the author served are link targets: theirs to keep, even on a rebuilt node.
    const served = new Set()
    const owners = new Map()
    const all = (root, s) => (root === page ? Element : Document).prototype.querySelectorAll.call(root, s)
    const assign = loading => {
      const held = [...all(page, '[id]')]
      const keeper = new Map()
      for (const el of held) {
        const id = idOf(el)
        if (owners.get(id) === el || !keeper.has(id)) keeper.set(id, el)
      }
      for (const el of held) {
        const id = idOf(el)
        if (loading && id) served.add(id)
        const known = served.has(id) || owners.get(id) === el || ID.test(id)
        if (keeper.get(id) !== el || !known) removeAttribute.call(el, 'id')
      }
      owners.clear()
      const taken = new Set()
      for (const el of all(document, '[id]')) taken.add(idOf(el))
      const suffix = new Map()
      for (const el of all(page, '*')) {
        let id = idOf(el)
        if (!id && BLOCK.test(tagOf.call(el))) {
          id = loading ? derive(el, taken, suffix) : fresh(taken)
          setAttribute.call(el, 'id', id)
          taken.add(id)
        }
        if (id) owners.set(id, el)
      }
    }
    assign(true)
    // An added element or a rewritten id can bring a duplicate or a gap; what
    // the page's own scripts place while it is still loading is served content.
    const upkeep = new MutationObserver(records => {
      if (records.some(r => r.type === 'attributes' || [...r.addedNodes].some(n => n instanceof Element))) {
        assign(stateOf.call(document) === 'loading')
        upkeep.takeRecords()
      }
    })
    upkeep.observe(page, { childList: true, subtree: true, attributes: true, attributeFilter: ['id'] })
    // Whatever the live upkeep missed, a save never carries one id on two elements.
    page.addEventListener('kit-serialize', e => {
      const seen = new Set()
      for (const el of Element.prototype.querySelectorAll.call(e.detail.root, '[id]')) {
        const id = idOf(el)
        if (seen.has(id)) removeAttribute.call(el, 'id')
        else seen.add(id)
      }
    })
  })();
  // DOC:anchors:end

  // KIT:editor:begin — toolbar wiring: the page is the editing surface,
  // the toolbar drives the live selection; word count and a save status
  // ride the right side. Toolbar markup is per kind; this wiring is
  // byte-shared and treats every control as optional.
  (() => {
    const page = document.querySelector('.page')
    const toolbar = document.querySelector('.toolbar')
    if (!page || !toolbar) return
    // The toolbar never takes focus: the page selection it acts on stays put.
    toolbar.addEventListener('mousedown', ev => ev.preventDefault())
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
    const runCmd = (cmd, arg) => {
      const sel = document.getSelection()
      if (!sel || !sel.rangeCount) return false
      if (!page.contains(sel.getRangeAt(0).commonAncestorContainer)) return false
      return document.execCommand(cmd, false, arg)
    }
    // Kinds that ship the comment kit float drafts over the page (a
    // composer, reply fields in a side panel); the guards below keep
    // toolbar commands off the page selection while one is live, and are
    // inert where no kit exists. One predicate decides "a reply draft is
    // live" so the toolbar and the style picker never disagree.
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
      // Clicks land while a draft keeps focus (mousedown is prevented):
      // commands must not touch the page selection mid-draft. A draft's
      // textarea lives in its own iframe (own document, own undo stack
      // on Blink and Gecko; WebKit's is per-page — a recorded
      // limitation), so undo/redo need no mid-draft handling here — the
      // selection-targeted commands still must not fire from outside the
      // page while a draft is live (.has-draft is the composer's signal).
      const ae = document.activeElement
      // A focused reply draft (an iframe in the side panel) is mid-typing
      // like the composer's fields: commands must not run.
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
    // The paragraph-style menu (kinds that carry one): a toggle, a list of
    // options rendered in their own style, and a label that tracks the
    // block under the caret. Mousedown is prevented toolbar-wide, so the
    // page selection survives every click in here.
    const blockMenu = toolbar.querySelector('[data-block-menu]')
    const blockToggle = blockMenu && blockMenu.querySelector('[data-block-toggle]')
    const blockList = blockMenu && blockMenu.querySelector('.tb-menu-list')
    const blockLabel = blockMenu && blockMenu.querySelector('[data-block-label]')
    const setBlockMenu = open => {
      if (!blockList || !blockToggle) return
      blockList.hidden = !open
      blockToggle.setAttribute('aria-expanded', open ? 'true' : 'false')
    }
    const showBlock = tag => {
      if (!blockList) return
      for (const o of blockList.querySelectorAll('[data-block-value]')) {
        const on = o.dataset.blockValue === tag
        o.setAttribute('aria-selected', on ? 'true' : 'false')
        if (on && blockLabel) blockLabel.textContent = o.textContent
        // Mirror the current style into the toggle's accessible name; the
        // static aria-label would otherwise mask the live label from AT.
        if (on && blockToggle) blockToggle.setAttribute('aria-label', 'Paragraph style: ' + o.textContent)
      }
    }
    if (blockMenu) {
      blockToggle.addEventListener('click', () => setBlockMenu(blockList.hidden))
      blockList.addEventListener('click', ev => {
        const opt = ev.target.closest('[data-block-value]')
        if (!opt) return
        // A keyboard pick focuses the option; closing the menu hides it, so
        // focus must return to the toggle. A mouse pick leaves focus in the
        // page (toolbar mousedown is prevented) — don't pull it out.
        const restoreFocus = blockMenu.contains(document.activeElement)
        setBlockMenu(false)
        // Re-picking the current style is a no-op, like the native select this
        // replaced — formatBlock would rebuild the block and drop its id,
        // detaching any comment pinned to it.
        if (opt.getAttribute('aria-selected') === 'true') { if (restoreFocus && blockToggle) blockToggle.focus(); return }
        // A live comment draft outranks restyling the page.
        const ae = document.activeElement
        if (ae && ae.tagName === 'IFRAME' && ae.closest && ae.closest('.cpanel')) return
        if (document.querySelector('.ccomposer.has-draft') || anyReplyDrafting()) return
        if (runCmd('formatBlock', opt.dataset.blockValue)) page.focus()
        else if (restoreFocus && blockToggle) blockToggle.focus()
        refresh()
      })
      document.addEventListener('mousedown', ev => {
        if (!blockList.hidden && !blockMenu.contains(ev.target)) setBlockMenu(false)
      }, true)
      document.addEventListener('keydown', ev => {
        if (blockList.hidden) return
        if (ev.key === 'Escape') { setBlockMenu(false); page.focus(); return }
        // Arrow keys walk the options, but only while the menu itself holds
        // focus; with the caret back in the page, leave editing keys —
        // Shift/Cmd arrow selection and navigation included — untouched.
        if (ev.key !== 'ArrowDown' && ev.key !== 'ArrowUp') return
        if (ev.altKey || ev.ctrlKey || ev.metaKey || ev.shiftKey) return
        if (!blockMenu.contains(document.activeElement)) return
        ev.preventDefault()
        const opts = [...blockList.querySelectorAll('[data-block-value]')]
        const at = opts.indexOf(document.activeElement)
        const from = at >= 0 ? at : opts.findIndex(o => o.getAttribute('aria-selected') === 'true')
        const next = opts[(from + (ev.key === 'ArrowDown' ? 1 : opts.length - 1)) % opts.length]
        if (next) next.focus()
      })
      // Tabbing out of the list closes it, like a native picker.
      blockMenu.addEventListener('focusout', ev => {
        if (!blockMenu.contains(ev.relatedTarget)) setBlockMenu(false)
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
      if (blockMenu && sel && sel.anchorNode && page.contains(sel.anchorNode)) {
        const el = sel.anchorNode.nodeType === 1 ? sel.anchorNode : sel.anchorNode.parentElement
        const block = el && el.closest('h1, h2, h3, p, blockquote, li')
        if (block) {
          const tag = block.tagName.toLowerCase()
          showBlock(['h1', 'h2', 'h3'].includes(tag) ? tag : 'p')
        }
      }
    }
    document.addEventListener('selectionchange', () => {
      // Draft keystrokes fire selectionchange while the page selection
      // is pinned — toolbar state provably cannot change there.
      const ae = document.activeElement
      if (ae && ae.closest && ae.closest('.ccomposer')) return
      refresh()
    })
    page.addEventListener('input', () => { refresh(); refreshWords() })
    refresh()
    refreshWords()
  })();
  // KIT:editor:end

  // KIT:persist:begin — Save republishes the served source with the live
  // page content spliced in, through the artifact publish capability;
  // without the capability or write access, edits stay in this tab.
  // Unsaved edits are kept in session storage; a page that loads with some
  // shows them, read-only, until the writer saves or discards them.
  (() => {
    const page = document.querySelector('.page')
    const status = document.querySelector('[data-status]')
    const saveBtn = document.querySelector('[data-save]')
    const restoreBtn = document.querySelector('[data-restore]')
    const discardBtn = document.querySelector('[data-discard]')
    if (!page) return
    const KIND = page.className
    const COPY = {
      saved: 'Saved',
      dirty: 'Unsaved changes',
      saving: 'Saving…',
      failed: 'Couldn’t save. Try again.',
      limited: 'Save limit reached. Try again later.',
      tooLarge: 'Too large to save. Remove some content.',
      refused: 'Couldn’t save. Part of this content can’t be published.',
      conflict: 'A newer version exists. Reload to edit it.',
      viewOnly: 'View only. Edits stay in this tab.',
      kept: 'Showing recovered edits. Not saved yet.',
      keptOver: 'Showing recovered edits over a newer version. Saving replaces it.',
      keptHeld: 'Showing recovered edits. Can’t save right now. Reload to try again.',
      keptRefused: 'Can’t save these edits as they are. Edit or discard them.',
    }
    const SETTLE_MS = 3000
    const MIN_GAP_MS = 10000
    const PUBLISH_MS = 45000
    const ASK_MS = 5000
    const STASH_TTL_MS = 120000
    const STASH_KEY = 'kit:restore:' + location.host
    const KEEP_MS = 1000
    const KEEP_TTL_MS = 86400000
    const KEEP_KEY = 'kit:unsaved:' + location.host
    // Split literals: the source must never contain the sentinels it strips.
    const RUNTIME_OPEN = '<!-- frame-' + 'runtime -->'
    const RUNTIME_CLOSE = '<!-- /frame-' + 'runtime -->'
    const COMMENTS_OPEN = '<' + 'script type="application/json" id="__frame_comments__">'
    const COMMENTS_CLOSE = '</' + 'script>'
    let mode = 'boot'
    let dirty = false
    let rev = 0
    let saving = false
    let waitTimer = null
    let lastPublishAt = 0
    let settling = false
    let stale = false
    let errKey = null
    let source = null
    let art = null
    let shown = ''
    let kept = null
    let keptFrom = null
    let keptBase = null
    let keepTimer = null
    let base = null
    let srcMark = null
    let recovered = false
    let over = false

    const say = (key, tone) => {
      if (!status || shown === key) return
      shown = key
      status.textContent = COPY[key]
      if (tone) status.dataset.tone = tone
      else delete status.dataset.tone
    }
    const render = () => {
      // Page-wide hook: per-kind chrome keys reader styling off the mode.
      document.documentElement.dataset.kitMode = mode
      // Recovered edits hold the page until they are saved or discarded.
      const offer = kept !== null && mode === 'writer' && !stale
      // Read-only through the flight and the host reload that follows, so
      // nothing typed can miss the version being saved.
      page.toggleAttribute('inert', saving || settling || kept !== null)
      if (saveBtn) {
        saveBtn.hidden = mode !== 'writer' || offer
        saveBtn.disabled = !dirty || saving || settling || stale || waitTimer !== null
        saveBtn.classList.toggle('is-dirty', dirty)
      }
      if (restoreBtn) restoreBtn.hidden = !offer
      // The copy can go from first paint until a save carries it, even from
      // a page that could not confirm write access or could not save it as
      // it was.
      if (discardBtn) discardBtn.hidden = !recovered || stale
      for (const b of [restoreBtn, discardBtn]) if (b) b.disabled = saving || settling || waitTimer !== null
      if (mode === 'reader') say(kept === null ? 'viewOnly' : 'keptHeld', 'muted')
      else if (stale) say('conflict', 'error')
      else if (saving || waitTimer !== null) say('saving', 'busy')
      else if (errKey) say(errKey, 'error')
      else if (kept !== null) say(over ? 'keptOver' : 'kept', 'warning')
      else if (dirty) say('dirty', 'warning')
      else say('saved')
    }
    const markDirty = () => {
      rev++
      dirty = true
      if (keepTimer === null) keepTimer = setTimeout(keep, KEEP_MS)
      render()
    }
    page.addEventListener('input', markDirty)
    // Programmatic edits (a formula bar, a comment, a slide control)
    // announce themselves; capture phase so non-bubbling dispatches count.
    page.addEventListener('kit-commit', markDirty, true)

    // Source handling: strip exactly what the serve path adds, so a save
    // stores the same shape a tool publish does and never compounds.
    const stripServed = text => {
      let src = text
      const a = src.indexOf(RUNTIME_OPEN)
      const b = a === -1 ? -1 : src.indexOf(RUNTIME_CLOSE, a)
      if (a !== -1 && b !== -1 && a < 8192) {
        src = src.slice(0, a) + src.slice(b + RUNTIME_CLOSE.length)
      }
      let end = src.length
      while (end > 0 && ' \\t\\r\\n'.includes(src[end - 1])) end--
      const trimmed = src.slice(0, end)
      if (trimmed.endsWith(COMMENTS_CLOSE)) {
        const body = trimmed.slice(0, -COMMENTS_CLOSE.length)
        const at = body.lastIndexOf(COMMENTS_OPEN)
        if (at !== -1 && isEnvelope(body.slice(at + COMMENTS_OPEN.length))) {
          src = body.slice(0, body[at - 1] === '\\n' ? at - 1 : at)
        }
      }
      return src
    }
    // The serve path's own test for its block, so both sides agree on
    // what is one: a '<'-free JSON object with a mac and a payload.
    const isEnvelope = s => {
      if (s.includes('<')) return false
      let env
      try { env = JSON.parse(s) } catch { return false }
      return !!env && typeof env === 'object' && !Array.isArray(env) &&
        typeof env.mac === 'string' && env.mac !== '' && Object.hasOwn(env, 'payload')
    }
    // The page article's span, located by position alone: the first page
    // open tag, and the last close before this script, so nothing the
    // content happens to contain can move either end.
    const articleSpan = src => {
      const open = /<article\\s[^>]*\\bclass="(?:[^"]*\\s)?page(?:\\s[^"]*)?"[^>]*>/.exec(src)
      const tail = src.lastIndexOf('KIT:persist:' + 'begin')
      if (!open || tail === -1 || src.indexOf('KIT:persist:' + 'end', tail) === -1) return null
      const openEnd = open.index + open[0].length
      const closeStart = src.lastIndexOf('</' + 'article>', tail)
      return closeStart >= openEnd ? { openEnd, closeStart } : null
    }
    const validSource = src =>
      /^\\s*<!doctype html>/i.test(src) && !src.includes(RUNTIME_OPEN) && articleSpan(src) !== null
    const parse = html => new DOMParser().parseFromString(html, 'text/html')

    // Scriptable surface picked up by a paste must not ride into a version
    // that other viewers' grants will run.
    const DROP = /^(SCRIPT|STYLE|IFRAME|FRAME|FRAMESET|OBJECT|EMBED|APPLET|LINK|META|BASE|TITLE|TEMPLATE|NOSCRIPT|FORM|INPUT|BUTTON|SELECT|TEXTAREA|OPTION|DIALOG|PORTAL|FOREIGNOBJECT|MATH|XMP|LISTING|PLAINTEXT|NOEMBED|NOFRAMES)$/i
    const URL_ATTRS = /^(href|src|xlink:href|action|formaction|poster|background|cite|data|srcset|ping)$/i
    const SAFE_URL = /^(?:https?:|mailto:|#|\\/|\\.\\.?\\/|[^:/?#]*(?:[/?#]|$))/i
    const DATA_IMG = /^data:image\\/(?:png|jpeg|gif|webp|avif);/i
    const TOP_LAYER = /^(popover|popovertarget|interestfor|commandfor|command)$/
    const sanitize = root => {
      // Comments that could end early, or that would read as the runtime's
      // marker once saved, do not come back.
      const notes = Document.prototype.createTreeWalker.call(root.ownerDocument || root, root, NodeFilter.SHOW_COMMENT | NodeFilter.SHOW_PROCESSING_INSTRUCTION)
      const found = []
      while (notes.nextNode()) found.push(notes.currentNode)
      for (const note of found) if (note.nodeType !== Node.COMMENT_NODE || /--|^-|-$|^>|frame-runtime/i.test(note.data)) note.remove()
      // Saved content never poses as the page, the comment store (the
      // article's own trailing block), or the kit's ids.
      const store = [...root.children].findLast(el => el.classList.contains('cstore')) || [...root.querySelectorAll('.cstore')].pop() || null
      for (const el of [...root.querySelectorAll('*')]) {
        if (!root.contains(el)) continue
        // Named descendants can shadow a form's own localName/attributes.
        if (typeof el.localName !== 'string' || !(el.attributes instanceof NamedNodeMap) || DROP.test(el.localName) ||
            /^(animate|set$|discard$)/i.test(el.localName)) {
          Element.prototype.remove.call(el)
          continue
        }
        for (const at of [...el.attributes]) {
          const n = at.name.toLowerCase()
          const v = at.value
          if (n.startsWith('on') || n === 'srcdoc' || n === 'data-frame-runtime' || n === 'autofocus' || n === 'name' ||
              TOP_LAYER.test(n) || (n === 'id' && (v === 'claude' || v.startsWith('__frame') || v.startsWith('cpanel-')))) {
            el.removeAttributeNode(at)
          } else if (URL_ATTRS.test(n)) {
            const val = v.replace(/[\\u0000-\\u0020\\u007f]+/g, '')
            // List-valued attributes are only as safe as each entry.
            const urls = n === 'srcset' ? v.split(',').map(s => s.trim().split(/\\s+/)[0] || '')
              : n === 'ping' ? v.trim().split(/\\s+/) : [val]
            const ok = urls.every(u => SAFE_URL.test(u.replace(/[\\u0000-\\u0020\\u007f]+/g, ''))) ||
              (n === 'src' && el.localName === 'img' && DATA_IMG.test(val))
            if (!ok) el.removeAttributeNode(at)
          } else if (n === 'style' && (!v.trim() || /\\/\\*|\\\\|expression\\s*\\(|url\\s*\\(|image-set\\s*\\(/i.test(v))) {
            el.removeAttributeNode(at)
          }
        }
        el.classList.remove('page')
        if (el !== store) el.classList.remove('cstore')
        if (el.getAttribute('class') === '') el.removeAttribute('class')
      }
      return root
    }
    const serialize = () => {
      const clone = page.cloneNode(true)
      // Load-time decoration (grid chrome, comment marks, a presenting
      // deck) comes off the CLONE, so the saved article is the authored model.
      page.dispatchEvent(new CustomEvent('kit-serialize', { detail: { root: clone } }))
      return sanitize(clone).innerHTML
    }
    // A save must be a fixed point of the browser's own parse: outside the
    // page it is the served source node for node, and inside the page
    // nothing is left for sanitize to strip.
    const shell = doc => {
      const pages = doc.querySelectorAll('article.page')
      if (pages.length !== 1) return null
      pages[0].replaceChildren()
      return [...doc.childNodes].map(n => n.nodeType + (n.outerHTML ?? n.data ?? n.name ?? '')).join('\\n')
    }
    const settled = out => {
      const doc = parse(out)
      const inner = doc.querySelector('article.page')
      if (!inner) return false
      const html = inner.innerHTML
      if (sanitize(inner).innerHTML !== html) return false
      const frame = shell(doc)
      return frame !== null && frame === shell(parse(source))
    }
    const buildDocument = inner => {
      if (source === null) return null
      const span = articleSpan(source)
      if (!span) return null
      const out = source.slice(0, span.openEnd) + inner + source.slice(span.closeStart)
      return validSource(out) && settled(out) ? out : null
    }

    // A short fingerprint of a served source, to tell one version from another.
    const mark = s => {
      let h = 2166136261
      for (let i = 0; i < s.length; i++) h = Math.imul(h ^ s.charCodeAt(i), 16777619)
      return (h >>> 0).toString(36) + ':' + s.length
    }
    // Unsaved edits outlive this page: written while dirty (throttled, and as
    // the page goes away), dropped once saved, discarded, or undone.
    const dropKept = () => { try { sessionStorage.removeItem(KEEP_KEY) } catch {} }
    const keep = () => {
      if (keepTimer !== null) { clearTimeout(keepTimer); keepTimer = null }
      if (mode !== 'writer' || !dirty || kept !== null) return
      try {
        const html = serialize()
        if (html === base) { dropKept(); return }
        const copy = { at: Date.now(), kind: KIND, from: srcMark, html }
        // Room permitting, the copy carries the article it departs from: a
        // page showing the copy has no other way to read that article as a
        // save would write it.
        try { sessionStorage.setItem(KEEP_KEY, JSON.stringify({ ...copy, base })) } catch { sessionStorage.setItem(KEEP_KEY, JSON.stringify(copy)) }
      } catch {}
    }
    addEventListener('pagehide', keep)
    const readKept = () => {
      try {
        const s = JSON.parse(sessionStorage.getItem(KEEP_KEY) || 'null')
        if (s && typeof s === 'object' && typeof s.html === 'string' && s.at <= Date.now() && Date.now() - s.at < KEEP_TTL_MS) {
          // Another kit page on this host looks after its own copy.
          if (s.kind !== KIND) return null
          // Whatever wrote the kept copy, it comes back as parsed, sanitized
          // markup; an edit since undone, or one this page already serves
          // (a save that landed after all), is no edit.
          const was = typeof s.base === 'string' ? s.base : base
          const moot = h => h === was || h === base
          const html = moot(s.html) ? '' : sanitize(parse('<body>' + s.html).body).innerHTML
          if (html && !moot(html)) {
            keptFrom = typeof s.from === 'string' ? s.from : null
            keptBase = typeof s.base === 'string' ? s.base : null
            return html
          }
        }
      } catch {}
      dropKept()
      return null
    }

    // Caret and scroll survive the reload that follows a save.
    const blocks = () => [...page.querySelectorAll('h1,h2,h3,h4,p,li,blockquote,td,th,pre,figcaption,section')]
    const stash = () => {
      try {
        const sel = document.getSelection()
        let block = -1
        let offset = 0
        if (sel && sel.anchorNode && page.contains(sel.anchorNode)) {
          const el = sel.anchorNode.nodeType === 1 ? sel.anchorNode : sel.anchorNode.parentElement
          const holder = el && el.closest('h1,h2,h3,h4,p,li,blockquote,td,th,pre,figcaption,section')
          block = holder ? blocks().indexOf(holder) : -1
          if (holder) {
            const r = document.createRange()
            r.selectNodeContents(holder)
            r.setEnd(sel.anchorNode, sel.anchorOffset)
            offset = r.toString().length
          }
        }
        const scroller = document.scrollingElement || document.documentElement
        // Kind scripts add their own view state (the deck's current
        // slide) to the same stash and read it back on kit-restore.
        const extra = {}
        page.dispatchEvent(new CustomEvent('kit-stash', { detail: extra }))
        sessionStorage.setItem(STASH_KEY, JSON.stringify({ at: Date.now(), block, offset, scroll: scroller.scrollTop, extra }))
      } catch {}
    }
    const clearStash = () => { try { sessionStorage.removeItem(STASH_KEY) } catch {} }
    const restore = () => {
      let s = null
      try { s = JSON.parse(sessionStorage.getItem(STASH_KEY) || 'null') } catch {}
      clearStash()
      if (!s || typeof s !== 'object' || Date.now() - s.at > STASH_TTL_MS) return
      page.dispatchEvent(new CustomEvent('kit-restore', { detail: s.extra && typeof s.extra === 'object' ? s.extra : {} }))
      const scroller = document.scrollingElement || document.documentElement
      if (typeof s.scroll === 'number') scroller.scrollTop = s.scroll
      const holder = blocks()[s.block]
      if (!holder) return
      const walker = document.createTreeWalker(holder, NodeFilter.SHOW_TEXT)
      let left = typeof s.offset === 'number' ? s.offset : 0
      for (let n = walker.nextNode(); n; n = walker.nextNode()) {
        if (left <= n.data.length) {
          const sel = document.getSelection()
          if (sel) sel.collapse(n, left)
          return
        }
        left -= n.data.length
      }
    }

    const codeOf = e => (e && typeof e === 'object' && 'code' in e ? String(e.code) : 'upstream_error')
    const READER_CODES = /^(not_writer|not_granted|not_declared|capability_disabled|capability_removed)$/
    // A host that never answers is a failure to show, not a wait to sit in.
    const within = (p, ms) => {
      let timer = null
      const late = new Promise((resolve, reject) => { timer = setTimeout(() => reject(new Error('timeout')), ms) })
      return Promise.race([p, late]).finally(() => clearTimeout(timer))
    }
    const run = async (restoring = false) => {
      saving = true
      errKey = null
      render()
      const startRev = rev
      let content = null
      let html = null
      try { content = serialize(); html = buildDocument(content) } catch {}
      // Recovered edits that cannot go out as they are open up for editing.
      if (html === null) {
        saving = false
        errKey = restoring ? 'keptRefused' : 'refused'
        if (restoring) { kept = null; dirty = true }
        render()
        return
      }
      stash()
      try {
        await within(art.publish(html), PUBLISH_MS)
        lastPublishAt = Date.now()
        saving = false
        kept = null
        recovered = false
        dropKept()
        base = content
        srcMark = mark(html)
        if ((dirty = rev !== startRev)) keep()
        // The host reloads this view onto the new version next.
        settling = true
        setTimeout(() => { settling = false; render() }, SETTLE_MS)
        render()
      } catch (e) {
        saving = false
        const code = codeOf(e)
        // On conflict the host reloads onto the newer version; both stashes
        // stand, so the caret lands where it was and the edits are offered back.
        if (code === 'conflict') { stale = true; keep(); render(); return }
        clearStash()
        if (READER_CODES.test(code)) {
          // Not this viewer's to save: back to the served version.
          mode = 'reader'
          if (restoring) { dropKept(); kept = null; recovered = false; render(); location.reload(); return }
          render()
          return
        }
        if (code === 'rate_limited') lastPublishAt = Date.now()
        errKey = code === 'rate_limited' ? 'limited' : code === 'too_large' ? 'tooLarge' : 'failed'
        if (restoring && errKey === 'tooLarge') { kept = null; dirty = true }
        render()
      }
    }
    const attempt = (restoring = false) => {
      const wait = lastPublishAt + MIN_GAP_MS - Date.now()
      if (wait > 0) {
        if (waitTimer === null) waitTimer = setTimeout(() => { waitTimer = null; if (restoring) restoreKept(); else save() }, wait)
        render()
        return
      }
      // Kind chrome outside the page (a formula bar, a comment draft)
      // settles or objects before anything is read.
      if (!page.dispatchEvent(new CustomEvent('kit-presave', { cancelable: true }))) { render(); return }
      run(restoring)
    }
    const save = () => {
      if (mode === 'writer' && dirty && kept === null && !saving && !settling && !stale) attempt()
    }
    const restoreKept = () => {
      if (kept !== null && mode === 'writer' && !saving && !settling && !stale && waitTimer === null) attempt(true)
    }
    if (saveBtn) saveBtn.addEventListener('click', save)
    if (restoreBtn) restoreBtn.addEventListener('click', restoreKept)
    if (discardBtn) discardBtn.addEventListener('click', () => {
      if (saving || settling || waitTimer !== null || !recovered) return
      dropKept()
      // Nothing on show outlives this reload, not even a copy a failed
      // restore opened up for editing.
      dirty = false
      settling = true
      setTimeout(() => { settling = false; render() }, SETTLE_MS)
      render()
      // The served version comes back with the page's own scripts wired to it.
      location.reload()
    })
    document.addEventListener('keydown', e => {
      if (mode === 'writer' && (e.metaKey || e.ctrlKey) && !e.altKey && !e.shiftKey && (e.key === 's' || e.key === 'S')) {
        e.preventDefault()
        if (kept === null) save(); else restoreKept()
      }
    })

    // Capability resolution. A host may attach window.claude a beat after
    // inline scripts run, so absence is concluded only after a few seconds
    // of looking.
    const runtime = () => {
      const c = window.claude
      return c && typeof c === 'object' && !c.nodeType ? c : null
    }
    const acquire = name => {
      const c = runtime()
      if (!c) return Promise.resolve(null)
      if (typeof c.use === 'function') {
        const slow = new Promise(resolve => setTimeout(() => resolve(null), ASK_MS))
        try { return Promise.race([Promise.resolve(c.use(name)).catch(() => null), slow]) } catch { return Promise.resolve(null) }
      }
      return Promise.resolve(c[name] || (name === 'artifact' ? c.self : null) || null)
    }
    const whenRuntime = () => new Promise(resolve => {
      if (runtime()) { resolve(); return }
      let tries = 0
      const tick = () => {
        if (runtime() || ++tries > 30) resolve()
        else setTimeout(tick, 100)
      }
      setTimeout(tick, 100)
    })
    const boot = async () => {
      // Later kind scripts listen for kit-restore and kit-serialize; wait
      // until they ran.
      let read = false
      const early = () => { if (read) return; read = true; if (kept === null) base = serialize(); restore() }
      if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', early, { once: true })
      else setTimeout(early, 0)
      // One deadline for the whole read, body included.
      const fetched = within(typeof fetch === 'function' ? fetch('./', { credentials: 'same-origin', cache: 'no-store' }).then(r => (r.ok ? r.text() : null)) : Promise.reject(), 4 * ASK_MS)
        .then(t => (t === null ? null : stripServed(t)))
        .catch(() => null)
      await whenRuntime()
      const [cap, user, text] = await Promise.all([acquire('artifact'), acquire('user'), fetched])
      art = cap && typeof cap.publish === 'function' ? cap : null
      source = text !== null && validSource(text) ? text : null
      let writer = art !== null && source !== null
      let denied = false
      if (writer && user && typeof user.canEdit === 'function') {
        // Only an explicit no is a denial; any other answer merely fails to confirm.
        try { const a = await within(user.canEdit(), ASK_MS); denied = a === false; if (a !== true) writer = false } catch { writer = false }
      }
      mode = writer ? 'writer' : 'reader'
      // A reader has nothing to decide: back to the served version. A page
      // that merely failed to confirm access keeps the copy for the next load.
      if (denied && kept !== null) { dropKept(); kept = null; recovered = false; render(); location.reload(); return }
      if (source !== null) srcMark = mark(source)
      over = kept !== null && keptFrom !== null && srcMark !== null && keptFrom !== srcMark
      // Over the same version, the copy's record of the article stands in
      // for the reading this page could not take before showing the copy.
      if (kept !== null && !over && keptBase !== null) base = keptBase
      early()
      render()
      keep()
    }
    // Recovered edits take the served article's place at first paint, so
    // they are seen exactly as they would be saved.
    base = serialize()
    kept = readKept()
    recovered = kept !== null
    if (recovered) page.replaceChildren(...sanitize(parse('<body>' + kept).body).childNodes)
    render()
    boot()
  })();
  // KIT:persist:end
</script>
