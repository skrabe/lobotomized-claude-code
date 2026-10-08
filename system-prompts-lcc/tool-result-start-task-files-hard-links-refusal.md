<!--
name: Start task hard-link attachment refusal
description: Rejects a task attachment whose file has multiple hard links.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_START_TASK_FILES_HARD_LINKS_REFUSAL_VAR_0
  - TOOL_RESULT_START_TASK_FILES_HARD_LINKS_REFUSAL_VAR_1
-->
Cannot attach "${TOOL_RESULT_START_TASK_FILES_HARD_LINKS_REFUSAL_VAR_0}": the file has more than one hard link, which can point at a file outside the folders this session may read. Copy the file and attach the copy. ${TOOL_RESULT_START_TASK_FILES_HARD_LINKS_REFUSAL_VAR_1}
