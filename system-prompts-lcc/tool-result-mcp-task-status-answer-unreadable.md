<!--
name: 'Tool result: MCP task status answer unreadable'
description: >-
  Reports the server's task status answer was unreadable, listing fault codes,
  and that Claude Code asked the server to cancel
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_TASK_STATUS_ANSWER_UNREADABLE_VAR_0
  - TOOL_RESULT_MCP_TASK_STATUS_ANSWER_UNREADABLE_VAR_1
-->
the server's answer about the task was not one this client can read (${TOOL_RESULT_MCP_TASK_STATUS_ANSWER_UNREADABLE_VAR_0.length===1?"1 fault":`${TOOL_RESULT_MCP_TASK_STATUS_ANSWER_UNREADABLE_VAR_0.length} faults`}: ${TOOL_RESULT_MCP_TASK_STATUS_ANSWER_UNREADABLE_VAR_1(TOOL_RESULT_MCP_TASK_STATUS_ANSWER_UNREADABLE_VAR_0).sort().join(", ")}), so Claude Code asked the server to cancel it
