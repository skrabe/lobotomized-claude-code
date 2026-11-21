<!--
name: 'Tool Result: Full-screen control declined'
description: >-
  isError tool_result from request_full_control when the user declined or did
  not confirm takeover.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_REQUEST_FULL_CONTROL_DECLINED_VAR_0
  - TOOL_RESULT_REQUEST_FULL_CONTROL_DECLINED_VAR_1
-->
Full-screen control was not approved (declined or not confirmed). Instead, ${TOOL_RESULT_REQUEST_FULL_CONTROL_DECLINED_VAR_0(TOOL_RESULT_REQUEST_FULL_CONTROL_DECLINED_VAR_1)}, or explain what full-screen access is needed for and let the user decide.
