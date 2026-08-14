<!--
name: 'Data: Artifact decision component styles'
description: >-
  Provides the byte-pinned CSS asset for reusable Artifact decision cards,
  option rows, confirmation chrome, and responsive and print states
ccVersion: 2.1.232
-->
/* Decision-component styles, carved VERBATIM from the workshop-page
   template's presentation layer (each section below is a byte-exact slice;
   drift-pinned by test). Requires the CDS custom properties listed in
   SKILL.md — embed the template's vendored token block or define them. */

/* Decision cards, option rows, live confirm chrome (footer, painter, spinner). */
  .call-item {
    display: flex;
    gap: var(--gap-sm);
    /* Separation: air AFTER each card — the unit boundary. The card's
       own diagram stays at the base flex gap above it (tight grouping);
       margin-top here would invert that proximity. margin-bottom is
       adjacency-independent, so the lanes' varying between-elements
       can't defeat it. Shadow is theme-aware: --shadow-sm composes
       --shadow-color, darkens for dark scheme, re-pinned for print. */
    margin-bottom: var(--gap-xs);
    box-shadow: var(--shadow-sm);
    /* Right padding mirrors the marker column (card padding + marker
       width + flex gap) so option rows sit equidistant from the card's
       left and right edges. */
    padding: var(--gap-sm) calc(var(--gap-md) + 14px + var(--gap-sm)) var(--gap-sm) var(--gap-md);
    border: 1px solid var(--border-strong);
    border-radius: var(--radius);
    background: var(--fill-control);
  }
  .call-item .marker { flex: 0 0 14px; color: var(--text-accent); line-height: 1.5; }
  /* flex: 1 (not shrink-wrap): the body — and so every option row —
     spans the full card width regardless of the longest text line. */
  .call-body { display: flex; flex-direction: column; gap: var(--gap-xs); flex: 1 1 0%; min-width: 0; }
  .call-body .q { font-weight: 600; }
  .call-body .anchor { color: var(--text-secondary); font-size: 13px; }
  .call-body .decided { color: var(--text-secondary); font-size: 13px; font-weight: 600; }
  .options { display: flex; flex-direction: column; gap: 6px; margin-top: 2px; }
  .option {
    display: flex;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 4px 8px;
    /* No fixed height, and break anywhere: labels (≤60 chars) and
       reasons (≤200 chars) must wrap within the row even when they are
       a single unbroken token — an unbreakable word would otherwise set
       the flex item's min-content width and overflow the card. */
    overflow-wrap: anywhere;
    min-width: 0;
    padding: 6px 10px;
    border-radius: 5px;
    font-size: 12px;
    color: var(--text-primary);
    box-shadow: inset 0 0 0 1px var(--border-stronger);
    opacity: 0.75;
    cursor: default;
  }
  .option .option-label { font-weight: 500; }
  .option.recommended {
    /* Deliberately quiet: the recommendation is information, not a
       state — only the badge and reason distinguish it, so the SELECTED
       treatment (accent ring + tint + checkmark) reads unmistakably as
       the user's own action. */
    opacity: 1;
  }
  .option .badge {
    display: inline-flex;
    align-items: center;
    height: 16px;
    padding: 0 6px;
    border-radius: 999px;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.02em;
    text-transform: uppercase;
    color: var(--text-accent);
    background: none;
    box-shadow: inset 0 0 0 1px var(--text-accent);
  }
  .option .why { color: var(--text-secondary); }
  .option.chosen { background: var(--fill-accent); color: #fff; opacity: 1; box-shadow: none; }
  .option.chosen .why { color: #fff; opacity: 0.85; }
  .option.dim { opacity: 0.4; }
  /* Armed/selected/confirm states: live-view-only affordances managed by
     the baked decisions script below. None of these classes or elements
     ever reach published bytes — the script publishes fetched STORED
     source, never the live DOM. */
  .option.armed { cursor: pointer; opacity: 1; }
  .option.armed:hover { box-shadow: inset 0 0 0 1.5px var(--border-stronger); }
  .option.selected { box-shadow: inset 0 0 0 1.5px var(--text-accent); background: color-mix(in srgb, var(--text-accent) 10%, transparent); opacity: 1; }
  .ws-footer {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    gap: var(--gap-sm);
    /* Same height reserve as .ws-status-footer: the two rules share the
       fixed bottom band (the script swaps between them), so they must
       share the floor or the band jumps on every swap. */
    min-height: 72px;
    box-sizing: border-box;
    /* Content left-aligns with the article's text column: the article is
       a centered content-box of 76ch + 24px side padding, so its text
       edge sits at (100% - 76ch) / 2 from the viewport — the Confirm
       button lines up under the decisions it confirms. */
    padding: 14px 24px 14px max(24px, calc((100% - 76ch) / 2));
    /* Deliberately prominent: an accent-tinted surface, accent top rule,
       and elevation — the footer is the page's one call to action while
       selections are pending, in both themes. */
    /* Opaque by requirement: content must not scroll through the
       footer — accent tint layered over the page background. */
    background: color-mix(in srgb, var(--fill-accent) 7%, var(--page-bg));
    border-top: 2px solid var(--fill-accent);
    box-shadow: 0 -6px 24px rgba(0, 0, 0, 0.18);
    animation: ws-footer-in 0.22s ease-out;
  }
  @keyframes ws-footer-in {
    from { transform: translateY(100%); }
    to { transform: translateY(0); }
  }
  @media (prefers-reduced-motion: reduce) {
    .ws-footer { animation: none; }
  }
  /* Waiting-state painter: live-view-only chrome, built by the script
     below — never published bytes, like the armed/selected states. */
  .ws-painter {
    position: fixed;
    top: 16px;
    right: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
    pointer-events: none;
    color: var(--text-secondary);
    font-size: 11px;
  }
  .ws-painter canvas {
    width: 64px;
    height: 56px;
    image-rendering: pixelated;
    animation: ws-hover 2.6s ease-in-out infinite;
  }
  @keyframes ws-hover { 50% { transform: translateY(-4px); } }
  @media (prefers-reduced-motion: reduce) {
    .ws-painter canvas { animation: none; }
  }
  .confirm-btn {
    font: inherit;
    font-size: 13px;
    font-weight: 600;
    color: #fff;
    background: var(--fill-accent);
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    cursor: pointer;
  }
  .clear-btn {
    font: inherit;
    font-size: 12px;
    color: var(--text-primary);
    background: none;
    border: none;
    border-radius: 5px;
    box-shadow: inset 0 0 0 1px var(--border-stronger);
    padding: 6px 12px;
    cursor: pointer;
  }
  .confirm-hint { color: var(--text-secondary); font-size: 12px; }
  .footer-note { color: var(--text-primary); font-size: 12px; font-weight: 500; }
  .ws-spin {
    width: 14px;
    height: 14px;
    flex: 0 0 auto;
    border: 2px solid var(--border-stronger);
    border-top-color: var(--fill-accent);
    border-radius: 50%;
    animation: ws-rot 0.8s linear infinite;
  }
  @keyframes ws-rot { to { transform: rotate(360deg); } }
  @media (prefers-reduced-motion: reduce) {
    .ws-spin { animation: none; }
  }
  .note-live { color: var(--text-secondary); font-size: 12px; }

/* Direct-HTML lane: later cascade rule resolving the card shadow theme-aware. */
  .call-item {
    background: var(--surface-0);
    border: 1px solid var(--border);
    border-left: 3px solid var(--fill-accent);
    /* This later rule is where the cascade resolves the card shadow on
       this lane — it must stay theme-aware or dark mode loses the lift. */
    box-shadow: var(--shadow-sm);
  }

/* Status banner (only if the page carries a data-ws-state banner). */
  .ws-banner {
    display: inline-flex;
    align-items: center;
    align-self: flex-start;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.01em;
    color: var(--text-secondary);
    background: var(--fill-control);
    box-shadow: inset 0 0 0 1px var(--border-stronger);
  }
  .ws-banner[data-ws-state="ready"] {
    color: var(--text-accent);
    background: color-mix(in srgb, var(--text-accent) 8%, transparent);
    box-shadow: inset 0 0 0 1px var(--text-accent);
  }
  .ws-banner[data-ws-state="started"] {
    color: #fff;
    background: var(--fill-accent);
    box-shadow: none;
  }
  

/* Kickoff status footer (only if the page uses the reserved kickoff block),
   and the typed-answer input row. */
  .ws-status-footer {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    gap: var(--gap-sm);
    /* Height reserve: state changes swap the footer's content (CTAs vs a
       single status line); min-height keeps the bar, and the body padding
       that matches it, stable across states. */
    min-height: 72px;
    box-sizing: border-box;
    padding: 14px 24px 14px max(24px, calc((100% - 76ch) / 2));
    /* Opaque by requirement: content must not scroll through the
       footer — accent tint layered over the page background. */
    background: color-mix(in srgb, var(--fill-accent) 7%, var(--page-bg));
    border-top: 2px solid var(--fill-accent);
    box-shadow: 0 -6px 24px rgba(0, 0, 0, 0.18);
  }
  .ws-status-footer.ws-hidden { display: none; }
  body:has(.ws-status-footer) { padding-bottom: 72px; }
  .ws-status-note {
    color: var(--text-primary);
    font-size: 12px;
    font-weight: 500;
    margin-right: var(--gap-sm);
  }
  .ws-status-footer .option { flex: 0 0 auto; }
  /* Fixed height + explicit hover states: the shared .option.armed:hover
     rule swaps box-shadow thickness and the base .option uses baseline
     alignment — both read as the button changing size. The CTA pair pins
     its box and keeps hover to color only. */
  .option.cta,
  .option.cta-quiet {
    opacity: 1;
    height: 36px;
    box-sizing: border-box;
    align-items: center;
    padding: 0 16px;
    border-radius: 6px;
    font-size: 13px;
  }
  .option.cta {
    color: #fff;
    background: var(--fill-accent);
    box-shadow: none;
  }
  .option.cta .option-label { font-weight: 600; }
  .option.cta.armed:hover {
    box-shadow: none;
    background: color-mix(in srgb, var(--fill-accent) 88%, #000);
  }
  .option.cta-quiet { box-shadow: inset 0 0 0 1px var(--border-stronger); }
  .option.cta-quiet.armed:hover {
    box-shadow: inset 0 0 0 1px var(--border-stronger);
    background: var(--fill-control);
  }
  /* After the kickoff resolves, the footer shows only its note: the
     chosen/dim rows stay in the MARKUP (the island↔markup agreement
     check requires one data-choice element per opts token) but render
     hidden. */
  .ws-status-footer .option.chosen,
  .ws-status-footer .option.dim { display: none; }
  /* The typed-answer row: a formless input (allowed by the publish
     verifier); its live value never reaches published bytes — publish is
     fetched stored source. Selected treatment mirrors rows: accent ring
     + checkmark when the typed text is the item's active pick. */
  .custom-answer { display: flex; align-items: center; min-width: 0; }
  .option-input {
    flex: 1 1 auto;
    min-width: 0;
    font: inherit;
    font-size: 12px;
    color: var(--text-primary);
    background: transparent;
    border: none;
    border-radius: 5px;
    box-shadow: inset 0 0 0 1px var(--border-stronger);
    padding: 7px 10px;
  }
  .option-input::placeholder { color: var(--text-secondary); }
  .option-input:focus {
    outline: none;
    box-shadow: inset 0 0 0 1.5px var(--text-accent);
  }
  .custom-answer.selected .option-input {
    box-shadow: inset 0 0 0 1.5px var(--text-accent);
    background: color-mix(in srgb, var(--text-accent) 10%, transparent);
  }

