<!--
name: 'Tool Result: MCP Server Not Connected'
description: >-
  Thrown TelemetrySafeError from Owi/oEi when an MCP dial does not reach
  type:"connected", returned as the MCP tool error the model reads.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_MCP_CONNECT_NOT_CONNECTED_VAR_0
  - TOOL_RESULT_MCP_CONNECT_NOT_CONNECTED_VAR_1
  - TOOL_RESULT_MCP_CONNECT_NOT_CONNECTED_VAR_2
  - TOOL_RESULT_MCP_CONNECT_NOT_CONNECTED_VAR_3
-->
MCP server "${TOOL_RESULT_MCP_CONNECT_NOT_CONNECTED_VAR_0.name}" is not connected${TOOL_RESULT_MCP_CONNECT_NOT_CONNECTED_VAR_1()&&TOOL_RESULT_MCP_CONNECT_NOT_CONNECTED_VAR_2.type==="failed"&&TOOL_RESULT_MCP_CONNECT_NOT_CONNECTED_VAR_2.error?`: ${TOOL_RESULT_MCP_CONNECT_NOT_CONNECTED_VAR_3(TOOL_RESULT_MCP_CONNECT_NOT_CONNECTED_VAR_2.error)}`:""}
