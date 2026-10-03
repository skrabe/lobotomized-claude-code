<!--
name: 'Tool Result: remote tool background task check via task tool'
description: >-
  Part of the remote background-task note telling the model to call the
  task-status tool with the task ID to see whether it still runs and how it
  ended.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_CHECK_VIA_TASK_TOOL_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_CHECK_VIA_TASK_TOOL_VAR_1
-->
To check on it, call ${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_CHECK_VIA_TASK_TOOL_VAR_0} with that ID: ${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_CHECK_VIA_TASK_TOOL_VAR_1} itself says whether it is still running, how it ended, and the end of its output.
