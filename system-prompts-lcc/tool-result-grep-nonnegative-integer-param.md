<!--
name: Grep numeric param validation error
description: >-
  Grep tool validateInput error returned to the model when head_limit/offset is
  not a whole number of 0 or more.
ccVersion: 2.1.210
variables:
  - TOOL_RESULT_GREP_NONNEGATIVE_INTEGER_PARAM_VAR_0
  - TOOL_RESULT_GREP_NONNEGATIVE_INTEGER_PARAM_VAR_1
-->
${TOOL_RESULT_GREP_NONNEGATIVE_INTEGER_PARAM_VAR_0} must be a whole number of 0 or more, got ${TOOL_RESULT_GREP_NONNEGATIVE_INTEGER_PARAM_VAR_1}.${TOOL_RESULT_GREP_NONNEGATIVE_INTEGER_PARAM_VAR_0==="head_limit"?" Pass 0 for unlimited.":""}
