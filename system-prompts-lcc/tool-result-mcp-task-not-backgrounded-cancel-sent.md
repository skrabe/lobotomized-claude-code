<!--
name: 'Tool Result: MCP task not backgrounded (cancel sent)'
description: >-
  MCP tool error result when a server started a task that was not moved to the
  background: a cancel was sent, the server may still run it, and no result will
  follow; a reason suffix is appended.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_CANCEL_SENT_VAR_0
  - TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_CANCEL_SENT_VAR_1
  - TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_CANCEL_SENT_VAR_2
-->
MCP server "${TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_CANCEL_SENT_VAR_0}" started a task, but it was not moved to the background. A cancel was sent to the server, which may still run it; no result will follow.${TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_CANCEL_SENT_VAR_1[TOOL_RESULT_MCP_TASK_NOT_BACKGROUNDED_CANCEL_SENT_VAR_2]}
