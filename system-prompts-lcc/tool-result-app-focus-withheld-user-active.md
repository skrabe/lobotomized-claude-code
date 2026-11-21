<!--
name: 'Tool result: app focus withheld user active'
description: >-
  Reason for withheld focus: the user is working in the app; wait until they
  leave, then retry.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_FOCUS_WITHHELD_USER_ACTIVE_VAR_0
  - TOOL_RESULT_APP_FOCUS_WITHHELD_USER_ACTIVE_VAR_1
-->
The user is working in ${TOOL_RESULT_APP_FOCUS_WITHHELD_USER_ACTIVE_VAR_0(TOOL_RESULT_APP_FOCUS_WITHHELD_USER_ACTIVE_VAR_1)} (it is frontmost, or the frontmost app could not be read): wait until they are in another app, then retry.
