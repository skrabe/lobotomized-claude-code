<!--
name: 'Tool Result: unattributed window at point'
description: >-
  Refusal: window at point belongs to a process with no app bundle; act on an
  app window instead.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_UNATTRIBUTED_WINDOW_VAR_0
  - TOOL_RESULT_COMPUTER_USE_UNATTRIBUTED_WINDOW_VAR_1
-->
The window at this point belongs to "${TOOL_RESULT_COMPUTER_USE_UNATTRIBUTED_WINDOW_VAR_0({displayName:TOOL_RESULT_COMPUTER_USE_UNATTRIBUTED_WINDOW_VAR_1})}", a process with no app bundle that no running app answers for, so no grant can cover it and actions on it are refused. Act on a window that belongs to an application instead, or ask the user to close or move this one.
