<!--
name: 'System Reminder: Dir Sync Filter Attributed Files'
description: >-
  Reminds the model that git-lfs/git-crypt/re-encoding attributed files are
  never synced in either direction.
ccVersion: 2.1.261
variables:
  - SYSTEM_REMINDER_DIR_SYNC_FILTER_ATTRIBUTED_FILES_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_FILTER_ATTRIBUTED_FILES_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_FILTER_ATTRIBUTED_FILES_VAR_2
-->
Directory sync: these files are under a content-filter or re-encoding attribute here (git-lfs, git-crypt, working-tree-encoding or similar), so sync never carries their contents in either direction — this checkout's version of them is NOT sent to the user's machine, which keeps its own: ${SYSTEM_REMINDER_DIR_SYNC_FILTER_ATTRIBUTED_FILES_VAR_0}${SYSTEM_REMINDER_DIR_SYNC_FILTER_ATTRIBUTED_FILES_VAR_1.length>SYSTEM_REMINDER_DIR_SYNC_FILTER_ATTRIBUTED_FILES_VAR_2?` and ${SYSTEM_REMINDER_DIR_SYNC_FILTER_ATTRIBUTED_FILES_VAR_1.length-SYSTEM_REMINDER_DIR_SYNC_FILTER_ATTRIBUTED_FILES_VAR_2} more`:""}. Tell the user if changes you made to them matter.
