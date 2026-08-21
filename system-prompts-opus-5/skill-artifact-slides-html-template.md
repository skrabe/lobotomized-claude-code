<!--
name: 'Skill: Artifact slides HTML template'
description: >-
  Bundled live slide-deck Artifact editor template used by the slides skill,
  including presentation mode, notes, comments, and overflow handling.
ccVersion: 2.1.238
-->
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title><!-- SLOT: TITLE — the deck's name alone, short and distinctive; never a "Name — explainer" compound; the explainer lives in SUBTITLE -->Deck</title>
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
  /* KIT:comment-chrome:begin — styles for the select-to-comment kit:
     bubble, composer, side panel, anchor marks. Carried only by the
     kinds that ship KIT:comment. */
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
  /* The anchor mark is a change-bar in the margin, not an underline a
     reader mistakes for a rule; the wash (.cmark) is reserved for hover
     and panel focus. */
  .cmark { background: var(--cds-accent-bg); border-bottom: 1px solid var(--cds-text-accent); }
  .canchor { position: relative; }
  .canchor::before {
    content: ""; position: absolute; left: -14px; top: 2px; bottom: 2px;
    width: 3px; border-radius: 2px; background: var(--cds-text-accent); opacity: 0.5;
  }
  .canchor:hover { background: var(--cds-accent-bg); }
  .canchor:hover::before { opacity: 1; }
  /* A reader cannot save, so a comment drafted in their tab would never
     reach anyone: the writing controls step aside and the panel reads. */
  [data-kit-mode="reader"] .cbub,
  [data-kit-mode="reader"] .ccomposer,
  [data-kit-mode="reader"] .rop-comment,
  [data-kit-mode="reader"] .cpanel .cact button:not([data-act="goto"]),
  [data-kit-mode="reader"] .cpanel .crow-reply { display: none; }
  @media (prefers-reduced-motion: no-preference) {
    .cpanel, .ccomposer, .cbub { animation: kit-enter 140ms ease-out; }
    @keyframes kit-enter { from { opacity: 0; transform: translateY(2px); } to { opacity: 1; transform: none; } }
  }
  /* KIT:comment-chrome:end */

  /* ── The studio (slides-specific): rail of live thumbnails on the
     left, the current slide large on the right. ─────────────────── */
  .studio { display: flex; gap: 16px; max-width: 1480px; margin: 0 auto; align-items: flex-start; }
  .rail {
    flex: 0 0 184px; position: sticky; top: 44px;
    max-height: calc(100vh - 60px); overflow-y: auto;
    display: flex; flex-direction: column; gap: 10px;
    font-family: var(--cds-font-sans);
  }
  .rthumb {
    appearance: none; border: 1px solid var(--cds-border); background: none;
    border-radius: var(--cds-radius); padding: 3px; cursor: pointer; text-align: left;
    /* The rail previews the deck in the deck's own voice. */
    font: inherit; color: inherit;
  }
  .rthumb:hover { border-color: var(--cds-border-strong); }
  .rthumb.on { border-color: var(--cds-text-accent); }
  .rthumb .frame { pointer-events: none; cursor: default; border: none; }
  .rnum { font-size: 11px; color: var(--cds-text-muted); padding: 2px 4px 0; display: block; }
  .radd {
    appearance: none; border: 1px dashed var(--cds-border-strong); background: none;
    color: var(--cds-text-muted); font-family: var(--cds-font-sans); font-size: 13px;
    border-radius: var(--cds-radius); padding: 10px; cursor: pointer;
  }
  .rcell { position: relative; }
  .rcell .rthumb { display: block; width: 100%; }
  .radd-group { display: flex; flex-direction: column; gap: 2px; padding: 6px 2px; }
  .radd-label { font: 11px var(--cds-font-sans); letter-spacing: 0.05em; text-transform: uppercase; color: var(--cds-text-muted); padding: 0 2px 2px; }
  .radd-group .radd { text-align: left; }
  .rops {
    display: none; gap: 2px; padding: 3px;
    position: absolute; left: 4px; right: 4px; bottom: 4px;
    background: var(--cds-surface-1); border: 1px solid var(--cds-border);
    border-radius: var(--cds-radius);
  }
  .rcell.on .rops, .rcell .rops:focus-within { display: flex; }
  .rops button {
    appearance: none; border: 1px solid transparent; background: none;
    color: var(--cds-text-secondary); font-size: 13px; border-radius: var(--cds-radius);
    padding: 4px 7px; cursor: pointer; flex: 1;
  }
  .rops button:hover { background: var(--cds-accent-bg); color: var(--cds-text-primary); }
  .rops button:disabled { opacity: 0.3; cursor: default; background: none; }
  body:has(.page[inert]) .rops, body:has(.page[inert]) .radd-group, body:has(.page[inert]) .slide-undo button { opacity: 0.4; pointer-events: none; }
  .radd:hover { background: var(--cds-accent-bg); color: var(--cds-text-accent); }
  .page.deck { flex: 1; min-width: 0; outline: none; }

  /* The deck: one slide in the editor at a time; every slide in print.
     Type inside a frame is sized in cqw so the same styles carry from a
     rail thumbnail to the editor to the full present-mode viewport. */
  .slide { display: none; min-width: 0; }
  .slide.current { display: block; }
  .frame {
    aspect-ratio: 16 / 9;
    container-type: size;
    background: var(--cds-surface-1);
    border: 1px solid var(--cds-border);
    border-radius: var(--cds-radius);
    overflow: hidden;
    position: relative;
  }
  .frame-body {
    position: absolute;
    inset: 0;
    padding: 7cqh 8cqw;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .notes {
    display: block;
    font-family: var(--cds-font-sans);
    font-size: 13px;
    line-height: 1.5;
    color: var(--cds-text-secondary);
    margin: 8px 2px 0;
  }
  .notes::before { content: "Speaker notes"; display: block; font-size: 11px; color: var(--cds-text-muted); margin-bottom: 2px; }
  /* Empty notes stay AUTHORABLE in the studio: a visible invitation,
     :empty semantics preserved. Presenting hides them. */
  .notes:empty::before { content: "Add speaker notes\\u2026"; color: var(--cds-text-muted); }
  body.present .notes:empty { display: none; }

  /* Slide typography — cqw-proportional so every size renders alike. */
  .frame h1 { font-size: 6.5cqw; line-height: 1.12; margin: 0 0 3cqh; font-weight: 600; text-wrap: balance; }
  .frame h2 { font-size: 5cqw; line-height: 1.18; margin: 0 0 4cqh; font-weight: 600; text-wrap: balance; }
  .frame p, .frame li { font-size: 3.1cqw; line-height: 1.45; }
  .frame p { margin: 0 0 2cqh; }
  .frame ul, .frame ol { margin: 0; padding-left: 4cqw; }
  .frame li { margin-bottom: 2.2cqh; }
  .frame li::marker { color: var(--cds-text-muted); }
  .frame a { color: var(--cds-text-accent); }

  .title .frame-body, .statement .frame-body, .closing .frame-body { align-items: flex-start; text-align: left; }
  .title .subtitle { font-size: 3.4cqw; color: var(--cds-text-secondary); }
  .title .byline, .closing .next { font-family: var(--cds-font-sans); font-size: 2.4cqw; color: var(--cds-text-muted); margin-top: 4cqh; }
  /* One status garment family-wide: quiet letterspaced caps, scaled to
     the frame like the byline it sits in. */
  .status { display: inline-block; font-weight: 700; font-size: 2cqw; letter-spacing: 0.08em; text-transform: uppercase; color: var(--cds-text-secondary); white-space: nowrap; margin-right: 0.8cqw; }
  .statement .frame-body p, .closing .frame-body > p:first-child { font-size: 5.2cqw; line-height: 1.3; font-weight: 600; text-wrap: balance; margin: 0; }

  .frame table { border-collapse: collapse; font-family: var(--cds-font-sans); font-size: 2.6cqw; width: 100%; }
  .frame th { text-align: left; font-weight: 600; border-bottom: 1px solid var(--cds-border-strong); padding: 1.6cqh 3cqw 1.2cqh 0; }
  .frame td { border-bottom: 1px solid var(--cds-border); padding: 1.6cqh 3cqw 1.6cqh 0; vertical-align: top; }
  .stats { display: flex; gap: 8cqw; }
  .stat-value { font-size: 8cqw; font-weight: 600; line-height: 1.1; }
  .stat-label { font-family: var(--cds-font-sans); font-size: 2.3cqw; color: var(--cds-text-secondary); margin-top: 1cqh; }

  /* Present mode: the current slide's frame fills the viewport, letterboxed
     to 16:9; the counter and the notes panel are fixed chrome. */
  body.present { overflow: hidden; }
  body.present .toolbar, body.present .rail { display: none; }
  /* The audience sees the slide, never the collaboration chrome. The
     anchor layer goes inert too: clicks fall through to the step gesture,
     keeping the kit byte-shared and present-agnostic. */
  body.present .canchor { border-bottom: none; background: none; pointer-events: none; }
  body.present .canchor::before { display: none; }
  body.present .cmark { background: none; border-bottom: none; }
  /* The collaboration layer is hidden, never removed — the kit's module
     state must survive a Present/Esc cycle. */
  body.present .cbub, body.present .ccomposer, body.present .cpanel, body.present .ovf-badge,
  body.present .slide-undo { display: none; }
  body.present { background: #0b0b0b; }
  body.present .canvas { padding: 0; }
  body.present .slide.current .frame {
    position: fixed;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: min(100vw, calc(100vh * 16 / 9));
    border: none;
    border-radius: 0;
  }
  body.present .slide.current .notes { display: none; }
  body.present.notes-open .slide.current .notes {
    display: block;
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    margin: 0;
    padding: 14px 20px 16px;
    background: var(--cds-surface-1);
    border-top: 1px solid var(--cds-border);
    font-size: 17px;
    line-height: 1.55;
    height: 28vh;
    overflow: auto;
  }
  body.present.notes-open .slide.current .notes { padding-left: max(20px, calc((100vw - 70ch) / 2)); padding-right: max(20px, calc((100vw - 70ch) / 2)); }
  body.present.notes-open .slide.current .notes::before {
    content: "Next: " attr(data-next);
    display: block; margin-bottom: 6px;
    font: 12px var(--cds-font-sans); color: var(--cds-text-secondary);
  }
  body.present.notes-open .slide.current .notes::after {
    content: "presenter notes — visible on THIS screen; press N before sharing it";
    display: block; margin-top: 8px;
    font: 11px var(--cds-font-sans); letter-spacing: 0.06em; text-transform: uppercase;
    color: var(--cds-text-muted);
  }
  /* The slide yields the notes band instead of being occluded by it:
     centered in the 72vh above the notes, never underneath them. */
  body.present.notes-open .slide.current .frame {
    top: 36vh;
    width: min(96vw, calc(68vh * 16 / 9));
  }
  /* Blank screen: B toggles a black field, the presenter's pause. */
  body.present.blanked .slide.current .frame { visibility: hidden; }
  body.present.blanked { background: #000; }
  /* An aside-less slide keeps the presenter band: a studio-owned
     stand-in, so the frame's yielded 28vh never renders as a hole. */
  .next-peek {
    display: none;
    position: fixed; left: 0; right: 0; bottom: 0;
    margin: 0; height: 28vh; overflow: auto;
    padding: 14px max(20px, calc((100vw - 70ch) / 2)) 16px;
    background: var(--cds-surface-1); border-top: 1px solid var(--cds-border);
    font-size: 17px; line-height: 1.55; color: var(--cds-text-muted);
  }
  body.present.notes-open.no-notes .next-peek { display: block; }
  .next-peek .npk-next { font: 12px var(--cds-font-sans); color: var(--cds-text-secondary); margin-bottom: 6px; }
  .next-peek::after {
    content: "presenter notes — visible on THIS screen; press N before sharing it";
    display: block; margin-top: 8px;
    font: 11px var(--cds-font-sans); letter-spacing: 0.06em; text-transform: uppercase;
    color: var(--cds-text-muted);
  }
  .present-hint {
    position: fixed; left: 50%; top: 24px; transform: translateX(-50%);
    font: 13px var(--cds-font-sans); color: var(--cds-text-secondary);
    background: var(--cds-surface-1); border: 1px solid var(--cds-border);
    border-radius: 999px; padding: 6px 16px; transition: opacity 1s ease;
  }
  .present-hint.fade { opacity: 0; }
  .present-hud {
    display: none;
    position: fixed; left: 16px; bottom: 12px;
    font-family: var(--cds-font-sans); font-size: 13px; color: var(--cds-text-muted);
    font-variant-numeric: tabular-nums;
  }
  body.present.notes-open .present-hud, body.present .present-hud.on { display: block; }
  .end-cue {
    display: none;
    position: fixed; left: 50%; bottom: 48px; transform: translateX(-50%);
    font-family: var(--cds-font-sans); font-size: 13px; color: var(--cds-text-muted);
    background: var(--cds-surface-1); border: 1px solid var(--cds-border);
    border-radius: 999px; padding: 4px 14px;
  }
  body.present .end-cue.on { display: block; }
  .slide-undo {
    position: fixed; left: 50%; bottom: 20px; transform: translateX(-50%); z-index: 30;
    font-family: var(--cds-font-sans); font-size: 13px;
    background: var(--cds-surface-1); border: 1px solid var(--cds-border-strong);
    border-radius: var(--cds-radius); padding: 8px 12px; display: flex; gap: 10px; align-items: center;
  }
  .slide-undo button {
    appearance: none; border: 1px solid var(--cds-border); background: none;
    color: var(--cds-text-accent); font: inherit; border-radius: var(--cds-radius);
    padding: 3px 10px; cursor: pointer;
  }
  .ovf-badge {
    position: absolute; right: 8px; bottom: 6px;
    font: 10px var(--cds-font-sans); color: var(--cds-text-danger); letter-spacing: 0.04em;
  }
  /* The label is CSS content, so the badge contributes no textContent
     to the slide it sits in and never reaches a save. */
  .ovf-badge::before { content: "overflows"; }
  .counter {
    display: none;
    position: fixed;
    right: 16px;
    bottom: 12px;
    font-family: var(--cds-font-sans);
    font-size: 13px;
    color: var(--cds-text-muted);
  }
  body.present .counter { display: block; }

  @media print {
    /* Print is always light, regardless of the screen color scheme or the
       shell's theme stamp (the selector list out-specifies both dark rules),
       and always one slide per page, whatever mode the screen was in. */
    :root, :root[data-theme="dark"], :root:not([data-theme="light"]) {
      --cds-surface-0: #ffffff;
      --cds-surface-1: #ffffff;
      --cds-surface-2: #ffffff;
      --cds-text-primary: #0b0b0b;
      --cds-text-secondary: #52514e;
      --cds-text-muted: #898781;
      --cds-border: rgba(11, 11, 11, 0.1);
      --cds-border-strong: rgba(11, 11, 11, 0.2);
      --cds-text-accent: #184f95;
      --cds-accent-bg: rgba(24, 79, 149, 0.08);
      --cds-text-danger: #b3261e;
      --cds-text-warning: #c25124;
    }
    .toolbar, .rail, .counter, body.present .counter,
    .cbub, .ccomposer, .cpanel, .slide-undo, .ovf-badge,
    .next-peek, .present-hud, .present-hint, .end-cue { display: none; }
    .canchor::before { display: none; }
    .canvas, body.present .canvas { padding: 0; }
    .studio { display: block; max-width: none; }
    .slide, body.present .slide { display: block; }
    .slide:not(:last-child), body.present .slide:not(:last-child) { break-after: page; }
    .frame, body.present .slide .frame, body.present .slide.current .frame {
      position: static;
      transform: none;
      width: 100%;
      border: 1px solid var(--cds-border);
      border-radius: 0;
    }
    .notes, body.present .slide .notes, body.present .slide.current .notes,
    body.present.notes-open .slide.current .notes { display: block; position: static; font-size: 10pt; padding: 6pt 0 0; border: none; max-height: none; }
    /* The :empty invitation is editor chrome — never ink. */
    .notes:empty, body.present .slide .notes:empty,
    body.present .slide.current .notes:empty { display: none; }
  }
</style>

<!-- TOOLBAR (slides variant): inline marks + bullets + undo/redo, the
     Present control, and the save status. Toolbar markup is per kind;
     the shared kit styles (KIT:chrome) and wires (KIT:editor) whatever
     controls a kind carries. -->
<div class="toolbar" role="toolbar" aria-label="Formatting">
  <button data-cmd="bold" title="Bold" aria-label="Bold"><b>B</b></button>
  <button data-cmd="italic" title="Italic" aria-label="Italic"><i>I</i></button>
  <button data-cmd="underline" title="Underline" aria-label="Underline"><u>U</u></button>
  <span class="tb-sep"></span>
  <button data-cmd="insertUnorderedList" title="Bulleted list" aria-label="Bulleted list"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="2.5" cy="3.5" r="0.8" fill="currentColor" stroke="none"/><circle cx="2.5" cy="8" r="0.8" fill="currentColor" stroke="none"/><circle cx="2.5" cy="12.5" r="0.8" fill="currentColor" stroke="none"/><path d="M6 3.5h8M6 8h8M6 12.5h8"/></svg></button>
  <span class="tb-sep"></span>
  <button data-cmd="undo" title="Undo" aria-label="Undo"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5.5 3 2.5 6l3 3"/><path d="M2.5 6h7a4 4 0 0 1 0 8H6"/></svg></button>
  <button data-cmd="redo" title="Redo" aria-label="Redo"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.5 3l3 3-3 3"/><path d="M13.5 6h-7a4 4 0 0 0 0 8H10"/></svg></button>
  <span class="tb-sep"></span>
  <button data-present title="Present (Esc to exit)" aria-label="Present"><svg viewBox="0 0 16 16" width="15" height="15" fill="currentColor" stroke="none" aria-hidden="true"><path d="M4.5 2.8v10.4L13 8z"/></svg> Present</button>
  <button data-cpanel-toggle title="All comments" aria-label="All comments" aria-expanded="false"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 3.5h11v7h-6l-3 3v-3h-2z"/></svg> <span data-ccount>0</span></button>
  <span class="tb-right">
    <button class="tb-save" data-save hidden disabled title="Save (Ctrl+S / Cmd+S)" aria-label="Save">Save</button>
    <button class="tb-save" data-restore hidden title="Save the recovered edits as a new version" aria-label="Save recovered edits">Save</button>
    <button class="tb-save" data-discard hidden title="Discard the recovered edits and reload the saved version" aria-label="Discard recovered edits">Discard</button>
    <span class="tb-status" data-status role="status">Saved</span>
  </span>
</div>
<!-- /TOOLBAR -->

<div class="canvas">
  <div class="studio">
    <nav class="rail" aria-label="Slides"></nav>
    <article class="page deck" data-comment-empty="No comments yet — select slide text, or use the thumbnail’s comment button" contenteditable="true" spellcheck="true">

      <section class="slide title current">
        <div class="frame"><div class="frame-body">
          <h1><!-- SLOT: TITLE — the deck's name alone, short and distinctive; never a "Name — explainer" compound --> Deck title</h1>
          <p class="subtitle"><!-- SLOT: SUBTITLE — one line: what this deck is for and for whom -->What this deck is for and for whom.</p>
          <p class="byline"><span class="status"><!-- SLOT: STATUS — where the deck is: Draft, In review, or Final -->Draft</span> <!-- SLOT: DECK_META — presenter and date, e.g. "Riley Chen · June 2026" -->Presenter · Month Year</p>
        </div></div>
        <aside class="notes"><!-- SLOT: NOTES — the spoken argument for this slide, in full sentences; omit the aside when there is nothing to add -->How to open the presentation.</aside>
      </section>

      <!-- SLOT: SLIDES
           One <section class="slide"> per idea, in speaking order. Three shapes:
           the default below (an <h2> that asserts the slide's point, then short
           bullets), class="statement" for one line that carries the slide
           alone, and class="data" for a single small <table> or a .stats row
           of a few numbers. Duplicate a shape's section per new slide; the
           rail picks up every slide automatically. The spoken argument goes
           in each slide's <aside class="notes">. -->
      <section class="slide">
        <div class="frame"><div class="frame-body">
          <h2>The point this slide asserts</h2>
          <ul>
            <li>Short phrase, not a sentence</li>
            <li>Five bullets at most</li>
          </ul>
        </div></div>
        <aside class="notes">What to say over this slide.</aside>
      </section>

      <section class="slide statement">
        <div class="frame"><div class="frame-body">
          <p>One line that carries the slide alone.</p>
        </div></div>
        <aside class="notes">What to say over this slide.</aside>
      </section>

      <section class="slide data">
        <div class="frame"><div class="frame-body">
          <h2>What the numbers say</h2>
          <div class="stats">
            <div class="stat">
              <div class="stat-value">0%</div>
              <div class="stat-label">What this number is</div>
            </div>
          </div>
        </div></div>
        <aside class="notes">What to say over this slide.</aside>
      </section>

      <!-- SLOT: CLOSING
           The last slide: the one takeaway to leave the room with, and what
           happens next. -->
      <section class="slide closing">
        <div class="frame"><div class="frame-body">
          <p>The one takeaway to leave the room with.</p>
          <p class="next">What happens next.</p>
        </div></div>
        <aside class="notes">How to close the presentation.</aside>
      </section>

      <p class="cstore" hidden aria-hidden="true" contenteditable="false"><!-- SLOT: COMMENTS_STORE — leave as an empty JSON array; readers comments accumulate here -->[]</p>

    </article>
  </div>
  <div class="counter" aria-hidden="true"></div>
</div>

<script>
  // SLIDES:anchors:begin — slide anchor identity and the kit's per-kind
  // anchor hooks. Installed BEFORE the kit regions evaluate: KIT:comment
  // renders marks at its own init, which must resolve slide anchors
  // through the slide-id and fingerprint legs — the generic path walk
  // would mark whole sections and honor a drifted index unverified.
  (() => {
    const page = document.querySelector('.page')
    if (!page) return
    // Durable slide identity: every slide gets a local id at load (and
    // on creation); comment anchors live in {slide: id} space, so
    // reorders, duplicates, and deletions can never retarget a
    // conversation to the wrong slide.
    let slideSeq = 0
    const ensureSlideId = s => {
      // The id is saved with the page, so it stays stable across saves
      // and reloads; a fresh one can only miss, never mis-target.
      if (!s.dataset.slideId) s.dataset.slideId = 'sl' + (++slideSeq) + '-' + Math.random().toString(36).slice(2, 6)
      return s.dataset.slideId
    }
    // A repeated id (a slide pasted in whole) is re-minted on the
    // newcomer, wherever it lands, so one conversation never answers to
    // two slides and never wanders to the copy.
    const owners = new Map()
    const dedupeIds = () => {
      const slides = [...page.querySelectorAll('.slide')]
      const keeper = new Map()
      for (const s of slides) {
        const id = s.dataset.slideId
        if (id && (owners.get(id) === s || !keeper.has(id))) keeper.set(id, s)
      }
      owners.clear()
      for (const s of slides) {
        if (keeper.get(s.dataset.slideId) !== s) delete s.dataset.slideId
        owners.set(ensureSlideId(s), s)
      }
    }
    dedupeIds()
    // And again when slides arrive in bulk, wherever they land: a
    // recovered copy, a paste.
    new MutationObserver(dedupeIds).observe(page, { childList: true, subtree: true })
    const slideFp = s => {
      const h = s.querySelector('.frame h1, .frame h2') || s.querySelector('.frame')
      return h ? h.textContent.trim().slice(0, 80) : ''
    }
    const slideAnchor = s => {
      const a = { slide: ensureSlideId(s), path: 'section:' + [...page.children].indexOf(s) }
      const fp = slideFp(s)
      if (fp) a.fp = fp
      return a
    }
    page.kitAnchorResolver = a => {
      if (!a || !a.slide) return undefined
      const s = [...page.querySelectorAll('.slide')].find(x => x.dataset.slideId === a.slide)
      if (s) return s.querySelector('.frame h1, .frame h2') || s.querySelector('.frame')
      // The path leg is honored only with a matching content fingerprint —
      // a bare index would select whatever slide drifted into it.
      if (a.fp && typeof a.path === 'string') {
        const idx = Number(a.path.split(':')[1])
        const el = Number.isInteger(idx) ? page.children[idx] : null
        if (el && el.classList && el.classList.contains('slide') && slideFp(el) === a.fp) {
          return el.querySelector('.frame h1, .frame h2') || el.querySelector('.frame')
        }
      }
      return null
    }
    page.kitAnchorBuilder = range => {
      const n = range && range.startContainer
      const holder = n && (n.nodeType === 1 ? n : n.parentElement)
      const s = holder && holder.closest ? holder.closest('.slide') : null
      if (!s) return undefined
      return slideAnchor(s)
    }
    page.slidesEnsureId = ensureSlideId
    page.slidesAnchor = slideAnchor
  })();
  // SLIDES:anchors:end

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

  // KIT:comment:begin — select-to-comment: a selection raises a Comment
  // bubble (and Ctrl/Cmd+Alt+M opens the composer — the editable surface
  // swallows bare shortcuts, so keyboard commenting needs a chord); the
  // composer files into the document's OWN comment store (the hidden
  // .cstore block), saved with the page like every other edit.
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
    // "A reply draft is live", for a reply iframe — the literal the
    // toolbar's guard (KIT:editor) carries too; a test pins them equal.
    const replyDraft = f => {
      const d0 = f.contentDocument
      const ins0 = d0 ? d0.querySelectorAll('input') : []
      // A typed byline is a draft too — compared against its own
      // prefill, so the convenience text alone never blocks a close.
      return ins0.length && (ins0[0].value.trim() !== '' ||
        (ins0[1] && ins0[1].value.trim() !== (ins0[1].dataset.prefill || '').trim()))
    }
    // Comments live IN the document: one hidden annotated block (.cstore)
    // holds the serialized list, and appends are edits saved with the
    // page like any other. Every stored
    // string is other people's input: rendered with textContent, never
    // markup. IDENTITY SEAM (documented, not active): the entry schema
    // reserves an author id field for the user capability's opaque
    // per-organization tokens (resolved live, per viewer, via
    // profiles()); writing such a token into doc content is a mint site
    // in that program's enumeration, so activation is coordinated there
    // — shipped code stores only commenter-typed bylines or nothing.
    const storeEl = () => [...page.children].findLast(el => el.classList.contains('cstore')) || [...page.querySelectorAll('.cstore')].pop() || null
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
      // Read at the moment of the write, so the rewrite carries whatever
      // the store holds now rather than a copy cached at load.
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
      // Anchor on the nearest block: an inline mark can be split, merged,
      // or retyped away, so a hop through one would not survive.
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
    // Decoration stays out of a save: the clone sheds its marks.
    page.addEventListener('kit-serialize', e => {
      for (const el of e.detail.root.querySelectorAll('.canchor, .cmark')) {
        el.classList.remove('canchor', 'cmark')
        el.removeAttribute('aria-details')
        el.removeAttribute('aria-description')
        delete el.dataset.canchorId
      }
    })
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
            // The same read-append-recommit path appends ride.
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
    // Resolve/reopen rewrites the one entry and recommits the store.
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
          const fr2 = [...panel.querySelectorAll('.crow-reply iframe')].find(replyDraft)
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
    // Observe the store block so the count and an open panel follow any
    // rewrite of it, not only this region's own appends.
    const follow = new MutationObserver(() => {
      refreshCount(); renderMarks()
      // Drafts and focus survive the rebuild (renderPanel captures
      // and restores them), so the panel can always follow the store.
      renderPanel()
      if (pcount && !document.body.classList.contains('present')) {
        pcount.classList.remove('pulse')
        void pcount.offsetWidth
        pcount.classList.add('pulse')
      }
    })
    let followed = null
    // A replaced article (recovered edits) brings its own store block.
    const bind = () => {
      const st = storeEl()
      if (st === followed) return
      followed = st
      follow.disconnect()
      if (st) follow.observe(st, { childList: true, characterData: true, subtree: true })
      refreshCount()
      renderMarks()
    }
    new MutationObserver(bind).observe(page, { childList: true })
    bind()
    // The textarea lives in the composer's own iframe: on Blink and
    // Gecko its document carries its own undo stack, so page and draft
    // history never interleave there (WebKit's undo manager is
    // per-page — a recorded limitation). The .has-draft class on the
    // host div is the cross-region signal for a non-empty draft.
    const openComposer = (range, quoted, anchorOverride) => {
      if (document.documentElement.dataset.kitMode === 'reader') return
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
    // A save ends in a reload no open draft would survive: Save waits for
    // the draft and hands it the keyboard, as closing the panel does.
    page.addEventListener('kit-presave', e => {
      const fr0 = composer && composer.classList.contains('has-draft')
        ? composer.querySelector('iframe')
        : [...document.querySelectorAll('.cpanel .crow-reply iframe')].find(replyDraft)
      const d0 = fr0 && fr0.contentDocument
      const live = d0 ? [...d0.querySelectorAll('textarea, input')] : []
      if (!live.length) return
      e.preventDefault()
      const tgt = live[0].value.trim() ? live[0] : live[1] || live[0]
      tgt.focus()
      announceComment(fr0.closest('.crow-reply') ? 'A reply draft is open — send or clear it first' : 'A comment draft is open — add or cancel it first')
    })
    // A page that turns out to be read-only drops a draft begun while it
    // loaded; nothing written there could reach anyone.
    new MutationObserver(() => {
      if (document.documentElement.dataset.kitMode !== 'reader' || !composer) return
      clear(composer); composer = null; clear(bubble); bubble = null
    }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-kit-mode'] })
    // The comment chrome holds whenever the page does: a reply sent then
    // would not reach the version that ends up saved.
    const hold = () => {
      for (const el of document.querySelectorAll('.cpanel, .ccomposer, .cbub')) if (!page.contains(el)) el.toggleAttribute('inert', page.hasAttribute('inert'))
    }
    new MutationObserver(hold).observe(page, { attributes: true, attributeFilter: ['inert'] })
    new MutationObserver(hold).observe(document.body, { childList: true })
  })();
  // KIT:comment:end

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

  // Slide studio (kind-specific): the rail of live thumbnails, slide
  // selection, adding a slide, and present mode.
  (() => {
    const page = document.querySelector('.page')
    const rail = document.querySelector('.rail')
    const counter = document.querySelector('.counter')
    if (!page || !rail) return
    const slides = () => [...page.querySelectorAll('.slide')]
    // Structural edits (add, duplicate, move, delete, undo) are unsaved
    // changes like any keystroke: one signal tells the persistence kit.
    const edited = () => page.dispatchEvent(new CustomEvent('kit-commit'))
    // The page's read-only spells (a save in flight) hold the rail's
    // structural edits too.
    const frozen = () => page.hasAttribute('inert')

    const select = slide => {
      if (slide && !page.contains(slide)) { rebuild(); slide = null }
      const list = slides()
      if (!slide) slide = list.find(s => s.classList.contains('current')) || list[0]
      if (!slide) return
      for (const s of list) s.classList.toggle('current', s === slide)
      for (const [i, b] of [...rail.querySelectorAll('.rthumb')].entries()) {
        b.classList.toggle('on', list[i] === slide)
        const cell = b.closest('.rcell')
        if (cell) cell.classList.toggle('on', list[i] === slide)
      }
      if (counter) counter.textContent = (list.indexOf(slide) + 1) + ' / ' + list.length
      // The operations ride the selection.
      {
        const ops0 = rail.querySelector('.rops')
        const onCell = rail.querySelector('.rcell.on')
        if (ops0 && onCell && ops0.parentElement !== onCell) onCell.appendChild(ops0)
        for (const t of rail.querySelectorAll('.rthumb')) {
          if (t.classList.contains('on')) t.setAttribute('aria-current', 'true')
          else t.removeAttribute('aria-current')
        }
      }
      // Rehearsal accounting rides the one shared path every
      // navigation uses — arrows, digits, Home/End, clicks alike.
      {
        const i2 = list.indexOf(slide)
        if (i2 > furthest) furthest = i2
        clockSlide(slide)
      }
      // The rehearse band knows what comes next — with or without an
      // aside: the stand-in band carries the cue when no aside exists.
      {
        const nxt = list[list.indexOf(slide) + 1]
        const peek2 = nxt ? (nxt.querySelector('h1, h2, p') ? nxt.querySelector('h1, h2, p').textContent.trim().slice(0, 70) : 'next slide') : 'end of deck'
        const notes = slide.querySelector('.notes')
        if (notes) notes.dataset.next = peek2
        peekNext.textContent = 'Next: ' + peek2
        document.body.classList.toggle('no-notes', !notes)
      }
    }
    const current = () => page.querySelector('.slide.current') || slides()[0]

    // The rail shows each slide as a real scaled render: cloned frames
    // re-rendered through the same container-query typography. The
    // variant classes ride on the thumb so section-scoped type rules
    // still match; element ids are stripped so the clones never shadow
    // the page's own anchors.
    // One undo slot: the removed slide is HELD, not destroyed, and one
    // click puts it back where it was.
    const offerUndo = (node, anchor) => {
      const old = document.querySelector('.slide-undo')
      if (old) old.remove()
      const bar = document.createElement('div')
      bar.className = 'slide-undo'
      bar.setAttribute('role', 'status')
      const msg = document.createElement('span')
      msg.textContent = 'Slide deleted'
      const undo = document.createElement('button')
      undo.type = 'button'
      undo.textContent = 'Undo'
      undo.addEventListener('click', () => {
        if (frozen()) return
        if (anchor && anchor.isConnected) anchor.after(node)
        else page.prepend(node)
        bar.remove()
        rebuild(); select(node)
        edited()
        // The click detached the focused button: land on the restored
        // slide's thumb instead of <body>.
        const t = rail.querySelectorAll('.rthumb')[slides().indexOf(node)]
        if (t) t.focus()
      })
      bar.append(msg, undo)
      document.body.appendChild(bar)
      // The bar stays until the next delete replaces it — a deadline
      // would make the only restore path a race.
    }
    // After a rebuild replaces the rail's DOM, focus returns to the
    // equivalent control instead of falling to the body.
    const restoreOpsFocus = idx => {
      const b = rail.querySelectorAll('.rops button')[idx]
      if (b) b.focus()
    }
    // Any focused rail control survives a rebuild: ops by index, thumbs
    // by index, add-slide buttons by label.
    const railFocusKey = () => {
      const af = document.activeElement
      if (!af || !rail.contains(af)) return null
      const i = [...rail.querySelectorAll('.rops button')].indexOf(af)
      if (i >= 0) return { kind: 'ops', i }
      const t = [...rail.querySelectorAll('.rthumb')].indexOf(af.closest('.rthumb'))
      if (t >= 0) return { kind: 'thumb', i: t }
      if (af.classList.contains('radd')) return { kind: 'radd', label: af.textContent }
      return null
    }
    const restoreRailFocus = k => {
      if (!k) return
      if (k.kind === 'ops') restoreOpsFocus(k.i)
      else if (k.kind === 'thumb') { const b = rail.querySelectorAll('.rthumb')[k.i]; if (b) b.focus() }
      else { const b = [...rail.querySelectorAll('.radd')].find(x => x.textContent === k.label); if (b) b.focus() }
    }
    // Slide identity and the anchor hooks live in SLIDES:anchors at the
    // top of this script, installed pre-kit.
    const ensureSlideId = page.slidesEnsureId
    const slideAnchor = page.slidesAnchor
    const thumbOf = slide => {
      const f = slide.querySelector('.frame')
      const c = f ? f.cloneNode(true) : document.createElement('div')
      c.removeAttribute('contenteditable')
      for (const el of c.querySelectorAll('[contenteditable]')) el.removeAttribute('contenteditable')
      for (const el of c.querySelectorAll('[id]')) el.removeAttribute('id')
      c.className = 'frame'
      // The clone is presentation: aria-hidden here, not at the call
      // sites, so the observer's thumb refresh cannot drop it.
      c.setAttribute('aria-hidden', 'true')
      return c
    }
    const rebuild = () => {
      rail.textContent = ''
      const all = slides()
      for (const [i, s] of all.entries()) {
        // The cell hosts the thumb BUTTON and the ops row as siblings —
        // a button may not contain interactive descendants, and ARIA
        // flattens a button's subtree for assistive tech.
        const cell = document.createElement('div')
        cell.className = 'rcell' + (s.classList.contains('current') ? ' on' : '')
        const b = document.createElement('button')
        b.type = 'button'
        b.className = ('rthumb ' +
          [...s.classList].filter(x => x !== 'slide' && x !== 'current').join(' ')).trim() +
          (s.classList.contains('current') ? ' on' : '')
        const tclone = thumbOf(s)
        b.appendChild(tclone)
        const n = document.createElement('span')
        n.className = 'rnum'
        n.textContent = String(i + 1)
        n.setAttribute('aria-hidden', 'true')
        b.appendChild(n)
        const t0 = s.querySelector('h1, h2, p')
        b.setAttribute('aria-label', 'Slide ' + (i + 1) + ' of ' + all.length + (t0 ? ': ' + t0.textContent.trim().slice(0, 60) : ''))
        b.addEventListener('click', () => select(s))
        cell.appendChild(b)
        rail.appendChild(cell)
      }
      // New slides arrive in a LAYOUT — the vocabulary the deck's CSS
      // already speaks, offered at the moment of creation.
      const LAYOUTS = [
        ['Bullets', '', '<h2>New slide</h2><ul><li></li></ul>'],
        ['Statement', 'statement', '<p>One line that carries the slide</p>'],
        ['Stat', 'data', '<h2>New stat</h2><div class="stats"><div class="stat"><div class="stat-value">0</div><div class="stat-label">what it measures</div></div></div>'],
        ['Table', 'data', '<h2>New comparison</h2><table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td></td><td></td></tr></tbody></table>'],
        ['Title', 'title', '<h1>New title</h1><p class="subtitle"></p>'],
        ['Closing', 'closing', '<p>New takeaway</p><p class="next">What comes next</p>'],
      ]
      const add = document.createElement('div')
      add.className = 'radd-group'
      const addLabel = document.createElement('span')
      addLabel.className = 'radd-label'
      addLabel.textContent = '+ New slide'
      add.appendChild(addLabel)
      for (const [name, cls, inner] of LAYOUTS) {
        const b = document.createElement('button')
        b.type = 'button'
        b.className = 'radd'
        b.textContent = name
        b.title = 'Insert a "' + name + '" slide after the current one'
        b.addEventListener('click', () => {
          if (frozen()) return
          const tpl = document.createElement('section')
          tpl.className = ('slide ' + cls).trim()
          tpl.innerHTML = '<div class="frame"><div class="frame-body">' + inner + '</div></div>' +
            '<aside class="notes"></aside>'
          ensureSlideId(tpl)
          const cur = current()
          if (cur) cur.after(tpl)
          else page.appendChild(tpl)
          const fk = railFocusKey()
          rebuild()
          select(tpl)
          restoreRailFocus(fk)
          edited()
        })
        add.appendChild(b)
      }
      rail.appendChild(add)
      // The operations ride the SELECTED thumbnail — revealed where the
      // eye already is, not in a global strip below the rail.
      const ops = document.createElement('div')
      ops.className = 'rops'
      const curCell = [...rail.querySelectorAll('.rcell')].find(c => c.classList.contains('on'))
      if (curCell) curCell.appendChild(ops)
      else rail.appendChild(ops)
      ops.addEventListener('keydown', e => {
        if ((e.ctrlKey || e.metaKey) && (e.key === 'ArrowUp' || e.key === 'ArrowDown')) {
          e.preventDefault()
          const fns = ops.querySelectorAll('button')
          // buttons: 0 dup, 1 up, 2 down, 3 delete, 4 comment
          if (e.key === 'ArrowUp' && fns[1] && !fns[1].disabled) fns[1].click()
          if (e.key === 'ArrowDown' && fns[2] && !fns[2].disabled) fns[2].click()
        }
      })
      const mk = (label, title, fn) => {
        const b = document.createElement('button')
        b.type = 'button'
        if (label.startsWith('<svg')) b.innerHTML = label
        else b.textContent = label
        b.title = title
        b.setAttribute('aria-label', title)
        b.addEventListener('click', () => { if (!frozen()) fn() })
        ops.appendChild(b)
        return b
      }
      mk("<svg viewBox=\\"0 0 16 16\\" width=\\"13\\" height=\\"13\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"1.5\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" aria-hidden=\\"true\\"><rect x=\\"5\\" y=\\"5\\" width=\\"8\\" height=\\"8\\" rx=\\"1\\"/><path d=\\"M11 5V3.5A1.5 1.5 0 0 0 9.5 2h-5A1.5 1.5 0 0 0 3 3.5v5A1.5 1.5 0 0 0 4.5 10H5\\"/></svg>", 'Duplicate this slide', () => {
        const cur = current()
        if (!cur) return
        const copy = cur.cloneNode(true)
        copy.classList.remove('current')
        // The clone must not share the original's comment-anchor identity
        // — nor wear its rendered comment marks: a phantom .canchor would
        // open the ORIGINAL's conversation from the copy.
        delete copy.dataset.slideId
        for (const el of [copy, ...copy.querySelectorAll('.canchor')]) {
          el.classList.remove('canchor')
          el.removeAttribute('aria-description')
          delete el.dataset.canchorId
        }
        ensureSlideId(copy)
        cur.after(copy)
        rebuild(); select(copy)
        restoreOpsFocus(0)
        edited()
      })
      const moveUp = () => {
        const cur = current()
        const prev = cur && cur.previousElementSibling
        if (prev && prev.classList.contains('slide')) { cur.after(prev); rebuild(); select(cur); restoreOpsFocus(1); edited() }
      }
      const moveDown = () => {
        const cur = current()
        const next = cur && cur.nextElementSibling
        if (next && next.classList.contains('slide')) { cur.before(next); rebuild(); select(cur); restoreOpsFocus(2); edited() }
      }
      mk("<svg viewBox=\\"0 0 16 16\\" width=\\"13\\" height=\\"13\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"1.5\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" aria-hidden=\\"true\\"><path d=\\"M8 13V3M4 7l4-4 4 4\\"/></svg>", 'Move this slide up', moveUp)
      mk("<svg viewBox=\\"0 0 16 16\\" width=\\"13\\" height=\\"13\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"1.5\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" aria-hidden=\\"true\\"><path d=\\"M8 3v10M4 9l4 4 4-4\\"/></svg>", 'Move this slide down', moveDown)
      mk("<svg viewBox=\\"0 0 16 16\\" width=\\"13\\" height=\\"13\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"1.5\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" aria-hidden=\\"true\\"><path d=\\"M3 4.5h10M6.5 4.5V3h3v1.5M4.5 4.5l.7 8a1 1 0 0 0 1 .9h3.6a1 1 0 0 0 1-.9l.7-8\\"/></svg>", 'Delete this slide', () => {
        const list = slides()
        const cur = current()
        if (!cur || list.length < 2) return
        const fallback = cur.nextElementSibling && cur.nextElementSibling.classList.contains('slide')
          ? cur.nextElementSibling : cur.previousElementSibling
        // Undoable: the node is kept, not destroyed — one click restores.
        const anchor = cur.previousElementSibling
        cur.remove()
        rebuild(); select(fallback)
        offerUndo(cur, anchor)
        restoreOpsFocus(3)
        liveSay('Slide deleted — Undo available')
        edited()
      })
      const ropComment = mk("<svg viewBox=\\"0 0 16 16\\" width=\\"13\\" height=\\"13\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"1.5\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" aria-hidden=\\"true\\"><path d=\\"M2.5 3.5h11v7h-6l-3 3v-3h-2z\\"/></svg>", 'Comment on this slide', () => {
        const cur = current()
        const target = cur && (cur.querySelector('.frame h1, .frame h2') || cur.querySelector('.frame'))
        if (!target) return
        const r = document.createRange()
        r.selectNodeContents(target)
        document.dispatchEvent(new CustomEvent('kit-comment-on',
          { detail: { range: r, quote: target.textContent.trim(), anchor: slideAnchor(cur) } }))
      })
      ropComment.classList.add('rop-comment')
    }

    // One observer keeps the rail honest against every mutation source —
    // typing, execCommand, undo, and programmatic writes.
    let pending = null
    const touched = new Set()
    new MutationObserver(muts => {
      let saw = false
      for (const m of muts) {
        const n = m.target.nodeType === 1 ? m.target : m.target.parentElement
        // Comment-store writes are invisible to the rail — the kit's own
        // observer answers them; a rebuild here is pure waste.
        if (n && n.closest && n.closest('.cstore')) continue
        const s = n && n.closest ? n.closest('.slide') : null
        touched.add(s && page.contains(s) ? s : null)
        saw = true
      }
      if (!saw) return
      clearTimeout(pending)
      pending = setTimeout(() => {
        const list = slides()
        const thumbs = rail.querySelectorAll('.rthumb')
        if (touched.has(null) || thumbs.length !== list.length) {
          touched.clear()
          // The rebuild replaces the rail's DOM mid-interaction: hand
          // focus back the way the operation handlers do.
          const fk = railFocusKey()
          rebuild()
          select(current())
          restoreRailFocus(fk)
          return
        }
        for (const s of touched) {
          const i = list.indexOf(s)
          const b = thumbs[i]
          const old = b && b.querySelector('.frame')
          if (old) b.replaceChild(thumbOf(s), old)
          // The accessible name tracks the content the clone shows.
          if (b) {
            const t0 = s.querySelector('h1, h2, p')
            b.setAttribute('aria-label', 'Slide ' + (i + 1) + ' of ' + list.length + (t0 ? ': ' + t0.textContent.trim().slice(0, 60) : ''))
          }
        }
        touched.clear()
      }, 400)
    }).observe(page, { childList: true, characterData: true, subtree: true })

    // Present mode: full-viewport stepping, editing off for the duration.
    const presentBtn = document.querySelector('[data-present]')
    let wasEditable = null
    const enter = () => {
      wasEditable = page.getAttribute('contenteditable')
      // Blur first, explicitly: an engine's implicit blur-on-revoke is not
      // something to rely on.
      if (document.activeElement && document.activeElement.blur) document.activeElement.blur()
      const sel = document.getSelection()
      if (sel) sel.removeAllRanges()
      page.setAttribute('contenteditable', 'false')
      document.body.classList.add('present')
      if (rehearse) document.body.classList.add('notes-open')
      // Fullscreen is a request, not a requirement — presenting works
      // identically when the browser declines.
      if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen().catch(() => {})
      }
      startedAt = Date.now()
      elapsedBase = 0
      timerOn = true
      furthest = slides().indexOf(current())
      slideSinks.clear()
      slideClock = { id: null, at: 0 }
      clockSlide(current())
      endCue.classList.remove('on')
      tickHud()
      // First entry teaches the keys, then gets out of the way.
      if (!hintShown) {
        hintShown = true
        const hint = document.createElement('div')
        hint.className = 'present-hint'
        hint.textContent = '\\u2190 \\u2192 step \\u00b7 N notes \\u00b7 B or . blank \\u00b7 T timer (Shift+T resets) \\u00b7 digits jump \\u00b7 Esc exit'
        document.body.appendChild(hint)
        setTimeout(() => hint.classList.add('fade'), 4000)
        setTimeout(() => hint.remove(), 5000)
      }
      hudTimer = setInterval(tickHud, 1000)
      select(current())
      liveSay('Presenting — slide ' + (slides().indexOf(current()) + 1) + ' of ' + slides().length)
    }
    const leave = () => {
      // The run's state is read BEFORE the classes drop: clockSlide's
      // present-guard must still pass to bank the final slide's dwell,
      // and the report gates on whether THE RUN had notes open.
      clockSlide(null)
      const hadNotes = document.body.classList.contains('notes-open')
      document.body.classList.remove('present', 'notes-open', 'blanked', 'no-notes')
      // The keys hint is present chrome — an early Esc must not strand
      // it over the toolbar until its removal timer fires.
      const hint = document.querySelector('.present-hint')
      if (hint) hint.remove()
      // Per-run present state must not leak into the next run.
      hud.classList.remove('on')
      clearTimeout(jumpTimer)
      jumpBuf = ''
      if (wasEditable !== null) page.setAttribute('contenteditable', wasEditable)
      clearInterval(hudTimer)
      if (document.fullscreenElement && document.exitFullscreen) document.exitFullscreen().catch(() => {})
      // The run reports itself: time on stage and how far the deck got.
      {
        const list = slides()
        const sinks = [...slideSinks.entries()]
          .map(([id, ms]) => ({ i: list.findIndex(s => s.dataset.slideId === id), ms }))
          .filter(x => x.i >= 0 && x.ms > 3000)
          .sort((a, b) => b.ms - a.ms).slice(0, 2)
        const sinkTxt = sinks.length && hadNotes
          ? ' \\u00b7 longest: ' + sinks.map(x => 'slide ' + (x.i + 1) + ' ' + fmtElapsed(x.ms)).join(', ')
          : ''
        const msg = 'Run: ' + fmtElapsed(elapsedMs()) + ' \\u00b7 reached slide ' + (furthest + 1) + ' of ' + list.length + sinkTxt
        const toast = document.createElement('div')
        toast.className = 'slide-undo'
        toast.textContent = msg
        document.body.appendChild(toast)
        setTimeout(() => toast.remove(), 6000)
        liveSay(msg)
      }
      select(current())
    }
    // The presenter's HUD: elapsed + clock, by the counter. T toggles
    // the elapsed timer (and resets it), B blanks the screen.
    let startedAt = 0, timerOn = true, hudTimer = null
    let elapsedBase = 0 // accumulated ms from completed running spans
    let furthest = 0
    let slideClock = { id: null, at: 0 }
    const slideSinks = new Map()
    const clockSlide = s => {
      if (!document.body.classList.contains('present')) return
      const now = Date.now()
      if (slideClock.id) slideSinks.set(slideClock.id, (slideSinks.get(slideClock.id) || 0) + (now - slideClock.at))
      slideClock = { id: s ? s.dataset.slideId : null, at: now }
    }
    let jumpBuf = '', jumpTimer = null
    const elapsedMs = () => elapsedBase + (timerOn ? Date.now() - startedAt : 0)
    const fmtElapsed = ms => {
      const s = Math.floor(ms / 1000)
      return String(Math.floor(s / 60)).padStart(2, '0') + '\\u2236' + String(s % 60).padStart(2, '0')
    }
    const hud = document.createElement('div')
    hud.className = 'present-hud'
    document.body.appendChild(hud)
    const endCue = document.createElement('div')
    endCue.className = 'end-cue'
    endCue.textContent = 'End of deck — Esc to exit'
    document.body.appendChild(endCue)
    const liveRegion = document.createElement('span')
    liveRegion.className = 'visually-hidden'
    liveRegion.setAttribute('aria-live', 'polite')
    document.body.appendChild(liveRegion)
    const peekBand = document.createElement('div')
    peekBand.className = 'next-peek'
    const peekNext = document.createElement('div')
    peekNext.className = 'npk-next'
    const peekEmpty = document.createElement('div')
    peekEmpty.textContent = 'No notes for this slide'
    peekBand.append(peekNext, peekEmpty)
    document.body.appendChild(peekBand)
    const liveSay = msg => { liveRegion.textContent = ''; setTimeout(() => { liveRegion.textContent = msg }, 30) }
    const tickHud = () => {
      // Paused time shows FROZEN, never hidden — and never counts.
      hud.textContent = fmtElapsed(elapsedMs()) + (timerOn ? '' : ' \\u23f8') + '  ·  ' +
        new Date().toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' })
    }
    let rehearse = false
    // R from the studio rehearses — the key the comments promise.
    document.addEventListener('keydown', e => {
      if (document.body.classList.contains('present')) return
      if (e.ctrlKey || e.metaKey || e.altKey) return
      if (e.target && (e.target.isContentEditable || e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) return
      if (e.key === 'r' || e.key === 'R') { e.preventDefault(); rehearse = true; document.body.classList.add('notes-open'); enter() }
    })
    let hintShown = false
    // Rehearse: the presenter's private run — notes and timer on from
    // the first slide. Shift+click or the R key from the studio. One
    // listener: enter() reads the flag and opens the notes band itself.
    if (presentBtn) {
      presentBtn.title = 'Present (Shift+click to rehearse with notes)'
      presentBtn.addEventListener('click', e => { rehearse = e.shiftKey; enter() })
    }
    // Every present-mode navigation announces — arrows, Home/End, and
    // digit jumps alike; a silent landing strands a screen reader.
    const announceSlide = s => {
      if (!document.body.classList.contains('present')) return
      const list = slides()
      const title = s.querySelector('h1, h2')
      liveSay('Slide ' + (list.indexOf(s) + 1) + ' of ' + list.length + (title ? ' — ' + title.textContent.trim().slice(0, 60) : ''))
    }
    const step = d => {
      const list = slides()
      const i = list.indexOf(current())
      const j = Math.min(list.length - 1, Math.max(0, i + d))
      const atEnd = d > 0 && i === list.length - 1
      endCue.classList.toggle('on', atEnd)
      select(list[j])
      announceSlide(list[j])
    }
    document.addEventListener('keydown', e => {
      if (!document.body.classList.contains('present')) return
      if (e.ctrlKey || e.metaKey || e.altKey) return
      if (e.target.closest && e.target.closest('.ccomposer')) return
      if (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT') return
      // While blanked, the FIRST interaction only unblanks.
      if (document.body.classList.contains('blanked') && e.key !== 'b' && e.key !== 'B' && e.key !== '.') {
        e.preventDefault()
        document.body.classList.remove('blanked')
        return
      }
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown' || e.key === 'Enter') { e.preventDefault(); step(1) }
      if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); step(-1) }
      if (e.key === 'n' || e.key === 'N') {
        e.preventDefault()
        document.body.classList.toggle('notes-open')
        liveSay(document.body.classList.contains('notes-open') ? 'Notes open' : 'Notes closed')
      }
      if (e.key === 't' || e.key === 'T') {
        e.preventDefault()
        // In plain present, T first SUMMONS the HUD (the audience never
        // sees it unasked); further presses pause/resume, Shift+T resets.
        if (!document.body.classList.contains('notes-open') && !hud.classList.contains('on')) {
          hud.classList.add('on')
        } else if (e.shiftKey) { elapsedBase = 0; startedAt = Date.now(); timerOn = true }
        else if (timerOn) { elapsedBase += Date.now() - startedAt; timerOn = false }
        else { startedAt = Date.now(); timerOn = true }
        tickHud()
        liveSay(timerOn ? 'Timer running' : 'Timer paused')
      }
      if (e.key === 'b' || e.key === 'B' || e.key === '.') {
        e.preventDefault()
        document.body.classList.toggle('blanked')
        liveSay(document.body.classList.contains('blanked') ? 'Screen blanked — press any key to resume' : 'Screen restored')
      }
      if (e.key === 'Home') { e.preventDefault(); const s0 = slides()[0]; select(s0); announceSlide(s0); endCue.classList.remove('on') }
      if (e.key === 'End') { e.preventDefault(); const l = slides(); select(l[l.length - 1]); announceSlide(l[l.length - 1]) }
      if (/^[0-9]$/.test(e.key)) {
        e.preventDefault()
        // Two-digit jumps: digits buffer briefly, so 1 then 2 reaches
        // slide 12 instead of flashing slide 1.
        jumpBuf += e.key
        clearTimeout(jumpTimer)
        jumpTimer = setTimeout(() => {
          const l = slides()
          const n = Number(jumpBuf)
          jumpBuf = ''
          if (n >= 1 && n <= l.length) { select(l[n - 1]); announceSlide(l[n - 1]); endCue.classList.remove('on') }
        }, 400)
      }
      if (e.key === 'Escape') { e.preventDefault(); leave() }
    })
    document.addEventListener('click', e => {
      if (!document.body.classList.contains('present')) return
      if (document.body.classList.contains('blanked')) { document.body.classList.remove('blanked'); return }
      if (e.target.closest('.notes, .next-peek, .toolbar, .counter, .cbub, .ccomposer, .cpanel, .slide-undo')) return
      const sel = document.getSelection()
      if (sel && !sel.isCollapsed) return
      // A click advances, everywhere, like every remote and every tool —
      // going back is the arrows' job.
      step(1)
    })

    // The comments panel can point into ANY slide: before the kit
    // scrolls and focuses, the owning slide must be current — the studio
    // answers the reveal event by selecting it first.
    document.addEventListener('kit-reveal-anchor', e => {
      const el = e.detail && e.detail.element
      const owner = el && el.closest && el.closest('.slide')
      if (owner && !owner.classList.contains('current')) select(owner)
    })

    // A slide holding more than its frame shows is a surprise on the
    // projector — badge the overflow in the editor and the rail.
    const checkOverflow = () => {
      // A display:none slide has no boxes — reveal hidden slides
      // off-screen for the measure. Phased: every reveal, then every
      // read, then every restore — interleaving them forces a fresh
      // synchronous layout per hidden slide.
      const entries = []
      const w = page.clientWidth || 800
      for (const s of slides()) {
        const fb = s.querySelector('.frame-body')
        const fr = s.querySelector('.frame')
        if (!fb || !fr) continue
        entries.push({ s, fb, fr, staged: !s.classList.contains('current'), prev: '' })
      }
      for (const p of entries) {
        if (p.staged) {
          p.prev = p.s.style.cssText
          p.s.style.cssText = 'display: block; position: absolute; visibility: hidden; left: -9999px; width: ' + w + 'px'
        }
      }
      for (const p of entries) p.over = p.fb.scrollHeight > p.fb.clientHeight + 2
      for (const p of entries) {
        if (p.staged) p.s.style.cssText = p.prev
      }
      for (const p of entries) {
        let badge = p.fr.querySelector('.ovf-badge')
        if (p.over && !badge) {
          badge = document.createElement('div')
          badge.className = 'ovf-badge'
          badge.setAttribute('contenteditable', 'false')
          p.fr.appendChild(badge)
        } else if (!p.over && badge) badge.remove()
      }
    }
    setTimeout(checkOverflow, 300)
    page.addEventListener('input', () => { clearTimeout(checkOverflow._t); checkOverflow._t = setTimeout(checkOverflow, 600) })

    // View state rides the persistence kit's stash across the reload a
    // save triggers; the saved article itself carries none of it.
    page.addEventListener('kit-stash', e => { e.detail.slide = slides().indexOf(current()) })
    page.addEventListener('kit-restore', e => {
      const s = typeof e.detail.slide === 'number' ? slides()[e.detail.slide] : null
      if (s) select(s)
    })
    page.addEventListener('kit-serialize', e => {
      const root = e.detail.root
      const all = [...root.querySelectorAll('.slide')]
      all.forEach((s, i) => s.classList.toggle('current', i === 0))
      for (const b of root.querySelectorAll('.ovf-badge')) b.remove()
      for (const n of root.querySelectorAll('.notes[data-next]')) delete n.dataset.next
    })

    rebuild()
    select(current())
  })();
</script>
