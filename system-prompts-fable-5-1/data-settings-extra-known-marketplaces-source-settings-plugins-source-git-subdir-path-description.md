<!--
name: >-
  Data:
  extraKnownMarketplaces.source.(settings).plugins.source.(git-subdir).path
  setting description
description: >-
  Description of the
  `extraKnownMarketplaces.source.(settings).plugins.source.(git-subdir).path`
  setting in Claude Code's settings JSON schema. The model reads it through
  /update-config and settings validation errors; it is also shown to users in
  the settings help.
ccVersion: 2.1.276
-->
Subdirectory within the repo containing the plugin (e.g., "tools/claude-plugin"). Cloned sparsely using partial clone (--filter=tree:0) to minimize bandwidth for monorepos.
