<!--
name: 'System reminder: memory delete failed, will be restored'
description: >-
  Tells the model memory sync could not delete a file from shared memory, so it
  stays and will be restored locally at next sync.
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_MEMORY_DELETE_FAILED_RESTORED_VAR_0
  - SYSTEM_REMINDER_MEMORY_DELETE_FAILED_RESTORED_VAR_1
-->
Memory sync could not delete ${SYSTEM_REMINDER_MEMORY_DELETE_FAILED_RESTORED_VAR_0(SYSTEM_REMINDER_MEMORY_DELETE_FAILED_RESTORED_VAR_1.path)} from shared memory, so it stays there and will be restored on this machine at the next sync.
