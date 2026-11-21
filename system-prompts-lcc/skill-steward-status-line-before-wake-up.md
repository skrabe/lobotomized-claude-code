<!--
name: 'Skill: Steward status line before wake-up'
description: >-
  Asks for one short status line saying what the pass did, what the pull request
  waits for, and that Claude looks again
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_STATUS_LINE_BEFORE_WAKE_UP_VAR_0
  - SKILL_STEWARD_STATUS_LINE_BEFORE_WAKE_UP_VAR_2
  - SKILL_STEWARD_STATUS_LINE_BEFORE_WAKE_UP_VAR_1
-->
write one short status line: what this pass did, what the pull request waits for, and that you look again when something changes. ${SKILL_STEWARD_STATUS_LINE_BEFORE_WAKE_UP_VAR_0({preArmStatus:SKILL_STEWARD_STATUS_LINE_BEFORE_WAKE_UP_VAR_2,briefMode:SKILL_STEWARD_STATUS_LINE_BEFORE_WAKE_UP_VAR_1()})}
