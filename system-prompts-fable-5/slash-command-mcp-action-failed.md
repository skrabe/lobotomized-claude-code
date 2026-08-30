<!--
name: MCP Action Failed Result
description: >-
  Generic /mcp failure result naming the attempted action, the server, and the
  underlying error, returned when an enable/disable/reconnect promise rejects.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_ACTION_FAILED_VAR_0
  - SLASH_COMMAND_MCP_ACTION_FAILED_VAR_1
  - SLASH_COMMAND_MCP_ACTION_FAILED_VAR_2
  - SLASH_COMMAND_MCP_ACTION_FAILED_VAR_3
  - SLASH_COMMAND_MCP_ACTION_FAILED_VAR_4
-->
Couldn't ${SLASH_COMMAND_MCP_ACTION_FAILED_VAR_0} "${SLASH_COMMAND_MCP_ACTION_FAILED_VAR_1(SLASH_COMMAND_MCP_ACTION_FAILED_VAR_2)}" — ${SLASH_COMMAND_MCP_ACTION_FAILED_VAR_3(SLASH_COMMAND_MCP_ACTION_FAILED_VAR_4(SLASH_COMMAND_MCP_ACTION_FAILED_VAR_5))}. Run \`/mcp\` in the terminal to check.
