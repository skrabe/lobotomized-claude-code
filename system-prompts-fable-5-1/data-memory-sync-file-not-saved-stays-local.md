<!--
name: 'Data: Memory Sync File Not Saved Stays Local'
description: >-
  PostToolUse additionalContext when the server refused one memory file: it
  stays local, other files keep syncing, and the model should tell the user.
ccVersion: 2.1.277
variables:
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_0
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_1
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_2
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_3
-->
The memory file ${DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_0(DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_1.path)} was NOT saved to shared memory (${DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_2.reason}). ${DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_3[Qt.reason]??""} Your other memory files keep syncing. This file stays local only, and its changes will be lost when this session's machine is recycled. Once you change or delete it, the next sync tries again. Tell the user this memory file is not being persisted.
