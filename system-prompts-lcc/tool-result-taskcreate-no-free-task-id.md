<!--
name: 'Tool Result: TaskCreate no free task id'
description: >-
  Error returned when TaskCreate cannot claim a free task id after repeated
  attempts.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_TASKCREATE_NO_FREE_TASK_ID_VAR_0
  - TOOL_RESULT_TASKCREATE_NO_FREE_TASK_ID_VAR_1
  - TOOL_RESULT_TASKCREATE_NO_FREE_TASK_ID_VAR_2
  - TOOL_RESULT_TASKCREATE_NO_FREE_TASK_ID_VAR_3
-->
[Tasks] Failed to create a task: could not claim a free task id after ${TOOL_RESULT_TASKCREATE_NO_FREE_TASK_ID_VAR_0} attempts; last tried ${TOOL_RESULT_TASKCREATE_NO_FREE_TASK_ID_VAR_1(TOOL_RESULT_TASKCREATE_NO_FREE_TASK_ID_VAR_2,TOOL_RESULT_TASKCREATE_NO_FREE_TASK_ID_VAR_3)}, which exists and could not be claimed — the task listing may have failed, or the entry is not a task file
