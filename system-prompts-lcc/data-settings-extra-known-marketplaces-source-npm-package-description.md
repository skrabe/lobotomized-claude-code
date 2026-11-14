<!--
name: 'Data: extraKnownMarketplaces.source.(npm).package setting description'
description: >-
  Description of the `extraKnownMarketplaces.source.(npm).package` setting in
  Claude Code's settings JSON schema. The model reads it through /update-config
  and settings validation errors; it is also shown to users in the settings
  help.
ccVersion: 2.1.325
-->
npm package containing marketplace.json (e.g. "@acme/claude-marketplace"). A scope wildcard such as "@acme/*" still parses in a managed list, so a list that holds one stays valid, but it matches no marketplace package.
