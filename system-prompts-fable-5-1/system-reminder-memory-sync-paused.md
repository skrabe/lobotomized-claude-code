<!--
name: Memory sync paused
description: >-
  Memory-sync status notice injected into the model's context via
  additionalContext warning a memory store's sync is paused and writes will be
  lost.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_MEMORY_SYNC_PAUSED_VAR_0
  - SYSTEM_REMINDER_MEMORY_SYNC_PAUSED_VAR_1
-->
Memory sync is paused for one of your memory stores (${SYSTEM_REMINDER_MEMORY_SYNC_PAUSED_VAR_0}): ${SYSTEM_REMINDER_MEMORY_SYNC_PAUSED_VAR_1} Affected memory writes are NOT being persisted to shared memory and will be lost when this session's machine is recycled.
