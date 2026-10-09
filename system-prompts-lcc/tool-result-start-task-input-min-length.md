<!--
name: 'Tool Result: Start task input — min length'
description: Input validation error for a string shorter than the minimum.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_START_TASK_INPUT_MIN_LENGTH_VAR_0
  - TOOL_RESULT_START_TASK_INPUT_MIN_LENGTH_VAR_1
  - TOOL_RESULT_START_TASK_INPUT_MIN_LENGTH_VAR_2
-->
${TOOL_RESULT_START_TASK_INPUT_MIN_LENGTH_VAR_0??"the arguments"} must be at least ${TOOL_RESULT_START_TASK_INPUT_MIN_LENGTH_VAR_1(TOOL_RESULT_START_TASK_INPUT_MIN_LENGTH_VAR_2.limit)} characters
