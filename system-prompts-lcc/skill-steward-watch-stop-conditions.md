<!--
name: 'Skill: Steward watch stop conditions'
description: >-
  Stop condition for a git-only watch: the branch is gone from its remote or
  adds nothing to the base any more, or the host stays out of reach for some two
  hours
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_WATCH_STOP_CONDITIONS_VAR_0
  - SKILL_STEWARD_WATCH_STOP_CONDITIONS_VAR_1
  - SKILL_STEWARD_WATCH_STOP_CONDITIONS_VAR_2
  - SKILL_STEWARD_WATCH_STOP_CONDITIONS_VAR_3
-->
${SKILL_STEWARD_WATCH_STOP_CONDITIONS_VAR_0} is gone from ${SKILL_STEWARD_WATCH_STOP_CONDITIONS_VAR_1} or adds nothing to ${SKILL_STEWARD_WATCH_STOP_CONDITIONS_VAR_2} any more, or when ${SKILL_STEWARD_WATCH_STOP_CONDITIONS_VAR_3} stays out of reach for some two hours
