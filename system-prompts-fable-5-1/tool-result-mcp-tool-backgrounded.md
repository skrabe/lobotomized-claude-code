<!--
name: 'Tool Result: MCP Tool Moved To Background'
description: >-
  Text tool_result returned to the model when a slow MCP tool call is
  auto-backgrounded as a task, telling it how to stop the task.
ccVersion: 2.1.214
variables:
  - TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_0
  - TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_1
  - TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_2
-->
MCP tool "${TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_0}" is still running after ${TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_1}s; moved to the background as task ${TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_2}. You'll be notified when it completes. Stop it with TaskStop, task_id "${TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_2}". It does not survive exiting this session.
