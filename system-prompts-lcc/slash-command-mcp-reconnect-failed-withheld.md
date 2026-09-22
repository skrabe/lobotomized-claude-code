<!--
name: 'Slash Command: MCP Reconnect Failed Withheld'
description: >-
  Off-box /mcp reconnect failure result with optional withheld-detail suffix;
  returned via local-jsx onComplete.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_RECONNECT_FAILED_WITHHELD_VAR_0
  - SLASH_COMMAND_MCP_RECONNECT_FAILED_WITHHELD_VAR_1
  - SLASH_COMMAND_MCP_RECONNECT_FAILED_WITHHELD_VAR_2
-->
Failed to reconnect to ${SLASH_COMMAND_MCP_RECONNECT_FAILED_WITHHELD_VAR_0(SLASH_COMMAND_MCP_RECONNECT_FAILED_WITHHELD_VAR_1)}${SLASH_COMMAND_MCP_RECONNECT_FAILED_WITHHELD_VAR_2?" (detail withheld on this connection)":""}.
