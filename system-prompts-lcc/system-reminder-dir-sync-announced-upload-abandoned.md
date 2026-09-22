<!--
name: Dir Sync Announced Upload Abandoned
description: >-
  Model reminder that the user's machine could not upload its latest changes
  (quoting its reason); this turn runs on the files as they were.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DIR_SYNC_ANNOUNCED_UPLOAD_ABANDONED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_ANNOUNCED_UPLOAD_ABANDONED_VAR_1
-->
Directory sync: the user's machine could not upload its latest changes${SYSTEM_REMINDER_DIR_SYNC_ANNOUNCED_UPLOAD_ABANDONED_VAR_0.reason===null?"":` (it said: "${SYSTEM_REMINDER_DIR_SYNC_ANNOUNCED_UPLOAD_ABANDONED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_ANNOUNCED_UPLOAD_ABANDONED_VAR_0.reason)}")`}; this turn runs on the files as they were.
