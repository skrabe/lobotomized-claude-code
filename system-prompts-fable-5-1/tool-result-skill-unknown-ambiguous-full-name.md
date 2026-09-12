<!--
name: 'Tool Result: Unknown skill ambiguous full name'
description: >-
  Skill-tool validateInput error when several named skills match a suffix;
  invoke one by its full name.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_FULL_NAME_VAR_0
  - TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_FULL_NAME_VAR_1
  - TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_FULL_NAME_VAR_2
-->
Unknown skill: ${TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_FULL_NAME_VAR_0}. Several skills match that name: ${TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_FULL_NAME_VAR_1.map((TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_FULL_NAME_VAR_2)=>TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_FULL_NAME_VAR_2.name).join(", ")} — invoke one by its full name.
