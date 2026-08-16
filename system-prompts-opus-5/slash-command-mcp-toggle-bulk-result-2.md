<!--
name: 'Slash Command: /mcp enable|disable all — bulk result'
description: >-
  Reports how many MCP servers were enabled or disabled, how many could not be
  changed, and how to inspect the rest, so the model knows the toggle only
  partly landed.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_0
  - SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_1
-->
${SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_0?"Enabled":"Disabled"} ${SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_1} MCP server(s)
