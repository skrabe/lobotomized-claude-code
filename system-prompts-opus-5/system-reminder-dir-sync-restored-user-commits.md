<!--
name: 'System Reminder: Dir Sync Restored User Commits'
description: >-
  Tells the cloud agent it had removed or rewritten commits the user already
  has, so those commits were put back and must not be reset/amended/rebased.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_RESTORED_USER_COMMITS_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_RESTORED_USER_COMMITS_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_RESTORED_USER_COMMITS_VAR_2
-->
You had removed or rewritten ${SYSTEM_REMINDER_DIR_SYNC_RESTORED_USER_COMMITS_VAR_0.restored.truncated?"more than ":""}${SYSTEM_REMINDER_DIR_SYNC_RESTORED_USER_COMMITS_VAR_0.restored.commits.length} commit(s) the user's checkout already has (${SYSTEM_REMINDER_DIR_SYNC_RESTORED_USER_COMMITS_VAR_0.restored.commits.map(SYSTEM_REMINDER_DIR_SYNC_RESTORED_USER_COMMITS_VAR_1).join(", ")}); history the user holds cannot be rewritten from here, so they are back on the work branch. ${SYSTEM_REMINDER_DIR_SYNC_RESTORED_USER_COMMITS_VAR_2} — do not reset, amend or rebase commits the user has.
