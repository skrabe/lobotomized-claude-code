<!--
name: ProposeSkills Read Before Improve
description: >-
  ProposeSkills validateInput envelope telling the model a saved proposal
  replaces SKILL.md entirely, so unread or stale files must be read first.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_PROPOSESKILLS_READ_BEFORE_IMPROVE_VAR_0
  - TOOL_RESULT_PROPOSESKILLS_READ_BEFORE_IMPROVE_VAR_1
  - TOOL_RESULT_PROPOSESKILLS_READ_BEFORE_IMPROVE_VAR_2
-->
${TOOL_RESULT_PROPOSESKILLS_READ_BEFORE_IMPROVE_VAR_0.join(" ")} A saved proposal replaces a skill's SKILL.md entirely — read ${TOOL_RESULT_PROPOSESKILLS_READ_BEFORE_IMPROVE_VAR_1===1?"that whole file":"those whole files"} ${TOOL_RESULT_PROPOSESKILLS_READ_BEFORE_IMPROVE_VAR_2.length===0?"again":"first"}, then propose the complete updated SKILL.md.
