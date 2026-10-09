<!--
name: Shared memory file remains local
description: >-
  Warns that a rejected memory file is not persisted while other memory files
  continue syncing.
ccVersion: 2.1.295
variables:
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_0
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_1
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_2
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_3
-->
The memory file ${DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_0(DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_1.path)} was NOT saved to shared memory (${DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_2.reason}). ${DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_3[Me.reason]??""} Your other memory files keep syncing. This file stays local only, and its changes will be lost when this session's machine is recycled. Once you change or delete it, the next sync tries again. Tell the user this memory file is not being persisted.
