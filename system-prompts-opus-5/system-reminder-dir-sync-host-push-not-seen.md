<!--
name: 'System Reminder: Dir Sync Host Push Not Seen'
description: >-
  dir_sync_notice that the host says it sent post-command changes that have not
  landed yet, so the model should read those files on the host.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DIR_SYNC_HOST_PUSH_NOT_SEEN_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_HOST_PUSH_NOT_SEEN_VAR_1
-->
Directory sync: ${SYSTEM_REMINDER_DIR_SYNC_HOST_PUSH_NOT_SEEN_VAR_0.name} says it sent what the last command run there changed, but it has not reached this session yet; it is taken in when it lands — until then, read those files on ${SYSTEM_REMINDER_DIR_SYNC_HOST_PUSH_NOT_SEEN_VAR_0.name} (the ${SYSTEM_REMINDER_DIR_SYNC_HOST_PUSH_NOT_SEEN_VAR_1} argument).
