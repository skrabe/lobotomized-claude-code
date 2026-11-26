<!--
name: 'System Reminder: Send-to-project memory section routines'
description: Lists the scheduled tasks offered by the brief in the MEMORY.md section
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_SEND_TO_PROJECT_MEMORY_SECTION_ROUTINES_VAR_0
  - SYSTEM_REMINDER_SEND_TO_PROJECT_MEMORY_SECTION_ROUTINES_VAR_1
-->
- Scheduled tasks offered: ${SYSTEM_REMINDER_SEND_TO_PROJECT_MEMORY_SECTION_ROUTINES_VAR_0.map((SYSTEM_REMINDER_SEND_TO_PROJECT_MEMORY_SECTION_ROUTINES_VAR_1)=>SYSTEM_REMINDER_SEND_TO_PROJECT_MEMORY_SECTION_ROUTINES_VAR_1.name).join("; ")}.
