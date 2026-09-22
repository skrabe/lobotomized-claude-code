<!--
name: 'Tool Description: Artifact Page Contract If Written Before Skill Load'
description: >-
  Inline page-contract fallback (title, color tokens, dark mode, CDN allowlist,
  phone layout) that still applies if Claude writes a page before the design
  skill has loaded.
ccVersion: 2.1.269
-->
**If Claude writes a page before that skill has loaded**, the skill's contract still applies. Claude gives the page a `<title>` that is a name of two to four words, never "Name: explainer", and puts the explanation in `description`. Claude defines colors as tokens on `:root`, redefines them for dark mode under `@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])` and again under `:root[data-theme="dark"]`, and gives `body` an explicit background. Claude loads external scripts only from cdnjs.cloudflare.com or cdn.jsdelivr.net/npm/ (the skill has the full list) and stylesheets only from Google Fonts, and puts everything else inline. Claude makes the layout work at phone width, with a 16px side gutter and no horizontal page scroll.
