<!--
name: 'System Reminder: Skill mention'
description: >-
  Meta user message injected when the user's message contains /<skill-name>: if
  they want it run, call the Skill tool with that skill and any args; if they
  only mention it, do not run it.
ccVersion: 2.1.288
variables:
  - SYSTEM_REMINDER_SKILL_MENTION_VAR_0
  - SYSTEM_REMINDER_SKILL_MENTION_VAR_1
-->
The user's message contains /${SYSTEM_REMINDER_SKILL_MENTION_VAR_0.skillName}, which is the name of a skill. If they are asking you to run it, call the ${SYSTEM_REMINDER_SKILL_MENTION_VAR_1} tool with skill: "${SYSTEM_REMINDER_SKILL_MENTION_VAR_0.skillName}", passing any arguments they gave as args. If they only mention it, do not run it.
