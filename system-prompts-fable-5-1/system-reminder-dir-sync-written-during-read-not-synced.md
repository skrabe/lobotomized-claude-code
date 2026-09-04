<!--
name: Dir Sync Written During Read Not Synced
description: >-
  User-machine dir-sync report that files still being written in the cloud
  checkout were not synced this turn and stay as last received until they are at
  rest.
ccVersion: 2.1.261
variables:
  - SYSTEM_REMINDER_DIR_SYNC_WRITTEN_DURING_READ_NOT_SYNCED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_WRITTEN_DURING_READ_NOT_SYNCED_VAR_1
-->
Still being written in the cloud session when the turn's files were read, so not synced this time: ${SYSTEM_REMINDER_DIR_SYNC_WRITTEN_DURING_READ_NOT_SYNCED_VAR_0}${SYSTEM_REMINDER_DIR_SYNC_WRITTEN_DURING_READ_NOT_SYNCED_VAR_1}; your machine keeps what it last had there, and the file goes out with the next turn that finds it at rest.
