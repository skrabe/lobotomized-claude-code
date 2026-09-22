<!--
name: 'System Reminder: Dir Sync Files Displaced'
description: >-
  Tells the cloud agent local-only files that blocked incoming paths were moved
  to session trash rather than overwritten.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_FILES_DISPLACED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_FILES_DISPLACED_VAR_1
-->
Files of this checkout that no snapshot carried (ignored, outside sync's scope, or created since the snapshot was read) were in the way of incoming paths and were moved to the session trash, not overwritten: ${SYSTEM_REMINDER_DIR_SYNC_FILES_DISPLACED_VAR_0(SYSTEM_REMINDER_DIR_SYNC_FILES_DISPLACED_VAR_1.files.displaced)}.
