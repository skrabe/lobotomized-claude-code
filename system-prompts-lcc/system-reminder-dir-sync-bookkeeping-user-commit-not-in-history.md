<!--
name: 'System Reminder: Dir Sync Bookkeeping User Commit Not In History'
description: >-
  Bookkeeping-commit reminder arm when the user's current commit is not in this
  history: their machine takes nothing until git reset moves the branch back
  onto their history.
ccVersion: 2.1.277
variables:
  - SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_USER_COMMIT_NOT_IN_HISTORY_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_USER_COMMIT_NOT_IN_HISTORY_VAR_1
-->
The user's current commit ${SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_USER_COMMIT_NOT_IN_HISTORY_VAR_0} is not in this history (they committed, or moved their branch, since that snapshot), so their machine takes nothing from these turns until the branch is back on their history. \`git reset ${SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_USER_COMMIT_NOT_IN_HISTORY_VAR_0}\` moves the branch there without touching the files${SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_USER_COMMIT_NOT_IN_HISTORY_VAR_1===null?"":`; then compare the files with the user's own as last synced here, uncommitted work included: ${SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_USER_COMMIT_NOT_IN_HISTORY_VAR_1}; then \`git diff <that ref>\`, and restore from that snapshot every path you did not deliberately change (\`git checkout <that ref> -- <path>\`) — left stale, those paths would reach the user's machine as reverts of their newer work`}.
