<!--
name: 'System Reminder: Dir Sync Head Fast-Forwarded'
description: >-
  Cloud dir-sync notice that the user's machine fast-forwarded the work branch
  with new commits.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_HEAD_FAST_FORWARDED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_HEAD_FAST_FORWARDED_VAR_1
-->
The user's machine synced ${SYSTEM_REMINDER_DIR_SYNC_HEAD_FAST_FORWARDED_VAR_0.head.commits} new commit(s): the work branch fast-forwarded ${SYSTEM_REMINDER_DIR_SYNC_HEAD_FAST_FORWARDED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_HEAD_FAST_FORWARDED_VAR_0.head.from)}..${SYSTEM_REMINDER_DIR_SYNC_HEAD_FAST_FORWARDED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_HEAD_FAST_FORWARDED_VAR_0.head.to)}.
