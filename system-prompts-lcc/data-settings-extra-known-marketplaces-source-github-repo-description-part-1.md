<!--
name: >-
  Data: extraKnownMarketplaces.source.(github).repo setting description (part 1
  of 2)
description: >-
  Description of the `extraKnownMarketplaces.source.(github).repo` setting in
  Claude Code's settings JSON schema. The model reads it through /update-config
  and settings validation errors; it is also shown to users in the settings
  help.
ccVersion: 2.1.276
-->
GitHub repository in owner/repo format. ONLY in the managed-settings policy lists (strictKnownMarketplaces / blockedMarketplaces) the owner-wildcard form "owner/*" matches every repository under exactly that owner. Everywhere else (marketplace add, extraKnownMarketplaces, known_marketplaces.json) the value 
