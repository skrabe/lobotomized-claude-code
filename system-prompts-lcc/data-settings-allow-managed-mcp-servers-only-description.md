<!--
name: 'Data: allowManagedMcpServersOnly setting description'
description: >-
  Description of the `allowManagedMcpServersOnly` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.328
-->
When true (and set in managed settings), allowedMcpServers is only read from managed settings. deniedMcpServers still merges from all sources, so users can deny servers for themselves, in user settings for a server the organization provides. Users can still add their own MCP servers, but only the admin-defined allowlist applies.
