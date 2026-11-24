<!--
name: 'Skill: Steward git pass status line'
description: Asks for one short status line at the end of a git watch pass
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_GIT_PASS_STATUS_LINE_VAR_0
  - SKILL_STEWARD_GIT_PASS_STATUS_LINE_VAR_2
  - SKILL_STEWARD_GIT_PASS_STATUS_LINE_VAR_1
-->
write one short status line: what this pass did, and that you look again when something changes. ${SKILL_STEWARD_GIT_PASS_STATUS_LINE_VAR_0({preArmStatus:SKILL_STEWARD_GIT_PASS_STATUS_LINE_VAR_2,briefMode:SKILL_STEWARD_GIT_PASS_STATUS_LINE_VAR_1()})}
