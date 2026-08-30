<!--
name: 'Slash Command: MCP OAuth reconnect failed restart opaque'
description: >-
  OnComplete message after MCP OAuth reconnect failed when detail is withheld on
  this connection.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_0
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_1
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_2
-->
Got new credentials, but reconnecting to ${SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_0(SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_1.name)} failed${SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_2?" (detail withheld on this connection)":""}. Restart Claude Code to retry.
