<!--
name: 'MCP connect status: disabled'
description: MCP-connect tool_result line listing disabled servers.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_MCP_CONNECT_DISABLED_VAR_0
-->
Disabled (ask the user to enable via /mcp): ${TOOL_RESULT_MCP_CONNECT_DISABLED_VAR_0.disabled.join(", ")}
