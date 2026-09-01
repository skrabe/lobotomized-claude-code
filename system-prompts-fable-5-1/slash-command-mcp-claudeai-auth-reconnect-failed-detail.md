<!--
name: 'Slash Command: /mcp — reconnect after auth failed, with reason'
description: >-
  Reports that the post-authentication reconnect failed and carries the
  sanitized failure reason so the model can tell the user what went wrong.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_VAR_0
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_VAR_1
-->
Tried reconnecting to ${SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_VAR_0(SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_VAR_1.name)}, but the connection failed: ${SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_DETAIL_VAR_2}
