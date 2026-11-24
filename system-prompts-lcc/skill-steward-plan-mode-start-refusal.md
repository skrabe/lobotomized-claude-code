<!--
name: 'Skill: Steward plan mode start refusal'
description: >-
  Refusal when the session is in plan mode: the command commits/pushes, nothing
  changed, leave plan mode and run again.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_PLAN_MODE_START_REFUSAL_VAR_0
  - SKILL_STEWARD_PLAN_MODE_START_REFUSAL_VAR_1
  - SKILL_STEWARD_PLAN_MODE_START_REFUSAL_VAR_2
-->
${SKILL_STEWARD_PLAN_MODE_START_REFUSAL_VAR_0} didn't start: this session is in plan mode, and ${SKILL_STEWARD_PLAN_MODE_START_REFUSAL_VAR_1?`${SKILL_STEWARD_PLAN_MODE_START_REFUSAL_VAR_0} commits, pushes, and opens a pull request`:"a watch commits and pushes"}. Nothing changed. Leave plan mode${SKILL_STEWARD_PLAN_MODE_START_REFUSAL_VAR_2()?"":" (Shift+Tab)"}, then run ${SKILL_STEWARD_PLAN_MODE_START_REFUSAL_VAR_0} again.
