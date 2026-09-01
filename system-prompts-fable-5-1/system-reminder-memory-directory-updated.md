<!--
name: Memory Directory Updated Reminder
description: >-
  Model-facing system-reminder (memory_update case in the L6l registry, isMeta
  meta-message) announcing that a source updated the agent's memory directory
  and which files changed.
ccVersion: 2.1.191
variables:
  - SYSTEM_REMINDER_MEMORY_DIRECTORY_UPDATED_VAR_0
  - SYSTEM_REMINDER_MEMORY_DIRECTORY_UPDATED_VAR_1
-->
${SYSTEM_REMINDER_MEMORY_DIRECTORY_UPDATED_VAR_0[e.source]} updated your memory directory: ${SYSTEM_REMINDER_MEMORY_DIRECTORY_UPDATED_VAR_1.summary}
