<!--
name: 'Slash Command: /mcp — still unauthorized after reconnect'
description: >-
  Tells the model the browser sign-in did not take effect and that the user must
  complete it before retrying from /mcp, so it stops assuming the server is
  usable.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_STILL_UNAUTHORIZED_VAR_0
-->
Tried reconnecting, but ${SLASH_COMMAND_MCP_CLAUDEAI_AUTH_STILL_UNAUTHORIZED_VAR_0(SLASH_COMMAND_MCP_CLAUDEAI_AUTH_STILL_UNAUTHORIZED_VAR_1.name)} is still unauthorized. Make sure the browser sign-in completed, then try again from /mcp.
