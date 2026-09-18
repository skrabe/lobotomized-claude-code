<!--
name: >-
  Data: extraKnownMarketplaces.source.(github).repo setting description (part 2
  of 2)
description: >-
  Description of the `extraKnownMarketplaces.source.(github).repo` setting in
  Claude Code's settings JSON schema. The model reads it through /update-config
  and settings validation errors; it is also shown to users in the settings
  help.
ccVersion: 2.1.276
-->
must name a single repository — a wildcard is taken literally and fails to clone.
