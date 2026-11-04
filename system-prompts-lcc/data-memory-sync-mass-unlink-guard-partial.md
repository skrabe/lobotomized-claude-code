<!--
name: 'Data: memory sync mass-unlink guard (some already deleted)'
description: >-
  Mass-delete guard notice when some synced files were already deleted within
  the last minute: nothing more is deleted this cycle, the rest will be
  restored.
ccVersion: 2.1.318
variables:
  - DATA_MEMORY_SYNC_MASS_UNLINK_GUARD_PARTIAL_VAR_0
  - DATA_MEMORY_SYNC_MASS_UNLINK_GUARD_PARTIAL_VAR_1
-->
Memory sync did NOT delete anything more from shared memory this cycle: ${DATA_MEMORY_SYNC_MASS_UNLINK_GUARD_PARTIAL_VAR_0} synced memory files are missing from this session's disk or were just deleted, too many at once. ${DATA_MEMORY_SYNC_MASS_UNLINK_GUARD_PARTIAL_VAR_1} of them were already deleted from shared memory within the last minute and will not come back. The others will be restored on the next sync. 
