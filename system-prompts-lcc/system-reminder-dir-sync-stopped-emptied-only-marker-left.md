<!--
name: Dir Sync Stopped Emptied Only Marker Left
description: >-
  Stopped-sync reminder clause that the synced copy was emptied (git history
  included), optionally noting where everything was moved, and only
  FILE_SYNC_STOPPED.md is left.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_ONLY_MARKER_LEFT_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_ONLY_MARKER_LEFT_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_ONLY_MARKER_LEFT_VAR_2
-->
this session's synced copy of the project at ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_ONLY_MARKER_LEFT_VAR_0} has been EMPTIED (git history included)${SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_ONLY_MARKER_LEFT_VAR_1===null?"":` — everything that stood there was moved under ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_ONLY_MARKER_LEFT_VAR_1}, not deleted`}; only ${SYSTEM_REMINDER_DIR_SYNC_STOPPED_EMPTIED_ONLY_MARKER_LEFT_VAR_2} is left.
