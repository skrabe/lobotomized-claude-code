<!--
name: 'Slash Command: /mcp Reconnect Failed Detail Withheld'
description: >-
  Reconnect-failed /mcp result that withholds the failure detail on connections
  that persist off-box and tells the model to restart.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_0
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_1
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_2
-->
Tried reconnecting to ${SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_0(SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_1.name)}, but the connection failed${SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_2?" (detail withheld on this connection)":""}. Restart Claude Code to retry.
