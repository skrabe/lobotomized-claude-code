<!--
name: Memory Sync Held Local Replaced By Shared
description: >-
  Notice that a never-synced local memory file was replaced by another session's
  shared file, so re-read it; the local copy was not kept.
ccVersion: 2.1.276
variables:
  - DATA_MEMORY_SYNC_HELD_LOCAL_REPLACED_BY_SHARED_VAR_0
  - DATA_MEMORY_SYNC_HELD_LOCAL_REPLACED_BY_SHARED_VAR_1
-->
The local copy of the memory file ${DATA_MEMORY_SYNC_HELD_LOCAL_REPLACED_BY_SHARED_VAR_0(DATA_MEMORY_SYNC_HELD_LOCAL_REPLACED_BY_SHARED_VAR_1)}, kept on this machine and never saved to shared memory, was replaced: another session saved a file at that path. The file on disk now has the shared version. Re-read it. The local copy was not kept, so anything from it that is still wanted has to come from the user.
