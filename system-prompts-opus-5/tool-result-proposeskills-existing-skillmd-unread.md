<!--
name: 'Tool Result: ProposeSkills Existing SKILL.md Unread'
description: >-
  ProposeSkills validateInput failure telling the model to read the current
  SKILL.md before proposing a full replacement.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_PROPOSESKILLS_EXISTING_SKILLMD_UNREAD_VAR_0
-->
Existing SKILL.md not read yet for ${TOOL_RESULT_PROPOSESKILLS_EXISTING_SKILLMD_UNREAD_VAR_0.join(", ")}. A saved proposal replaces a skill's SKILL.md entirely — read ${TOOL_RESULT_PROPOSESKILLS_EXISTING_SKILLMD_UNREAD_VAR_0.length===1?"that file":"those files"} first, then propose the complete updated SKILL.md.
