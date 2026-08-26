<!--
name: 'System Reminder: Dir Sync Head Moved'
description: >-
  Cloud dir-sync notice that the user moved their checkout (branch
  switch/rebase/amend/reset) so the work branch now points at a history that
  does not contain the previous HEAD.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_HEAD_MOVED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_HEAD_MOVED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_HEAD_MOVED_VAR_2
-->
The user moved their checkout${SYSTEM_REMINDER_DIR_SYNC_HEAD_MOVED_VAR_0.head.laptopBranch===null?"":` (now on ${SYSTEM_REMINDER_DIR_SYNC_HEAD_MOVED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_HEAD_MOVED_VAR_0.head.laptopBranch)})`} to ${SYSTEM_REMINDER_DIR_SYNC_HEAD_MOVED_VAR_2(SYSTEM_REMINDER_DIR_SYNC_HEAD_MOVED_VAR_0.head.to)}, which does not contain the previous HEAD ${SYSTEM_REMINDER_DIR_SYNC_HEAD_MOVED_VAR_2(SYSTEM_REMINDER_DIR_SYNC_HEAD_MOVED_VAR_0.head.from)} (a branch switch, rebase, amend or reset on their side); the work branch now points there, and commits that were only on the previous history are no longer on it.
