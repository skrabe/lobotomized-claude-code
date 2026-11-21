<!--
name: 'App action: screen locked with remedy'
description: 'Refusal: screen locked, rest/nothing sent, with remedy slot; wait for unlock.'
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_ACTION_SCREEN_LOCKED_PARTIAL_SEND_VAR_0
  - TOOL_RESULT_APP_ACTION_SCREEN_LOCKED_PARTIAL_SEND_VAR_1
-->
the screen is locked, so ${TOOL_RESULT_APP_ACTION_SCREEN_LOCKED_PARTIAL_SEND_VAR_0.someTextWasTyped===!0?"the rest was not":"nothing was"} sent. ${TOOL_RESULT_APP_ACTION_SCREEN_LOCKED_PARTIAL_SEND_VAR_1}. To act on the window, wait until the user unlocks the screen
