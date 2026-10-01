<!--
name: 'Data: Memory sync file not saved stays local'
description: >-
  Memory-sync notice that shared memory refused a memory file, so it stays local
  only; tells the model to tell the user it is not persisted.
ccVersion: 2.1.286
variables:
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_0
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_1
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_2
  - DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_3
-->
The memory file ${DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_0(DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_1.path)} was NOT saved to shared memory (${DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_2.reason}). ${DATA_MEMORY_SYNC_FILE_NOT_SAVED_STAYS_LOCAL_VAR_3[Ge.reason]??""} Your other memory files keep syncing. This file stays local only, and its changes will be lost when this session's machine is recycled. Once you change or delete it, the next sync tries again. Tell the user this memory file is not being persisted.
