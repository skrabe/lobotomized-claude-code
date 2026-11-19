<!--
name: 'Slash Command: /mcp — claude.ai auth still not signed in'
description: >-
  Result when the server still needs auth after the claude.ai flow; tells the
  model the browser sign-in must finish before retrying from /mcp.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_STILL_UNAUTHORIZED_VAR_0
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_STILL_UNAUTHORIZED_VAR_1
-->
Still not signed in to ${SLASH_COMMAND_MCP_CLAUDEAI_AUTH_STILL_UNAUTHORIZED_VAR_0(SLASH_COMMAND_MCP_CLAUDEAI_AUTH_STILL_UNAUTHORIZED_VAR_1.name)}. Finish signing in with your browser, then try again from /mcp.
