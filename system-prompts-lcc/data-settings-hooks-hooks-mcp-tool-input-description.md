<!--
name: 'Data: hooks.hooks.(mcp_tool).input setting description'
description: >-
  Description of the `hooks.hooks.(mcp_tool).input` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Arguments passed to the MCP tool. String values support ${path} interpolation from the hook input JSON (e.g. "${tool_input.file_path}").
