<!--
name: 'System Reminder: Dir Sync Bookkeeping Reset To User Commit'
description: >-
  Bookkeeping-commit reminder arm when the user's head is named: file changes
  still reach the user as uncommitted changes, so git reset to their commit and
  re-commit only your own changes by path.
ccVersion: 2.1.277
variables:
  - SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_RESET_TO_USER_COMMIT_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_RESET_TO_USER_COMMIT_VAR_1
-->
Your file changes keep reaching the user's machine, but as uncommitted changes on their current commit ${SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_RESET_TO_USER_COMMIT_VAR_0}, and no commit of yours lands there until the branch is back on real history. \`git reset ${SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_RESET_TO_USER_COMMIT_VAR_0}\` puts it back and keeps the working files exactly as they are; then re-commit only your own changes, by path — not the user's uncommitted work this checkout mirrors${SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_RESET_TO_USER_COMMIT_VAR_1===null?"":` (after a hard reset, compare the files with the user's own as last synced here: ${SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_RESET_TO_USER_COMMIT_VAR_1}; then \`git diff <that ref>\`, and restore from that snapshot any path you did not deliberately change (\`git checkout <that ref> -- <path>\`))`}.
