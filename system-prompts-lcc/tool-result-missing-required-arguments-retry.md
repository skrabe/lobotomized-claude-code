<!--
name: 'Tool result: Missing required arguments retry'
description: >-
  InputValidationError listing missing required arguments and asking to call
  again with all of them
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MISSING_REQUIRED_ARGUMENTS_RETRY_VAR_0
  - TOOL_RESULT_MISSING_REQUIRED_ARGUMENTS_RETRY_VAR_1
  - TOOL_RESULT_MISSING_REQUIRED_ARGUMENTS_RETRY_VAR_2
-->
InputValidationError: ${TOOL_RESULT_MISSING_REQUIRED_ARGUMENTS_RETRY_VAR_0.name} did not run. Missing required arguments: ${TOOL_RESULT_MISSING_REQUIRED_ARGUMENTS_RETRY_VAR_1.missingKeys.slice(0,5).map(TOOL_RESULT_MISSING_REQUIRED_ARGUMENTS_RETRY_VAR_2).join(", ")}${TOOL_RESULT_MISSING_REQUIRED_ARGUMENTS_RETRY_VAR_1.missingKeys.length>5?" and others":""}. Call it again with all of them.
