<!--
name: 'Tool Result: MCP resource server not found'
description: MCP resource tool error naming an unknown server and listing available ones.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_MCP_RESOURCE_SERVER_NOT_FOUND_VAR_0
  - TOOL_RESULT_MCP_RESOURCE_SERVER_NOT_FOUND_VAR_1
  - TOOL_RESULT_MCP_RESOURCE_SERVER_NOT_FOUND_VAR_2
-->
Server "${TOOL_RESULT_MCP_RESOURCE_SERVER_NOT_FOUND_VAR_0}" not found. Available servers: ${TOOL_RESULT_MCP_RESOURCE_SERVER_NOT_FOUND_VAR_1.map((TOOL_RESULT_MCP_RESOURCE_SERVER_NOT_FOUND_VAR_2)=>TOOL_RESULT_MCP_RESOURCE_SERVER_NOT_FOUND_VAR_2.name).join(", ")}
