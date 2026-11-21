<!--
name: 'System Reminder: Setup choices header'
description: >-
  Heading for the user's setup choices block that wraps the chosen check-in
  rules
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_SETUP_CHOICES_HEADER_VAR_0
  - SYSTEM_REMINDER_SETUP_CHOICES_HEADER_VAR_1
  - SYSTEM_REMINDER_SETUP_CHOICES_HEADER_VAR_2
-->
# This user's setup choices
${["The user chose this at setup. They are at the keyboard and will reply.",...SYSTEM_REMINDER_SETUP_CHOICES_HEADER_VAR_0.map((SYSTEM_REMINDER_SETUP_CHOICES_HEADER_VAR_1)=>SYSTEM_REMINDER_SETUP_CHOICES_HEADER_VAR_2[SYSTEM_REMINDER_SETUP_CHOICES_HEADER_VAR_1]),"Do not save this to memory or pass it to other agents."].join(`

`)}
