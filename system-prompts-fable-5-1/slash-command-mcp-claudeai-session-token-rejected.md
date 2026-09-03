<!--
name: 'Slash Command: /mcp Reconnect Session Token Rejected'
description: >-
  Tells the model a claude.ai reconnect succeeded but the session token was
  rejected, so /login is required before reconnecting.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_CLAUDEAI_SESSION_TOKEN_REJECTED_VAR_0
  - SLASH_COMMAND_MCP_CLAUDEAI_SESSION_TOKEN_REJECTED_VAR_1
-->
Reconnected to ${SLASH_COMMAND_MCP_CLAUDEAI_SESSION_TOKEN_REJECTED_VAR_0(SLASH_COMMAND_MCP_CLAUDEAI_SESSION_TOKEN_REJECTED_VAR_1)}, but your claude.ai session token was rejected. Run /login, then reconnect.
