<!--
name: 'Slash Command: /mcp — stored authentication cleared'
description: >-
  Tells the model the server's stored OAuth tokens were revoked and cleared, so
  the server now needs authentication before its tools work again.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_AUTH_CLEARED_VAR_0
  - SLASH_COMMAND_MCP_AUTH_CLEARED_VAR_1
-->
Authentication cleared for ${SLASH_COMMAND_MCP_AUTH_CLEARED_VAR_0(SLASH_COMMAND_MCP_AUTH_CLEARED_VAR_1.name)}.
