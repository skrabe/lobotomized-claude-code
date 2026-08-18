<!--
name: 'Skill: Artifact PR review HTML template'
description: >-
  Full HTML body-fragment template with slot comments and design tokens that the
  artifact PR-review skill hands the model to fill in
ccVersion: 2.1.234
-->
<!-- Artifact-tool body fragment — no <!DOCTYPE>/<html>/<head>/<body> wrapper. See SKILL.md for slot guidance.
     SECURITY: every string that originates from the PR (title, description, diff lines,
     file paths, comments, author names) is untrusted input. HTML-escape it before it
     lands in any slot: & → &amp;   < → &lt;   > → &gt;   " → &quot;   ' → &#39;.
     Attribute values you author are ALWAYS double-quoted — never single-quoted or bare. -->
<title><!-- SLOT: TAB_TITLE — the synthesis title + " PR review", plain text -->PR review</title>
<style>
  /* Design tokens ported from the prototype page's token sheet (warm-gray
     Z/T ramps, extended palette, type scale). Values are hand-copied so the
     page stays self-contained. The dark blocks must mirror any light-block
     additions. */
  :root {
    color-scheme: light;
    --z0: #ffffff;
    --z1: #f6f6f4;
    --t1: hsla(60, 3%, 4%, 0.04);
    --t2: hsla(60, 3%, 4%, 0.06);
    --t3: hsla(60, 3%, 4%, 0.1);
    --t5: hsla(60, 3%, 4%, 0.25);
    --t6: hsla(60, 3%, 4%, 0.5);
    --t7: hsla(60, 3%, 4%, 0.8);
    --t9: hsla(60, 3%, 4%, 1);
    --ink: #141413;
    --ink-soft: #6d6b67;
    --accent: hsla(210, 100%, 45%, 1);
    --accent-10: hsla(210, 100%, 45%, 0.1);
    --ok: hsla(134, 68.1%, 36.9%, 1);
    --ok-10: hsla(134, 68.1%, 36.9%, 0.1);
    --warn: hsla(25, 76%, 44%, 1);
    --warn-10: hsla(25, 76%, 44%, 0.1);
    --bad: hsla(3, 100%, 59.4%, 1);
    --bad-10: hsla(3, 100%, 59.4%, 0.1);
    --sans: "Anthropic Sans", "Styrene B LC", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
    --mono: "Anthropic Mono", "SF Mono", ui-monospace, Menlo, Consolas, monospace;
    font-family: var(--sans);
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      color-scheme: dark;
      --z0: #262624;
      --z1: #1b1a17;
      --t1: hsla(50, 9%, 94%, 0.05);
      --t2: hsla(50, 9%, 94%, 0.08);
      --t3: hsla(50, 9%, 94%, 0.13);
      --t5: hsla(50, 9%, 94%, 0.3);
      --t6: hsla(50, 9%, 94%, 0.55);
      --t7: hsla(50, 9%, 94%, 0.85);
      --t9: hsla(50, 9%, 94%, 1);
      --ink: #faf9f5;
      --ink-soft: #b8b5ad;
      --accent: hsla(210, 100%, 62%, 1);
      --accent-10: hsla(210, 100%, 62%, 0.12);
      --ok: hsla(134, 55%, 52%, 1);
      --ok-10: hsla(134, 55%, 52%, 0.12);
      --warn: hsla(25, 85%, 58%, 1);
      --warn-10: hsla(25, 85%, 58%, 0.12);
      --bad: hsla(3, 100%, 68%, 1);
      --bad-10: hsla(3, 100%, 68%, 0.12);
    }
  }
  :root[data-theme="dark"] {
    color-scheme: dark;
    --z0: #262624;
    --z1: #1b1a17;
    --t1: hsla(50, 9%, 94%, 0.05);
    --t2: hsla(50, 9%, 94%, 0.08);
    --t3: hsla(50, 9%, 94%, 0.13);
    --t5: hsla(50, 9%, 94%, 0.3);
    --t6: hsla(50, 9%, 94%, 0.55);
    --t7: hsla(50, 9%, 94%, 0.85);
    --t9: hsla(50, 9%, 94%, 1);
    --ink: #faf9f5;
    --ink-soft: #b8b5ad;
    --accent: hsla(210, 100%, 62%, 1);
    --accent-10: hsla(210, 100%, 62%, 0.12);
    --ok: hsla(134, 55%, 52%, 1);
    --ok-10: hsla(134, 55%, 52%, 0.12);
    --warn: hsla(25, 85%, 58%, 1);
    --warn-10: hsla(25, 85%, 58%, 0.12);
    --bad: hsla(3, 100%, 68%, 1);
    --bad-10: hsla(3, 100%, 68%, 0.12);
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--z1); color: var(--ink); font-size: 13px; line-height: 18px; -webkit-font-smoothing: antialiased; }
  .page { padding: 24px 24px 56px; display: flex; flex-direction: column; align-items: center; }
  .window { width: 100%; max-width: 1200px; background: var(--z0); border-radius: 16px; box-shadow: 0 0 0 1px var(--t2), 0 6px 16px 0 hsla(60, 3%, 4%, 0.06); }

  .topbar { display: flex; align-items: center; gap: 8px; padding: 12px 12px 10px 12px; border-bottom: 1px solid var(--t2); }
  .brand { font-weight: 500; font-size: 13px; white-space: nowrap; margin-left: 2px; }
  .crumb { font-size: 12px; line-height: 15px; color: var(--t6); }
  .topbar .gh { margin-left: auto; font-size: 12px; color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }

  /* Staleness banner: hidden until the baked script (bottom of this file) learns the PR
     head moved since publish. Its copy is fixed here in the template — never filled from
     PR content. */
  .stale-banner { padding: 9px 14px; border-bottom: 1px solid var(--t2); border-left: 3px solid var(--warn); background: var(--warn-10); color: var(--ink); font-size: 12px; line-height: 17px; }
  .stale-banner .lead { color: var(--ink); font-weight: 600; }
  .stale-banner code { font-family: var(--mono); font-size: 0.92em; background: var(--t1); border-radius: 3px; padding: 0 3px; }

  main { max-width: 720px; width: 100%; margin: 0 auto; padding: 32px 30px 24px; display: flex; flex-direction: column; gap: 44px; }
  main > section { margin: 0; }

  .byline { display: flex; align-items: center; gap: 9px; font-size: 12px; line-height: 15px; color: var(--t6); flex-wrap: wrap; }
  .byline .spark { width: 18px; height: 18px; flex-shrink: 0; display: grid; place-items: center; background: var(--warn-10); border-radius: 5px; color: var(--warn); }
  .byline .who { color: var(--ink); font-weight: 500; }
  .byline .ref { margin-left: auto; font-family: var(--mono); font-size: 12px; color: var(--t5); }

  h1.title { margin: 10px 0 0; font-size: 22px; line-height: 28px; font-weight: 600; letter-spacing: -0.01em; color: var(--ink); text-wrap: pretty; }

  .chips { display: flex; align-items: center; gap: 6px; margin-top: 12px; flex-wrap: wrap; }
  .chip { display: inline-flex; align-items: center; height: 16px; padding: 0 4px; border-radius: 4px; font-size: 12px; line-height: 15px; font-weight: 500; white-space: nowrap; background: var(--t2); color: var(--t7); }
  .chip.ok     { background: var(--ok-10);     color: var(--ok); }
  .chip.warn   { background: var(--warn-10);   color: var(--warn); }
  .chip.bad    { background: var(--bad-10);    color: var(--bad); }
  .chip.accent { background: var(--accent-10); color: var(--accent); }
  .chips-note { font-size: 11px; line-height: 13px; color: var(--t5); }

  .bottom-line { margin: 14px 0 0; font-size: 15.5px; line-height: 26px; color: var(--ink); text-wrap: pretty; border-left: 2px solid var(--t2); padding-left: 18px; }
  .bottom-line code, code.chip-code { font-family: var(--mono); font-size: 0.92em; background: var(--t1); border-radius: 3px; padding: 0 3px; }

  figure.visual { margin: 18px 0 0 18px; }
  figure.visual figcaption { font-size: 11px; line-height: 13px; color: var(--t6); margin-top: 8px; }
  .diagram { background: var(--t1); border-radius: 8px; padding: 16px; overflow-x: auto; }
  .diagram svg { display: block; max-width: 100%; height: auto; }

  /* Flow block: vertical timeline. Marker hue per step: .new → accent, .changed → warn, .unchanged → faint. */
  ol.flow { list-style: none; margin: 0; padding: 0; }
  ol.flow li { display: flex; gap: 8px; }
  ol.flow .rail { display: flex; flex-direction: column; align-items: center; width: 9px; flex-shrink: 0; }
  ol.flow .dot { width: 9px; height: 9px; margin-top: 3px; border-radius: 999px; background: var(--t5); }
  ol.flow li.changed .dot { background: var(--warn); box-shadow: 0 0 0 3px var(--warn-10); }
  ol.flow li.new .dot { background: var(--accent); box-shadow: 0 0 0 3px var(--accent-10); }
  ol.flow .stem { width: 1px; flex: 1; min-height: 10px; background: var(--t3); }
  ol.flow li:last-child .stem { display: none; }
  ol.flow .step-body { padding-bottom: 10px; min-width: 0; display: flex; flex-direction: column; gap: 1px; }
  ol.flow .step-label { font-size: 12px; line-height: 15px; font-weight: 500; color: var(--ink); display: inline-flex; align-items: center; gap: 6px; flex-wrap: wrap; }
  ol.flow .step-label .chip { height: 12px; border-radius: 3px; font-size: 11px; line-height: 13px; text-transform: uppercase; }
  ol.flow .step-detail { display: block; font-size: 12px; line-height: 15px; color: var(--ink-soft); }
  ol.flow .step-was { display: block; font-size: 11px; line-height: 13px; color: var(--t6); }

  /* Before/after panels */
  .ba { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .ba .panel { background: var(--z0); box-shadow: inset 0 0 0 1px var(--t2); border-radius: 8px; padding: 12px 14px; }
  .ba h4 { margin: 0 0 8px; font-size: 11px; line-height: 13px; text-transform: uppercase; letter-spacing: 0.06em; font-weight: 600; color: var(--t6); }
  .ba ul { margin: 0; padding: 0; list-style: none; }
  .ba li { font-size: 13px; line-height: 18px; padding: 3px 0; }
  .ba li.good::before { content: "●"; color: var(--ok); margin-right: 7px; font-size: 9px; vertical-align: 1px; }
  .ba li.bad::before { content: "●"; color: var(--bad); margin-right: 7px; font-size: 9px; vertical-align: 1px; }
  .ba li.neutral::before { content: "●"; color: var(--t5); margin-right: 7px; font-size: 9px; vertical-align: 1px; }

  .your-call { margin: 0; }
  .your-call > h2 { margin: 0 0 14px; font-size: 11px; line-height: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; color: var(--t6); }
  .call-item { display: grid; grid-template-columns: 14px 1fr; gap: 12px; padding-left: 2px; }
  .call-item + .call-item { margin-top: 22px; }
  .call-item .marker { color: var(--warn); font-size: 13px; line-height: 21px; }
  .call-item p { margin: 0; font-size: 13.5px; line-height: 21px; color: var(--t7); text-wrap: pretty; }
  .call-item .q { color: var(--ink); font-weight: 500; }
  .call-item .lean { margin: 8px 0 0; font-size: 12px; line-height: 18px; color: var(--t6); }
  .anchor-snippet { display: block; font-family: var(--mono); font-size: 12px; line-height: 17px; color: var(--t6); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 100%; margin-top: 4px; }
  .pills { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
  .pill { display: inline-flex; align-items: center; height: 22px; padding: 0 10px; border-radius: 5px; font-size: 12px; background: var(--z0); color: var(--t7); box-shadow: inset 0 0 0 1px var(--t3); opacity: 0.7; cursor: default; }
  /* Decided/acted states: the baked decisions script (end of this file) renders
     "resolved" after a click; the session renders "acted" on its republish. */
  .pill.chosen { background: var(--accent); color: #fff; opacity: 1; box-shadow: none; }
  .pill.dim { opacity: 0.35; }
  .call-item .decided { margin: 10px 0 0; font-size: 12px; line-height: 18px; font-weight: 500; color: var(--ok); }
  .call-item .acted { margin: 4px 0 0; font-size: 12px; line-height: 18px; color: var(--t6); }
  /* Transient status line the decisions script manages in the live view only;
     published bytes come from fetched stored source and never carry it. */
  .call-item .note-live { margin: 6px 0 0; font-size: 11px; line-height: 14px; color: var(--t5); }

  .actions { margin: 0; }
  .actions .gh-btn { display: inline-flex; align-items: center; justify-content: center; gap: 6px; height: 34px; padding: 0 16px; border-radius: 8px; font-size: 13.5px; font-weight: 500; color: var(--t6); text-decoration: none; background: transparent; box-shadow: inset 0 0 0 1px var(--t3); }
  .actions .note { margin: 8px 0 0; font-size: 11px; line-height: 14px; color: var(--t5); padding-left: 2px; }
  .stamp { display: flex; flex-direction: column; align-items: flex-start; gap: 8px; margin-bottom: 12px; }
  .stamp[hidden] { display: none; }
  .stamp-btn { font: inherit; font-size: 13.5px; font-weight: 500; height: 34px; padding: 0 16px; border-radius: 8px; border: 0; cursor: pointer; background: var(--accent-fill, var(--accent)); color: #ffffff; }
  .stamp-btn:disabled { opacity: 0.3; cursor: not-allowed; }
  .stamp-sub { margin: 0; font-size: 12px; line-height: 17px; color: var(--t6); }
  .stamp-sub[hidden] { display: none; }
  .stamp-sub code { font-family: var(--mono); font-size: 0.92em; background: var(--t1); border-radius: 3px; padding: 0 4px; }
  /* Revealed by the done note alone: the approved state is the only one where
     dismissing on GitHub is the page's next affordance. */
  .actions .gh-dismiss { display: none; }
  .actions:has(.stamp-done:not([hidden])) .gh-dismiss { display: block; width: fit-content; margin: 8px 0 0; font-size: 12px; line-height: 17px; color: var(--t6); text-decoration: underline; }
  .stamp-states p { margin: 0; font-size: 12px; line-height: 17px; color: var(--t7); }
  .stamp-states p[hidden] { display: none; }
  .stamp-states .stamp-done { color: var(--ok); font-weight: 500; }
  .stamp-states .stamp-stale, .stamp-states .stamp-precheck, .stamp-states .stamp-unclear, .stamp-states .stamp-submitted, .stamp-states .stamp-reauth, .stamp-states .stamp-unavail, .stamp-states .stamp-blocked, .stamp-states .stamp-refused { color: var(--warn); }

  .followups { margin: 0; }
  .followups h2 { margin: 0 0 6px; font-size: 11px; line-height: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; color: var(--t6); }
  .followups ul { margin: 0 2px; padding-left: 16px; }
  .followups li { font-size: 12px; line-height: 18px; color: var(--t7); padding: 1px 0; }

  details.more { border-top: 1px solid var(--t2); padding-top: 18px; }
  details.more > summary { list-style: none; cursor: pointer; display: flex; align-items: center; gap: 8px; font-size: 13px; color: var(--t7); }
  details.more > summary::-webkit-details-marker { display: none; }
  details.more > summary::before { content: "›"; color: var(--t5); display: inline-block; width: 8px; transition: transform 0.15s ease; }
  details.more[open] > summary::before { transform: rotate(90deg); }
  details.more > summary .sum-meta { font-weight: 400; color: var(--t5); font-size: 12px; }
  .more-body { display: flex; flex-direction: column; gap: 18px; padding: 18px 0 4px 16px; font-size: 12px; line-height: 18px; color: var(--ink-soft); }
  .more-body h3 { margin: 0 0 6px; font-size: 12px; font-weight: 600; color: var(--ink); }

  .signal-grid { display: grid; grid-template-columns: auto 1fr; gap: 6px 14px; align-items: baseline; font-size: 12px; line-height: 18px; }
  .signal-grid .k { color: var(--accent); font-weight: 500; }

  .file-row { display: grid; grid-template-columns: 12px 1fr auto; gap: 10px; font-family: var(--mono); font-size: 12px; line-height: 17px; padding: 4px 0; border-bottom: 1px solid var(--t2); align-items: baseline; }
  .file-row:last-child { border-bottom: 0; }
  .file-row .mode { font-weight: 600; color: var(--warn); }
  .file-row .mode.add { color: var(--ok); }
  .file-row .mode.del { color: var(--bad); }
  .file-row .mode.ren { color: var(--t6); }
  .file-row .delta { white-space: nowrap; }
  .file-row .plus { color: var(--ok); }
  .file-row .minus { color: var(--bad); }

  .explainer { background: var(--t1); border-radius: 8px; padding: 8px 12px 12px; }
  .explainer .headline { font-size: 12px; line-height: 18px; margin: 6px 0 12px; color: var(--ink-soft); }
  .explainer .headline strong { font-weight: 500; color: var(--ink); }
  .explainer-blocks { display: flex; flex-direction: column; gap: 16px; }
  .explainer-blocks figure.visual { margin-left: 0; }
  details.concern { border-top: 1px solid var(--t2); padding-top: 10px; }
  details.concern > summary { list-style: none; cursor: pointer; font-size: 12px; line-height: 18px; font-weight: 500; color: var(--ink); display: flex; gap: 6px; }
  details.concern > summary::-webkit-details-marker { display: none; }
  details.concern > summary::before { content: "›"; color: var(--t5); flex-shrink: 0; width: 8px; transition: transform 0.15s ease; }
  details.concern[open] > summary::before { transform: rotate(90deg); }
  details.concern p { font-size: 12px; line-height: 18px; color: var(--ink-soft); margin: 8px 0 0 16px; text-wrap: pretty; }

  .blind-spots { border-top: 1px solid var(--t2); padding-top: 10px; font-size: 11px; line-height: 16px; color: var(--t6); margin: 0; }

  .lede-foot { margin: 0; font-size: 11px; line-height: 16px; color: var(--t5); }

  @media (max-width: 760px) {
    main { padding: 28px 8px 20px; gap: 36px; }
    h1.title { font-size: 20px; line-height: 26px; }
    .bottom-line { padding-left: 14px; font-size: 15px; line-height: 24px; }
    .ba { grid-template-columns: 1fr; }
    .byline .ref { display: none; }
  }
</style>

<div class="page">
  <div class="window">

    <div class="topbar">
      <span class="brand">Claude Code</span>
      <span class="crumb">Review / <!-- SLOT: REPO — "owner/repo", escaped -->owner/repo</span>
      <a class="gh" href="https://github.com/owner/repo/pull/1" target="_blank" rel="noopener noreferrer"><!-- SLOT: GH_LINK — set href to the PR's GitHub URL (also used twice more below, on the Review on GitHub button and the dismiss link) -->GitHub</a>
    </div>

    <!-- Staleness banner: fixed copy, hidden by default. Only the baked script at the end
         of this template toggles its hidden flag. Not a slot — never edit or fill it. -->
    <div class="stale-banner" role="status" hidden><span class="lead">This page is out of date.</span> The pull request's branch has changed since this page was written. The author can refresh it by re-running <code>/artifact-pr-review</code>.</div>

    <main>
      <section>
        <div class="byline">
          <span class="spark" aria-hidden="true"><svg width="11" height="11" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0l1.6 5.2L15 4l-3.6 4L15 12l-5.4-1.2L8 16l-1.6-5.2L1 12l3.6-4L1 4l5.4 1.2z"/></svg></span>
          <span><span class="who">Claude</span> read <!-- SLOT: ACTIONS_READ — join synthesis.actions_read with ", " (last joined with " and ") -->the PR description, the diff and changed files</span>
          <span class="ref"><!-- SLOT: PR_REF — "repo#N", escaped -->repo#1</span>
        </div>

        <h1 class="title"><!-- SLOT: TITLE — synthesis.title, escaped. Also mirror into TAB_TITLE above. -->Plain-English description of what this PR does</h1>

        <div class="chips">
          <!-- SLOT: CHIPS — one class chip (the change class you inferred, neutral styling)
               and one recommendation chip rendering synthesis.recommendation from the generated
               JSON — class AND display text: approve → class "chip ok", text "approve";
               approve_once_resolved → class "chip warn", text "approve once resolved";
               request_changes → class "chip bad", text "request changes" (spaces, never the
               raw snake_case token). Keep to these two chips, and keep the inferred-note
               span that follows them: nothing on this page is computed by a backend, and the
               reader must be able to see that. -->
          <span class="chip">mechanical</span>
          <span class="chip ok">approve</span>
          <span class="chips-note">inferred by Claude — not a computed status</span>
        </div>

        <p class="bottom-line"><!-- SLOT: BOTTOM_LINE — synthesis.bottom_line, escaped; wrap identifier-like
             tokens you would say in monospace in <code> (that markup is yours, not the PR's). -->Three to five sentences on what the PR changes, why, and how — written for someone who has not read the diff.</p>

        <!-- SLOT: SYN_VISUAL — synthesis.visual rendered as ONE of the three block shapes
             (flow timeline / delta diagram / before-after panels; markup patterns are in the
             explainer section below — reuse them here). DELETE this whole figure when
             synthesis.visual is null. -->
        <figure class="visual">
          <ol class="flow">
            <li class="changed">
              <span class="rail" aria-hidden="true"><span class="dot"></span><span class="stem"></span></span>
              <span class="step-body">
                <span class="step-label">First pipeline step <span class="chip warn">changed</span></span>
                <span class="step-detail">What this step does now.</span>
                <span class="step-was">was: what it did before</span>
              </span>
            </li>
            <li class="unchanged">
              <span class="rail" aria-hidden="true"><span class="dot"></span><span class="stem"></span></span>
              <span class="step-body">
                <span class="step-label">Second pipeline step</span>
                <span class="step-detail">Unchanged context step.</span>
              </span>
            </li>
          </ol>
          <figcaption>One-line caption for the visual.</figcaption>
        </figure>
      </section>

      <!-- SLOT: YOUR_CALL — one .call-item per synthesis.concerns entry. DELETE the whole
           section when concerns is empty (zero is the common case). Update the count in the h2.
           Each .call-item carries data-decision-id (the concern's id from your JSON) and
           data-decision-state="open"; each pill carries data-choice with its POSITIONAL
           token — "opt1", "opt2", … in option order, and "skip" for the final Skip pill.
           Ids and tokens are identifiers you mint, never PR text; labels are escaped TEXT
           CONTENT. Keep the inert affordances (aria-disabled, title) exactly as below —
           the baked decisions script at the end of this file arms the pills only where the
           page can save a decision. Mirror every item into the prr-decisions island (same
           ids, same token order, state "open", choice null) per SKILL.md step 3c.
           When a concern has an anchor, append to its context paragraph:
           <code class="chip-code">{anchor.file, escaped}:{anchor.line}</code> (omit the
           ":{anchor.line}" part when line is null), then on its own line
           <span class="anchor-snippet">{anchor.snippet, escaped}</span>.
           Both render as escaped TEXT CONTENT — the snippet is a verbatim attacker-authored
           diff line and must never land in an attribute value. -->
      <section class="your-call">
        <h2>Needs your call · 1</h2>
        <div class="call-item" data-decision-id="q1" data-decision-state="open">
          <span class="marker" aria-hidden="true">●</span>
          <div class="call-body">
            <p><span class="q">The bolded question a reviewer should weigh?</span> Context for the question — why it is worth the reviewer's attention.</p>
            <p class="lean">Claude leans: the one-line recommended answer.</p>
            <div class="pills">
              <span class="pill" role="button" aria-disabled="true" title="Deciding from the page needs this Artifact to be able to update itself" data-choice="opt1">Option one</span>
              <span class="pill" role="button" aria-disabled="true" title="Deciding from the page needs this Artifact to be able to update itself" data-choice="opt2">Option two</span>
              <span class="pill" role="button" aria-disabled="true" title="Deciding from the page needs this Artifact to be able to update itself" data-choice="skip">Skip</span>
            </div>
          </div>
        </div>
      </section>

      <section class="actions">
        <!-- Approve control: fixed copy, hidden by default. Only the baked approve script at the
             end of this template reveals it, and only when the viewer's own GitHub connector can
             post a review as them. Not a slot — never edit or fill it. The empty .stamp-target
             span is written by that script from the anchor's owner/repo/number (validated
             identifier fields), never from PR text. The click acts directly, so the as-you
             disclosure must stay visible with the armed button, never behind another step. -->
        <div class="stamp" hidden>
          <button type="button" class="stamp-btn" aria-describedby="stamp-disclosure">Approve on GitHub</button>
          <p class="stamp-sub" id="stamp-disclosure">Posts an approving review of <code class="stamp-target"></code> from your own GitHub account, as you, if the branch is unchanged.</p>
          <div class="stamp-states" role="status">
            <p class="stamp-checking" hidden>Checking that the branch is unchanged…</p>
            <p class="stamp-busy" hidden>Approving…</p>
            <p class="stamp-done" hidden>Approved by you. The review is posted on GitHub.</p>
            <p class="stamp-submitted" hidden>GitHub accepted the review, but this page couldn't confirm it shows as approved. Check the pull request on GitHub.</p>
            <p class="stamp-stale" hidden>The branch changed since this briefing. Review the new commits on GitHub before approving there.</p>
            <p class="stamp-precheck" hidden>Couldn't confirm the branch is unchanged. Try again, or approve on GitHub.</p>
            <p class="stamp-reauth" hidden>The GitHub connector needs reconnecting. Reconnect it in claude.ai settings and reload this page, or approve on GitHub.</p>
            <p class="stamp-unavail" hidden>Approving isn't available from this page. Approve on GitHub.</p>
            <p class="stamp-blocked" hidden>This page was published without permission to use its approve tool, so approving from here can't work. The author can fix that by re-running <code>/artifact-pr-review</code>. Approve on GitHub.</p>
            <p class="stamp-refused" hidden>GitHub didn't accept the approval. Open the pull request on GitHub and try approving there.</p>
            <p class="stamp-unclear" hidden>The approval may not have gone through. Check the pull request on GitHub.</p>
          </div>
        </div>
        <a class="gh-btn" href="https://github.com/owner/repo/pull/1" target="_blank" rel="noopener noreferrer">Review on GitHub ↗</a>
        <a class="gh-dismiss" href="https://github.com/owner/repo/pull/1" target="_blank" rel="noopener noreferrer">Changed your mind? Dismiss your review on GitHub ↗</a>
        <p class="note">Approve and comment on GitHub. When the decision pills are active, a click saves your call to this page for the review session to act on.</p>
      </section>

      <section class="followups">
        <h2>Likely follow-ups</h2>
        <ul>
          <!-- SLOT: FOLLOWUPS — one <li> per synthesis.followups item, escaped. -->
          <li>a short lowercase question the reviewer is likely to ask next?</li>
        </ul>
      </section>

      <details class="more">
        <summary>Details<span class="sum-meta"><!-- SLOT: SUM_META — "N signals · N files"; the file count is the PR's total changed files, not the capped row count -->2 signals · 3 files</span></summary>
        <div class="more-body">

          <div>
            <h3>Signals</h3>
            <div class="signal-grid">
              <!-- SLOT: SIGNALS — one k/v row per signal observed via gh (CI status, review
                   decision, mergeability, bot reviews), plus a Coverage row when the diff was
                   only partially read (that one states your own coverage). Values are statements
                   of what you saw, escaped; omit rows you could not observe rather than guessing. -->
              <span class="k">CI</span><span>12/12 checks passing @ abc1234</span>
              <span class="k">Reviews</span><span>no human review yet</span>
            </div>
          </div>

          <div>
            <h3>Files</h3>
            <!-- SLOT: FILES — one .file-row per changed file (cap at 20; add a final
                 "… and N more" plain row beyond that). Mode letter from the files
                 endpoint's status field (step 1) or the diff you actually read:
                 modified/changed → M, added/copied → A (class "mode add"),
                 removed → D (class "mode del"), renamed → R (class "mode ren").
                 When the change type wasn't observed, leave the mode span EMPTY
                 rather than guessing. Paths escaped. -->
            <div class="file-row"><span class="mode">M</span><span>src/example/path.ts</span><span class="delta"><span class="plus">+10</span> <span class="minus">−2</span></span></div>
          </div>

          <div class="explainer">
            <p class="headline"><strong>Visual explainer.</strong> <!-- SLOT: EXPLAINER_HEADLINE — explainer.headline, escaped -->One complete-thought sentence a reviewer reads without expanding anything.</p>
            <div class="explainer-blocks">

              <!-- SLOT: EXPLAINER_BLOCKS — render explainer.blocks in order, one element per
                   block, using these four markup patterns. Delete the sample blocks below.

                   delta_diagram (at most one): ONE inline <svg> with a fixed viewBox and no
                   width/height, wrapped in <figure class="visual"><div class="diagram">…</div>
                   <figcaption>caption</figcaption></figure>. Draw the DELTA, not the final
                   state: boxes for nodes (rounded <rect> + <text>), arrows for edges
                   (<path> + marker or plain line+polygon). Color by kind, via style attributes
                   only (var() fails silently in bare SVG attributes): new → var(--accent),
                   modified → var(--warn), existing → var(--t5) at opacity 0.5. Label
                   edges with small text. 14–16px text, generous padding — cramped diagrams are
                   the most common failure. role="img" + aria-label on the svg; the aria-label
                   is written in your own words, never copied PR text (see the untrusted-input
                   rules — PR-derived strings never go in attributes).

                   flow: the ol.flow timeline pattern (see SYN_VISUAL sample above), wrapped in
                   figure.visual with a figcaption. Step marker class: new | changed | unchanged;
                   label chip matches the marker — new → <span class="chip accent">new</span>,
                   changed → <span class="chip warn">changed</span>, unchanged → no chip;
                   "annotation" goes in .step-was.

                   before_after: <figure class="visual"><div class="ba">
                     <div class="panel"><h4>Before</h4><ul><li class="bad|neutral|good">item</li>…</ul></div>
                     <div class="panel"><h4>After</h4><ul>…</ul></div>
                   </div><figcaption>what flipped</figcaption></figure>

                   concern: the details.concern pattern below, one per concern block, summary =
                   the complete-thought summary, body paragraphs inside. -->
              <details class="concern">
                <summary>A complete-thought concern summary the reader understands without expanding.</summary>
                <p>Mechanism and trade-offs, paragraph one.</p>
              </details>

            </div>
            <p class="blind-spots" style="margin-top: 16px;"><!-- SLOT: BLIND_SPOTS — "Didn't change: " + blind_spots.didnt_change items joined with " · ", escaped. DELETE this <p> when the list is empty. -->Didn't change: adjacent thing one · adjacent thing two</p>
          </div>

        </div>
      </details>

      <p class="lede-foot"><!-- SLOT: LEDE — the top-level lede sentence, escaped -->One sentence: what this PR does and why.</p>
    </main>

  </div>
</div>

<!-- STALENESS ANCHOR (publish-time data island). Fill ONLY the values, per SKILL.md § Step 3b:
     owner, repo, number, headSha (40 lowercase hex), publishedAt (UTC ISO-8601). Leave "live"
     as null unless the GitHub-connector gate in § Step 3b passed; a null "live" makes the page
     render exactly as the static briefing. Values here are validated identifier fields —
     never PR title, description, or diff text.
     Cross-lane contract: "kind", "owner", "repo", "number", and "publishedAt" are the fields every
     review-artifact anchor shares; each "kind" adds its own version field ("pr" → "headSha";
     other kinds add their own) and ships its own baked staleness script with its own hash pin. The script below watches only kind "pr" and
     ignores any other kind, so sibling kinds never edit this block. -->
<script type="application/json" id="prr-anchor">{"anchor":{"kind":"pr","owner":"owner","repo":"repo","number":1,"headSha":"0000000000000000000000000000000000000000","publishedAt":"1970-01-01T00:00:00Z"},"live":null}</script>

<!-- STALENESS SCRIPT — FIXED, VETTED CODE. Copy byte-for-byte; never edit, reorder, or extend
     it. A test pins this block by exact hash, so any change is a deliberate, reviewed hash
     update in the same change. It reads only the #prr-anchor island above and
     the viewer's GitHub connector via the runtime's mcp capability, and the only thing it can
     ever change is the hidden flag of the .stale-banner element (fixed copy).
     Contract: written against the artifact viewer's runtime MCP surface (claude.use('mcp'), or
     window.claude.mcp on a 0.1.x runtime: listTools/watchTool, readOnlyHint, McpError codes);
     the exact contract version is recorded next to the hash pin in the test suite. A change to
     that surface requires editing this block and re-deriving its pinned hash together;
     published pages keep the block they shipped with and fall back to the static page on any
     mismatch. -->
<script>
(function prReviewStaleness() {
  var island = document.getElementById('prr-anchor');
  var banner = document.querySelector('.stale-banner');
  if (!island || !banner) return;

  var cfg;
  try {
    cfg = JSON.parse(island.textContent || 'null');
  } catch (e) {
    return;
  }
  if (!cfg || typeof cfg !== 'object') return;
  var anchor = cfg.anchor;
  var live = cfg.live;

  var HEX40 = /^[0-9a-f]{40}$/i;
  var IDENT = /^[A-Za-z0-9_.-]{1,64}$/;
  var KEY = /^[A-Za-z0-9_]{1,48}$/;
  var METHOD_KEY = /^method$/i;

  if (!anchor || anchor.kind !== 'pr') return;
  if (typeof anchor.headSha !== 'string' || !HEX40.test(anchor.headSha)) return;
  if (!live || typeof live !== 'object' || Array.isArray(live)) return;
  if (typeof live.tool !== 'string' || !IDENT.test(live.tool)) return;
  var input = live.input;
  if (!input || typeof input !== 'object' || Array.isArray(input)) return;
  var inputKeys = Object.keys(input);
  if (inputKeys.length > 8) return;
  for (var k = 0; k < inputKeys.length; k++) {
    if (!KEY.test(inputKeys[k])) return;
    var val = input[inputKeys[k]];
    /* A method-named key holds an operation selector, which is a word —
       never a number. Any identifier word is tolerated (this loose lane
       pins no vocabulary); only the type narrows. */
    if (METHOD_KEY.test(inputKeys[k]) && typeof val !== 'string') return;
    if (typeof val === 'string') {
      if (!IDENT.test(val)) return;
    } else if (typeof val === 'number') {
      if (!Number.isSafeInteger(val)) return;
    } else {
      return;
    }
  }
  var path = live.shaPath;
  if (!Array.isArray(path) || path.length === 0 || path.length > 6) return;
  for (var p = 0; p < path.length; p++) {
    if (typeof path[p] !== 'string' || !KEY.test(path[p])) return;
  }

  /* Bind the watch to the anchored pull request: the live call's input must carry the
     anchor's owner, repo, and number as DISTINCT entries, or the page stays static.
     Distinct-entry consumption (not membership): when owner === repo (grafana/grafana),
     one value must not satisfy both probes — each anchor part consumes its own entry. */
  var OWNER = /^[A-Za-z0-9-]{1,39}$/;
  if (typeof anchor.owner !== 'string' || !OWNER.test(anchor.owner)) return;
  if (typeof anchor.repo !== 'string' || !IDENT.test(anchor.repo)) return;
  if (!Number.isSafeInteger(anchor.number) || anchor.number < 1) return;
  var inputValues = [];
  for (var vk = 0; vk < inputKeys.length; vk++) {
    /* A method entry is never evidence the binding names the PR: blank it
       so the distinct-entry consumption below cannot consume it as the
       owner, repository, or number. */
    inputValues.push(METHOD_KEY.test(inputKeys[vk]) ? undefined : input[inputKeys[vk]]);
  }
  var need = [anchor.owner, anchor.repo, anchor.number];
  var used = [];
  for (var nd = 0; nd < need.length; nd++) {
    var foundAt = -1;
    for (var iv = 0; iv < inputValues.length; iv++) {
      if (!used[iv] && inputValues[iv] === need[nd]) { foundAt = iv; break; }
    }
    if (foundAt === -1) return;
    used[foundAt] = true;
  }

  /* A 0.2.x viewer runtime hands the connector surface to claude.use('mcp') and
     answers null when this view cannot run it; a 0.1.x runtime has no use() and
     mounts window.claude.mcp synchronously instead. */
  function mcpApi() {
    var c = window.claude;
    if (!c) return Promise.resolve(null);
    return typeof c.use === 'function' ? c.use('mcp') : Promise.resolve(c.mcp);
  }
  var mcp = null;

  var anchorSha = anchor.headSha.toLowerCase();

  /* true = head moved (stale), false = head matches, null = payload shape not understood. */
  function staleVerdict(payload) {
    var cur = payload;
    for (var i = 0; i < path.length; i++) {
      if (!cur || typeof cur !== 'object') return null;
      cur = cur[path[i]];
    }
    if (typeof cur !== 'string' || !HEX40.test(cur)) return null;
    return cur.toLowerCase() !== anchorSha;
  }

  /* A watched tool must be a wire-declared read: the connector itself must
     annotate it readOnlyHint: true. Name-based trust is not enough — an
     unannotated write tool must never be bound to a refetching watch. */
  function isDeclaredRead(tool) {
    var notes = tool ? tool.annotations : null;
    return notes ? notes.readOnlyHint === true : false;
  }

  /* The one exemption to the declared-read requirement: some serving paths
     strip annotations, so exactly the name pull_request_read — a read by
     GitHub's own contract — with the hint ABSENT (a present readOnlyHint
     key of any value still refuses) on a GitHub-presenting server. */
  function isExemptRead(tool, serverName) {
    if (!tool || tool.name !== 'pull_request_read') return false;
    var notes = tool.annotations;
    var absent = notes == null || (typeof notes === 'object' && !Array.isArray(notes) && !('readOnlyHint' in notes));
    if (!absent) return false;
    return typeof serverName === 'string' && /github/i.test(serverName);
  }

  mcpApi().then(function (got) {
    if (!got || typeof got.listTools !== 'function' || typeof got.watchTool !== 'function') return null;
    mcp = got;
    return mcp.listTools();
  }).then(function (res) {
    var servers = (res ? res.servers : null) || [];
    var server = null;
    var matches = 0;
    for (var s = 0; s < servers.length; s++) {
      var tools = (servers[s] ? servers[s].tools : null) || [];
      for (var t = 0; t < tools.length; t++) {
        var candidate = tools[t];
        if (candidate ? candidate.name === live.tool : false) {
          if (!isDeclaredRead(candidate) && !isExemptRead(candidate, servers[s] ? servers[s].server : null)) return;
          server = servers[s].server;
          matches++;
          break;
        }
      }
    }
    if (matches !== 1 || typeof server !== 'string') return;

    var denied = false;
    var stop = mcp.watchTool(
      server,
      live.tool,
      input,
      function (ev) {
        if (!ev) return;
        if (ev.type === 'data') {
          var result = ev.result || {};
          var verdict = staleVerdict(result.payload);
          if (verdict === true) banner.hidden = false;
          else if (verdict === false) banner.hidden = true;
          return;
        }
        if (ev.type === 'error') {
          var code = ev.error ? ev.error.code : undefined;
          switch (code) {
            case 'needs_reauth':
            case 'server_not_connected':
            case 'blocked_by_policy':
            case 'approval_required':
            case 'not_in_manifest':
            case 'not_granted':
            case 'capability_disabled':
            case 'capability_removed':
            case 'selection_required':
            case 'server_not_found':
              banner.hidden = true;
              denied = true;
              if (typeof stop === 'function') { stop(); stop = null; }
              return;
            default:
              return;
          }
        }
      },
      { refetchInterval: 120000, cache: { staleTime: 60000 } }
    );
    /* A denial delivered synchronously during watchTool() runs before \`stop\`
       exists; the flag carries that cancel across the assignment. Nulling
       after every stop() makes the cancel single-shot even if the runtime
       delivers another denial to an already-dead watch. */
    if (denied && typeof stop === 'function') { stop(); stop = null; }
  }).catch(function () {
    return;
  });
})();
</script>

<!-- DECISIONS ISLAND (publish-time data island). Fill ONLY the values, per SKILL.md § Step 3c:
     one entry per "Needs your call" item — id (the concern's id, e.g. "q1"), opts (the pill
     tokens in order: "opt1".."optN" then "skip"), state "open", choice null. Identifier
     tokens only (grammar ^[a-z0-9-]{1,24}$) — NEVER PR title, prose, pill labels, or URLs.
     When the your-call section is deleted (no concerns), fill this island with {"items":[]}.
     This island is the ONLY surface the review session reads decisions from — the baked
     script below and the session's acting loop both treat page markup as display only. -->
<script type="application/json" id="prr-decisions">{"items":[{"id":"q1","opts":["opt1","opt2","skip"],"state":"open","choice":null}]}</script>

<!-- DECISIONS SCRIPT — FIXED, VETTED CODE. Copy byte-for-byte; never edit, reorder, or
     extend it. A test pins this block by exact hash, so any change is a deliberate,
     reviewed hash update in the same change. It arms the "Needs your call" pills only
     where the page can save a decision (the publish declared the artifact-publish capability; the
     shell enforces the writer gate server-side — this
     script holds no authority). A click republishes THIS page with the clicked item
     recorded: the published bytes come from a same-origin fetch of the page's own STORED
     source — never from serializing the live DOM — with the clicked item's markup and its
     prr-decisions island entry mutated together in the parsed copy, so the page and its
     machine-readable record cannot publish out of sync. First click wins per item: the
     stored source is re-checked before publishing, and the server's version
     compare-and-swap arbitrates racing clicks (the loser's view reloads to the winner).
     Without the capability, or without write access, the pills stay the inert spans the
     template ships. -->
<script>
(function prReviewDecisions() {
  'use strict';
  var busy = false;
  var TOKEN = /^[a-z0-9-]{1,24}$/;
  /* A 0.2.x viewer runtime hands the namespace to claude.use('artifact'),
     null when this view cannot run it; a 0.1.x runtime has no use() and
     mounts it on window.claude synchronously (artifact, legacy self). A
     read-only view gets it either way and learns so when publish() rejects. */
  var used = null;
  var asked = false;
  function selfApi() {
    var c = window.claude;
    if (c && typeof c.use === 'function') {
      if (!asked) {
        asked = true;
        c.use('artifact').then(function (got) {
          used = got;
          arm();
        });
      }
      return used && typeof used.publish === 'function' ? used : null;
    }
    var a = c && (c.artifact || c.self);
    return a && typeof a.publish === 'function' ? a : null;
  }
  function openPills(scope) {
    return scope.querySelectorAll('[data-decision-state="open"] .pill[data-choice]');
  }
  /* Affordance only — authorization stays server-side. Arms once, from
     whichever answers first: use()'s resolution, or a brief poll that on
     a 0.1.x runtime covers only script-order skew (the stub mounts
     synchronously when the capability is declared). No open pills while
     the markup is still parsing only means not yet, so the latch waits
     for a later tick. */
  var armed = false;
  function arm() {
    if (armed || !selfApi()) return;
    var pills = openPills(document);
    if (!pills.length && document.readyState === 'loading') return;
    armed = true;
    for (var i = 0; i < pills.length; i++) {
      pills[i].removeAttribute('aria-disabled');
      pills[i].removeAttribute('title');
      pills[i].setAttribute('tabindex', '0');
      pills[i].style.cursor = 'pointer';
      pills[i].style.opacity = '1';
    }
  }
  var tries = 0;
  var timer = setInterval(function () {
    arm();
    if (armed || ++tries > 20) clearInterval(timer);
  }, 250);
  selfApi();
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
  /* The resolved mutation, applied to the live item (optimistic copy) and to
     the PARSED stored copy (the published bytes) alike — elements are built
     via item.ownerDocument, so one builder serves both. The literals here
     (state, choice attribute, chosen/dim classes, the Decided line and its
     position) are the rendering contract SKILL.md "Acting on decisions"
     replays when the session marks an item acted. */
  function markResolved(item, token) {
    item.setAttribute('data-decision-state', 'resolved');
    item.setAttribute('data-resolved-choice', token);
    var pills = item.querySelectorAll('.pill[data-choice]');
    var label = '';
    for (var i = 0; i < pills.length; i++) {
      var p = pills[i];
      var chosen = p.getAttribute('data-choice') === token;
      if (chosen) label = p.textContent;
      p.className = chosen ? 'pill chosen' : 'pill dim';
      p.removeAttribute('role');
      p.removeAttribute('aria-disabled');
      p.removeAttribute('title');
      p.removeAttribute('tabindex');
      p.removeAttribute('style');
    }
    var decided = item.ownerDocument.createElement('p');
    decided.className = 'decided';
    decided.textContent = 'Decided: ' + label;
    var body = item.querySelector('.call-body') || item;
    body.insertBefore(decided, body.querySelector('.pills'));
  }
  /* One island entry, validated against the full step-3c contract — every
     key known, every value grammar-bound. Strictness is a security boundary,
     not pedantry: the rewrite below is JSON.parse → JSON.stringify, and that
     round-trip would turn a JSON-escaped markup sequence in a hostile island
     (harmless as stored bytes) into raw breakout bytes inside a RAWTEXT
     script element. Grammar-bound values cannot carry markup at all, so an
     out-of-contract island simply never republishes. */
  function validEntry(entry) {
    if (!entry || typeof entry !== 'object') return false;
    var keys = Object.keys(entry);
    if (keys.length !== 4) return false;
    if (typeof entry.id !== 'string' || !TOKEN.test(entry.id)) return false;
    if (entry.state !== 'open' && entry.state !== 'resolved' && entry.state !== 'acted') return false;
    if (!Array.isArray(entry.opts) || entry.opts.length < 1 || entry.opts.length > 8) return false;
    for (var i = 0; i < entry.opts.length; i++) {
      if (typeof entry.opts[i] !== 'string' || !TOKEN.test(entry.opts[i])) return false;
    }
    if (entry.choice !== null && (typeof entry.choice !== 'string' || !TOKEN.test(entry.choice))) return false;
    return true;
  }
  /* The island entry must exist, be open, and declare the token — and the
     WHOLE island must be contract-valid (every entry, unique ids, ≤20
     items) — or nothing publishes: the island is the machine-readable
     record the session acts on, so a page whose island disagrees with its
     markup or its grammar is out of contract. This is the same whole-island
     contract the acting session's read loop enforces (SKILL.md "Acting on
     decisions" item 1) — the page refuses to extend what the session would
     refuse to read. The rewrite REBUILDS the island from validated fields
     only, so the serialized output's alphabet is provably TOKEN characters,
     JSON punctuation, and the three state words — it can never form a
     script-closing or markup sequence, whatever the stored bytes spelled. */
  function syncIsland(doc, id, token) {
    var island = doc.getElementById('prr-decisions');
    if (!island) return false;
    var cfg;
    try {
      cfg = JSON.parse(island.textContent || 'null');
    } catch (e) {
      return false;
    }
    if (!cfg || typeof cfg !== 'object' || Array.isArray(cfg)) return false;
    if (Object.keys(cfg).length !== 1 || !Array.isArray(cfg.items)) return false;
    if (cfg.items.length > 20) return false;
    var out = [];
    var hit = false;
    for (var i = 0; i < cfg.items.length; i++) {
      var entry = cfg.items[i];
      if (!validEntry(entry)) return false;
      if (entry.choice !== null && entry.opts.indexOf(entry.choice) === -1) return false;
      for (var k = 0; k < out.length; k++) {
        if (out[k].id === entry.id) return false;
      }
      var state = entry.state;
      var choice = entry.choice;
      if (entry.id === id) {
        if (state !== 'open' || entry.opts.indexOf(token) === -1) return false;
        state = 'resolved';
        choice = token;
        hit = true;
      }
      out.push({ id: entry.id, opts: entry.opts.slice(), state: state, choice: choice });
    }
    if (!hit) return false;
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
      return false;
    }
    island.textContent = json;
    return true;
  }
  /* Publishable source, as a Promise: this view's own stored bytes
     (same-origin GET of the URL the document loaded from), with frame-asset's
     per-serve head injection excised and the clicked item resolved. Fetching
     source — instead of serializing the live DOM — keeps every client
     runtime's DOM work (theme stamps, this script's own notes and
     affordances) out of published bytes by construction. */
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
  function hasScriptOpen(s) {
    /* '<' then 'script' in any ASCII case, no terminator required — the
       reach of the CLI's case-insensitive script-open test, folded per
       char like isScriptCloseAt. */
    for (var i = s.indexOf('<'); i !== -1; i = s.indexOf('<', i + 1)) {
      var k = 0;
      for (; k < 6; k++) {
        var c = s.charCodeAt(i + 1 + k);
        if (c >= 65 && c <= 90) c = c | 32;
        if (c !== 'script'.charCodeAt(k)) break;
      }
      if (k === 6) return true;
    }
    return false;
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
          /* A comment-open plus a script-open in the data can leave the
             tokenizer in its (double-)escaped states, where this close
             does NOT end the script. Refuse the pair rather than model
             them: the injectors refuse it too, so no emitted block has
             it. The comment-open is spelled split below so this script's
             own source never enters the escaped state here. */
          var d = s.slice(from, i);
          if (d.indexOf('<' + '!--') !== -1 && hasScriptOpen(d)) return -1;
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
  /* Exactly the HTML ASCII whitespace set (space, TAB, LF, FF, carriage
     return), used in-tag AND between tags; String trim or regex whitespace
     would also accept chars the tokenizer renders as text (NBSP, U+2028,
     U+FEFF…) and so could excise author-visible bytes. charCodes keep this
     template backslash-free. KEEP-IN-SYNC: goCp isFrameAssetInjection. */
  function wsCode(c) {
    return c === 32 || c === 9 || c === 10 || c === 12 || c === 13;
  }
  function wsTrim(s) {
    var a = 0;
    var b = s.length;
    while (a < b && wsCode(s.charCodeAt(a))) a++;
    while (b > a && wsCode(s.charCodeAt(b - 1))) b--;
    return s.slice(a, b);
  }
  function scriptOpenEnd(s, from) {
    /* Where the open tag whose attributes begin at s[from] ends, walked
       the way the tokenizer walks attributes (KEEP-IN-SYNC with goCp's
       openTagEnd): greater-than ends the tag everywhere EXCEPT
       inside a quoted attribute value, and a quote opens a value only
       straight after an attribute's equals sign (whitespace allowed);
       anywhere else it is an ordinary name or value byte. Returns the
       offset AFTER the tag, or -1 when the text ends inside it. Ending
       at the first greater-than would end a planted tag inside its
       quoted value, where the browser keeps consuming, and validate a
       span the browser never closed. States: 0 before name, 1 name,
       2 after name, 3 before value, 4 unquoted value, 5 after quoted. */
    var st = 0;
    var i = from;
    while (i < s.length) {
      var c = s.charCodeAt(i);
      if (st === 3) {
        if (c === 34 || c === 39) {
          var q = s.indexOf(c === 34 ? '"' : "'", i + 1);
          if (q === -1) return -1;
          i = q + 1;
          st = 5;
          continue;
        }
        if (wsCode(c)) {
          i++;
          continue;
        }
        if (c === 62) return i + 1;
        st = 4;
        i++;
        continue;
      }
      if (c === 62) return i + 1;
      if (wsCode(c)) st = st === 1 || st === 2 ? 2 : 0;
      else if (c === 47 && st !== 4) st = 0;
      else if (c === 61 && (st === 1 || st === 2)) st = 3;
      else st = st === 4 ? 4 : 1;
      i++;
    }
    return -1;
  }
  function isFrameAssetInjection(inner) {
    var s = wsTrim(inner);
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
    s = wsTrim(s.slice(gt + 1));
    while (s.length) {
      if (s.indexOf('<script') !== 0) return false;
      /* Word boundary after 'script' — '<scriptfoo>' must fail like
         goCp's <script-then-boundary grammar. */
      var bnd = s.charCodeAt(7);
      if (bnd !== 62 && bnd !== 47 && !wsCode(bnd)) return false;
      var open = scriptOpenEnd(s, 7);
      if (open === -1) return false;
      var after = findScriptClose(s, open);
      if (after === -1) return false;
      s = wsTrim(s.slice(after));
    }
    return true;
  }
  function sourceHtml(itemId, token) {
    /* Bounded read: a hung fetch would otherwise leave \`busy\` stuck (no
       reject, no catch, pills frozen until reload). 15s is far under the
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
        var doc = new DOMParser().parseFromString(text, 'text/html');
        var sel =
          '[data-decision-id="' +
          (window.CSS && CSS.escape ? CSS.escape(itemId) : itemId) +
          '"]';
        var item = doc.querySelector(sel);
        /* A missing or non-open item in the STORED source means this click
           raced a newer version — return null so the caller reverts. */
        if (!item || item.getAttribute('data-decision-state') !== 'open') {
          return null;
        }
        if (!syncIsland(doc, itemId, token)) {
          return null;
        }
        markResolved(item, token);
        /* Assembled: the template must stay a doctype-free body fragment
           (inventory test), so the literal can't appear in stored bytes. */
        var out = doc.doctype ? '<!' + 'doctype html>' : '';
        return out + doc.documentElement.outerHTML;
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
  function onActivate(e) {
    var target = e.target;
    if (!target || !target.closest) return;
    var pill = target.closest('.pill[data-choice]');
    if (!pill || busy) return;
    var item = pill.closest('[data-decision-id]');
    if (!item || item.getAttribute('data-decision-state') !== 'open') return;
    var api = selfApi();
    if (!api) return;
    var token = pill.getAttribute('data-choice');
    if (!token || !TOKEN.test(token)) return;
    var undo = item.innerHTML;
    function revert() {
      item.innerHTML = undo;
      item.setAttribute('data-decision-state', 'open');
      item.removeAttribute('data-resolved-choice');
      busy = false;
    }
    busy = true;
    try {
      /* Optimistic live-DOM copy of the mutation; the published bytes come
         from sourceHtml's fetched source, never from this DOM. A throw here
         (hand-edited markup) must not leave the page looking
         decided-but-unsaved with busy stuck. */
      markResolved(item, token);
      note(item, 'Saving…');
    } catch (err) {
      revert();
      return;
    }
    sourceHtml(item.getAttribute('data-decision-id'), token)
      .then(function (html) {
        if (html === null) {
          revert();
          note(item, 'This item changed under you — reload to see it.');
          return;
        }
        return api.publish(html).then(function () {
          /* The shell reboots this view to the new version; the note is
             cosmetic until then. */
          note(item, 'Saved — the review session will pick this up.');
          busy = false;
        });
      })
      .catch(function (err) {
        var text = friendly(err);
        if (text === null) {
          note(item, 'Someone else updated this page — reloading…');
          busy = false;
          return;
        }
        revert();
        note(item, text);
      });
  }
  document.addEventListener('click', onActivate);
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    if (!e.target || !e.target.closest) return;
    if (!e.target.closest('.pill[data-choice]')) return;
    e.preventDefault();
    onActivate(e);
  });
})();
</script>

<!-- APPROVE BINDING (publish-time data island). The composed lane fills this from the
     payload's "stamp" field; the raw lane ALWAYS keeps {"stamp":null} — publish refuses a
     non-null stamp outside the composed lane. A filled binding names the single review-write
     tool the publishing session observed on the GitHub connector, the exact approve input,
     and the result key path of the review's state. Every input value must be one of the
     anchor's own identifiers, an approve vocabulary word, or the create method word under
     exactly the key named method, so the approve can only target the anchored pull
     request. With "stamp": null the page keeps the "Review on GitHub"
     fallback and shows no approve control. Never PR title, description, diff text, or any URL. -->
<script type="application/json" id="prr-stamp">{"stamp":null}</script>

<!-- APPROVE SCRIPT — FIXED, VETTED CODE. Copy byte-for-byte; never edit, reorder, or extend
     it. A test pins this block by exact hash, so any change is a deliberate, reviewed hash
     update in the same change. It reads only the #prr-anchor and #prr-stamp islands and the
     fixed approve control above, and it calls the viewer's own GitHub connector — once, on
     the viewer's explicit click beside the always-visible as-you disclosure, and only after
     a fresh re-read confirms the pull request's head still matches the anchor. It writes no
     fetched data into the page, follows no URLs, and never retries a write.
     Contract: written against the artifact viewer's runtime MCP surface (claude.use('mcp'), or
     window.claude.mcp on a 0.1.x runtime: listTools/callTool, readOnlyHint, McpError codes);
     the exact contract version is recorded next to the hash pin in the test suite. The
     click-time freshness re-read passes callTool's cache refresh option; a runtime that
     ignores it serves a cached head at most staleTime old, and the write then rides a
     slightly wider re-read window — the banner latch and the anchored-values wall still
     hold. A change to that surface requires editing this block and re-deriving its pinned
     hash together; published pages keep the block they shipped with and fall back to the
     static page on any mismatch. -->
<script>
(function prReviewApprove() {
  var anchorIsland = document.getElementById('prr-anchor');
  var stampIsland = document.getElementById('prr-stamp');
  var banner = document.querySelector('.stale-banner');
  var box = document.querySelector('.stamp');
  if (!anchorIsland || !stampIsland || !banner || !box) return;
  var btn = box.querySelector('.stamp-btn');
  var sub = box.querySelector('.stamp-sub');
  var target = box.querySelector('.stamp-target');
  var notes = {
    checking: box.querySelector('.stamp-checking'),
    busy: box.querySelector('.stamp-busy'),
    done: box.querySelector('.stamp-done'),
    submitted: box.querySelector('.stamp-submitted'),
    stale: box.querySelector('.stamp-stale'),
    precheck: box.querySelector('.stamp-precheck'),
    reauth: box.querySelector('.stamp-reauth'),
    unavail: box.querySelector('.stamp-unavail'),
    blocked: box.querySelector('.stamp-blocked'),
    refused: box.querySelector('.stamp-refused'),
    unclear: box.querySelector('.stamp-unclear')
  };
  if (!btn || !sub || !target) return;
  for (var name in notes) {
    if (!notes[name]) return;
  }

  var cfg;
  var scfg;
  try {
    cfg = JSON.parse(anchorIsland.textContent || 'null');
    scfg = JSON.parse(stampIsland.textContent || 'null');
  } catch (e) {
    return;
  }
  if (!cfg || typeof cfg !== 'object' || !scfg || typeof scfg !== 'object') return;
  var anchor = cfg.anchor;
  var live = cfg.live;
  var stamp = scfg.stamp;

  var HEX40 = /^[0-9a-f]{40}$/i;
  var IDENT = /^[A-Za-z0-9_.-]{1,64}$/;
  var KEY = /^[A-Za-z0-9_]{1,48}$/;
  var OWNER = /^[A-Za-z0-9-]{1,39}$/;
  /* The only words, besides the anchor's own identifiers, that an approve input may carry. */
  var VOCAB = /^approved?$/i;
  var METHOD_KEY = /^method$/i;
  var METHOD_VOCAB = /^create$/i;
  var LIVE_METHOD_VOCAB = /^get$/i;
  /* Positive name allowlist: the tool must BE a create-and-submit review tool by name. The
     absence of banned words is too weak a grammar — a review-named non-approve write
     (request_copilot_review) or a renamed submit-pending tool passes a denylist, and
     submitting a reviewer's own pre-existing pending review would publish their unreleased
     draft comments under the approval. The denylist stays as a second, independent wall. */
  var APPROVE_TOOL = /^(create_(and_submit_)?)?(pull_?request_|pr_)?review(_write)?$/i;
  /* The approve verb may only ride an event-named key: under any other key
     (body, method) the write would post an event-less PENDING draft while
     the page claims a submission. */
  var EVENT_KEY = /^(review_?)?event$/i;
  var DESTRUCTIVE_TOOL = /merge|delete|dismiss|close|remove|update|branch|file|push|comment|request_changes|pending|reviewers/i;
  /* Identity-family keys must hold exactly the anchor's own value, and an owner/repo value
     may only ride a key of its own family: a value-level allowlist alone still admits
     swapped or decoy-keyed owner/repo values, which name a different (squattable)
     repository. SUBSTRING classes, not exact spellings, so nonstandard connector key
     spellings (ownerName, repo_name) classify too; a key matching both families refuses. */
  var OWNERISH_KEY = /owner|org|login|user/i;
  var REPOISH_KEY = /repo|project/i;

  if (!anchor || anchor.kind !== 'pr') return;
  if (typeof anchor.headSha !== 'string' || !HEX40.test(anchor.headSha)) return;
  if (typeof anchor.owner !== 'string' || !OWNER.test(anchor.owner)) return;
  if (typeof anchor.repo !== 'string' || !IDENT.test(anchor.repo)) return;
  if (!Number.isSafeInteger(anchor.number) || anchor.number < 1) return;
  var anchorSha = anchor.headSha.toLowerCase();
  /* The unfilled template's placeholder anchor names a squattable owner/repo and a head
     no branch can ever match; a control armed against it could only mislead. */
  if (anchorSha === '0000000000000000000000000000000000000000') return;

  function validPath(path) {
    if (!Array.isArray(path) || path.length === 0 || path.length > 6) return null;
    for (var i = 0; i < path.length; i++) {
      if (typeof path[i] !== 'string' || !KEY.test(path[i])) return null;
    }
    return path;
  }

  /* The live READ binding. PR-membership alone is not enough here: this read is what the
     click-time freshness check trusts, so every value must BE one of the anchor's own
     identifiers (owner, repo, number) — or, under exactly the key named method, the read
     method word "get" the real connector's consolidated read tool REQUIRES — a value the
     anchor does not name could point the re-read at a resource that is not the reviewed
     pull request. The anchored head SHA is deliberately NOT allowed: a read tool that
     echoes its arguments would let a publisher point shaPath at the echo and make the
     freshness check vacuously pass. A read input carrying anything else never arms. */
  function liveInputOf(b) {
    if (!b || typeof b !== 'object' || Array.isArray(b)) return null;
    if (typeof b.tool !== 'string' || !IDENT.test(b.tool)) return null;
    var input = b.input;
    if (!input || typeof input !== 'object' || Array.isArray(input)) return null;
    var keys = Object.keys(input);
    if (keys.length === 0 || keys.length > 8) return null;
    var hasOwner = false;
    var hasRepo = false;
    var hasNumber = false;
    for (var i = 0; i < keys.length; i++) {
      if (!KEY.test(keys[i])) return null;
      var val = input[keys[i]];
      /* Key-class before value-class: a method-named key admits ONLY the
         read method word, decided before any value branch can consume the
         entry (an anchor-valued method entry must refuse, not certify). */
      if (METHOD_KEY.test(keys[i])) {
        if (typeof val !== 'string' || !LIVE_METHOD_VOCAB.test(val)) return null;
        continue;
      }
      var ownerish = OWNERISH_KEY.test(keys[i]);
      var repoish = REPOISH_KEY.test(keys[i]);
      if (ownerish && repoish) return null;
      if (ownerish) {
        if (val !== anchor.owner) return null;
        hasOwner = true;
        continue;
      }
      if (repoish) {
        if (val !== anchor.repo) return null;
        hasRepo = true;
        continue;
      }
      if (typeof val === 'number') {
        if (val !== anchor.number) return null;
        hasNumber = true;
        continue;
      }
      if (typeof val !== 'string' || !IDENT.test(val)) return null;
      if (val === String(anchor.number)) {
        hasNumber = true;
        continue;
      }
      /* Bidirectional-pin backstop: a method word under a non-method key
         refuses here by name, independent of the terminal refusal — so
         the pin survives any future branch added between them. */
      if (LIVE_METHOD_VOCAB.test(val)) return null;
      return null;
    }
    if (!hasOwner || !hasRepo || !hasNumber) return null;
    return input;
  }

  /* The approve WRITE binding, held to a stricter wall: EVERY value is one of the anchor's
     own identifiers (owner, repo, number, head SHA), an approve vocabulary word, or — under
     exactly the key named method — the create method word selecting the connector's
     create-and-submit operation; a family key pins its entry to exactly its anchor value
     (a number can never be one), an owner or repo value may only ride a key of its own
     family, and the input must name the anchored pull request and carry an explicit
     "approve" value. An input that could target any other pull request, or do anything but
     approve, yields null and the control never arms. */
  function stampInputOf(b) {
    if (!b || typeof b !== 'object' || Array.isArray(b)) return null;
    if (typeof b.tool !== 'string' || !IDENT.test(b.tool)) return null;
    if (!APPROVE_TOOL.test(b.tool) || DESTRUCTIVE_TOOL.test(b.tool)) return null;
    var input = b.input;
    if (!input || typeof input !== 'object' || Array.isArray(input)) return null;
    var keys = Object.keys(input);
    if (keys.length === 0 || keys.length > 8) return null;
    var hasOwner = false;
    var hasRepo = false;
    var hasNumber = false;
    var hasApprove = false;
    for (var i = 0; i < keys.length; i++) {
      if (!KEY.test(keys[i])) return null;
      var val = input[keys[i]];
      /* Key-class before value-class: a method-named key admits ONLY the
         create method word, decided before any value branch can consume
         the entry (an anchor-valued method entry must refuse, not
         certify — and must never satisfy hasNumber). */
      if (METHOD_KEY.test(keys[i])) {
        if (typeof val !== 'string' || !METHOD_VOCAB.test(val)) return null;
        continue;
      }
      var ownerish = OWNERISH_KEY.test(keys[i]);
      var repoish = REPOISH_KEY.test(keys[i]);
      if (ownerish && repoish) return null;
      if (ownerish) {
        if (val !== anchor.owner) return null;
        hasOwner = true;
        continue;
      }
      if (repoish) {
        if (val !== anchor.repo) return null;
        hasRepo = true;
        continue;
      }
      if (typeof val === 'number') {
        if (val !== anchor.number) return null;
        hasNumber = true;
        continue;
      }
      if (typeof val !== 'string' || !IDENT.test(val)) return null;
      if (val === anchor.owner || val === anchor.repo) return null;
      if (val === String(anchor.number)) {
        hasNumber = true;
        continue;
      }
      if (val.toLowerCase() === anchorSha) continue;
      /* Bidirectional-pin backstop: a method word under a non-method key
         refuses here by name, independent of the vocabulary refusal — so
         the pin survives any future branch added between them. */
      if (METHOD_VOCAB.test(val)) return null;
      if (!VOCAB.test(val)) return null;
      if (val.toLowerCase() === 'approve') {
        if (!EVENT_KEY.test(keys[i])) return null;
        hasApprove = true;
      }
    }
    if (!hasOwner || !hasRepo || !hasNumber || !hasApprove) return null;
    return input;
  }

  /* The freshness read's SHA pointer must name a HEAD field: a free pointer
     could be aimed at a stable field (base.sha, merge_commit_sha) with the
     anchor's headSha set to match, silencing the gate forever. */
  function validShaPath(path) {
    if (!validPath(path)) return null;
    var lastSegment = path[path.length - 1];
    if (/^head_?sha$/i.test(lastSegment)) return path;
    if (!/^sha$/i.test(lastSegment)) return null;
    for (var s = 0; s < path.length - 1; s++) {
      if (/^head$/i.test(path[s])) return path;
    }
    return null;
  }

  var liveInput = liveInputOf(live);
  if (!liveInput) return;
  var shaPath = validShaPath(live.shaPath);
  if (!shaPath) return;
  var stampInput = stampInputOf(stamp);
  if (!stampInput) return;
  var statePath = validPath(stamp.statePath);
  if (!statePath) return;
  if (stamp.tool === live.tool) return;

  /* The stale-button coupling observes the banner element; an environment that cannot
     observe it cannot keep the control honest, so stay static. */
  if (typeof MutationObserver !== 'function') return;
  /* A 0.2.x viewer runtime hands the connector surface to claude.use('mcp') and
     answers null when this view cannot run it; a 0.1.x runtime has no use() and
     mounts window.claude.mcp synchronously instead. */
  function mcpApi() {
    var c = window.claude;
    if (!c) return Promise.resolve(null);
    return typeof c.use === 'function' ? c.use('mcp') : Promise.resolve(c.mcp);
  }
  var mcp = null;

  /* Walk a result payload along a key path; the terminal string or null. */
  function walk(payload, path) {
    var cur = payload;
    for (var i = 0; i < path.length; i++) {
      if (!cur || typeof cur !== 'object') return null;
      cur = cur[path[i]];
    }
    return typeof cur === 'string' ? cur : null;
  }

  /* The one exemption to the declared-read requirement: some serving paths
     strip annotations, so exactly the name pull_request_read — a read by
     GitHub's own contract — with the hint ABSENT (a present readOnlyHint
     key of any value still refuses) on a GitHub-presenting server. */
  function isExemptRead(tool, serverName) {
    if (!tool || tool.name !== 'pull_request_read') return false;
    var notes = tool.annotations;
    var absent = notes == null || (typeof notes === 'object' && !Array.isArray(notes) && !('readOnlyHint' in notes));
    if (!absent) return false;
    return typeof serverName === 'string' && /github/i.test(serverName);
  }

  /* Exactly one connector may offer the named tool, with the required wire-declared
     annotation: the read must declare readOnlyHint: true (or fall under the one
     exemption above); the approve tool must not declare itself a read. Ambiguity,
     absence, or a wrong annotation all yield null. The write path carries no exemption. */
  function findServer(servers, toolName, mustBeRead) {
    var found = null;
    var matches = 0;
    for (var s = 0; s < servers.length; s++) {
      var tools = (servers[s] ? servers[s].tools : null) || [];
      for (var t = 0; t < tools.length; t++) {
        var candidate = tools[t];
        if (candidate ? candidate.name === toolName : false) {
          var hints = candidate.annotations;
          var isRead = hints ? hints.readOnlyHint === true : false;
          if (mustBeRead) {
            if (!isRead && !isExemptRead(candidate, servers[s] ? servers[s].server : null)) return null;
          } else if (isRead) {
            return null;
          }
          found = servers[s].server;
          matches++;
          break;
        }
      }
    }
    return matches === 1 && typeof found === 'string' ? found : null;
  }

  var server = null;
  /* state: ready | checking | busy | done | submitted | denied | retry.
     moved latches the first time anything shows the head left the anchor — the banner
     (including a later flicker) or the click-time re-read — and is never cleared. */
  var state = 'ready';
  var note = null;
  var moved = false;

  function show(shown) {
    for (var key in notes) notes[key].hidden = key !== shown;
  }

  function render() {
    if (banner.hidden === false) moved = true;
    var terminal = state === 'done' || state === 'submitted' || state === 'denied';
    var working = state === 'checking' || state === 'busy';
    btn.hidden = terminal;
    btn.disabled = moved || working;
    /* The disclosure rides the actionable button: hidden with it, and hidden once the
       latched stale note has replaced the action. */
    sub.hidden = terminal || moved;
    if (terminal) {
      show(note);
    } else if (working) {
      show(state);
    } else if (moved) {
      show('stale');
    } else if (state === 'retry') {
      show(note);
    } else {
      show(null);
    }
  }

  function settle(newState, newNote) {
    state = newState;
    note = newNote || null;
    render();
  }

  /* McpError code -> [state, note]. Everything on a write is terminal: a rejected write is
     not proof the approval did not land, so it is never re-issued — not automatically and not
     by re-arming the button. Only a failed re-read that could not say the branch is unchanged
     offers a fresh try, because no write was attempted. */
  function classify(code, isWrite) {
    switch (code) {
      case 'needs_reauth':
        return ['denied', 'reauth'];
      case 'not_in_manifest':
        /* On the write this is the one failure that is a PUBLISH bug — the stamp island was
           filled but the approve tool was left out of the capabilities manifest — and its
           remedy (the author republishes) is the opposite of a policy denial's, so it gets
           its own note. */
        return ['denied', isWrite ? 'blocked' : 'unavail'];
      case 'server_not_connected':
      case 'server_not_found':
      case 'selection_required':
      case 'blocked_by_policy':
      case 'approval_required':
      case 'not_granted':
      case 'capability_disabled':
      case 'capability_removed':
      case 'bad_request':
      case 'transform_error':
        return ['denied', 'unavail'];
      case 'tool_error':
        return ['denied', isWrite ? 'refused' : 'unavail'];
      default:
        return isWrite ? ['denied', 'unclear'] : ['retry', 'precheck'];
    }
  }

  btn.addEventListener('click', function () {
    if (!mcp) return;
    if (state !== 'ready' && state !== 'retry') return;
    if (moved || banner.hidden === false) {
      render();
      return;
    }
    settle('checking', null);
    mcp.callTool(server, live.tool, liveInput, { cache: { refresh: true } })
      .then(function (readResult) {
        var sha = walk(readResult ? readResult.payload : undefined, shaPath);
        if (sha === null || !HEX40.test(sha)) {
          settle('retry', 'precheck');
          return;
        }
        if (sha.toLowerCase() !== anchorSha) {
          moved = true;
          settle('ready', null);
          return;
        }
        settle('busy', null);
        return mcp.callTool(server, stamp.tool, stampInput).then(
          function (writeResult) {
            var outcome = walk(writeResult ? writeResult.payload : undefined, statePath);
            if (outcome === 'APPROVED') {
              settle('done', 'done');
            } else {
              settle('submitted', 'submitted');
            }
          },
          function (err) {
            var verdict = classify(err ? err.code : undefined, true);
            settle(verdict[0], verdict[1]);
          }
        );
      }, function (err) {
        var verdict = classify(err ? err.code : undefined, false);
        settle(verdict[0], verdict[1]);
      })
      .catch(function () {
        /* A throw that interrupts the CHECKING phase provably precedes any
           write (busy is set synchronously before the write call), so it
           gets the read-failure treatment: a fresh try, never a hedge
           about an approval that was never attempted. */
        if (state === 'checking') {
          settle('retry', 'precheck');
          return;
        }
        if (state !== 'busy') return;
        settle('denied', 'unclear');
      });
  });

  mcpApi().then(function (got) {
    if (!got || typeof got.listTools !== 'function' || typeof got.callTool !== 'function') return null;
    mcp = got;
    return mcp.listTools();
  }).then(function (res) {
    var servers = (res ? res.servers : null) || [];
    var readServer = findServer(servers, live.tool, true);
    if (readServer === null) return;
    var writeServer = findServer(servers, stamp.tool, false);
    if (writeServer === null || writeServer !== readServer) return;
    /* Name-CLASS pin, not identity: connector display names are the only
       identity at this layer, so this narrows arming to connectors that
       PRESENT as GitHub in the viewer's consent dialog — which is the
       control that actually names what the viewer granted. */
    if (!/github/i.test(writeServer)) return;
    server = writeServer;
    target.textContent = anchor.owner + '/' + anchor.repo + ' #' + String(anchor.number);
    new MutationObserver(function () {
      render();
    }).observe(banner, { attributes: true, attributeFilter: ['hidden'] });
    render();
    box.hidden = false;
  }).catch(function () {
    return;
  });
})();
</script>
