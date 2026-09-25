<!--
name: 'Tool result: MCP connect disabled for this project'
description: >-
  MCP connect status line listing servers disabled for this project and how the
  user can re-enable them via /mcp.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_MCP_CONNECT_DISABLED_FOR_PROJECT_VAR_0
-->
Disabled for this project (the user can turn these servers back on by running /mcp in this project, in a terminal where this session runs): ${TOOL_RESULT_MCP_CONNECT_DISABLED_FOR_PROJECT_VAR_0.disabled.join(", ")}
