<!--
name: 'Tool Result: MCP Task Server Rejected Submitted Answer'
description: >-
  Error message when an MCP server keeps a task in input_required after the
  client answered its input requests, naming the rejected keys.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_MCP_TASK_SERVER_REJECTED_SUBMITTED_ANSWER_VAR_0
  - TOOL_RESULT_MCP_TASK_SERVER_REJECTED_SUBMITTED_ANSWER_VAR_1
  - TOOL_RESULT_MCP_TASK_SERVER_REJECTED_SUBMITTED_ANSWER_VAR_2
-->
Task ${TOOL_RESULT_MCP_TASK_SERVER_REJECTED_SUBMITTED_ANSWER_VAR_0}: the server rejected the submitted answer to ${TOOL_RESULT_MCP_TASK_SERVER_REJECTED_SUBMITTED_ANSWER_VAR_1.map(([TOOL_RESULT_MCP_TASK_SERVER_REJECTED_SUBMITTED_ANSWER_VAR_2])=>TOOL_RESULT_MCP_TASK_SERVER_REJECTED_SUBMITTED_ANSWER_VAR_2).join(", ")} and still requires input
