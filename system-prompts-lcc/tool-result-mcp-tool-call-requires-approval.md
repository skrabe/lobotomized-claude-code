<!--
name: 'Tool result: MCP tool call requires approval'
description: >-
  Tool result returned when a remote MCP tool call needs an approval that was
  not given; v1 servers prefix it with the MCP error code.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_TOOL_CALL_REQUIRES_APPROVAL_VAR_0
  - TOOL_RESULT_MCP_TOOL_CALL_REQUIRES_APPROVAL_VAR_1
-->
${TOOL_RESULT_MCP_TOOL_CALL_REQUIRES_APPROVAL_VAR_0()==="v1"?`MCP error ${TOOL_RESULT_MCP_TOOL_CALL_REQUIRES_APPROVAL_VAR_1}: `:""}MCP tool call requires approval
