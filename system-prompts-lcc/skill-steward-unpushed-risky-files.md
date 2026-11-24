<!--
name: 'Skill: Steward unpushed risky files'
description: >-
  Lists files in the unpushed commits that can run code or set rules elsewhere,
  which the command doesn't push, followed by the push-or-remove choice.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_0
  - SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_1
  - SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_2
  - SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_3
  - SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_4
-->
Your unpushed commits change ${SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_0(SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_1.risky.length,"a file","files")} that can run code or set rules elsewhere: ${SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_2(SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_1.risky)}. ${SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_3} doesn't push such ${SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_0(SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_1.risky.length,"a file","files")}. ${SKILL_STEWARD_UNPUSHED_RISKY_FILES_VAR_4}
