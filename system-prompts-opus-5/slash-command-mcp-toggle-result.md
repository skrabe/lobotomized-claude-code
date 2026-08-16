<!--
name: 'Slash Command: /mcp enable|disable — server toggled'
description: >-
  Confirms the named server was actually enabled or disabled, which tells the
  model whether that server's tools are now in play.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MCP_TOGGLE_RESULT_VAR_0
  - SLASH_COMMAND_MCP_TOGGLE_RESULT_VAR_1
-->
MCP server "${SLASH_COMMAND_MCP_TOGGLE_RESULT_VAR_0}" ${SLASH_COMMAND_MCP_TOGGLE_RESULT_VAR_1?"enabled":"disabled"}
