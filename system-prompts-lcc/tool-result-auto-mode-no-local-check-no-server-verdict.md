<!--
name: 'Tool Result: Auto mode no local check and no server verdict'
description: >-
  Reports a call was not run because Claude Code no longer checks actions
  locally and no server verdict covers it
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_AUTO_MODE_NO_LOCAL_CHECK_NO_SERVER_VERDICT_VAR_0
  - TOOL_RESULT_AUTO_MODE_NO_LOCAL_CHECK_NO_SERVER_VERDICT_VAR_1
  - TOOL_RESULT_AUTO_MODE_NO_LOCAL_CHECK_NO_SERVER_VERDICT_VAR_2
-->
${TOOL_RESULT_AUTO_MODE_NO_LOCAL_CHECK_NO_SERVER_VERDICT_VAR_0} was not run: ${TOOL_RESULT_AUTO_MODE_NO_LOCAL_CHECK_NO_SERVER_VERDICT_VAR_1}${TOOL_RESULT_AUTO_MODE_NO_LOCAL_CHECK_NO_SERVER_VERDICT_VAR_2}${TOOL_RESULT_AUTO_MODE_NO_LOCAL_CHECK_NO_SERVER_VERDICT_VAR_0}. This is not a judgment that the action is unsafe, and retrying will not help. Continue with work that doesn't need ${TOOL_RESULT_AUTO_MODE_NO_LOCAL_CHECK_NO_SERVER_VERDICT_VAR_0}. If the task needs it, stop and tell the user that it was not run because it could not be checked, so that they can decide how to go on. 
