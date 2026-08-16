<!--
name: 'Slash Command: /mcp — agent server authenticated, connects on next run'
description: >-
  Tells the model the agent-scoped MCP server is authenticated but deliberately
  stays unconnected until the agent runs, so it does not treat the absent tools
  as a failure.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MCP_AGENT_SERVER_AUTH_SUCCESS_VAR_0
-->
Authentication successful for ${SLASH_COMMAND_MCP_AGENT_SERVER_AUTH_SUCCESS_VAR_0.name}. The server will connect when the agent runs.
