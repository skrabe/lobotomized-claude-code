<!--
name: 'Data: Artifact decision component script'
description: >-
  Provides the pinned JavaScript asset for the reusable Artifact decision
  component, including selection, confirmation, persistence, restore, and
  conflict behavior
ccVersion: 2.1.232
-->
<script>
(function workshopDecisions() {
  'use strict';
  var busy = false;
  /* Live waiting chrome (bar + painter). waitingActive lets the restore
     path's timers stand down once the chrome is already gone (see the
     waiting-marker block below enterWaiting). */
  var waitingActive = false;
  var waitingBar = null;
  var painterCanvas = null;
  var paintTimer = null;
  var paintFrame = 0;
  var TOKEN = /^[a-z0-9][a-z0-9-]{0,63}$/;
  /* Free-text answer codec — one of THREE independent legs (this script,
     the md-lane renderer, the publish verifier); none trusts another.
     KEEP-IN-SYNC with MAX_CUSTOM_* in src/frame/decisionBlocks.ts.
     Canonical base64 only: decode → re-encode → byte-equality kills
     base64 malleability and every lenient-decoder differential (one
     text, exactly one spelling); strict UTF-8 via TextDecoder fatal;
     forbidden characters rejected by CATEGORY (review r3618820207):
     C0/C1 controls and the U+2028/U+2029 separators numerically, plus
     every Cf or Default_Ignorable codepoint via Unicode property
     classes — the whole invisible-in-rendering class (an RLO could
     visually reverse a decided line; tag-encoded text is invisible to
     humans but legible to models) — minus the ZWNJ/ZWJ and
     variation-selector carve-outs legitimate text needs; the carve-outs
     are themselves invisible, so their total count is capped at 8
     (review r3620974864 — unbounded they are a hidden byte-per-
     codepoint channel inside the caps; 8 covers composed emoji). The regex is
     built with fromCharCode(92): this template bans the backslash
     byte, so escapes cannot be spelled literally. KEEP-IN-SYNC:
     FORBIDDEN_ANSWER_CHAR_RE in src/frame/decisionBlocks.ts is the
     equivalent literal, and the cross-validator tests run the same
     fixtures through both legs. The b64 alphabet carries none of the
     island's five RAWTEXT breakout bytes, so the belt check is
     untouched by free text. */
  var B64 = /^[A-Za-z0-9+/]*={0,2}$/;
  var BS = String.fromCharCode(92);
  var FORBIDDEN_RE = new RegExp(
    '[' + BS + 'u0000-' + BS + 'u001f' + BS + 'u007f-' + BS + 'u009f' + BS + 'u2028' + BS + 'u2029]|(?![' + BS + 'u200C' + BS + 'u200D' + BS + 'uFE00-' + BS + 'uFE0F' + BS + 'u{E0100}-' + BS + 'u{E01EF}])[' + BS + 'p{Cf}' + BS + 'p{Default_Ignorable_Code_Point}]',
    'u'
  );
  function validAnswerText(text) {
    if (!text) return false;
    /* Trim-equality mirrors isValidCustomAnswerText: the fence grammar
       trims every recorded value, so non-trimmed text has no faithful
       fence representation. The input handler trims before encoding;
       this check is the tamper and legacy-island defense. */
    if (text !== text.trim()) return false;
    if (FORBIDDEN_RE.test(text)) return false;
    var n = 0;
    var invis = 0;
    for (var i = 0; i < text.length; ) {
      var cp = text.codePointAt(i);
      n++;
      /* Count the carved-out invisibles (ZWNJ/ZWJ + variation
         selectors): KEEP-IN-SYNC with EXEMPT_INVISIBLE_RE and
         MAX_EXEMPT_INVISIBLE in src/frame/decisionBlocks.ts. */
      if (
        cp === 0x200c || cp === 0x200d ||
        (cp >= 0xfe00 && cp <= 0xfe0f) ||
        (cp >= 0xe0100 && cp <= 0xe01ef)
      ) invis++;
      i += cp > 0xffff ? 2 : 1;
    }
    if (invis > 8) return false;
    return n <= 280;
  }
  function encodeAnswer(text) {
    if (!validAnswerText(text)) return null;
    var bytes = new TextEncoder().encode(text);
    if (bytes.length > 1120) return null;
    var bin = '';
    for (var i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
    return btoa(bin);
  }
  function decodeAnswer(b64) {
    if (!b64 || b64.length % 4 !== 0 || b64.length > 1496 || !B64.test(b64)) return null;
    var bin;
    try {
      bin = atob(b64);
    } catch (e) {
      return null;
    }
    var bytes = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
    var text;
    try {
      text = new TextDecoder('utf-8', { fatal: true }).decode(bytes);
    } catch (e) {
      return null;
    }
    if (encodeAnswer(text) !== b64) return null;
    return text;
  }
  /* Selections: decision id → {item, row, token, undo}. At most one per
     decision item, any number of items — the sticky footer confirms them
     all in ONE republish. \`undo\` is the item's PRE-selection innerHTML,
     captured at first selection and kept while the selection merely
     moves within the item, so a failed confirm reverts past both
     mutation stages (selection and optimistic resolve), never to a
     half-selected state. Toggle-off is surgical and never consumes the
     snapshot; a re-pick after toggle-off re-captures it, so the undo is
     always the item's CURRENT pre-selection bytes. Null-prototype, and
     so for every id-keyed accumulator below: a decision id like
     \`constructor\` is legal per the slug grammar, and a plain object would
     resolve it through Object.prototype — an unguarded read would see a
     truthy inherited value and crash on first selection. */
  var picks = Object.create(null);
  var footer = null;
  function pickCount() {
    var n = 0;
    for (var id in picks) {
      if (Object.prototype.hasOwnProperty.call(picks, id)) n++;
    }
    return n;
  }
  function selfApi() {
    var c = window.claude;
    var a = c && (c.artifact || c.self);
    return a && typeof a.publish === 'function' ? a : null;
  }
  function openRows(scope) {
    return scope.querySelectorAll('[data-decision-state="open"] .option[data-choice]');
  }
  function itemSel(id) {
    return '[data-decision-id="' + (window.CSS && CSS.escape ? CSS.escape(id) : id) + '"]';
  }
  /* Affordance only — authorization stays server-side. The viewer runtime
     mounts a queueing self-write stub (window.claude.artifact, legacy
     window.claude.self) synchronously when the
     capability is declared, so a brief poll covers only script-order skew.
     No island means nothing to arm: the render emits the island exactly
     when the page shows open call-items. */
  var tries = 0;
  var timer = setInterval(function () {
    if (selfApi()) {
      if (document.getElementById('ws-decisions')) {
        var rows = openRows(document);
        for (var i = 0; i < rows.length; i++) {
          rows[i].removeAttribute('aria-disabled');
          rows[i].removeAttribute('title');
          rows[i].setAttribute('tabindex', '0');
          rows[i].className += ' armed';
        }
        /* The typed-answer inputs arm under the SAME gate as the rows
           (review r3618320565): on a static publish they stay disabled
           and explain themselves via the title, exactly like the greyed
           rows, instead of eating text that can never confirm. */
        var ins = document.querySelectorAll('[data-decision-state="open"] .option-input');
        for (var j = 0; j < ins.length; j++) {
          ins[j].removeAttribute('disabled');
          ins[j].removeAttribute('aria-disabled');
          ins[j].removeAttribute('title');
        }
      }
      clearInterval(timer);
    } else if (++tries > 20) {
      clearInterval(timer);
    }
  }, 250);
  function note(item, text) {
    var n = item.querySelector('.note-live');
    if (!n) {
      n = document.createElement('p');
      n.className = 'note-live';
      var body = item.querySelector('.call-body') || item;
      body.appendChild(n);
    }
    n.textContent = text;
  }
  /* The sticky footer: live-DOM-only chrome, built via createElement and
     textContent exclusively — it never reaches published bytes (publish
     is fetched stored source) and never interprets document content as
     markup. It doubles as the batch OUTCOME surface: raced items can sit
     below the fold, so per-item notes alone would under-report. */
  function footerStatus(text) {
    if (!footer) return;
    while (footer.firstChild) footer.removeChild(footer.firstChild);
    var s = document.createElement('span');
    s.className = 'footer-note';
    s.textContent = text;
    footer.appendChild(s);
  }
  function removeFooter() {
    if (footer) {
      footer.parentNode.removeChild(footer);
      footer = null;
      document.body.style.paddingBottom = '';
      setStatusFooterHidden(false);
    }
  }
  /* Post-save waiting state: the page is now STALE (the workshop session
     republishes it and the shell reboots the view to the new version),
     so further picks would only race the update. Disarm every row and
     show one persistent waiting bar — created via createElement and
     textContent only, live-DOM chrome that never reaches published
     bytes, like the footer it replaces. */
  function disarmAll() {
    var rows = document.querySelectorAll('.option.armed');
    for (var i = 0; i < rows.length; i++) {
      rows[i].className = rows[i].className.replace(' armed', '');
      rows[i].setAttribute('aria-disabled', 'true');
    }
    var inputs = document.querySelectorAll('.option-input');
    for (var k = 0; k < inputs.length; k++) {
      inputs[k].setAttribute('disabled', 'disabled');
    }
  }
  function removeWaitingBar() {
    if (waitingBar && waitingBar.parentNode) waitingBar.parentNode.removeChild(waitingBar);
    waitingBar = null;
  }
  function enterWaiting(text, since) {
    waitingActive = true;
    disarmAll();
    removeFooter();
    removeWaitingBar();
    setStatusFooterHidden(true);
    var w = document.createElement('div');
    w.className = 'ws-footer';
    var sp = document.createElement('span');
    sp.className = 'ws-spin';
    w.appendChild(sp);
    var s = document.createElement('span');
    s.className = 'footer-note';
    s.textContent = text;
    w.appendChild(s);
    document.body.appendChild(w);
    document.body.style.paddingBottom = '72px';
    waitingBar = w;
    showPainter(true);
    /* The shell normally reboots the view within seconds; if the session
       died first, don't leave a viewer staring at a spinner forever.
       textContent-only escalation, same note element. A restored wait
       counts from the original confirm (marker.since), so the notes do
       not reset across the reboot. Two stages, because the page cannot
       observe the session: first a nudge, then the honest state — the
       save is real, the watcher may not be. */
    var elapsed = typeof since === 'number' ? Date.now() - since : 0;
    var delay = 60000 - elapsed;
    if (delay < 0) delay = 0;
    setTimeout(function () {
      if (w.parentNode) {
        s.textContent = text + ' Taking longer than expected — reload to check for the latest version.';
      }
    }, delay);
    var later = 180000 - elapsed;
    if (later < 0) later = 0;
    setTimeout(function () {
      if (w.parentNode) {
        s.textContent = text + ' Still nothing — Claude may not be watching this page right now. Reload to check for the latest version.';
      }
    }, later);
  }
  /* Clawd writing in the corner while the page waits on the session —
     the whiteboard template's painter pose, holding a pencil here
     (eraser-ferrule-shaft-wood-graphite, paw to tip) so the two pages
     read as different activities. Same live-chrome rule as the footer:
     createElement + textContent only, never published bytes. */
  var CLAWD_FRAMES = [[
    '................',
    '................',
    '................',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '..OODOODOO......',
    '..OODOODOO......',
    '..OOOOOOOOOEFPWG',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '...OO..OO......b',
    '...OO..OO.......',
    '................',
    '................'], [
    '................',
    '..............WG',
    '.............P..',
    '..OOOOOOOO..P...',
    '..OOOOOOOO.F....',
    '..OODOODOOE.....',
    '..OODOODOOO.....',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '..OOOOOOOO......',
    '...OO..OO.......',
    '...OO..OO.......',
    '................',
    '................']];
  var CLAWD_PAL = {
    O: '#d97757', D: '#2a1f1b', E: '#e98fa2', F: '#7d848a',
    P: '#e8b93c', W: '#d9a066', G: '#4a4a4a'
  };
  function penColor() {
    var v = '';
    try {
      v = getComputedStyle(document.documentElement).getPropertyValue('--fill-accent');
    } catch (_) {}
    v = v ? v.trim() : '';
    return v || '#d97706';
  }
  function drawClawd(frame) {
    if (!painterCanvas) return;
    var c = painterCanvas.getContext('2d');
    if (!c) return;
    var pen = penColor();
    c.clearRect(0, 0, 16, 14);
    var grid = CLAWD_FRAMES[frame % 2];
    for (var y = 0; y < grid.length; y++) {
      for (var x = 0; x < grid[y].length; x++) {
        var ch = grid[y].charAt(x);
        if (ch === '.') continue;
        /* b is the written stroke in the page accent; half alpha keeps
           it lighter than the pencil. */
        c.globalAlpha = ch === 'b' ? 0.55 : 1;
        c.fillStyle = CLAWD_PAL[ch] || pen;
        c.fillRect(x, y, 1, 1);
      }
    }
    c.globalAlpha = 1;
  }
  function showPainter(on) {
    if (paintTimer) {
      clearInterval(paintTimer);
      paintTimer = null;
    }
    if (!on) {
      var wrap = painterCanvas && painterCanvas.parentNode;
      if (wrap && wrap.parentNode) wrap.parentNode.removeChild(wrap);
      painterCanvas = null;
      return;
    }
    if (!painterCanvas) {
      var el = document.createElement('div');
      el.className = 'ws-painter';
      painterCanvas = document.createElement('canvas');
      painterCanvas.width = 16;
      painterCanvas.height = 14;
      painterCanvas.setAttribute('aria-hidden', 'true');
      el.appendChild(painterCanvas);
      /* Evidence-neutral label: the page cannot observe whether a
         session is actually listening, so the chrome never asserts
         activity — it names the wait. */
      var lbl = document.createElement('span');
      lbl.textContent = 'Waiting for Claude…';
      el.appendChild(lbl);
      document.body.appendChild(el);
    }
    drawClawd(0);
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
      paintTimer = setInterval(function () {
        paintFrame ^= 1;
        drawClawd(paintFrame);
      }, 420);
    }
  }
  /* Waiting marker: survives the shell's reboot to the confirm-published
     version so the waiting state carries over instead of flashing back
     to an armed page (the reboot otherwise drops the bar and the scroll
     position). FNV-1a is NOT cryptographic — the marker gates only this
     live-DOM chrome and the scroll restore, never published bytes or
     write authority; sessionStorage is same-origin, per-tab. No display
     text rides in the marker: storage is writable by any same-origin
     script, so the bar only ever shows this script's fixed strings. */
  var WAIT_KEY = 'ws-waiting';
  var WAIT_TIMEOUT_MS = 15 * 60 * 1000;
  function fnv1a(s) {
    var h = 0x811c9dc5;
    for (var i = 0; i < s.length; i++) {
      h ^= s.charCodeAt(i);
      h = Math.imul(h, 0x01000193);
    }
    return h >>> 0;
  }
  function rememberWaiting(html) {
    try {
      sessionStorage.setItem(
        WAIT_KEY,
        JSON.stringify({ since: Date.now(), scrollY: window.scrollY, h: fnv1a(html) })
      );
    } catch (_) {}
  }
  function clearWaitingMarker() {
    try {
      sessionStorage.removeItem(WAIT_KEY);
    } catch (_) {}
  }
  function readWaitingMarker() {
    var w = null;
    try {
      var raw = sessionStorage.getItem(WAIT_KEY);
      if (raw) w = JSON.parse(raw);
    } catch (_) {}
    if (!w || typeof w.since !== 'number' || typeof w.h !== 'number') return null;
    return w;
  }
  function exitWaiting() {
    waitingActive = false;
    showPainter(false);
    removeWaitingBar();
    /* The selection footer may be up (rows stay clickable while the
       page waits) — then its padding and status-footer handling win. */
    if (!footer) {
      document.body.style.paddingBottom = '';
      setStatusFooterHidden(false);
    }
  }
  function confirmLabel(n) {
    if (n === 1) {
      var only;
      for (var id in picks) {
        if (Object.prototype.hasOwnProperty.call(picks, id)) only = picks[id];
      }
      if (only.kind === 'custom') {
        return 'Confirm your answer';
      }
      var l = only.row.querySelector('.option-label');
      return 'Confirm: ' + (l ? l.textContent : only.token);
    }
    return 'Confirm ' + n + ' decisions';
  }
  function updateFooter() {
    var n = pickCount();
    if (n === 0) {
      removeFooter();
      return;
    }
    if (!footer) {
      /* Rows stay clickable during a restored wait — the first pick
         hands the footer surface to the selection flow; the painter
         keeps signaling the in-flight update. */
      removeWaitingBar();
      footer = document.createElement('div');
      footer.className = 'ws-footer';
      document.body.appendChild(footer);
      document.body.style.paddingBottom = '72px';
      /* The selection footer REPLACES the static status footer while row
         picks are pending — the kickoff CTA cannot be clicked mid-batch
         by construction. */
      setStatusFooterHidden(true);
    }
    while (footer.firstChild) footer.removeChild(footer.firstChild);
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'confirm-btn';
    btn.textContent = confirmLabel(n);
    footer.appendChild(btn);
    var clear = document.createElement('button');
    clear.type = 'button';
    clear.className = 'clear-btn';
    clear.textContent = 'Clear';
    footer.appendChild(clear);
    var hint = document.createElement('span');
    hint.className = 'confirm-hint';
    hint.textContent = 'Confirming updates this page for everyone.';
    footer.appendChild(hint);
  }
  /* Clear ONE pick's visual state — row ring or the typed-answer box
     ring. Never touches typed TEXT: destroying 280 typed characters on a
     reflex Escape is data loss, and leftover text simply re-picks on the
     next keystroke. */
  function clearPickVisual(p) {
    if (p.kind === 'custom') {
      var box = p.input.closest('.custom-answer');
      if (box) box.className = box.className.replace(' selected', '');
    } else {
      p.row.className = p.row.className.replace(' selected', '');
      p.row.removeAttribute('aria-pressed');
    }
  }
  function select(row, item) {
    var id = item.getAttribute('data-decision-id');
    if (!id || !TOKEN.test(id)) return;
    var token = row.getAttribute('data-choice');
    if (!token || !TOKEN.test(token)) return;
    var prior = picks[id];
    if (prior && prior.kind !== 'custom' && prior.row === row) {
      /* Toggle off — surgical removal, never an innerHTML restore: the
         undo snapshot is reserved for failed-confirm revert. */
      row.className = row.className.replace(' selected', '');
      row.removeAttribute('aria-pressed');
      delete picks[id];
      updateFooter();
      return;
    }
    /* The undo must always be the item's PRE-selection bytes: captured
       fresh on a new pick (including a re-pick after toggle-off), kept
       when the selection merely moves within the item — including when
       it moves between a typed answer and a row. */
    var undo = prior ? prior.undo : item.innerHTML;
    if (prior) clearPickVisual(prior);
    row.className += ' selected';
    row.setAttribute('aria-pressed', 'true');
    picks[id] = { kind: 'row', item: item, row: row, token: token, undo: undo };
    updateFooter();
  }
  function clearAll() {
    for (var id in picks) {
      if (!Object.prototype.hasOwnProperty.call(picks, id)) continue;
      clearPickVisual(picks[id]);
    }
    picks = Object.create(null);
    removeFooter();
  }
  /* Generic live-form-state capture (review r3618820196): the undo
     snapshot is innerHTML, which structurally cannot carry live DOM
     state — input/textarea VALUES, checkbox/radio CHECKED, select
     INDEX. A failed confirm restores the snapshot and would otherwise
     destroy whatever the reader had typed, for EVERY pick kind: a ROW
     pick can sit on an item whose input still holds residual typed
     text (clearPickVisual deliberately preserves it). Captured per
     item at confirm time, keyed by traversal order, restored after any
     revert — closing the class for every stateful element kind, not
     one input. */
  function captureFormState(item) {
    var els = item.querySelectorAll('input, textarea, select');
    var st = [];
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      st.push({
        value: el.value,
        checked: !!el.checked,
        sel: typeof el.selectedIndex === 'number' ? el.selectedIndex : -1
      });
    }
    return st;
  }
  function restoreFormState(item, st) {
    if (!st) return;
    var els = item.querySelectorAll('input, textarea, select');
    for (var i = 0; i < els.length && i < st.length; i++) {
      var el = els[i];
      el.value = st[i].value;
      if (el.type === 'checkbox' || el.type === 'radio') el.checked = st[i].checked;
      if (st[i].sel >= 0 && typeof el.selectedIndex === 'number') el.selectedIndex = st[i].sel;
    }
  }
  function revertItem(p) {
    /* The single innerHTML write: restoring the element's own prior
       content, never constructed markup. */
    p.item.innerHTML = p.undo;
    p.item.setAttribute('data-decision-state', 'open');
    p.item.removeAttribute('data-resolved-choice');
    /* Set by markCustomResolved on the ITEM element — outside innerHTML,
       so the restore above cannot clear it. */
    p.item.removeAttribute('data-resolved-custom');
    /* Confirm-time form state back into the fresh innerHTML nodes —
       regardless of pick kind (see captureFormState). The custom-kind
       text restore below it is retained as the narrow fallback for a
       pick confirmed before formState existed (resume-mid-batch). */
    restoreFormState(p.item, p.formState);
    if (!p.formState && p.kind === 'custom' && typeof p.text === 'string') {
      var ri = p.item.querySelector('.option-input');
      if (ri) ri.value = p.text;
    }
  }
  /* The resolved mutation, applied to the live item (optimistic copy) and
     to the PARSED stored copy (the published bytes) alike — elements are
     built via item.ownerDocument, so one builder serves both. The literals
     here (state, choice attribute, chosen/dim classes, badge/why removal,
     the Decided line and its position) are the renderer contract
     (src/frame/decisionBlocks.ts renderDecisionHtml's resolved branch) the
     session's next mechanical republish replays from the markdown. */
  function markResolved(item, token) {
    item.setAttribute('data-decision-state', 'resolved');
    item.setAttribute('data-resolved-choice', token);
    var lean = item.getAttribute('data-lean-choice');
    var rows = item.querySelectorAll('.option[data-choice]');
    var label = '';
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      var chosen = r.getAttribute('data-choice') === token;
      if (chosen) {
        var l = r.querySelector('.option-label');
        label = l ? l.textContent : token;
      }
      r.className = chosen ? 'option chosen' : 'option dim';
      r.removeAttribute('role');
      r.removeAttribute('aria-disabled');
      r.removeAttribute('aria-pressed');
      r.removeAttribute('title');
      r.removeAttribute('tabindex');
      var badge = r.querySelector('.badge');
      if (badge) badge.parentNode.removeChild(badge);
      var why = r.querySelector('.why');
      if (why && !(chosen && lean === token)) why.parentNode.removeChild(why);
    }
    var ca = item.querySelector('.custom-answer');
    if (ca) ca.parentNode.removeChild(ca);
    var decided = item.ownerDocument.createElement('p');
    decided.className = 'decided';
    decided.textContent = 'Decided: ' + label;
    var body = item.querySelector('.call-body') || item;
    var anchorEl = body.querySelector('.anchor');
    body.insertBefore(decided, anchorEl || body.querySelector('.options'));
  }
  /* The kickoff footer is a decision item with its own resolved
     rendering: chosen/dim rows like any item, but the status note and
     the top banner flip instead of a Decided line — these literals are
     the renderer contract (renderKickoffFooter / renderStatusBanner in
     src/frame/decisionBlocks.ts) the session's next mechanical republish
     replays. Keyed on the ws-status-footer class the renderer emits only
     for the CANONICAL kickoff block. */
  function isKickoffItem(item) {
    return (
      (' ' + (item.getAttribute('class') || '') + ' ').indexOf(' ws-status-footer ') !== -1 &&
      item.getAttribute('data-decision-id') === 'get-started'
    );
  }
  function isKickoffEntry(e) {
    return (
      e.id === 'get-started' &&
      e.opts.length === 2 &&
      e.opts.indexOf('get-started') !== -1 &&
      e.opts.indexOf('keep-iterating') !== -1 &&
      e.custom === null
    );
  }
  /* Banner = pure function of the island, both directions: no optimistic
     flip (so failure paths have nothing to un-flip) and every publish
     carries a banner derived from the same rebuilt entries it ships.
     KEEP-IN-SYNC: deriveWorkshopState + renderStatusBanner in
     src/frame/decisionBlocks.ts — same precedence, same strings. */
  function applyBanner(doc, entries) {
    var b = doc.querySelector('.ws-banner');
    if (!b) return;
    var kickoff = null;
    for (var i = 0; i < entries.length; i++) {
      if (isKickoffEntry(entries[i])) { kickoff = entries[i]; break; }
    }
    var open = 0;
    for (var k = 0; k < entries.length; k++) {
      if (entries[k] !== kickoff && entries[k].state === 'open') open++;
    }
    var state;
    var text;
    if (open > 0) {
      state = 'in-progress';
      text = 'In progress — ' + open + (open === 1 ? ' decision open' : ' decisions open');
    } else if (kickoff !== null && kickoff.choice === 'get-started') {
      state = 'started';
      text = 'Build started';
    } else if (kickoff !== null && kickoff.state === 'open') {
      state = 'ready';
      text = 'Ready to build';
    } else {
      state = 'in-progress';
      text = 'In progress';
    }
    b.setAttribute('data-ws-state', state);
    b.textContent = text;
    /* The kickoff footer's open-note derives from the SAME rebuilt
       entries as the banner — without this, a batch confirm resolving
       the last open decisions publishes 'Ready to build' beside a
       footer still reading the open-note until the session's next
       republish. Skip when the kickoff itself is resolved:
       markKickoffResolved owns that wording. KEEP-IN-SYNC with the
       renderer's renderKickoffFooter note derivation
       (decisionBlocks.ts) — same two strings, same ready condition
       (zero open non-kickoff decisions). */
    if (kickoff !== null && kickoff.state === 'open') {
      var kitem = doc.querySelector(
        '[data-decision-id="' + kickoff.id + '"] .ws-status-note'
      );
      if (kitem) {
        kitem.textContent =
          open > 0 ? 'Decisions still open above.' : 'All decisions are in.';
      }
    }
  }
  function markKickoffResolved(item, token) {
    item.setAttribute('data-decision-state', 'resolved');
    item.setAttribute('data-resolved-choice', token);
    var rows = item.querySelectorAll('.option[data-choice]');
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      r.className = r.getAttribute('data-choice') === token ? 'option chosen' : 'option dim';
      r.removeAttribute('role');
      r.removeAttribute('aria-disabled');
      r.removeAttribute('aria-pressed');
      r.removeAttribute('title');
      r.removeAttribute('tabindex');
    }
    var n = item.querySelector('.ws-status-note');
    if (n) {
      n.textContent =
        token === 'get-started'
          ? 'Build started — the workshop session is on it.'
          : 'Keeping at it — more to come.';
    }
    /* No banner write here: the banner derives from the rebuilt island
       (applyBanner in syncIslandAll for the published copy; the live
       copy updates on publish success) — an optimistic flip would need
       un-flipping on every failure path. */
  }
  /* A typed answer's resolved rendering: every row dims, the input
     leaves BOTH copies (decided items carry no input — renderer
     contract), the decided line carries the text via textContent (never
     markup), and the canonical b64 rides the attribute for the
     island↔markup string-equality check. */
  function markCustomResolved(item, b64, text) {
    item.setAttribute('data-decision-state', 'resolved');
    item.setAttribute('data-resolved-custom', b64);
    var rows = item.querySelectorAll('.option[data-choice]');
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      r.className = 'option dim';
      r.removeAttribute('role');
      r.removeAttribute('aria-disabled');
      r.removeAttribute('aria-pressed');
      r.removeAttribute('title');
      r.removeAttribute('tabindex');
      /* Unconditionally — no row is chosen on a typed answer, and the
         renderer's custom-decided branch never emits a badge or reason
         (KEEP-IN-SYNC: renderDecisionHtml drops keepWhy unless the
         token resolution chose the recommended row). */
      var badge = r.querySelector('.badge');
      if (badge) badge.parentNode.removeChild(badge);
      var why = r.querySelector('.why');
      if (why) why.parentNode.removeChild(why);
    }
    var ca = item.querySelector('.custom-answer');
    if (ca) ca.parentNode.removeChild(ca);
    var decided = item.ownerDocument.createElement('p');
    decided.className = 'decided';
    decided.textContent = 'Decided: ' + text;
    var body = item.querySelector('.call-body') || item;
    var anchorEl = body.querySelector('.anchor');
    body.insertBefore(decided, anchorEl || body.querySelector('.options'));
  }
  /* One resolved-mutation chooser for BOTH copies (live DOM and the
     parsed stored source): token picks take markResolved (or the
     kickoff rendering), typed answers take markCustomResolved. The
     kickoff never takes a custom answer — its item is canonical-shape
     go/no-go only, keyed on BOTH the footer class and the reserved id. */
  function resolveMutation(item, want) {
    if (want.custom !== null) {
      markCustomResolved(item, want.custom, want.text);
    } else if (isKickoffItem(item)) {
      markKickoffResolved(item, want.choice);
    } else {
      markResolved(item, want.choice);
    }
  }
  /* One island entry, validated against the full render contract — every
     key known, every value grammar-bound. Strictness is a security
     boundary, not pedantry: the rewrite below is JSON.parse →
     JSON.stringify, and that round-trip would turn a JSON-escaped markup
     sequence in a hostile island (harmless as stored bytes) into raw
     breakout bytes inside a RAWTEXT script element. Grammar-bound values
     cannot carry markup at all, so an out-of-contract island simply never
     republishes. The grammar is the workshop slug charset — KEEP-IN-SYNC
     with SLUG_SRC in src/frame/decisionBlocks.ts (a narrower validator
     would silently reject legitimate ids; a wider one admits bytes the
     renderer never mints). */
  function validEntry(entry) {
    if (!entry || typeof entry !== 'object') return false;
    var keys = Object.keys(entry);
    if (keys.length !== 5) return false;
    if (typeof entry.id !== 'string' || !TOKEN.test(entry.id)) return false;
    if (entry.state !== 'open' && entry.state !== 'resolved') return false;
    if (!Array.isArray(entry.opts) || entry.opts.length < 2 || entry.opts.length > 5) return false;
    for (var i = 0; i < entry.opts.length; i++) {
      if (typeof entry.opts[i] !== 'string' || !TOKEN.test(entry.opts[i])) return false;
      /* Duplicate tokens would cross-contaminate choice references —
         reject here like the fence parser does (KEEP-IN-SYNC:
         validateWsIslandJson in decisionBlocks.ts). */
      if (entry.opts.indexOf(entry.opts[i]) !== i) return false;
    }
    if (entry.choice !== null && (typeof entry.choice !== 'string' || entry.opts.indexOf(entry.choice) === -1)) return false;
    if (entry.custom !== null && (typeof entry.custom !== 'string' || decodeAnswer(entry.custom) === null)) return false;
    /* Tamper-only shape: the fence parser rejects custom on the kickoff
       id, so no rendered island ever carries it (KEEP-IN-SYNC:
       parseDecisionFence / validateWsIslandJson in decisionBlocks.ts). */
    if (entry.id === 'get-started' && entry.custom !== null) return false;
    /* Resolution invariant: open carries neither; resolved carries
       exactly one of choice/custom. */
    if (entry.state === 'open' && (entry.choice !== null || entry.custom !== null)) return false;
    if (entry.state === 'resolved' && (entry.choice === null) === (entry.custom === null)) return false;
    return true;
  }
  /* Whole-island validation + batch rebuild: every wanted pick whose
     entry is open and declares the picked token flips to resolved; the
     rest of the island is rebuilt from validated fields unchanged. Null
     when the island is out of contract — the WHOLE island must be valid
     (every entry, unique ids, ≤20 items) or nothing publishes: the
     island is the machine-readable record the workshop session reads,
     so a page whose island disagrees with its grammar is out of
     contract. \`applied\` maps the ids actually flipped; a pick absent
     from it raced a newer version and does not publish (first confirm
     wins PER ITEM — the batch is not transactional by design, because
     aborting unrelated selections over one raced item punishes the user
     for a race the server would have arbitrated to the same subset).
     The rebuild REBUILDS the island from validated fields only, so the
     serialized output's alphabet is provably TOKEN characters, JSON
     punctuation, and the two state words — it can never form a
     script-closing or markup sequence, whatever the stored bytes
     spelled. */
  function syncIslandAll(doc, wanted) {
    var island = doc.getElementById('ws-decisions');
    if (!island) return null;
    var cfg;
    try {
      cfg = JSON.parse(island.textContent || 'null');
    } catch (e) {
      return null;
    }
    if (!cfg || typeof cfg !== 'object' || Array.isArray(cfg)) return null;
    if (Object.keys(cfg).length !== 1 || !Array.isArray(cfg.items)) return null;
    if (cfg.items.length > 20) return null;
    var out = [];
    var applied = Object.create(null);
    var appliedCount = 0;
    for (var i = 0; i < cfg.items.length; i++) {
      var entry = cfg.items[i];
      if (!validEntry(entry)) return null;
      if (entry.choice !== null && entry.opts.indexOf(entry.choice) === -1) return null;
      for (var k = 0; k < out.length; k++) {
        if (out[k].id === entry.id) return null;
      }
      var state = entry.state;
      var choice = entry.choice;
      var custom = entry.custom;
      var want = Object.prototype.hasOwnProperty.call(wanted, entry.id)
        ? wanted[entry.id]
        : undefined;
      if (want !== undefined && state === 'open') {
        if (want.choice !== null && entry.opts.indexOf(want.choice) !== -1) {
          state = 'resolved';
          choice = want.choice;
          custom = null;
          applied[entry.id] = want;
          appliedCount++;
        } else if (want.custom !== null && entry.id !== 'get-started' && decodeAnswer(want.custom) !== null) {
          state = 'resolved';
          choice = null;
          custom = want.custom;
          applied[entry.id] = want;
          appliedCount++;
        }
      }
      out.push({ id: entry.id, opts: entry.opts.slice(), state: state, choice: choice, custom: custom });
    }
    if (appliedCount === 0) {
      return { applied: applied, wrote: false, entries: out };
    }
    var json = JSON.stringify({ items: out });
    /* Belt over the grammar braces: provably redundant once every value is
       TOKEN-bound, but a hard stop if that ever drifts — the island is
       RAWTEXT, so these five bytes are the entire breakout alphabet.
       (fromCharCode(92) is the backslash — this template bans the byte.) */
    if (
      json.indexOf('<') !== -1 ||
      json.indexOf('>') !== -1 ||
      json.indexOf('&') !== -1 ||
      json.indexOf("'") !== -1 ||
      json.indexOf(String.fromCharCode(92)) !== -1
    ) {
      return null;
    }
    island.textContent = json;
    applyBanner(doc, out);
    return { applied: applied, wrote: true, entries: out };
  }
  /* Publishable source, as a Promise: this view's own stored bytes
     (same-origin GET of the URL the document loaded from), with
     frame-asset's per-serve head injection excised and every surviving
     pick resolved. Fetching source — instead of serializing the live
     DOM — keeps every client runtime's DOM work (theme stamps, this
     script's selections, the footer, and notes) out of published bytes
     by construction. */
  /* KEEP-IN-SYNC: mirrors isFrameAssetInjection in src/frame/goCp.ts.
     The position/span bounds above are cheap pre-filters; THIS is the
     real guard: the span must be exactly what frame-asset's serve-time
     injection emits — a /_f/ base tag then a run of script elements,
     nothing else. A marker pair hand-stored around author content
     fails and is left alone, so a confirm can never silently excise
     co-writer content under the confirming viewer's write authority.
     indexOf-only (no regexes): this template bans the backslash byte. */
  function isScriptCloseAt(s, i) {
    /* ASCII-folded compare of the 8-byte close prefix at s[i] — never a
       second lowercased string: toLowerCase() can CHANGE LENGTH (U+0130
       folds to two units), desyncing every later index between the
       folded copy and the original. The tokenizer case-folds ASCII
       alpha only, so per-char ASCII folding is also the spec-faithful
       comparison. (The prefix is never spelled contiguously anywhere in
       this script — a literal spelling would close THIS element.) */
    if (s.charCodeAt(i) !== 60 || s.charCodeAt(i + 1) !== 47) return false;
    var word = 'script';
    for (var k = 0; k < 6; k++) {
      var c = s.charCodeAt(i + 2 + k);
      if (c >= 65 && c <= 90) c = c | 32;
      if (c !== word.charCodeAt(k)) return false;
    }
    return true;
  }
  function findScriptClose(s, from) {
    /* Tokenizer-faithful close (review r3618929901, KEEP-IN-SYNC with
       goCp's isFrameAssetInjection): script data ends at the close-tag
       prefix matched ASCII-case-insensitively and followed by
       tab/LF/FF/carriage-return/space, slash, or greater-than; the close tag then
       runs to the next greater-than. Returns the offset AFTER the close
       tag, or -1. An exact-literal scan would treat a case-variant
       close as still inside the script and validate content the
       browser renders. */
    var i = from;
    for (;;) {
      i = s.indexOf('</', i);
      if (i === -1) return -1;
      if (isScriptCloseAt(s, i)) {
        var c = s.charCodeAt(i + 8);
        if (c === 62 || c === 47 || wsCode(c)) {
          var g = s.indexOf('>', i + 8);
          if (g === -1) return -1;
          /* This prefix IS the tokenizer's script-data exit, so it is
             final: a quote (34/39) before the greater-than means the
             real end tag runs past it (quoted attribute values keep
             greater-than bytes) — a shape frame-asset never emits.
             FAIL here rather than skipping to a later candidate:
             skipping would overshoot the browser's exit and validate
             a span whose tail renders as visible content. */
          for (var q = i + 8; q < g; q++) {
            var qc = s.charCodeAt(q);
            if (qc === 34 || qc === 39) return -1;
          }
          return g + 1;
        }
      }
      i += 2;
    }
  }
  /* charCode whitespace test — exactly the HTML ASCII whitespace set
     (space, tab, LF, FF, carriage return), no backslash escapes in this template.
     KEEP-IN-SYNC: goCp's isFrameAssetInjection uses the same set in
     all three whitespace positions, so the two grammars are equivalent
     and the agreement test asserts verdict equality on every fixture.
     Regex whitespace would overclaim (VT, NBSP, U+2028…), and an
     unknown element like a script tag followed by NBSP renders its
     content — accepting it could excise author-visible bytes. */
  function wsCode(c) {
    return c === 32 || c === 9 || c === 10 || c === 12 || c === 13;
  }
  function isFrameAssetInjection(inner) {
    var s = inner.trim();
    if (s.indexOf('<base') !== 0) return false;
    var gt = s.indexOf('>');
    if (gt === -1) return false;
    var tag = s.slice(0, gt);
    var h = tag.indexOf('href="/_f/');
    if (h === -1) return false;
    /* Everything between '<base' and href= must be whitespace — mirrors
       goCp's <base then whitespace-run grammar; '<basement href=' and
       attribute smuggling both fail here. */
    if (h < 6) return false;
    for (var w = 5; w < h; w++) {
      if (!wsCode(tag.charCodeAt(w))) return false;
    }
    /* Opening quote sits at h+5 (href="); the next quote closes it, and
       no third quote may exist in the tag. */
    var q = tag.indexOf('"', h + 6);
    if (q === -1) return false;
    if (tag.indexOf('"', q + 1) !== -1) return false;
    /* After the closing quote: a whitespace run, then nothing or a
       bare self-close slash IMMEDIATELY before '>' — leading-trim
       only, so quote-space-slash-space fails here exactly as it fails
       goCp (whose grammar allows whitespace before the slash but not
       after). A trailing trim would accept it and make this mirror
       BROADER than goCp — more willing to excise. */
    var r = q + 1;
    while (r < tag.length && wsCode(tag.charCodeAt(r))) r++;
    var rest = tag.slice(r);
    if (rest !== '' && rest !== '/') return false;
    s = s.slice(gt + 1).trim();
    while (s.length) {
      if (s.indexOf('<script') !== 0) return false;
      /* Word boundary after 'script' — '<scriptfoo>' must fail like
         goCp's <script-then-boundary grammar. */
      var bnd = s.charCodeAt(7);
      if (bnd !== 62 && bnd !== 47 && !wsCode(bnd)) return false;
      var open = s.indexOf('>');
      if (open === -1) return false;
      var after = findScriptClose(s, open + 1);
      if (after === -1) return false;
      s = s.slice(after).trim();
    }
    return true;
  }
  function fetchStoredSource() {
    /* The script's ONE network read — this page's own stored source —
       shared by the confirm pipeline and the load-time waiting verify.
       Bounded: a hung fetch would otherwise leave \`busy\` stuck (no
       reject, no catch, rows frozen until reload). 15s is far under the
       shell's own publish budget. */
    var signal =
      typeof AbortSignal !== 'undefined' && AbortSignal.timeout
        ? AbortSignal.timeout(15000)
        : undefined;
    return fetch(location.href, { credentials: 'same-origin', signal: signal })
      .then(function (r) {
        if (!r.ok) {
          throw {
            code: 'upstream_error',
            message: 'source read failed (' + r.status + ')',
          };
        }
        return r.text();
      })
      .then(function (text) {
        /* KEEP-IN-SYNC: FRAME_RUNTIME_BEGIN/END and the bounds
           FRAME_RUNTIME_HEAD_WINDOW (8192) / FRAME_RUNTIME_MAX_SPAN
           (300000) in src/frame/goCp.ts — frame-asset's serve-time
           injection markers, ASSEMBLED at runtime so the template itself
           never carries the sequence. The excision takes goCp's shape:
           BEGIN must sit in the head window, END is searched FROM BEGIN,
           and the span is capped — so even if marker bytes ever reach
           stored content (e.g. smuggled through an attribute value that a
           DOMParser round trip re-rawifies), a body-positioned or
           oversized pair can't excise arbitrary stored content. */
        var MARK = 'frame-' + 'runtime';
        var BEGIN = '<!-- ' + MARK + ' -->';
        var END = '<!-- /' + MARK + ' -->';
        var b = text.indexOf(BEGIN);
        var e = b === -1 ? -1 : text.indexOf(END, b);
        if (
          b !== -1 &&
          b < 8192 &&
          e > b &&
          e - b < 300000 &&
          isFrameAssetInjection(text.slice(b + BEGIN.length, e))
        ) {
          var after = e + END.length;
          /* One-trailing-newline eat, like goCp: consecutive confirms
             must not accrete blank lines in the head region.
             charCodeAt — this template bans the backslash byte, so no
             newline literal. */
          if (text.charCodeAt(after) === 10) after++;
          text = text.slice(0, b) + text.slice(after);
        }
        return text;
      });
  }
  function sourceHtmlAll(wanted) {
    return fetchStoredSource()
      .then(function (text) {
        var doc = new DOMParser().parseFromString(text, 'text/html');
        /* Per-pick stored-markup gate: an item missing or not open in the
           STORED source raced a newer version — it drops from the batch;
           the rest still publish. */
        var open = Object.create(null);
        for (var id in wanted) {
          if (!Object.prototype.hasOwnProperty.call(wanted, id)) continue;
          var item = doc.querySelector(itemSel(id));
          if (item && item.getAttribute('data-decision-state') === 'open') {
            open[id] = wanted[id];
          }
        }
        var synced = syncIslandAll(doc, open);
        if (synced === null) return null;
        for (var id2 in synced.applied) {
          if (!Object.prototype.hasOwnProperty.call(synced.applied, id2)) continue;
          resolveMutation(doc.querySelector(itemSel(id2)), synced.applied[id2]);
        }
        var html = null;
        if (synced.wrote) {
          /* Assembled: the template must stay a doctype-free fragment, so
             the literal can't appear in stored bytes. */
          var out = doc.doctype ? '<!' + 'doctype html>' : '';
          html = out + doc.documentElement.outerHTML;
        }
        return { html: html, applied: synced.applied, entries: synced.entries };
      });
  }
  function friendly(err) {
    var code = err && err.code;
    var msg = (err && err.message) || 'request failed';
    if (code === 'conflict') return null; /* shell reloads to the winner */
    if (code === 'upstream_error' && msg.indexOf('(409)') !== -1) return null;
    if (code === 'consent_required')
      return 'Page updates were not allowed for this artifact — reload and allow it to update itself to decide here.';
    if (code === 'not_writer')
      return 'Only someone with edit access can decide from the page.';
    if (code === 'not_declared')
      return 'This version cannot update itself — ask the author to republish it.';
    if (code === 'rate_limited') return 'Saving too often — try again in a moment.';
    return 'Could not save: ' + msg;
  }
  function confirmAll() {
    if (busy) return;
    var total = pickCount();
    if (total === 0) return;
    var batch = picks;
    picks = Object.create(null);
    runConfirm(batch, total, footerStatus);
  }
  /* The one confirm pipeline — shared by the selection footer (batch of
     row picks) and the kickoff CTA (a single one-click pick): one fetch,
     one publish, per-item first-confirm-wins, whatever the entry point. */
  function runConfirm(batch, total, report) {
    var api = selfApi();
    if (!api) return;
    var wanted = Object.create(null);
    for (var id in batch) {
      if (!Object.prototype.hasOwnProperty.call(batch, id)) continue;
      var pk = batch[id];
      /* Before any optimistic mutation touches the item (see
         captureFormState). */
      pk.formState = captureFormState(pk.item);
      if (pk.kind === 'custom') {
        /* The input's CURRENT value at confirm time is what publishes —
           never a stale snapshot from when typing started — trimmed to
           the fence grammar's canonical form so the stored base64
           round-trips the session loop byte-identical. Invalid (emptied,
           over-cap after edits, forbidden characters) drops the pick
           with a note instead of poisoning the batch. */
        var answer = pk.input.value.trim();
        var enc = encodeAnswer(answer);
        if (enc === null) {
          clearPickVisual(pk);
          note(pk.item, 'That answer cannot be saved — keep it under 280 characters of plain text.');
          delete batch[id];
          total--;
          continue;
        }
        pk.text = answer;
        wanted[id] = { choice: null, custom: enc, text: answer };
      } else {
        wanted[id] = { choice: pk.token, custom: null, text: null };
      }
    }
    if (total === 0) {
      removeFooter();
      return;
    }
    function revertAll() {
      for (var r in batch) {
        if (Object.prototype.hasOwnProperty.call(batch, r)) revertItem(batch[r]);
      }
    }
    busy = true;
    try {
      /* Optimistic live-DOM copy of the mutation; the published bytes come
         from sourceHtmlAll's fetched source, never from this DOM. A throw
         here (hand-edited markup) must not leave the page looking
         decided-but-unsaved with busy stuck. */
      for (var m in batch) {
        if (Object.prototype.hasOwnProperty.call(batch, m)) {
          resolveMutation(batch[m].item, wanted[m]);
        }
      }
      report('Saving…');
    } catch (err) {
      revertAll();
      removeFooter();
      busy = false;
      return;
    }
    sourceHtmlAll(wanted)
      .then(function (res) {
        if (res === null) {
          revertAll();
          report('This page is out of contract — reload to see its latest state.');
          busy = false;
          return;
        }
        /* Per-item raced reverts, with the K-of-N outcome IN THE FOOTER —
           raced items can sit below the fold, and a control that said
           "Confirm 3" must never go silent about a dropped third. */
        var raced = 0;
        for (var id3 in batch) {
          if (!Object.prototype.hasOwnProperty.call(batch, id3)) continue;
          if (!Object.prototype.hasOwnProperty.call(res.applied, id3)) {
            revertItem(batch[id3]);
            note(batch[id3].item, 'This item changed under you — reload to see it.');
            raced++;
          }
        }
        if (res.html === null) {
          report('Nothing saved — every selected item changed under you. Reload to see the latest.');
          busy = false;
          return;
        }
        return api.publish(res.html).then(function () {
          /* Live banner catches up to what just published — same
             entries, same derive. */
          applyBanner(document, res.entries);
          /* res.html is byte-for-byte what the shell now stores: the
             marker's hash must come from these bytes so the post-reboot
             self-read (same excision) can compare equal. */
          rememberWaiting(res.html);
          /* The shell reboots this view to the new version; until then
             the page is stale, so show an explicit waiting state instead
             of leaving rows clickable under a terse note. */
          enterWaiting(
            raced === 0
              ? 'Saved — waiting for this page to update…'
              : 'Saved ' + (total - raced) + ' of ' + total + ' (' + raced + ' changed under you) — waiting for this page to update…'
          );
          busy = false;
        });
      })
      .catch(function (err) {
        var text = friendly(err);
        if (text === null) {
          report('Someone else updated this page — reloading…');
          busy = false;
          return;
        }
        revertAll();
        report(text);
        busy = false;
      });
  }
  function confirmKickoff(row, item) {
    /* ONE-click by design: a large labeled CTA is not an ambiguous
       gesture (the two-step exists for row-click ambiguity, not
       consequence), and the selection footer hides this one while row
       picks are pending, so a mixed batch is impossible by
       construction. */
    if (busy || pickCount() > 0) return;
    var token = row.getAttribute('data-choice');
    if (!token || !TOKEN.test(token)) return;
    var id = item.getAttribute('data-decision-id');
    if (!id || !TOKEN.test(id)) return;
    var batch = Object.create(null);
    batch[id] = { kind: 'row', item: item, row: row, token: token, undo: item.innerHTML };
    runConfirm(batch, 1, function (text) {
      note(item, text);
    });
  }
  function setStatusFooterHidden(hidden) {
    var sf = document.querySelector('.ws-status-footer');
    if (!sf) return;
    var cls = (sf.getAttribute('class') || '').replace(' ws-hidden', '');
    sf.setAttribute('class', hidden ? cls + ' ws-hidden' : cls);
  }
  function onActivate(e) {
    var target = e.target;
    if (!target || !target.closest || busy) return;
    if (target.closest('.confirm-btn')) {
      confirmAll();
      return;
    }
    if (target.closest('.clear-btn')) {
      clearAll();
      return;
    }
    var row = target.closest('.option.armed[data-choice]');
    if (!row) return;
    var item = row.closest('[data-decision-id]');
    if (!item || item.getAttribute('data-decision-state') !== 'open') return;
    if (!selfApi()) return;
    if (isKickoffItem(item)) {
      confirmKickoff(row, item);
      return;
    }
    select(row, item);
    /* No click-away cancel: deselection is explicit (row toggle, the
       Clear button, or Escape) — a stray click must not destroy an
       accumulated multi-selection. */
  }
  document.addEventListener('click', onActivate);
  document.addEventListener('input', function (e) {
    var target = e.target;
    if (!target || !target.closest || busy) return;
    var box = target.closest('.custom-answer');
    if (!box) return;
    var item = box.closest('[data-decision-id]');
    if (!item || item.getAttribute('data-decision-state') !== 'open') return;
    /* Island presence mirrors the arming gate: without the island no
       confirm can ever publish, so a pick must not arm (the rows fail
       closed at arm time; the input fails closed here too). */
    if (!selfApi() || !document.getElementById('ws-decisions') || isKickoffItem(item)) return;
    var id = item.getAttribute('data-decision-id');
    if (!id || !TOKEN.test(id)) return;
    var prior = picks[id];
    if (target.value.trim() === '') {
      /* Empty or whitespace-only text clears the pick (and never arms
         one) — the fence grammar trims recorded values, so a
         whitespace-only answer has no valid record; arming it would
         produce a confirm that can only fail. A ROW pick stays. */
      if (prior && prior.kind === 'custom') {
        clearPickVisual(prior);
        delete picks[id];
        updateFooter();
      }
      return;
    }
    if (prior && prior.kind === 'custom') return;
    var undo = prior ? prior.undo : item.innerHTML;
    if (prior) clearPickVisual(prior);
    box.className += ' selected';
    picks[id] = { kind: 'custom', item: item, input: target, undo: undo };
    updateFooter();
  });
  document.addEventListener('keydown', function (e) {
    /* Keys inside the typed-answer input belong to the input: Enter
       neither activates rows nor confirms (confirm stays a deliberate
       footer click), and Escape while editing does not clear picks. */
    if (e.target && e.target.closest && e.target.closest('.option-input')) {
      return;
    }
    if (e.key === 'Escape') {
      if (!busy) clearAll();
      return;
    }
    if (e.key !== 'Enter' && e.key !== ' ') return;
    if (!e.target || !e.target.closest) return;
    /* Rows are spans and need manual key activation; the footer controls
       are real buttons — Enter/Space fire their clicks natively, and
       handling them here too would double-activate. */
    if (!e.target.closest('.option.armed[data-choice]')) return;
    e.preventDefault();
    onActivate(e);
  });
  /* Opening version: published before any decision exists (empty island,
     no decision rows), so the page is waiting on the session's next
     version — show the painter until that version loads. */
  (function () {
    var isl = document.getElementById('ws-decisions');
    if (!isl) return;
    var parsed = null;
    try {
      parsed = JSON.parse(isl.textContent || '');
    } catch (e) {
      return;
    }
    var items = parsed && parsed.items;
    if (!Array.isArray(items) || items.length !== 0) return;
    if (document.querySelector('[data-decision-id]')) return;
    showPainter(true);
    /* The session may have died between the two publishes: escalate once
       into the footer bar (textContent only) rather than spin forever. */
    setTimeout(function () {
      if (!painterCanvas) return;
      if (!footer) {
        footer = document.createElement('div');
        footer.className = 'ws-footer';
        document.body.appendChild(footer);
        document.body.style.paddingBottom = '72px';
      }
      footerStatus('Still nothing — Claude may not be watching this page right now. Reload to check for the latest version.');
    }, 180000);
  })();
  /* Confirm-reboot continuity: re-enter the waiting state recorded at
     publish time, then verify against the now-stored bytes and exit
     cleanly when a NEWER version (the session's apply) is what loaded.
     Both hash inputs are this script's own fnv1a over the same bytes:
     marker.h came from res.html on the pre-reboot page, and the stored
     page IS res.html, carrying this same script — so impl and input
     match on both sides. A template change that alters either makes the
     hashes differ, which fails toward CLEARING the chrome — the safe
     direction. */
  (function () {
    var w = readWaitingMarker();
    if (!w) return;
    var left = w.since + WAIT_TIMEOUT_MS - Date.now();
    if (left <= 0 || left > WAIT_TIMEOUT_MS) {
      /* Stale, or since sits in the future (tampered or clock-skewed) —
         drop it and load as a normal page. */
      clearWaitingMarker();
      return;
    }
    /* Static text page and this script runs at end of body, so layout
       is final here — no load-event re-scroll that could yank a reader
       who already started scrolling. */
    if (typeof w.scrollY === 'number') window.scrollTo(0, w.scrollY);
    /* The chrome only informs — open decisions stay clickable during
       the turnaround: the disarm inside enterWaiting runs before the
       poll above ever arms, so it holds nothing on this path. */
    enterWaiting('Saved — waiting for this page to update…', w.since);
    /* A confirm made from THIS view replaces the marker and owns the
       chrome; timers keyed to the old marker must then stand down. */
    function sameMarker() {
      var cur = readWaitingMarker();
      return !!cur && cur.h === w.h && cur.since === w.since;
    }
    /* Hard stop: stale chrome comes down at the marker's 15-minute
       horizon even if the verify never concluded. */
    setTimeout(function () {
      if (!waitingActive || !sameMarker()) return;
      clearWaitingMarker();
      exitWaiting();
    }, left);
    var attempts = 0;
    function verify() {
      fetchStoredSource()
        .then(function (text) {
          if (!waitingActive || !sameMarker()) return;
          if (fnv1a(text) === w.h) return; /* our confirm-version — keep waiting */
          clearWaitingMarker();
          exitWaiting();
        })
        .catch(function () {
          /* Transient self-read failure: keep the chrome and retry
             briefly; the hard stop above bounds it. */
          attempts++;
          if (attempts < 3) setTimeout(verify, attempts * 5000);
        });
    }
    verify();
  })();
})();
</script>
