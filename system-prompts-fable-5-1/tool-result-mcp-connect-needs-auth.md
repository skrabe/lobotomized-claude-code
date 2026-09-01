<!--
name: 'MCP connect status: needs auth'
description: MCP-connect tool_result line listing servers needing authentication.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_MCP_CONNECT_NEEDS_AUTH_VAR_0
-->
Needs authentication (ask the user to run /mcp): ${TOOL_RESULT_MCP_CONNECT_NEEDS_AUTH_VAR_0.needsAuth.join(", ")}
