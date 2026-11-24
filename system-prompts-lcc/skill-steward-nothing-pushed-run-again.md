<!--
name: 'Skill: Steward nothing pushed, run again'
description: >-
  Nothing committed/pushed message that wraps the reason (Do) and the run-again
  instruction, with an optional review hint.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_0
  - SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_1
  - SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_2
  - SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_3
  - SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_4
-->
Nothing ${SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_0.isClean?"":"committed or "}pushed${SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_1===0?".":":"} ${SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_2} ${SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_3} again.${SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_1===0?` For a review meanwhile, run /${SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_4}.`:""}
