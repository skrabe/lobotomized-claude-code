<!--
name: 'Slash Command: /mcp — OAuth reconnect failed, detail withheld'
description: >-
  Result after MCP OAuth got new credentials but reconnect failed on a
  connection whose detail is withheld; suggests restarting Claude Code.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_0
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_1
  - SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_2
-->
Got new credentials, but couldn't reconnect to ${SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_0(SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_1.name)}${SLASH_COMMAND_MCP_OAUTH_RECONNECT_FAILED_RESTART_OPAQUE_VAR_2?" (detail withheld on this connection)":""}. Restart Claude Code to try again.
