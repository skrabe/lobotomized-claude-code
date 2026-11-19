<!--
name: 'Tool Result: Resume MCP task waiting for input'
description: >-
  Resume-MCP-task result: the task awaits input, so this session polls it and
  cancels it if it cannot answer
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_RESUME_MCP_TASK_WAITING_FOR_INPUT_VAR_0
-->
Task ${TOOL_RESULT_RESUME_MCP_TASK_WAITING_FOR_INPUT_VAR_0} is waiting for input, so the polling service did not take it. This session polls it, and cancels it if it cannot give the input. A task notification tells the outcome.
