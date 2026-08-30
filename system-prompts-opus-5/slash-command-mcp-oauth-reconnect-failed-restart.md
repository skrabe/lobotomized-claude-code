<!--
name: 'Slash Command: MCP OAuth reconnect failed restart'
description: >-
  OnComplete message after MCP OAuth succeeded but reconnecting to the server
  failed, asking to restart Claude Code.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_VAR_0
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_VAR_1
-->
Got new credentials, but reconnecting to ${SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_VAR_0(SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_VAR_1.name)} failed. Restart Claude Code to retry.
