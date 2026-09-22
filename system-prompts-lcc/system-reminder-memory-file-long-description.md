<!--
name: 'System Reminder: Memory File Long Description'
description: >-
  PostToolUse additionalContext lint telling the model to shorten a memory
  file's description.
ccVersion: 2.1.247
variables:
  - SYSTEM_REMINDER_MEMORY_FILE_LONG_DESCRIPTION_VAR_0
  - SYSTEM_REMINDER_MEMORY_FILE_LONG_DESCRIPTION_VAR_1
-->
This memory file's \`description\` is ${SYSTEM_REMINDER_MEMORY_FILE_LONG_DESCRIPTION_VAR_0.length} characters. Recall matches on it as a one-line summary; shorten it to one specific line (about ${SYSTEM_REMINDER_MEMORY_FILE_LONG_DESCRIPTION_VAR_1/2} characters) that says what question the file answers.
