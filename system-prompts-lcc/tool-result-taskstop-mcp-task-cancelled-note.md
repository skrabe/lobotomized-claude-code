<!--
name: 'Tool Result: TaskStop MCP task cancelled note'
description: >-
  Note on stopping an MCP task: cancellation is fire-and-forget with no server
  confirmation, and to check on it only if the user asks
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_TASKSTOP_MCP_TASK_CANCELLED_NOTE_VAR_0
  - TOOL_RESULT_TASKSTOP_MCP_TASK_CANCELLED_NOTE_VAR_1
-->
(${TOOL_RESULT_TASKSTOP_MCP_TASK_CANCELLED_NOTE_VAR_0(TOOL_RESULT_TASKSTOP_MCP_TASK_CANCELLED_NOTE_VAR_1.description)}) is stopped. Cancellations are fire and forget, so there is no confirmation from the MCP server, and it may already have done some of the work. Only check on it if the user asks.
