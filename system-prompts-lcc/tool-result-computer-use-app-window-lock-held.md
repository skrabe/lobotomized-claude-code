<!--
name: App Window Lock Held
description: >-
  Error tool result when another session already holds the target window's app
  lock.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_APP_WINDOW_LOCK_HELD_VAR_0
  - TOOL_RESULT_COMPUTER_USE_APP_WINDOW_LOCK_HELD_VAR_1
  - TOOL_RESULT_COMPUTER_USE_APP_WINDOW_LOCK_HELD_VAR_2
-->
Another Claude session is currently controlling window_id ${TOOL_RESULT_COMPUTER_USE_APP_WINDOW_LOCK_HELD_VAR_0} of ${TOOL_RESULT_COMPUTER_USE_APP_WINDOW_LOCK_HELD_VAR_1(TOOL_RESULT_COMPUTER_USE_APP_WINDOW_LOCK_HELD_VAR_2)??"this app"}. Target a different window (app_list_windows shows all of them), or wait for that session to finish.
