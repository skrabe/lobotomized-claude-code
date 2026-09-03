<!--
name: 'Tool Result: app_* action ineffective'
description: >-
  Non-error tool_result when an app_* accessibility write returned success but
  the app has not visibly responded yet.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_APP_ACTION_INEFFECTIVE_VAR_0
  - TOOL_RESULT_APP_ACTION_INEFFECTIVE_VAR_1
  - TOOL_RESULT_APP_ACTION_INEFFECTIVE_VAR_2
  - TOOL_RESULT_APP_ACTION_INEFFECTIVE_VAR_3
-->
ineffective: ${TOOL_RESULT_APP_ACTION_INEFFECTIVE_VAR_0} on ${TOOL_RESULT_APP_ACTION_INEFFECTIVE_VAR_1}${TOOL_RESULT_APP_ACTION_INEFFECTIVE_VAR_2}${TOOL_RESULT_APP_ACTION_INEFFECTIVE_VAR_3} returned success but the app has not visibly responded yet. Take a fresh app_screenshot to confirm before assuming it failed.
