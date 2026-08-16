<!--
name: 'Slash Command: /mcp — enable/disable threw an error'
description: >-
  Reports that enabling or disabling a named MCP server failed with an exception
  and carries the sanitized reason, so the model does not treat the toggle as
  applied.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MCP_TOGGLE_THREW_VAR_0
  - SLASH_COMMAND_MCP_TOGGLE_THREW_VAR_1
  - SLASH_COMMAND_MCP_TOGGLE_THREW_VAR_2
  - SLASH_COMMAND_MCP_TOGGLE_THREW_VAR_3
  - SLASH_COMMAND_MCP_TOGGLE_THREW_VAR_4
-->
Failed to ${SLASH_COMMAND_MCP_TOGGLE_THREW_VAR_0} MCP server '${SLASH_COMMAND_MCP_TOGGLE_THREW_VAR_1}': ${SLASH_COMMAND_MCP_TOGGLE_THREW_VAR_2(SLASH_COMMAND_MCP_TOGGLE_THREW_VAR_3(SLASH_COMMAND_MCP_TOGGLE_THREW_VAR_4))}
