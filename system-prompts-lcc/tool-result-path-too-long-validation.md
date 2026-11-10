<!--
name: 'Tool Result: Path too long validation'
description: >-
  Validation error when a path parameter exceeds the length limit, asking Claude
  to normalize and resend it
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_PATH_TOO_LONG_VALIDATION_VAR_0
  - TOOL_RESULT_PATH_TOO_LONG_VALIDATION_VAR_1
  - TOOL_RESULT_PATH_TOO_LONG_VALIDATION_VAR_2
-->
${TOOL_RESULT_PATH_TOO_LONG_VALIDATION_VAR_0} ${TOOL_RESULT_PATH_TOO_LONG_VALIDATION_VAR_1[0]} has ${TOOL_RESULT_PATH_TOO_LONG_VALIDATION_VAR_1[1].length} characters, and ${TOOL_RESULT_PATH_TOO_LONG_VALIDATION_VAR_0} takes at most ${TOOL_RESULT_PATH_TOO_LONG_VALIDATION_VAR_2}. Resolve any "./" and "../" parts, drop any white space around the path, and send it again.
