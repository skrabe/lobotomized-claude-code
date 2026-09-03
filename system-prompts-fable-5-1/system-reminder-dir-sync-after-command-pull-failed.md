<!--
name: Dir Sync After Command Pull Failed
description: >-
  After-command note that command-changed files could not be taken in yet (with
  the pull reason), so read them on the host until they land.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_PULL_FAILED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_PULL_FAILED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_PULL_FAILED_VAR_2
-->
what that command changed on ${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_PULL_FAILED_VAR_0} could not be taken in here just now (${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_PULL_FAILED_VAR_1.reason.replace(/_/g," ")}); it is taken in when it lands — until then, read those files on ${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_PULL_FAILED_VAR_0} (the ${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_PULL_FAILED_VAR_2} argument).
