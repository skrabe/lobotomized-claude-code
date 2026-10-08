<!--
name: Start task total file size exceeded
description: >-
  Refuses an attachment set whose combined size exceeds the per-call upload
  limit.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_START_TASK_FILES_TOTAL_SIZE_EXCEEDED_VAR_0
  - TOOL_RESULT_START_TASK_FILES_TOTAL_SIZE_EXCEEDED_VAR_1
  - TOOL_RESULT_START_TASK_FILES_TOTAL_SIZE_EXCEEDED_VAR_2
-->
Cannot attach "${TOOL_RESULT_START_TASK_FILES_TOTAL_SIZE_EXCEEDED_VAR_0}": with the files before it, the files named to start_task add up to more than ${TOOL_RESULT_START_TASK_FILES_TOTAL_SIZE_EXCEEDED_VAR_1/1048576} MiB, the most one call may attach. Attach fewer or smaller files. ${TOOL_RESULT_START_TASK_FILES_TOTAL_SIZE_EXCEEDED_VAR_2}
