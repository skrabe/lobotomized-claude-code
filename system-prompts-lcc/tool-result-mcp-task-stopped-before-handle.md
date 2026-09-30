<!--
name: 'Tool Result: MCP task stopped before handle arrived'
description: >-
  MCP tool result saying the server-side task started but the background task
  was stopped by the user before the handle arrived, a cancel was sent, and no
  result will follow
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_MCP_TASK_STOPPED_BEFORE_HANDLE_VAR_0
  - TOOL_RESULT_MCP_TASK_STOPPED_BEFORE_HANDLE_VAR_1
  - TOOL_RESULT_MCP_TASK_STOPPED_BEFORE_HANDLE_VAR_2
  - TOOL_RESULT_MCP_TASK_STOPPED_BEFORE_HANDLE_VAR_3
  - TOOL_RESULT_MCP_TASK_STOPPED_BEFORE_HANDLE_VAR_4
-->
MCP tool "${TOOL_RESULT_MCP_TASK_STOPPED_BEFORE_HANDLE_VAR_0(TOOL_RESULT_MCP_TASK_STOPPED_BEFORE_HANDLE_VAR_1,TOOL_RESULT_MCP_TASK_STOPPED_BEFORE_HANDLE_VAR_2)}" started server-side task ${TOOL_RESULT_MCP_TASK_STOPPED_BEFORE_HANDLE_VAR_3}, but background task ${TOOL_RESULT_MCP_TASK_STOPPED_BEFORE_HANDLE_VAR_4} was stopped by the user before the task handle arrived. A cancel was sent to the server; no result will follow.
