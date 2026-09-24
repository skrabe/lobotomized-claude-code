<!--
name: 'System Reminder: Dir Sync Published Commits Off Work Branch'
description: >-
  Tells the cloud agent its commits already on a remote but not on the user's
  branch are now off the work branch (kept at a ref), and not to re-commit or
  cherry-pick their changes, which remain as uncommitted edits.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIR_SYNC_PUBLISHED_COMMITS_OFF_WORK_BRANCH_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_PUBLISHED_COMMITS_OFF_WORK_BRANCH_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_PUBLISHED_COMMITS_OFF_WORK_BRANCH_VAR_2
-->
The ${SYSTEM_REMINDER_DIR_SYNC_PUBLISHED_COMMITS_OFF_WORK_BRANCH_VAR_0.agentCommits.count} commit(s) up to ${SYSTEM_REMINDER_DIR_SYNC_PUBLISHED_COMMITS_OFF_WORK_BRANCH_VAR_1(SYSTEM_REMINDER_DIR_SYNC_PUBLISHED_COMMITS_OFF_WORK_BRANCH_VAR_0.agentCommits.tip)} are already on a remote (a remote-tracking ref has them: fetched, pulled, merged or rebased from it, or pushed) but not on the user's branch, and this checkout follows the user's HEAD, so they are off the work branch now (kept at ${SYSTEM_REMINDER_DIR_SYNC_PUBLISHED_COMMITS_OFF_WORK_BRANCH_VAR_0.agentCommits.ref}, and still on the remote). Do NOT re-commit or cherry-pick their changes, which still stand in the working tree as uncommitted edits (merged with the user's). ${SYSTEM_REMINDER_DIR_SYNC_PUBLISHED_COMMITS_OFF_WORK_BRANCH_VAR_2}
