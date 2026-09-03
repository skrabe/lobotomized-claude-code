<!--
name: 'System Reminder: Project Memory Re-Pick Pending'
description: >-
  Warns the model that a project-memory re-pick is still being applied, making
  prior memory context stale until the connection is checked again.
ccVersion: 2.1.227
variables:
  - SYSTEM_REMINDER_PROJECT_MEMORY_REPICK_PENDING_VAR_0
  - SYSTEM_REMINDER_PROJECT_MEMORY_REPICK_PENDING_VAR_1
  - SYSTEM_REMINDER_PROJECT_MEMORY_REPICK_PENDING_VAR_2
  - SYSTEM_REMINDER_PROJECT_MEMORY_REPICK_PENDING_VAR_3
-->
This session is no longer connected to ${SYSTEM_REMINDER_PROJECT_MEMORY_REPICK_PENDING_VAR_0(SYSTEM_REMINDER_PROJECT_MEMORY_REPICK_PENDING_VAR_1.project)} (a re-pick in /memory is still being applied). Any connected memory store list or shared memory index your system prompt may carry, and any ${SYSTEM_REMINDER_PROJECT_MEMORY_REPICK_PENDING_VAR_2} results earlier in this conversation, are stale. Call ${SYSTEM_REMINDER_PROJECT_MEMORY_REPICK_PENDING_VAR_3} with no arguments to check what, if anything, is connected before relying on the memory tools again.
