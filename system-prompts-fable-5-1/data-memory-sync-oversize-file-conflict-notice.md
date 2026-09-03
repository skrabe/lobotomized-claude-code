<!--
name: 'Data: Memory Sync Oversize File Notice'
description: >-
  Injected as PostToolUse additionalContext after Read/Edit/Write on a synced
  memory file that exceeds the per-file sync limit, telling Claude the file is
  saved locally but not synced to shared memory.
ccVersion: 2.1.224
variables:
  - DATA_MEMORY_SYNC_OVERSIZE_FILE_CONFLICT_NOTICE_VAR_0
  - DATA_MEMORY_SYNC_OVERSIZE_FILE_CONFLICT_NOTICE_VAR_1
  - DATA_MEMORY_SYNC_OVERSIZE_FILE_CONFLICT_NOTICE_VAR_2
  - DATA_MEMORY_SYNC_OVERSIZE_FILE_CONFLICT_NOTICE_VAR_3
-->
The memory file ${DATA_MEMORY_SYNC_OVERSIZE_FILE_CONFLICT_NOTICE_VAR_0(DATA_MEMORY_SYNC_OVERSIZE_FILE_CONFLICT_NOTICE_VAR_1.path)} is ${DATA_MEMORY_SYNC_OVERSIZE_FILE_CONFLICT_NOTICE_VAR_2(DATA_MEMORY_SYNC_OVERSIZE_FILE_CONFLICT_NOTICE_VAR_1.size)}, over the ${DATA_MEMORY_SYNC_OVERSIZE_FILE_CONFLICT_NOTICE_VAR_2(DATA_MEMORY_SYNC_OVERSIZE_FILE_CONFLICT_NOTICE_VAR_3)} per-file sync limit — it is saved locally but is NOT synced to shared memory, so its changes will be lost when this session's machine is recycled and other sessions only see the last version that was under the limit. 
