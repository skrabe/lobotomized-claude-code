<!--
name: 'Data: blockedMarketplaces setting description'
description: >-
  Description of the `blockedMarketplaces` setting in Claude Code's settings
  JSON schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.325
-->
Enterprise blocklist of marketplace sources. When set in managed settings, these sources are blocked from being added as marketplaces. Entries match exactly, except that a github entry may use the owner-wildcard form {"source":"github","repo":"owner/*"} to block every repository under that owner, and an entry naming a branch or tag in `ref` also blocks every full commit id in that repository. The check happens BEFORE downloading, so blocked sources never touch the filesystem.
