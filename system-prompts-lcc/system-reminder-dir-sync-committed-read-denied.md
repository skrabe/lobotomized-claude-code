<!--
name: Dir Sync Committed Read Denied
description: >-
  Snapshot-refused detail when read-denied files were committed since the
  session began.
ccVersion: 2.1.261
variables:
  - SYSTEM_REMINDER_DIR_SYNC_COMMITTED_READ_DENIED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_COMMITTED_READ_DENIED_VAR_1
-->
${SYSTEM_REMINDER_DIR_SYNC_COMMITTED_READ_DENIED_VAR_0} ${SYSTEM_REMINDER_DIR_SYNC_COMMITTED_READ_DENIED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_COMMITTED_READ_DENIED_VAR_0,"file")} covered by your Read rules or sandbox read-deny settings (or named like a credential under another spelling) ${SYSTEM_REMINDER_DIR_SYNC_COMMITTED_READ_DENIED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_COMMITTED_READ_DENIED_VAR_0,"was","were")} committed here since the session began; sync will not carry those commits
