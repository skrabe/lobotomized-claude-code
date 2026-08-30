<!--
name: 'Slash Command: /mcp enable|disable — server is pending approval'
description: >-
  Tells the model the server cannot be toggled until the user approves it via
  /mcp, naming the blocking step rather than a generic failure.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_TOGGLE_PENDING_APPROVAL_VAR_0
-->
MCP server "${SLASH_COMMAND_MCP_TOGGLE_PENDING_APPROVAL_VAR_0(SLASH_COMMAND_MCP_TOGGLE_PENDING_APPROVAL_VAR_1)}" is pending approval — approve it via /mcp first
