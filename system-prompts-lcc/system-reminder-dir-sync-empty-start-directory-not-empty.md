<!--
name: Dir Sync Empty Start Directory Not Empty
description: >-
  Reason fragment in the Directory sync is OFF reminder when empty-start failed
  because the working directory was not empty.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DIR_SYNC_EMPTY_START_DIRECTORY_NOT_EMPTY_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_EMPTY_START_DIRECTORY_NOT_EMPTY_VAR_1
-->
the working directory was not empty (found: ${SYSTEM_REMINDER_DIR_SYNC_EMPTY_START_DIRECTORY_NOT_EMPTY_VAR_0.found.map(SYSTEM_REMINDER_DIR_SYNC_EMPTY_START_DIRECTORY_NOT_EMPTY_VAR_1).join(", ")})
