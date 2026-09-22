<!--
name: Memory file truncated note
description: >-
  Note appended to injected memory-file content telling the model the file was
  truncated and how to view the full file.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_MEMORY_FILE_TRUNCATED_VAR_0
  - SYSTEM_REMINDER_MEMORY_FILE_TRUNCATED_VAR_1
  - SYSTEM_REMINDER_MEMORY_FILE_TRUNCATED_VAR_2
  - SYSTEM_REMINDER_MEMORY_FILE_TRUNCATED_VAR_3
  - SYSTEM_REMINDER_MEMORY_FILE_TRUNCATED_VAR_4
-->


> This memory file was truncated (${SYSTEM_REMINDER_MEMORY_FILE_TRUNCATED_VAR_0.truncatedByBytes?`${SYSTEM_REMINDER_MEMORY_FILE_TRUNCATED_VAR_1} byte limit`:`first ${SYSTEM_REMINDER_MEMORY_FILE_TRUNCATED_VAR_2} lines`}). Use the ${SYSTEM_REMINDER_MEMORY_FILE_TRUNCATED_VAR_3} tool to view the complete file at: ${SYSTEM_REMINDER_MEMORY_FILE_TRUNCATED_VAR_4}
