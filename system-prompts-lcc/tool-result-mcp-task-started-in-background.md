<!--
name: 'Tool Result: MCP task started in background'
description: >-
  Text returned for an MCP tool call that the server ran as a long-running task,
  telling the model the task id, the bound MCP server, and that it runs in the
  background with a notification on completion.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_MCP_TASK_STARTED_IN_BACKGROUND_VAR_0
  - TOOL_RESULT_MCP_TASK_STARTED_IN_BACKGROUND_VAR_1
  - TOOL_RESULT_MCP_TASK_STARTED_IN_BACKGROUND_VAR_2
-->
Task ${TOOL_RESULT_MCP_TASK_STARTED_IN_BACKGROUND_VAR_0} started on MCP server '${TOOL_RESULT_MCP_TASK_STARTED_IN_BACKGROUND_VAR_1.boundServerName(TOOL_RESULT_MCP_TASK_STARTED_IN_BACKGROUND_VAR_2)}'. Running in background; you'll be notified when it completes.
