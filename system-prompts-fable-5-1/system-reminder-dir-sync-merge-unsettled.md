<!--
name: 'System Reminder: Dir Sync Merge Unsettled'
description: >-
  Tells the cloud agent git could not settle some paths cleanly
  (rename/file-dir/submodule) so they must be checked before use.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_MERGE_UNSETTLED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_MERGE_UNSETTLED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_MERGE_UNSETTLED_VAR_2
-->
git could not settle these cleanly (a rename on both sides, a file where the other side has a directory, or a submodule), so check them before relying on them: ${SYSTEM_REMINDER_DIR_SYNC_MERGE_UNSETTLED_VAR_0(SYSTEM_REMINDER_DIR_SYNC_MERGE_UNSETTLED_VAR_1.map((SYSTEM_REMINDER_DIR_SYNC_MERGE_UNSETTLED_VAR_2)=>SYSTEM_REMINDER_DIR_SYNC_MERGE_UNSETTLED_VAR_2.path))}.
