<!--
name: 'Data: Artifact decision component HTML skeleton'
description: >-
  Provides the canonical HTML and JSON-island skeleton for embedding one
  reusable Artifact decision block
ccVersion: 2.1.232
-->
<!-- Decision-component skeleton: one complete, valid decision block plus its
     island entry. Replace the sample values (ids, labels, question, why)
     and delete these instruction comments before publishing.
     Invariants the publish verifier enforces are noted at each slot. -->

<!-- One .call-item per decision. data-decision-id: slug grammar
     [a-z0-9][a-z0-9-]{0,63}, unique, exactly one element per island entry;
     never the reserved kickoff id (get-started). data-decision-state must
     equal the island entry's state. data-lean-choice must be one of the
     entry's opts; put its row first with the Recommended badge (markdown-lane
     convention — not verifier-checked, but keeps the lanes uniform). -->
<div class="call-item" data-decision-id="sample-decision" data-decision-state="open" data-lean-choice="option-a">
  <span class="marker" aria-hidden="true">●</span>
  <div class="call-body">
    <p><span class="q">Which option should we pick?</span></p>
    <div class="options">
      <!-- Exactly one .option row per island opts token, no extras (orphan or
           forged rows refuse). Rows ship inert (aria-disabled + title); the
           decisions script arms them only under the artifact viewer when the
           publish declared the artifact-publish capability. -->
      <span class="option recommended" role="button" aria-disabled="true" title="Deciding from the page needs this Artifact to be able to update itself" data-choice="option-a"><span class="option-label">Option A</span><span class="badge">Recommended</span><span class="why">one short reason</span></span>
      <span class="option" role="button" aria-disabled="true" title="Deciding from the page needs this Artifact to be able to update itself" data-choice="option-b"><span class="option-label">Option B</span></span>
      <!-- Optional typed-answer row (free-text answers; 280 chars max). -->
      <div class="custom-answer"><input class="option-input" type="text" maxlength="280" disabled aria-disabled="true" title="Deciding from the page needs this Artifact to be able to update itself" placeholder="Or type your own answer…" aria-label="Your own answer"></div>
    </div>
  </div>
</div>

<!-- The machine-readable record — exactly ONE such JSON script per page, after
     the content. Spelling is pinned: keep the id attribute double-quoted and
     LAST in the open tag, close tag lowercase, and never repeat the id
     attribute's spelling anywhere else in the page bytes (prose included).
     Entries: exactly {id, opts, state, choice, custom}; open entries carry
     choice:null and custom:null; opts in lockstep with the data-choice rows. -->
<script type="application/json" id="ws-decisions">{"items":[{"id":"sample-decision","opts":["option-a","option-b"],"state":"open","choice":null,"custom":null}]}</script>

<!-- decisions-script.html goes after the island, last. theme-script.html
     belongs early in the head, right after <title>, as the workshop-page
     template ships it (theme before first paint). Both copied
     byte-identical (sha256-pinned — see SKILL.md); any edit, reindent, or
     reformat refuses the publish. -->
