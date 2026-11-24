<!--
name: 'Skill: Steward unpushed files may hold secrets'
description: >-
  Lists files in the unpushed commits whose names suggest secrets, followed by
  the push-or-remove choice.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_UNPUSHED_SECRETS_FILES_VAR_0
  - SKILL_STEWARD_UNPUSHED_SECRETS_FILES_VAR_1
  - SKILL_STEWARD_UNPUSHED_SECRETS_FILES_VAR_2
  - SKILL_STEWARD_UNPUSHED_SECRETS_FILES_VAR_3
-->
By ${SKILL_STEWARD_UNPUSHED_SECRETS_FILES_VAR_0(SKILL_STEWARD_UNPUSHED_SECRETS_FILES_VAR_1.secrets.length,"its name, this file","their names, these files")} in your unpushed commits may hold secrets: ${SKILL_STEWARD_UNPUSHED_SECRETS_FILES_VAR_2(SKILL_STEWARD_UNPUSHED_SECRETS_FILES_VAR_1.secrets)}. ${SKILL_STEWARD_UNPUSHED_SECRETS_FILES_VAR_3}
