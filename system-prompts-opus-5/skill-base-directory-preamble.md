<!--
name: Skill base directory preamble
description: >-
  Prefix prepended to a skill's prompt in getPromptForCommand (skill mode)
  telling the model the skill's base directory before its instructions, injected
  into the model context.
ccVersion: 2.1.246
variables:
  - SKILL_BASE_DIRECTORY_PREAMBLE_VAR_0
  - SKILL_BASE_DIRECTORY_PREAMBLE_VAR_1
  - SKILL_BASE_DIRECTORY_PREAMBLE_VAR_2
-->
Base directory for this skill: ${SKILL_BASE_DIRECTORY_PREAMBLE_VAR_0(SKILL_BASE_DIRECTORY_PREAMBLE_VAR_1.filePath)}

${SKILL_BASE_DIRECTORY_PREAMBLE_VAR_2}
