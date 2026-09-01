<!--
name: Dir Sync Stopped Repository Left Stale
description: >-
  Stopped-sync reminder clause that the session copy was emptied except the
  repository itself, which is stale until a later worker finishes the move.
ccVersion: 2.1.257
variables:
  - SYSTEM_REMINDER_DIR_SYNC_STOPPED_REPOSITORY_LEFT_STALE_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_STOPPED_REPOSITORY_LEFT_STALE_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_STOPPED_REPOSITORY_LEFT_STALE_VAR_2
  - SYSTEM_REMINDER_DIR_SYNC_STOPPED_REPOSITORY_LEFT_STALE_VAR_3
-->
this session's copy of the project at ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_REPOSITORY_LEFT_STALE_VAR_0} was emptied into ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_REPOSITORY_LEFT_STALE_VAR_1(SYSTEM_REMINDER_DIR_SYNC_STOPPED_REPOSITORY_LEFT_STALE_VAR_2.setAsideIn)} EXCEPT the repository itself (${SYSTEM_REMINDER_DIR_SYNC_STOPPED_REPOSITORY_LEFT_STALE_VAR_2.left.map(SYSTEM_REMINDER_DIR_SYNC_STOPPED_REPOSITORY_LEFT_STALE_VAR_3).join(", ")} could not be moved and ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_REPOSITORY_LEFT_STALE_VAR_2.left.length===1?"is":"are"} still there) — what is left is STALE: do not read, run or edit anything there; a later worker process finishes the move.
