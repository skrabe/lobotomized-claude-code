<!--
name: Artifact Type Slides Index Keys
description: >-
  Required keys of project/deck.json (v, title, order, sections, faces) for a
  slides Artifact kept as files.
ccVersion: 2.1.273
-->
`"v": 4`, `title`, `order`: the slide ids in deck order, `sections`: the outline (an id → `{"description", "start": <slide id>}`), and `faces`: one entry per typeface, keyed by family-id (`{"family"}` plus a Google Fonts `href` or an uploaded `src`)
