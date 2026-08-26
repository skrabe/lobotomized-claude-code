<!--
name: 'System Reminder: Dir Sync Files Trashed'
description: >-
  Tells the cloud agent paths removed on the user's machine were moved out of
  this checkout.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_FILES_TRASHED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_FILES_TRASHED_VAR_1
-->
Removed on the user's machine and moved out of the checkout here: ${SYSTEM_REMINDER_DIR_SYNC_FILES_TRASHED_VAR_0(SYSTEM_REMINDER_DIR_SYNC_FILES_TRASHED_VAR_1.files.trashed)}.
