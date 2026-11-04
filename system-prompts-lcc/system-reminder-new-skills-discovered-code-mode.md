<!--
name: 'System Reminder: New skills discovered (Code Mode)'
description: >-
  Code Mode variant announcing newly discovered skills loadable with tools.Skill
  from a script
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_CODE_MODE_VAR_0
  - SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_CODE_MODE_VAR_1
  - SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_CODE_MODE_VAR_2
-->
New skills discovered in ${SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_CODE_MODE_VAR_0}, now loadable with \`tools.Skill\` from a script:
${SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_CODE_MODE_VAR_1.map((SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_CODE_MODE_VAR_2)=>`- ${SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_CODE_MODE_VAR_2}`).join(`
`)}
