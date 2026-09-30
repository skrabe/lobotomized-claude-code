<!--
name: 'Tool Result: MCP Task Backgrounded Stop Hint'
description: >-
  Hint in the tool result of an MCP tool whose server-side task was moved to the
  background, saying which tool stops it (with the registry task_id) and that
  the result arrives as a task notification.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_STOP_HINT_VAR_0
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_STOP_HINT_VAR_1
-->
To stop it, use ${TOOL_RESULT_MCP_TASK_BACKGROUNDED_STOP_HINT_VAR_0} with task_id "${TOOL_RESULT_MCP_TASK_BACKGROUNDED_STOP_HINT_VAR_1}"; the result arrives as a task notification.
