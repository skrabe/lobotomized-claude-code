<!--
name: 'Tool Result: Check MCP task, server rejected id'
description: Check MCP task result when the server rejected the task id.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_CHECK_MCP_TASK_UNKNOWN_TO_SERVER_VAR_0
  - TOOL_RESULT_CHECK_MCP_TASK_UNKNOWN_TO_SERVER_VAR_1
  - TOOL_RESULT_CHECK_MCP_TASK_UNKNOWN_TO_SERVER_VAR_2
-->
The status of task ${TOOL_RESULT_CHECK_MCP_TASK_UNKNOWN_TO_SERVER_VAR_0} is not known: the server rejected the task's id, which normally means that it no longer knows the task. ${TOOL_RESULT_CHECK_MCP_TASK_UNKNOWN_TO_SERVER_VAR_1.follower==="this_session"?"A task notification comes once the outcome is known or the task is given up.":TOOL_RESULT_CHECK_MCP_TASK_UNKNOWN_TO_SERVER_VAR_2[TOOL_RESULT_CHECK_MCP_TASK_UNKNOWN_TO_SERVER_VAR_1.follower]} Tell the user, and do not check again unless they ask again.
