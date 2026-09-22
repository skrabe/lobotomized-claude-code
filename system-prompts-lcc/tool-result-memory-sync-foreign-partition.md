<!--
name: 'Tool Result: Memory sync foreign partition'
description: >-
  Tool-result note that a directory already holds another memory store's synced
  content, so writes here are saved locally but not synced.
ccVersion: 2.1.219
variables:
  - TOOL_RESULT_MEMORY_SYNC_FOREIGN_PARTITION_VAR_0
-->
Memory sync is disabled for this file's directory: it already holds the synced memory of a different memory store (mount_dir_foreign_partition), so writes here are saved locally but are NOT synced to shared/server memory. To resolve it, rename or relocate the conflicting directory team/${TOOL_RESULT_MEMORY_SYNC_FOREIGN_PARTITION_VAR_0.mountName}/ — sync re-enables automatically on the next sync cycle once it is out of the way (within the hour at most, sooner on the next write or restart); deleting it instead discards any unsynced files inside it, and writing new files into it first keeps sync disabled — 
