<!--
name: 'Slash Command: /mcp — agent server authenticated, connects on next run'
description: >-
  Tells the model the agent-scoped MCP server is authenticated but deliberately
  stays unconnected until the agent runs, so it does not treat the absent tools
  as a failure.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_AGENT_SERVER_AUTH_SUCCESS_VAR_0
-->
Authentication successful for ${SLASH_COMMAND_MCP_AGENT_SERVER_AUTH_SUCCESS_VAR_0(SLASH_COMMAND_MCP_AGENT_SERVER_AUTH_SUCCESS_VAR_1.name)}. The server will connect when the agent runs.
