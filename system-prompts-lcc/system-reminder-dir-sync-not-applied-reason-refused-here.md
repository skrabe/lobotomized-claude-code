<!--
name: 'System Reminder: Dir Sync Not-Applied Reason Refused Here'
description: >-
  Reason phrase interpolated into the cloud not-applied Directory sync reminder
  when this checkout cannot be read as it stands.
ccVersion: 2.1.261
variables:
  - SYSTEM_REMINDER_DIR_SYNC_NOT_APPLIED_REASON_REFUSED_HERE_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_NOT_APPLIED_REASON_REFUSED_HERE_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_NOT_APPLIED_REASON_REFUSED_HERE_VAR_2
-->
sync will not read this checkout as it stands${SYSTEM_REMINDER_DIR_SYNC_NOT_APPLIED_REASON_REFUSED_HERE_VAR_0===void 0?"":`: ${SYSTEM_REMINDER_DIR_SYNC_NOT_APPLIED_REASON_REFUSED_HERE_VAR_1(SYSTEM_REMINDER_DIR_SYNC_NOT_APPLIED_REASON_REFUSED_HERE_VAR_2(SYSTEM_REMINDER_DIR_SYNC_NOT_APPLIED_REASON_REFUSED_HERE_VAR_0))}`} — fix that and tell the user
