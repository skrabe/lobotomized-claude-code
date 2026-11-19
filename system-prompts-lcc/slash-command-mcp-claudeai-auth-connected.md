<!--
name: 'Slash Command: /mcp — signed in and connected'
description: >-
  Confirms the named MCP server is authenticated and connected (claude.ai auth
  and OAuth flows), so the model can use its tools.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_CONNECTED_VAR_0
  - SLASH_COMMAND_MCP_CLAUDEAI_AUTH_CONNECTED_VAR_1
-->
Signed in and connected to ${SLASH_COMMAND_MCP_CLAUDEAI_AUTH_CONNECTED_VAR_0(SLASH_COMMAND_MCP_CLAUDEAI_AUTH_CONNECTED_VAR_1.name)}.
