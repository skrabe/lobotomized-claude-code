<!--
name: 'System Reminder: Skill listing wrapper (Code Mode)'
description: >-
  Code Mode variant of the skill listing wrapper explaining that a script loads
  a skill with tools.Skill and its instructions arrive after the script result
ccVersion: 2.1.322
variables:
  - SYSTEM_REMINDER_SKILL_LISTING_WRAPPER_CODE_MODE_VAR_0
  - SYSTEM_REMINDER_SKILL_LISTING_WRAPPER_CODE_MODE_VAR_1
  - SYSTEM_REMINDER_SKILL_LISTING_WRAPPER_CODE_MODE_VAR_2
-->
The following skills are ${SYSTEM_REMINDER_SKILL_LISTING_WRAPPER_CODE_MODE_VAR_0}available; a script loads one with \`await tools.Skill({skill: "name"})\`, and its instructions arrive as a message right after the script's result${SYSTEM_REMINDER_SKILL_LISTING_WRAPPER_CODE_MODE_VAR_1}:

${SYSTEM_REMINDER_SKILL_LISTING_WRAPPER_CODE_MODE_VAR_2.content}
