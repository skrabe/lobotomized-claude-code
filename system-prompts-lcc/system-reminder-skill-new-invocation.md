<!--
name: Skill new-invocation reminder
description: >-
  Meta message injected into context telling the agent a previously-loaded skill
  is being newly invoked and to follow its instructions/setup now.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_SKILL_NEW_INVOCATION_VAR_0
  - SYSTEM_REMINDER_SKILL_NEW_INVOCATION_VAR_1
-->
Skill /${SYSTEM_REMINDER_SKILL_NEW_INVOCATION_VAR_0} was loaded earlier (see the invoked-skills reminder above); this is a NEW invocation — follow those instructions now, including any setup steps.${SYSTEM_REMINDER_SKILL_NEW_INVOCATION_VAR_1?` Arguments: ${SYSTEM_REMINDER_SKILL_NEW_INVOCATION_VAR_1}`:""}
