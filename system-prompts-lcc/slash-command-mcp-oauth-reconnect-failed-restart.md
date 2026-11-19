<!--
name: 'Slash Command: /mcp — OAuth reconnect failed, restart'
description: >-
  Result after MCP OAuth got new credentials but reconnecting failed with no
  detail; suggests restarting Claude Code.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_VAR_0
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_VAR_1
-->
Got new credentials, but couldn't reconnect to ${SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_VAR_0(SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_VAR_1.name)}. Restart Claude Code to try again.
