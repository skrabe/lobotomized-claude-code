<!--
name: 'Tool Result: Check MCP task, server unreachable'
description: >-
  Check MCP task result when the server is not connected or gave no usable
  answer.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_CHECK_MCP_TASK_UNREACHABLE_VAR_0
  - TOOL_RESULT_CHECK_MCP_TASK_UNREACHABLE_VAR_1
  - TOOL_RESULT_CHECK_MCP_TASK_UNREACHABLE_VAR_2
-->
The status of task ${TOOL_RESULT_CHECK_MCP_TASK_UNREACHABLE_VAR_0} is not known: its server is not connected or gave no usable answer (the user may need to sign in to it again). ${TOOL_RESULT_CHECK_MCP_TASK_UNREACHABLE_VAR_1[TOOL_RESULT_CHECK_MCP_TASK_UNREACHABLE_VAR_2.follower]} Tell the user, and do not check again unless they ask again.
