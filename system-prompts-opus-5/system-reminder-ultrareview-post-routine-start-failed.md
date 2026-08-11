<!--
name: 'System Reminder: Ultrareview Post Routine Start Failed'
description: >-
  Tells the model that the routine used to post review findings could not start
  and leaves the findings for manual posting.
ccVersion: 2.1.227
variables:
  - SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_START_FAILED_VAR_0
  - SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_START_FAILED_VAR_1
-->
The posting routine couldn't start${SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_START_FAILED_VAR_0?`: ${SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_START_FAILED_VAR_0}`:` (${SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_START_FAILED_VAR_1.status})`}. The findings are above if you want to post them by hand.
