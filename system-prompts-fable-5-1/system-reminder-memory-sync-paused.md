<!--
name: 'System Reminder: Memory Sync Paused'
description: >-
  Notice that memory sync is paused for a store so local writes are not
  persisted to shared memory.
ccVersion: 2.1.274
variables:
  - SYSTEM_REMINDER_MEMORY_SYNC_PAUSED_VAR_0
  - SYSTEM_REMINDER_MEMORY_SYNC_PAUSED_VAR_1
  - SYSTEM_REMINDER_MEMORY_SYNC_PAUSED_VAR_2
-->
Memory sync is paused for one of your memory stores (${SYSTEM_REMINDER_MEMORY_SYNC_PAUSED_VAR_0}): ${SYSTEM_REMINDER_MEMORY_SYNC_PAUSED_VAR_1}${SYSTEM_REMINDER_MEMORY_SYNC_PAUSED_VAR_2} Affected memory writes are NOT being persisted to shared memory and will be lost when this session's machine is recycled.
