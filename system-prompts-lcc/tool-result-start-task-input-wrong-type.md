<!--
name: 'Tool Result: Start task input — wrong type'
description: >-
  start_task input refusal clause saying a field (or the arguments) must be one
  of the listed JSON types, joined with "or"; returned to the model when the
  call's input fails the schema type check.
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_0
  - TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_1
  - TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_2
  - TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_3
  - TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_4
-->
${TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_0??"the arguments"} must be ${TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_1.map((TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_2)=>TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_3[String(M)]??TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_4(TOOL_RESULT_START_TASK_INPUT_WRONG_TYPE_VAR_2)).join(" or ")}
