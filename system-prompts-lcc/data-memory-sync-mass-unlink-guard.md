<!--
name: 'Memory Sync: Mass-Deletion Guard Notice'
description: >-
  Notice queued when many synced memory files vanish at once; injected into the
  model's context as PostToolUse additionalContext explaining that shared memory
  was not deleted.
ccVersion: 2.1.280
variables:
  - DATA_MEMORY_SYNC_MASS_UNLINK_GUARD_VAR_0
  - DATA_MEMORY_SYNC_MASS_UNLINK_GUARD_VAR_1
-->
Memory sync deleted nothing from shared memory this cycle: ${DATA_MEMORY_SYNC_MASS_UNLINK_GUARD_VAR_0} synced memory files went missing from this session's disk at once, and will be restored on the next sync. If you really do intend to remove that many memories, wait until the missing files have been restored, then delete at most ${DATA_MEMORY_SYNC_MASS_UNLINK_GUARD_VAR_1} at a time with about a minute between batches so memory sync can apply each one.
