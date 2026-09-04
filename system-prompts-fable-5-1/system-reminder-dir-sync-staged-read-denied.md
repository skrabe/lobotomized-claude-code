<!--
name: Dir Sync Staged Read Denied
description: >-
  Snapshot-refused detail when staged files are covered by Read/sandbox deny
  rules.
ccVersion: 2.1.261
variables:
  - SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_1
-->
${SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_0} staged ${SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_0,"file is","files are")} covered by your Read rules or sandbox read-deny settings (or named like a credential under another spelling); unstage ${SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_0,"it","them")} for sync to continue (committing ${SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_0,"it","them")} would ship ${SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_STAGED_READ_DENIED_VAR_0,"its","their")} bytes as history)
