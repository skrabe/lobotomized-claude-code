<!--
name: 'Data: extraKnownMarketplaces.source.ref setting description'
description: >-
  Description of the `extraKnownMarketplaces.source.ref` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.325
-->
Git branch, tag or full commit id to use (e.g., "main", "v1.0.0"). Defaults to repository default branch. A full commit id (40 or 64 lowercase hex digits) holds the marketplace at that commit: refreshes and auto-updates do not move it. A branch or tag of the repository must hold the commit. Plugins listed with a remote source follow that source unless they name a `sha`. Reserved Anthropic marketplace names do not accept a commit id.
