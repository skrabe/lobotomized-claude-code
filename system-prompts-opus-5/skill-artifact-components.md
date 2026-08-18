<!--
name: 'Skill: artifact-components'
description: >-
  Bundled artifact-components skill — Embed reusable artifact components in any
  HTML artifact — first entry: the workshop decision component (clickable option
  rows backed by a machine-readable record the session reads back). Use when a
  non-workshop artifact should carry decisions the reader answers from the
  published page, or to look up a component's exact scripts, styles, markup
  contract, and compo
ccVersion: 2.1.234
-->
---
name: artifact-components
description: "Embed reusable artifact components in any HTML artifact — first entry: the workshop decision component (clickable option rows backed by a machine-readable record the session reads back). Use when a non-workshop artifact should carry decisions the reader answers from the published page, or to look up a component's exact scripts, styles, markup contract, and composition limits."
---

Catalog of components an HTML artifact can embed. Each entry ships the exact
bytes the publish verifier holds a carrying page to: fixed scripts, carved
styles, and a markup skeleton with its invariants stated at each slot.

**Composition limits (today)** — two independent constraints:

1. **Script pinning under the workshop record name.** A page carrying the
   ws-decisions island is held to full workshop-page rules: every executable
   script must hash-match the blessed set, so any custom script — including a
   custom element implementing this same component — refuses as
   \`script-not-blessed\` (and a non-workshop island schema under that id
   refuses as \`island-grammar\`).
2. **One JSON island per such page.** The verifier admits exactly one JSON
   script element — the ws-decisions island — and refuses any other as
   \`unknown-data-island\`, even when the other component's executable scripts
   are individually blessed (a decision page plus a chart-spec island refuses
   on the island, not the scripts).

**The escape hatch and its cost**: a component using its OWN island id (not
the workshop's) publishes in the ordinary author-HTML lane, where custom
scripts are allowed and neither constraint applies — but the session's
\`read_page_data\` workshop-decisions schema does not read such an island, so
decisions recorded there need their own read-back path. A script in that
lane that writes reader-typed text into its island must never splice the
raw string: \`</\` inside a JSON string value ends the script element and
executes what follows for every later viewer. Encode free text (the pinned
decisions script stores it as canonical base64) or refuse the write when
the serialized island contains \`<\`, \`>\`, \`&\`, \`'\`, or a backslash, as the
pinned script does.

## Decision component (from the workshop skill)

Option rows the reader clicks on the published page; picks accumulate in a
sticky footer whose single Confirm republishes the page with the choices
recorded in the ws-decisions island; the session reads them back with the
Artifact tool's \`read_page_data\` action (schema \`workshop-decisions\`).

Files in this skill's \`decision/\` directory:

- \`skeleton.html\` — fill-in markup for one decision plus its island entry,
  invariants noted per slot. Start here.
- \`theme-script.html\` and \`decisions-script.html\` — the two fixed script
  elements, copied byte-identical from the workshop-page template. The
  publish allowlist admits inline scripts by sha256 of the script element's
  text content; the shipped blocks hash to
  \`cc92acd07b10a4a892834a8661cb4a69a299224a830e01b1e68f2b29c1c0c15b\` (theme) and
  \`08eafa73e8186c16026df60706aee612fc18689696a638759098aaa70834379d\` (decisions).
  Never edit, reindent, or reformat them — any byte difference refuses as
  \`script-not-blessed\`. The publish verifier's blessed set is the source of
  truth for these hashes; the literals here are documentation, held to the
  template by this skill's pin tests.
- \`component.css\` — the component's presentation rules, carved verbatim from
  the workshop-page template. Requires these CDS custom properties (embed
  \`tokens.css\` below, or define them yourself): \`--border\`,
  \`--border-strong\`, \`--border-stronger\`, \`--fill-accent\`,
  \`--fill-control\`, \`--gap-md\`, \`--gap-sm\`, \`--gap-xs\`, \`--page-bg\`,
  \`--radius\`, \`--shadow-sm\`, \`--surface-0\`, \`--text-accent\`,
  \`--text-primary\`, \`--text-secondary\`.
- \`tokens.css\` — the template's vendored CDS token block (defines all of
  the above plus the palette and dark-mode overrides they reference),
  carved verbatim and drift-pinned like the scripts. Embed once, before
  \`component.css\`.

## How to embed

1. Read the files above from this skill's base directory.
2. Build the page: \`theme-script.html\` early in the head, right after
   \`<title>\` (it mirrors the stored theme to \`data-mode\` before first
   paint — the template ships it there); \`tokens.css\` then \`component.css\`
   with your own styles; one filled \`skeleton.html\` block per decision; the
   island (one per page, entries in lockstep with the markup); then
   \`decisions-script.html\`, unmodified, last.
3. Publish with \`capabilities: {"artifact": {}}\` so readers can decide from the
   page. Without it the page still publishes and renders; rows stay inert
   with an explanatory tooltip.
4. Read decisions back with \`read_page_data\`; apply them and republish.

Rules that bite when hand-assembling:
full workshop-page rules refuse \`<link>\`, \`<form>\`, \`<iframe>\`,
\`<object>\`, \`<embed>\`, \`<base>\`, \`<noscript>\`, \`<frameset>\`/\`<frame>\`,
every \`on*\` event-handler attribute, \`ping\` and \`referrerpolicy\`
attributes, an \`opener\` token in \`rel\`, and anchor \`target\`s other than
\`_blank\`/\`_self\` — a retrofitted host page gives those features up;
the island's \`id\` attribute spelling may appear nowhere else in the page
bytes, prose included (refuses as \`island-sentinel-ambiguity\`); a banner
element carrying \`data-ws-state\` must match the island-derived state — any
open decision derives \`in-progress\` (refuses as \`banner-state-mismatch\`);
the decision id
\`get-started\` is reserved for the kickoff block, never an ordinary
decision — largely unenforced at publish; a misused one renders wrong;
option-row CLASSES (\`option\`, \`option-label\`, \`badge\`, \`why\`,
\`custom-answer\`, \`option-input\`) are not verifier-checked but the decisions
script and CSS key on them — drift breaks the UI silently, so copy the
skeleton rather than retype it. \`component.css\`'s selectors are not scoped
to the component: generic class names it styles page-wide (\`option\`,
\`options\`, \`call-item\`, \`call-body\`, \`custom-answer\`, \`option-input\`,
\`confirm-btn\`, \`clear-btn\`, \`confirm-hint\`, \`footer-note\`, \`note-live\`)
are reserved — a host page reusing one for its own elements gets silently
restyled. The sticky footer's left padding assumes a centered 76ch content
column (the workshop layout); in a host page with a different column the
Confirm button still works but won't align with the content.
