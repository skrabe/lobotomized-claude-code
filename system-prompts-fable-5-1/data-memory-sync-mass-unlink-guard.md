<!--
name: 'Memory Sync: Mass-Deletion Guard Notice'
description: >-
  Notice queued when many synced memory files vanish at once; injected into
  the model's context as PostToolUse additionalContext explaining that shared
  memory was not deleted.
ccVersion: 2.1.218
variables:
  - DATA_MEMORY_SYNC_MASS_UNLINK_GUARD_VAR_0
-->
Memory sync deleted nothing from shared memory this cycle: ${DATA_MEMORY_SYNC_MASS_UNLINK_GUARD_VAR_0} synced memory files went missing from this session's disk at once, and will be restored on the next sync. To remove that many memories deliberately, delete them in smaller batches.
