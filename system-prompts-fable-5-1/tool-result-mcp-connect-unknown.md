<!--
name: 'MCP connect status: unknown'
description: MCP-connect tool_result line listing unknown/unconfigured servers.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_MCP_CONNECT_UNKNOWN_VAR_0
-->
Unknown (no MCP server with this name is configured): ${TOOL_RESULT_MCP_CONNECT_UNKNOWN_VAR_0.unknown.join(", ")}
