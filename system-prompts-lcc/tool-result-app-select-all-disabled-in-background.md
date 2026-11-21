<!--
name: 'Tool result: app Select All disabled in background'
description: >-
  Refusal that cmd+a was not sent because Select All is disabled while the app
  is in the background.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_SELECT_ALL_DISABLED_IN_BACKGROUND_VAR_0
  - TOOL_RESULT_APP_SELECT_ALL_DISABLED_IN_BACKGROUND_VAR_1
  - TOOL_RESULT_APP_SELECT_ALL_DISABLED_IN_BACKGROUND_VAR_2
-->
cmd+a was NOT sent: Select All is disabled in ${TOOL_RESULT_APP_SELECT_ALL_DISABLED_IN_BACKGROUND_VAR_0(TOOL_RESULT_APP_SELECT_ALL_DISABLED_IN_BACKGROUND_VAR_1)} while it is in the background, so the app would ignore the key, select nothing, and the user would hear an alert sound. ${TOOL_RESULT_APP_SELECT_ALL_DISABLED_IN_BACKGROUND_VAR_2}.
