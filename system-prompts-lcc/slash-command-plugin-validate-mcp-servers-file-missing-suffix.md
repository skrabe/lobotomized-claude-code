<!--
name: 'Plugin Validate: MCP Servers File Missing Suffix'
description: >-
  Suffix on the plugin-validate 'Path not found' error for an mcpServers .json
  file, noting the loader silently skips a missing file so none of its servers
  load.
ccVersion: 2.1.281
-->
The plugin loader skips a missing MCP servers file without reporting it, so none of its servers will load.
