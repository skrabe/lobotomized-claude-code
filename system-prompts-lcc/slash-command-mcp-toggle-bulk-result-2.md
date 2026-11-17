<!--
name: 'Slash Command: /mcp enable|disable all — bulk result'
description: >-
  Reports how many MCP servers were enabled or disabled, how many could not be
  changed, and how to inspect the rest, so the model knows the toggle only
  partly landed.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_0
  - SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_1
  - SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_2
  - SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_3
-->
${SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_0} ${SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_1} MCP ${SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_2(SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_1,"server")}${SLASH_COMMAND_MCP_TOGGLE_BULK_RESULT_2_VAR_3}
