<!--
name: 'Tool Result: ProposeSkills update target not listed'
description: >-
  Tells Claude that a skill it proposed to update is not among the skills this
  session lists, so it should call again once and otherwise tell the user and
  propose a new skill name only if wanted
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_0
  - TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_1
  - TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_2
-->
${TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_0(TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_1(TOOL_RESULT_PROPOSESKILLS_UPDATE_TARGET_NOT_LISTED_VAR_2))} is not among the user's skills that this session lists right now, so it cannot be updated yet. If you proposed it as a new skill earlier in this conversation and the user has not saved it, call again with kind "new" under the same name. Otherwise call again once; if it is still not listed, tell the user, and propose it as a new skill under another name only if they want that.
