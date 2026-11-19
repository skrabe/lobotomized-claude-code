<!--
name: /mcp bulk enable/disable count
description: >-
  Head of the bulk /mcp enable|disable result giving how many servers were
  toggled.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_MCP_TOGGLE_BULK_COUNT_VAR_0
  - SLASH_COMMAND_MCP_TOGGLE_BULK_COUNT_VAR_1
  - SLASH_COMMAND_MCP_TOGGLE_BULK_COUNT_VAR_2
-->
${SLASH_COMMAND_MCP_TOGGLE_BULK_COUNT_VAR_0?"Turned on":"Turned off"} ${SLASH_COMMAND_MCP_TOGGLE_BULK_COUNT_VAR_1} MCP ${SLASH_COMMAND_MCP_TOGGLE_BULK_COUNT_VAR_2(SLASH_COMMAND_MCP_TOGGLE_BULK_COUNT_VAR_1,"server")}
