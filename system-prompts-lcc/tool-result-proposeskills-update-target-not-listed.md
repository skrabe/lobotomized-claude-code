<!--
name: 'Tool Result: ProposeSkills update target not listed'
description: >-
  Tells Claude that a skill it proposed to update is not among the skills this
  session lists, so it should call again once and otherwise tell the user and
  propose a new skill name only if wanted
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_0
  - TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_1
  - TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_2
-->
${TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_0(TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_1(TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_2))} is not among the user's skills that this session lists right now, so it cannot be updated yet. Call again once; if it is still not listed, tell the user, and propose it as a new skill under another name only if they want that.
