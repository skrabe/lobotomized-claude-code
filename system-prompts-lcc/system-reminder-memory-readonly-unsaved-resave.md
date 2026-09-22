<!--
name: 'System Reminder: Memory Readonly Unsaved Resave'
description: >-
  Tells Claude read-only memory files were not shared and where to re-save the
  content if it claimed they were remembered.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_MEMORY_READONLY_UNSAVED_RESAVE_VAR_0
-->
To keep content you wrote, ${SYSTEM_REMINDER_MEMORY_READONLY_UNSAVED_RESAVE_VAR_0}. If you told the user this was saved or remembered, tell them plainly that it was not shared and where you re-saved it (describe the memory location in plain terms, not as a filesystem path).
