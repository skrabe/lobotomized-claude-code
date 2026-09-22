<!--
name: 'Tool Result: Unknown skill ambiguous and scoped variants'
description: >-
  Skill-tool validateInput error when suffix matches and directory-scoped
  variants both exist; invoke one by its full name.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_AND_SCOPED_VARIANTS_VAR_0
  - TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_AND_SCOPED_VARIANTS_VAR_1
  - TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_AND_SCOPED_VARIANTS_VAR_2
  - TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_AND_SCOPED_VARIANTS_VAR_3
-->
Unknown skill: ${TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_AND_SCOPED_VARIANTS_VAR_0}. Several skills match that name: ${[...TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_AND_SCOPED_VARIANTS_VAR_1,...TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_AND_SCOPED_VARIANTS_VAR_2].map((TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_AND_SCOPED_VARIANTS_VAR_3)=>TOOL_RESULT_SKILL_UNKNOWN_AMBIGUOUS_AND_SCOPED_VARIANTS_VAR_3.name).join(", ")} — invoke one by its full name; the directory-scoped variants apply to the files under their directory.
