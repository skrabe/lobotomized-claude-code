<!--
name: 'System Reminder: Session continuation'
description: Notification that session continues from another machine
ccVersion: 2.1.332
variables:
  - GET_CWD_FN
  - SYSTEM_REMINDER_SESSION_CONTINUATION_VAR_1
  - SYSTEM_REMINDER_SESSION_CONTINUATION_VAR_2
-->
This session is being continued from another machine. Application state may have changed. The updated working directory is ${GET_CWD_FN()}${SYSTEM_REMINDER_SESSION_CONTINUATION_VAR_1}${SYSTEM_REMINDER_SESSION_CONTINUATION_VAR_2}
