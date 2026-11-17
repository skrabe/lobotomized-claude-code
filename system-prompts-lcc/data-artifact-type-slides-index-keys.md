<!--
name: 'Data: Artifact type slides index keys'
description: Lists the keys of a slides artifact's deck.json index
ccVersion: 2.1.326
-->
`"v": 5`, `"lists": "css"`, `"format": {"v": 1, "shared": ["project/deck.css"]}` (a deck that already has slides keeps its `v` and gains neither `lists` nor `format`; an index that gains `format` is published in one call with `project/deck.css`), `title`, `order`: the slide ids in deck order, `sections`: the outline (an id → `{"description", "start": <slide id>}`), and `faces`: one entry per typeface, keyed by family-id (`{"family"}` plus a Google Fonts `href` or an uploaded `src`)
