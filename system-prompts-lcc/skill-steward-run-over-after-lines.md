<!--
name: 'Skill: Steward run over after lines'
description: >-
  Thrown message joining the result lines and saying the command is over with
  nothing left to do.
ccVersion: 2.1.332
variables:
  - SKILL_STEWARD_RUN_OVER_AFTER_LINES_VAR_0
  - SKILL_STEWARD_RUN_OVER_AFTER_LINES_VAR_1
  - SKILL_STEWARD_RUN_OVER_AFTER_LINES_VAR_2
  - SKILL_STEWARD_RUN_OVER_AFTER_LINES_VAR_3
-->
${SKILL_STEWARD_RUN_OVER_AFTER_LINES_VAR_0.join(" ")}${SKILL_STEWARD_RUN_OVER_AFTER_LINES_VAR_1()}${SKILL_STEWARD_RUN_OVER_AFTER_LINES_VAR_2} is over: nothing is left to do for it.${SKILL_STEWARD_RUN_OVER_AFTER_LINES_VAR_3()}
