<!--
name: Empty tool input validation error
description: >-
  Feedback returned to the model when it calls a tool with an empty input object
  despite required parameters, listing them and a minimal valid call shape.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_EMPTY_INPUT_REQUIRED_PARAMS_VAR_0
  - TOOL_RESULT_EMPTY_INPUT_REQUIRED_PARAMS_VAR_1
  - TOOL_RESULT_EMPTY_INPUT_REQUIRED_PARAMS_VAR_2
  - TOOL_RESULT_EMPTY_INPUT_REQUIRED_PARAMS_VAR_3
-->
The ${TOOL_RESULT_EMPTY_INPUT_REQUIRED_PARAMS_VAR_0} tool was called with an empty input object ({}), but it has required parameters: ${TOOL_RESULT_EMPTY_INPUT_REQUIRED_PARAMS_VAR_1}. Minimal valid call shape: ${TOOL_RESULT_EMPTY_INPUT_REQUIRED_PARAMS_VAR_2(TOOL_RESULT_EMPTY_INPUT_REQUIRED_PARAMS_VAR_3)}. Re-issue the call with real values for each required parameter.
