<!--
name: 'Data: extraKnownMarketplaces.source.sparsePaths setting description'
description: >-
  Description of the `extraKnownMarketplaces.source.sparsePaths` setting in
  Claude Code's settings JSON schema. The model reads it through /update-config
  and settings validation errors; it is also shown to users in the settings
  help.
ccVersion: 2.1.276
-->
Directories to include via git sparse-checkout (cone mode). Use for monorepos where the marketplace lives in a subdirectory. Example: [".claude-plugin", "plugins"]. If omitted, the full repository is cloned.
