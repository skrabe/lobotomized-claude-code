<!--
name: 'System Reminder: Dir Sync Host Push Take-In Failed'
description: >-
  dir_sync_notice that post-command changes could not be taken in yet, so the
  model should read those files on the host until they land.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DIR_SYNC_HOST_PUSH_TAKE_IN_FAILED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_HOST_PUSH_TAKE_IN_FAILED_VAR_1
-->
Directory sync: what the last command run on ${SYSTEM_REMINDER_DIR_SYNC_HOST_PUSH_TAKE_IN_FAILED_VAR_0.name} changed there could not be taken in here just now; it is taken in when it lands — until then, read those files on ${SYSTEM_REMINDER_DIR_SYNC_HOST_PUSH_TAKE_IN_FAILED_VAR_0.name} (the ${SYSTEM_REMINDER_DIR_SYNC_HOST_PUSH_TAKE_IN_FAILED_VAR_1} argument).
