<!--
name: 'Data: Artifact document HTML template'
description: >-
  Provides the bundled live-document HTML template extracted for Claude when the
  document Artifact skill is activated.
ccVersion: 2.1.234
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
    --cds-text-warning: #c25124;
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
    --cds-text-warning: #ec835a;
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
  .tb-status[data-tone="warning"] { color: var(--cds-text-warning); font-weight: 600; }
  .tb-status[data-tone="error"] { color: var(--cds-text-danger); font-weight: 600; }
  .tb-status[data-tone="busy"], .tb-status[data-tone="muted"] { color: var(--cds-text-muted); }
  .toolbar .tb-save { opacity: 1; font-size: 12px; padding: 5px 10px; color: var(--cds-text-primary); border-color: var(--cds-border-strong); }
  .toolbar .tb-save:disabled { opacity: 0.45; color: var(--cds-text-secondary); border-color: var(--cds-border); }
  .tb-save.is-dirty::before { content: ""; width: 6px; height: 6px; border-radius: 50%; background: var(--cds-text-warning); }
  .toolbar [hidden] { display: none; }
  .canvas { padding: 20px 24px 120px; }
  /* Page content stacks below the chrome whatever it declares. */
  .page { isolation: isolate; }
  .visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
  :focus-visible { outline: 2px solid var(--cds-text-accent); outline-offset: 1px; }
  /* KIT:chrome:end */

  /* ── The page (doc-specific) ───────────────────────────────────── */
  .page {
    max-width: 620px; margin: 0 auto;
    padding: 56px 0 120px;
    /* Baseline rhythm: 17/30 — block margins snap to half- and
       whole-line multiples of the 30px line. */
    font-size: 17px; line-height: 30px;
  }
  .page:focus { outline: none; }
  .page h1 { font-size: 27px; line-height: 30px; margin: 0 0 15px; font-weight: 600; letter-spacing: -0.015em; }
  .page h2 { font-size: 21px; line-height: 30px; margin: 45px 0 15px; font-weight: 700; }
  .page h3 { font-size: 15px; line-height: 30px; margin: 30px 0 0; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--cds-text-secondary); }
  .page p, .page ul, .page ol { margin: 0 0 15px; }
  .page li { margin-bottom: 0; }
  .page blockquote { margin: 30px 0 15px; padding: 0 0 0 18px; border-left: 2px solid var(--cds-text-primary); }
  .page a { color: var(--cds-text-accent); }
  .docmeta {
    font-family: inherit; font-size: 13px; color: var(--cds-text-muted);
    margin: 0 0 30px; display: flex; gap: 10px; align-items: baseline; flex-wrap: wrap;
  }
  /* Each segment wraps as a unit — no orphaned separators or dangling
     years at a line break. */
  .docmeta .seg { white-space: nowrap; }
  .status { display: inline-block; font-weight: 700; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--cds-text-secondary); white-space: nowrap; }

  @media print {
    :root, :root[data-theme="dark"], :root:not([data-theme="light"]) {
      color-scheme: light;
      --cds-surface-0: #ffffff; --cds-surface-1: #ffffff; --cds-surface-2: #ffffff;
      --cds-text-primary: #0b0b0b; --cds-text-secondary: #52514e; --cds-text-muted: #898781;
      --cds-border: rgba(11, 11, 11, 0.1); --cds-border-strong: rgba(11, 11, 11, 0.2);
      --cds-text-accent: #184f95; --cds-accent-bg: transparent; --cds-text-danger: #b3261e; --cds-text-warning: #c25124;
    }
    .toolbar { display: none; }
    .canvas { padding: 0; }
    .page { max-width: 72ch; margin: 0 auto; padding: 0; }
  }
</style>

<!-- TOOLBAR (doc variant): block styles + inline marks + lists. Toolbar
     markup is per kind; the shared kit styles (KIT:chrome) and wires
     (KIT:editor) whatever controls a kind carries. -->
<div class="toolbar" role="toolbar" aria-label="Formatting">
  <select data-block title="Paragraph style" aria-label="Paragraph style">
    <option value="p">Body</option>
    <option value="h1">Title</option>
    <option value="h2">Heading</option>
    <option value="h3">Subheading</option>
  </select>
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

    <p class="docmeta" contenteditable="false">
      <span class="status"><!-- SLOT: STATUS — where the document is right now: Draft, In review, Decided, or Final -->Draft</span>
      <!-- SLOT: DOC_META — each fact is its own span.seg so a line break
           falls BETWEEN facts, never inside one: owner, then source or
           date — short segments, no trailing separators -->
      <span class="seg">Owner</span>
      <span class="seg">Month Year</span>
    </p>

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
    const blockSel = toolbar.querySelector('select[data-block]')
    if (blockSel) {
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
        lastEl = el && el.closest('h1, h2, h3, p, blockquote, li') || el
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
