<!--
name: 'Tool Result: MCP task did not complete'
description: >-
  MCP tool error when a server-side task for a tool was cancelled or failed,
  carrying the server's error text.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_TASK_DID_NOT_COMPLETE_VAR_0
  - TOOL_RESULT_MCP_TASK_DID_NOT_COMPLETE_VAR_1
  - TOOL_RESULT_MCP_TASK_DID_NOT_COMPLETE_VAR_2
  - TOOL_RESULT_MCP_TASK_DID_NOT_COMPLETE_VAR_3
-->
MCP server "${TOOL_RESULT_MCP_TASK_DID_NOT_COMPLETE_VAR_0}" task for tool "${TOOL_RESULT_MCP_TASK_DID_NOT_COMPLETE_VAR_1}" ${TOOL_RESULT_MCP_TASK_DID_NOT_COMPLETE_VAR_2?"was cancelled":"failed"}: ${TOOL_RESULT_MCP_TASK_DID_NOT_COMPLETE_VAR_3}
