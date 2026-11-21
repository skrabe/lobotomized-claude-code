<!--
name: 'Skill: /loop external wakeup — stop after max age'
description: 'Re-arm limit: stop after at most the recurring maximum age.'
ccVersion: 2.1.330
variables:
  - SKILL_LOOP_EXTERNAL_WAKEUP_MAX_AGE_VAR_0
  - SKILL_LOOP_EXTERNAL_WAKEUP_MAX_AGE_VAR_1
-->
stop after at most ${SKILL_LOOP_EXTERNAL_WAKEUP_MAX_AGE_VAR_0(SKILL_LOOP_EXTERNAL_WAKEUP_MAX_AGE_VAR_1)}
