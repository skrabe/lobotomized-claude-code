<!--
name: 'Slash Command: /mcp enable|disable all — nothing to change'
description: >-
  Tells the model every configured MCP server is already on/off as requested, so
  the /mcp enable|disable all command was a no-op and no retry is needed.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_MCP_TOGGLE_ALL_ALREADY_IN_STATE_VAR_0
-->
All MCP servers are already ${SLASH_COMMAND_MCP_TOGGLE_ALL_ALREADY_IN_STATE_VAR_0?"on":"off"}
