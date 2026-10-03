<!--
name: 'Tool Result: ProposeSkills SKILL.md could not be read'
description: >-
  Tells Claude that the current SKILL.md of a skill it proposed to update or
  replace could not be read, to call again once, and otherwise tell the user or
  choose another name
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_PROPOSESKILLS_SKILL_MD_COULD_NOT_BE_READ_VAR_0
  - TOOL_RESULT_PROPOSESKILLS_SKILL_MD_COULD_NOT_BE_READ_VAR_1
  - TOOL_RESULT_PROPOSESKILLS_SKILL_MD_COULD_NOT_BE_READ_VAR_2
-->
${TOOL_RESULT_PROPOSESKILLS_SKILL_MD_COULD_NOT_BE_READ_VAR_0} could not be read. Call again once; if it still cannot be read, ${TOOL_RESULT_PROPOSESKILLS_SKILL_MD_COULD_NOT_BE_READ_VAR_1?"tell the user the skill cannot be updated right now":TOOL_RESULT_PROPOSESKILLS_SKILL_MD_COULD_NOT_BE_READ_VAR_2}.
