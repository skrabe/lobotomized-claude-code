<!--
name: InputValidationError tool_use_error wrapper
description: >-
  tool_result content wrapping an InputValidationError message in a
  <tool_use_error> tag sent to the model; model-facing.
ccVersion: 2.1.191
variables:
  - TOOL_RESULT_INPUT_VALIDATION_ERROR_WRAPPER_VAR_0
-->
<tool_use_error>InputValidationError: ${TOOL_RESULT_INPUT_VALIDATION_ERROR_WRAPPER_VAR_0}</tool_use_error>
