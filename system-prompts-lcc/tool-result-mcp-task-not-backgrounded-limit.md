<!--
name: 'Tool Result: MCP task not backgrounded at limit'
description: >-
  MCP tool result when a server-side task could not be moved to the background
  because the per-user-message background task limit was reached; a cancel was
  sent and the model should tell the user
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_LIMIT_VAR_0
  - TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_LIMIT_VAR_1
  - TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_LIMIT_VAR_2
  - TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_LIMIT_VAR_3
  - TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_LIMIT_VAR_4
-->
MCP tool "${TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_LIMIT_VAR_0(TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_LIMIT_VAR_1,TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_LIMIT_VAR_2)}" started server-side task ${TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_LIMIT_VAR_3}, but it was not moved to the background: ${TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_LIMIT_VAR_4.mostSinceAPersonWrote} tasks have been moved there since the user last wrote, the most this session allows. A cancel was sent to the server; no result will follow, and the same goes for any further task until the user writes. Tell the user where things stand; you can start another after their next message.
