<!--
name: Dir Sync Stopped Emptied Except Unmoved
description: >-
  Stopped-sync reminder clause that emptying left some entries that could not be
  moved and are stale.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_EXCEPT_UNMOVED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_EXCEPT_UNMOVED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_EXCEPT_UNMOVED_VAR_2
-->
this session's synced copy of the project at ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_EXCEPT_UNMOVED_VAR_0} has been emptied (git history included) except for ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_EXCEPT_UNMOVED_VAR_1.left.length} ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_EXCEPT_UNMOVED_VAR_1.left.length===1?"entry":"entries"} that could not be moved and ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_EXCEPT_UNMOVED_VAR_1.left.length===1?"is":"are"} still there — stale, leave ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_EXCEPT_UNMOVED_VAR_1.left.length===1?"it":"them"} alone: ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_EXCEPT_UNMOVED_VAR_1.left.map(SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_EXCEPT_UNMOVED_VAR_2).join(", ")}.
