<!--
name: 'Tool Result: MCP Tool Moved To Background'
description: >-
  Text tool_result returned to the model when a slow MCP tool call is
  auto-backgrounded as a task, telling it how to stop the task.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_0
  - TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_1
-->
MCP tool "${TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_0}" was moved to the background as task ${TOOL_RESULT_MCP_TOOL_BACKGROUNDED_VAR_1} so that a message that arrived while it was running can reach you; it was not interrupted and keeps running
