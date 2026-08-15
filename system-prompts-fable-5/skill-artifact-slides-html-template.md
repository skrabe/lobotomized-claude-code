<!--
name: 'Skill: Artifact slides HTML template'
description: >-
  Bundled live slide-deck Artifact editor template used by the slides skill,
  including presentation mode, notes, comments, and overflow handling.
ccVersion: 2.1.233
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
     status. One implementation for the family. The chrome recedes until
     pointed at — the text is the interface; only the save status keeps
     full presence, since trust in it is the product. */
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
  /* A flash on text that changed under the reader (another viewer's
     edit arriving). */
  .cmark { background: var(--cds-accent-bg); border-bottom: 1px solid var(--cds-text-accent); }
  .visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
  :focus-visible { outline: 2px solid var(--cds-text-accent); outline-offset: 1px; }
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
     reader mistakes for a rule; the wash is reserved for hover and
     panel focus. */
  .canchor { position: relative; }
  .canchor::before {
    content: ""; position: absolute; left: -14px; top: 2px; bottom: 2px;
    width: 3px; border-radius: 2px; background: var(--cds-text-accent); opacity: 0.5;
  }
  .canchor:hover { background: var(--cds-accent-bg); }
  .canchor:hover::before { opacity: 1; }
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
  .clone-note {
    font: 10px var(--cds-font-sans); letter-spacing: 0.05em; text-transform: uppercase;
    color: var(--cds-text-danger); padding: 2px 0 0 2px;
  }
  .rops button {
    appearance: none; border: 1px solid transparent; background: none;
    color: var(--cds-text-secondary); font-size: 13px; border-radius: var(--cds-radius);
    padding: 4px 7px; cursor: pointer; flex: 1;
  }
  .rops button:hover { background: var(--cds-accent-bg); color: var(--cds-text-primary); }
  .rops button:disabled { opacity: 0.3; cursor: default; background: none; }
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
  body.present .slide-undo, body.present .clone-note { display: none; }
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
  /* The label is CSS content: the badge must contribute no textContent,
     or inserting it inside an annotated slide reads as a foreign write
     to KIT:persist's baseline compare. */
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
    }
    .toolbar, .rail, .counter, body.present .counter,
    .cbub, .ccomposer, .cpanel, .slide-undo, .ovf-badge,
    .clone-note, .next-peek, .present-hud, .present-hint, .end-cue { display: none; }
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
      // A server-addressed slide keeps one identity for every viewer and
      // load; an unaddressed one gets a session id that can only miss,
      // never mis-target — the anchor's path leg covers reloads.
      if (!s.dataset.slideId) s.dataset.slideId = s.dataset.id ? 'sd-' + s.dataset.id : 'sl' + (++slideSeq) + '-' + Math.random().toString(36).slice(2, 6)
      return s.dataset.slideId
    }
    for (const s of page.querySelectorAll('.slide')) ensureSlideId(s)
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
    const blockSel = toolbar.querySelector('select[data-block]')
    // Disabled at init on live docs and never re-enabled — the tracker
    // would maintain state its only consumer can never read.
    if (blockSel && !blockSel.disabled) {
      // The select steals focus — track the page's last selection live, so
      // the picked style lands on the block the user was in.
      let lastRange = null, lastEl = null, lastTag = 'p'
      document.addEventListener('selectionchange', () => {
        // Draft keystrokes pin the page selection — the tracker would
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
      // Draft keystrokes fire selectionchange while the page selection
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

  // KIT:persist:begin — live persistence, live docs only: artifact.edit
  // (legacy self.edit) is the live-doc write surface, so anywhere it is
  // absent or refused (no runtime, classic artifact, read-only viewer)
  // edits stay local to this view. It comes from claude.use('artifact')
  // when the runtime offers that, else lazily off window.claude; presence
  // alone does not prove a live doc (a declared capability mounts a
  // rejecting edit on a non-live doc), so the save status reports
  // persistence only after a first server-accepted commit.
  (() => {
    const page = document.querySelector('.page')
    const status = document.querySelector('[data-status]')
    if (!page) return
    let used = null
    let asked = false
    let answered = false
    const selfCap = () => {
      const c = window.claude
      if (c && typeof c.use === 'function') {
        if (!asked) {
          asked = true
          c.use('artifact').then(got => {
            used = got
            answered = true
            if (got) sweep()
            else if (dirty.size && !disabled) say('Local only')
          })
        }
        return used && typeof used.edit === 'function' ? used : null
      }
      const api = c && (c.artifact || c.self)
      return api && typeof api.edit === 'function' ? api : null
    }
    // Asked but not yet answered: edits are tracked as if the doc were
    // live (the fail-safe direction for the local-only latches) and the
    // status names them local only once use() has actually said no.
    const pending = () => asked && !answered
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
          else if (page.querySelector('[data-id]') && (selfCap() || pending())) degraded = true
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
      if (!block && (selfCap() || pending()) && !fmtInput) {
        const n = sel && sel.anchorNode
        queueMicrotask(() => {
          const live = document.getSelection()
          const probe = n && n.isConnected ? n : live && live.anchorNode
          if (!(probe && blockOf(probe))) degraded = true
        })
      }
      if (!disabled && !fmtInput) say(block && (selfCap() || pending()) ? 'Editing…' : 'Local only')
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
        if (selfCap() || pending()) degraded = true
        if (!disabled) say('Local only')
      }
    }, true)
    const flush = el => {
      const key = el.dataset.id
      if (disabled || inflight.has(key) || !dirty.has(el)) return
      const api = selfCap()
      if (api === null) { if (!pending()) say('Local only'); return }
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
    // Ask for the namespace at load so the first edit rarely waits on it.
    selfCap()
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
    // still match; cloned addressing ids are stripped — the clones live
    // outside the commit surface.
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
        if (anchor && anchor.isConnected) anchor.after(node)
        else page.prepend(node)
        bar.remove()
        rebuild(); select(node)
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
      c.removeAttribute('data-id')
      for (const el of c.querySelectorAll('[data-id]')) el.removeAttribute('data-id')
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
          const tpl = document.createElement('section')
          tpl.className = ('slide ' + cls).trim()
          tpl.innerHTML = '<div class="frame"><div class="frame-body">' + inner + '</div></div>' +
            '<aside class="notes"></aside>'
          // View-local on live docs, same standard as every structural op
          // — say so on the slide itself.
          if (live) {
            const tag = document.createElement('div')
            tag.className = 'clone-note'
            tag.setAttribute('contenteditable', 'false')
            tag.textContent = 'new — not saved to the live doc'
            tpl.appendChild(tag)
          }
          ensureSlideId(tpl)
          const cur = current()
          if (cur) cur.after(tpl)
          else page.appendChild(tpl)
          const fk = railFocusKey()
          rebuild()
          select(tpl)
          restoreRailFocus(fk)
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
      const live = !!page.querySelector('[data-id]')
      const mk = (label, title, fn, disabled) => {
        const b = document.createElement('button')
        b.type = 'button'
        if (label.startsWith('<svg')) b.innerHTML = label
        else b.textContent = label
        b.title = title
        b.setAttribute('aria-label', title)
        if (disabled) {
          b.disabled = true
          b.title = title + ' — not available on live docs yet'
          b.setAttribute('aria-label', b.title)
        }
        else b.addEventListener('click', fn)
        ops.appendChild(b)
      }
      mk("<svg viewBox=\\"0 0 16 16\\" width=\\"13\\" height=\\"13\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"1.5\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" aria-hidden=\\"true\\"><rect x=\\"5\\" y=\\"5\\" width=\\"8\\" height=\\"8\\" rx=\\"1\\"/><path d=\\"M11 5V3.5A1.5 1.5 0 0 0 9.5 2h-5A1.5 1.5 0 0 0 3 3.5v5A1.5 1.5 0 0 0 4.5 10H5\\"/></svg>", 'Duplicate this slide', () => {
        const cur = current()
        if (!cur) return
        const copy = cur.cloneNode(true)
        copy.classList.remove('current')
        // Clones live outside the commit surface on live docs — say so
        // ON the clone, loudly, not in a distant status line.
        copy.removeAttribute('data-id')
        for (const el of copy.querySelectorAll('[data-id]')) el.removeAttribute('data-id')
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
        for (const t of copy.querySelectorAll('.clone-note')) t.remove()
        if (live) {
          const tag = document.createElement('div')
          tag.className = 'clone-note'
          tag.setAttribute('contenteditable', 'false')
          tag.textContent = 'copy — not saved to the live doc'
          copy.appendChild(tag)
        }
        cur.after(copy)
        rebuild(); select(copy)
        restoreOpsFocus(0)
      })
      const moveUp = () => {
        const cur = current()
        const prev = cur && cur.previousElementSibling
        if (prev && prev.classList.contains('slide')) { cur.after(prev); rebuild(); select(cur); restoreOpsFocus(1) }
      }
      const moveDown = () => {
        const cur = current()
        const next = cur && cur.nextElementSibling
        if (next && next.classList.contains('slide')) { cur.before(next); rebuild(); select(cur); restoreOpsFocus(2) }
      }
      mk("<svg viewBox=\\"0 0 16 16\\" width=\\"13\\" height=\\"13\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"1.5\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" aria-hidden=\\"true\\"><path d=\\"M8 13V3M4 7l4-4 4 4\\"/></svg>", 'Move this slide up', moveUp, live)
      mk("<svg viewBox=\\"0 0 16 16\\" width=\\"13\\" height=\\"13\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"1.5\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" aria-hidden=\\"true\\"><path d=\\"M8 3v10M4 9l4 4 4-4\\"/></svg>", 'Move this slide down', moveDown, live)
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
      }, live)
      mk("<svg viewBox=\\"0 0 16 16\\" width=\\"13\\" height=\\"13\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"1.5\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" aria-hidden=\\"true\\"><path d=\\"M2.5 3.5h11v7h-6l-3 3v-3h-2z\\"/></svg>", 'Comment on this slide', () => {
        const cur = current()
        const target = cur && (cur.querySelector('.frame h1, .frame h2') || cur.querySelector('.frame'))
        if (!target) return
        const r = document.createRange()
        r.selectNodeContents(target)
        document.dispatchEvent(new CustomEvent('kit-comment-on',
          { detail: { range: r, quote: target.textContent.trim(), anchor: slideAnchor(cur) } }))
      })
    }

    // One observer keeps the rail honest against every mutation source —
    // typing, execCommand, undo, and programmatic or remote writes.
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
      // Blur first: the flush must not wait on an engine's implicit
      // blur-on-revoke behavior.
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

    rebuild()
    select(current())
  })();
</script>
