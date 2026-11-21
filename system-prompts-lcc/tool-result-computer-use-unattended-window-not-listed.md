<!--
name: 'Computer use: unattended window not listed'
description: >-
  Refusal when an unattended run targets a window not in the app's window list
  for the browser-engine check.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_UNATTENDED_WINDOW_NOT_LISTED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_UNATTENDED_WINDOW_NOT_LISTED_VAR_1
  - TOOL_RESULT_COMPUTER_USE_UNATTENDED_WINDOW_NOT_LISTED_VAR_2
-->
Window ${TOOL_RESULT_COMPUTER_USE_UNATTENDED_WINDOW_NOT_LISTED_VAR_0} of ${TOOL_RESULT_COMPUTER_USE_UNATTENDED_WINDOW_NOT_LISTED_VAR_1(TOOL_RESULT_COMPUTER_USE_UNATTENDED_WINDOW_NOT_LISTED_VAR_2)} is not in the app's current window list, so it could not be checked for a browser engine, which an unattended run must do before acting. Call app_list_windows and pass one of its window ids, or leave this step for when the user is present.
