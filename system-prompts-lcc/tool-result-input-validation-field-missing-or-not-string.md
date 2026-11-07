<!--
name: 'Tool Result: Input validation field missing or not string'
description: >-
  InputValidationError saying a tool did not run because a required field is
  absent or not a string, followed by the remedy
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_INPUT_VALIDATION_FIELD_MISSING_OR_NOT_STRING_VAR_0
  - TOOL_RESULT_INPUT_VALIDATION_FIELD_MISSING_OR_NOT_STRING_VAR_1
  - TOOL_RESULT_INPUT_VALIDATION_FIELD_MISSING_OR_NOT_STRING_VAR_2
-->
InputValidationError: ${TOOL_RESULT_INPUT_VALIDATION_FIELD_MISSING_OR_NOT_STRING_VAR_0.name} did not run: ${TOOL_RESULT_INPUT_VALIDATION_FIELD_MISSING_OR_NOT_STRING_VAR_1?`the call has no "${TOOL_RESULT_INPUT_VALIDATION_FIELD_MISSING_OR_NOT_STRING_VAR_2.key}"`:`its "${TOOL_RESULT_INPUT_VALIDATION_FIELD_MISSING_OR_NOT_STRING_VAR_2.key}" is not a string`}. ${TOOL_RESULT_INPUT_VALIDATION_FIELD_MISSING_OR_NOT_STRING_VAR_2.remedy}
