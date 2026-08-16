<!--
name: 'Slash Command: /mcp — reconnect failed after OAuth, with reason'
description: >-
  Reports that authentication succeeded but the reconnect failed, carrying the
  sanitized reason so the model can distinguish an auth problem from a transport
  problem.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_DETAIL_VAR_0
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_DETAIL_VAR_1
-->
Got new credentials, but reconnecting to ${SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_DETAIL_VAR_0.name} failed: ${SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_DETAIL_VAR_1}
