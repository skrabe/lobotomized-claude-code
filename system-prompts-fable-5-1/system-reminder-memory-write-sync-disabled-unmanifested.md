<!--
name: 'System Reminder: Memory write sync disabled (unmanifested dir)'
description: >-
  Tool-result note that memory sync is disabled for a directory that held
  content before the memory store was mounted, so writes stay local.
ccVersion: 2.1.219
variables:
  - SYSTEM_REMINDER_MEMORY_WRITE_SYNC_DISABLED_UNMANIFESTED_VAR_0
-->

Memory sync is disabled for this file's directory: it held content before this memory store was mounted (mount_dir_unmanifested_nonempty), so writes here are saved locally but are NOT synced to shared/server memory. To resolve it, rename or relocate the pre-existing directory team/${SYSTEM_REMINDER_MEMORY_WRITE_SYNC_DISABLED_UNMANIFESTED_VAR_0.mountName}/ — the store mounts automatically on the next sync cycle once the directory is empty or gone (within the hour at most, sooner on the next write or restart); deleting its files instead discards them, while writing new files into it first keeps sync disabled.
