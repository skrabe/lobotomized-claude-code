<!--
name: 'System Reminder: Dir Sync HEAD On Sync Snapshot Commit'
description: >-
  Inner clause of the user-branch-followed reminder: HEAD or the followed branch
  now points at one of directory sync's own snapshot commits, not the agent's
  commit.
ccVersion: 2.1.277
variables:
  - SYSTEM_REMINDER_DIR_SYNC_HEAD_ON_SYNC_SNAPSHOT_COMMIT_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_HEAD_ON_SYNC_SNAPSHOT_COMMIT_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_HEAD_ON_SYNC_SNAPSHOT_COMMIT_VAR_2
  - SYSTEM_REMINDER_DIR_SYNC_HEAD_ON_SYNC_SNAPSHOT_COMMIT_VAR_3
-->
 ${SYSTEM_REMINDER_DIR_SYNC_HEAD_ON_SYNC_SNAPSHOT_COMMIT_VAR_0.to===null?"HEAD":SYSTEM_REMINDER_DIR_SYNC_HEAD_ON_SYNC_SNAPSHOT_COMMIT_VAR_1(SYSTEM_REMINDER_DIR_SYNC_HEAD_ON_SYNC_SNAPSHOT_COMMIT_VAR_0.to)} now points at ${SYSTEM_REMINDER_DIR_SYNC_HEAD_ON_SYNC_SNAPSHOT_COMMIT_VAR_2(SYSTEM_REMINDER_DIR_SYNC_HEAD_ON_SYNC_SNAPSHOT_COMMIT_VAR_3.tip)}, one of directory sync's own snapshot commits this checkout had been pointed at — not a commit of yours; the directory-sync notice says how to put it back.
