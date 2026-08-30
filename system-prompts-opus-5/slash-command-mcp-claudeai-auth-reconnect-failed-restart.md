<!--
name: 'Slash Command: /mcp — reconnect after auth failed, restart to retry'
description: >-
  Sibling branch when no reason is available: tells the model the only remaining
  recovery is restarting Claude Code.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_RESTART_VAR_0
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_RESTART_VAR_1
-->
Tried reconnecting to ${SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_RESTART_VAR_0(SLASH_COMMAND_MCP_CLAUDEAI_AUTH_RECONNECT_FAILED_RESTART_VAR_1.name)}, but the connection failed. Restart Claude Code to retry.
