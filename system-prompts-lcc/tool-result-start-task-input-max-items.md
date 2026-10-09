<!--
name: 'Tool Result: Start task input — max items'
description: Input validation error for too many array entries.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_START_TASK_INPUT_MAX_ITEMS_VAR_0
  - TOOL_RESULT_START_TASK_INPUT_MAX_ITEMS_VAR_1
  - TOOL_RESULT_START_TASK_INPUT_MAX_ITEMS_VAR_2
-->
${TOOL_RESULT_START_TASK_INPUT_MAX_ITEMS_VAR_0??"the arguments"} must have at most ${TOOL_RESULT_START_TASK_INPUT_MAX_ITEMS_VAR_1(TOOL_RESULT_START_TASK_INPUT_MAX_ITEMS_VAR_2.limit)} entries
