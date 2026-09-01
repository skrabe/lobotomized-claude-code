<!--
name: 'Memory Write Warning: Synced Project Memory Parked Or Ended'
description: >-
  Warning injected into the model's context after a memory write when the
  discovery-sourced synced project memory session state is parked/ended, so
  the store is not syncing.
ccVersion: 2.1.218
variables:
  - DATA_MEMORY_SYNC_SYNCED_PROJECT_PARKED_OR_ENDED_VAR_0
-->
Synced project memory is ${DATA_MEMORY_SYNC_SYNCED_PROJECT_PARKED_OR_ENDED_VAR_0.state} for this session; this write was saved locally, not persisted to shared memory.
