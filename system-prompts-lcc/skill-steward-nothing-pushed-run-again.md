<!--
name: 'Skill: Steward nothing pushed, run again'
description: >-
  Nothing committed/pushed message that wraps the reason (Do) and the run-again
  instruction; the review hint is now appended by a separate wrapper.
ccVersion: 2.1.332
variables:
  - SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_0
  - SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_1
  - SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_2
  - SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_3
-->
Nothing ${SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_0.isClean?"":"committed or "}pushed${SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_1===0?".":":"} ${SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_2} ${SKILL_STEWARD_NOTHING_PUSHED_RUN_AGAIN_VAR_3} again.
