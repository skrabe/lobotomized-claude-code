<!--
name: 'Data: Artifact document HTML template'
description: >-
  Provides the bundled live-document HTML template extracted for Claude when the
  document Artifact skill is activated.
ccVersion: 2.1.233
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
      --cds-text-accent: #184f95; --cds-accent-bg: transparent; --cds-text-danger: #b3261e;
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
</script>
