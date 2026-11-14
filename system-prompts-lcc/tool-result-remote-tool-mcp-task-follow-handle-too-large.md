<!--
name: 'Tool Result: remote tool MCP task follow handle too large'
description: >-
  Remote tool result when an MCP tool started a background task but the server's
  follow handle was too large or too deeply nested to pass on, so the task is
  cancelled.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_TOOL_MCP_TASK_FOLLOW_HANDLE_TOO_LARGE_VAR_0
-->
The tool started a background task on ${TOOL_RESULT_REMOTE_TOOL_MCP_TASK_FOLLOW_HANDLE_TOO_LARGE_VAR_0}, but what its server sent to follow the task by was too large or too deeply nested to hand on, so the task is being cancelled. Nothing more of it will arrive.
