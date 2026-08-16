<!--
name: 'Slash Command: /mcp enable|disable — server already in that state'
description: >-
  Tells the model the single named server was already enabled/disabled, so
  nothing changed.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MCP_TOGGLE_ALREADY_IN_STATE_VAR_0
  - SLASH_COMMAND_MCP_TOGGLE_ALREADY_IN_STATE_VAR_1
-->
MCP server "${SLASH_COMMAND_MCP_TOGGLE_ALREADY_IN_STATE_VAR_0}" is already ${SLASH_COMMAND_MCP_TOGGLE_ALREADY_IN_STATE_VAR_1?"enabled":"disabled"}
