<!--
name: 'Slash Command: /mcp Reconnect Failed Detail Withheld'
description: >-
  Reconnect-failed /mcp result (claude.ai connector auth panel) that withholds
  the failure detail on connections that persist off-box and tells the model to
  restart Claude Code to try again.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_0
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_1
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_2
-->
Couldn't reconnect to ${SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_0(SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_1.name)}${SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_WITHHELD_VAR_2?" (detail withheld on this connection)":""}. Restart Claude Code to try again.
