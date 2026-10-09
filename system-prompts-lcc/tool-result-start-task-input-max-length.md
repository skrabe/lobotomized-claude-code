<!--
name: 'Tool Result: Start task input — max length'
description: Input validation error for a string longer than the maximum.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_START_TASK_INPUT_MAX_LENGTH_VAR_0
  - TOOL_RESULT_START_TASK_INPUT_MAX_LENGTH_VAR_1
  - TOOL_RESULT_START_TASK_INPUT_MAX_LENGTH_VAR_2
-->
${TOOL_RESULT_START_TASK_INPUT_MAX_LENGTH_VAR_0??"the arguments"} must be at most ${TOOL_RESULT_START_TASK_INPUT_MAX_LENGTH_VAR_1(TOOL_RESULT_START_TASK_INPUT_MAX_LENGTH_VAR_2.limit)} characters
