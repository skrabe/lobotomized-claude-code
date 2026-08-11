<!--
name: 'System Reminder: Ultrareview Post Routine Failed'
description: >-
  Tells the model that the posting routine failed during setup, start, or
  verification and leaves the findings available for manual posting.
ccVersion: 2.1.227
variables:
  - SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_FAILED_VAR_0
  - SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_FAILED_VAR_1
  - SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_FAILED_VAR_2
-->
The posting routine ${SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_FAILED_VAR_0==="fire"?"couldn't start":SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_FAILED_VAR_0==="verify"?"couldn't be verified":"couldn't be set up"}${SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_FAILED_VAR_1?`: ${SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_FAILED_VAR_1}`:` (${SYSTEM_REMINDER_ULTRAREVIEW_POST_ROUTINE_FAILED_VAR_2})`}. The findings are above if you want to post them by hand.
