<!--
name: 'Tool Result: Safety check not shown call, repeat it'
description: >-
  Deny message saying the tool did not run because the session's safety check
  was not shown the call, and to repeat the identical call once so it can be
  reviewed
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_AUTO_MODE_SAFETY_CHECK_NOT_SHOWN_REPEAT_CALL_VAR_0
-->
${TOOL_RESULT_AUTO_MODE_SAFETY_CHECK_NOT_SHOWN_REPEAT_CALL_VAR_0.name} did not run. This session's safety check gave no verdict because it was not shown this call. That is not a judgment that the call is unsafe. Repeat the identical ${TOOL_RESULT_AUTO_MODE_SAFETY_CHECK_NOT_SHOWN_REPEAT_CALL_VAR_0.name} call once now so that the check can review it.
