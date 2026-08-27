<!--
name: 'System Reminder: Memory File Approaching Recall Limit'
description: >-
  PostToolUse additionalContext when a memory file is approaching the recall
  cap.
ccVersion: 2.1.247
variables:
  - SYSTEM_REMINDER_MEMORY_FILE_APPROACHING_RECALL_LIMIT_VAR_0
  - SYSTEM_REMINDER_MEMORY_FILE_APPROACHING_RECALL_LIMIT_VAR_1
-->
The memory file at ${SYSTEM_REMINDER_MEMORY_FILE_APPROACHING_RECALL_LIMIT_VAR_0} is ${SYSTEM_REMINDER_MEMORY_FILE_APPROACHING_RECALL_LIMIT_VAR_1.sizeDesc}, approaching the ${SYSTEM_REMINDER_MEMORY_FILE_APPROACHING_RECALL_LIMIT_VAR_1.capDesc} recall limit. Keep it to one fact under ${SYSTEM_REMINDER_MEMORY_FILE_APPROACHING_RECALL_LIMIT_VAR_1.targetDesc}: summarize rather than append, and split distinct facts into their own files.
