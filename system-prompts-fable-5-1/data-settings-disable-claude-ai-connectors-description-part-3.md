<!--
name: 'Data: disableClaudeAiConnectors setting description (part 3 of 3)'
description: >-
  Description of the `disableClaudeAiConnectors` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
(e.g. via --mcp-config or the SDK mcpServers option) still follows the normal MCP config trust flow. Any-source-true wins: a project can opt out, but a project-level false cannot override a user-level true.
