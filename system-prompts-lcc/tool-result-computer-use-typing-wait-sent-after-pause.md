<!--
name: 'Computer use: sent after typing pause'
description: >-
  Note appended to a result that input was sent after waiting for a typing
  pause.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_TYPING_WAIT_SENT_AFTER_PAUSE_VAR_0
  - TOOL_RESULT_COMPUTER_USE_TYPING_WAIT_SENT_AFTER_PAUSE_VAR_1
-->
 It was sent after waiting ${TOOL_RESULT_COMPUTER_USE_TYPING_WAIT_SENT_AFTER_PAUSE_VAR_0.round(TOOL_RESULT_COMPUTER_USE_TYPING_WAIT_SENT_AFTER_PAUSE_VAR_1/1000)} s for a pause in the user's typing: the window may have changed since your last app_screenshot.
