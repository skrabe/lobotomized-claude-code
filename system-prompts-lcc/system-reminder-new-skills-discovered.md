<!--
name: New skills discovered reminder
description: System reminder injected when new skills become available via the Skill tool.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_VAR_0
  - SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_VAR_1
  - SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_VAR_2
-->
New skills discovered in ${SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_VAR_0}, now available via the Skill tool:
${SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_VAR_1.map((SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_VAR_2)=>`- ${SYSTEM_REMINDER_NEW_SKILLS_DISCOVERED_VAR_2}`).join(`
`)}
