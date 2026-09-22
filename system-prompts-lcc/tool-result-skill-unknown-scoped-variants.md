<!--
name: 'Tool Result: Unknown skill scoped variants'
description: >-
  Skill invocation error for an unknown bare name when directory-scoped variants
  exist
ccVersion: 2.1.204
variables:
  - TOOL_RESULT_SKILL_UNKNOWN_SCOPED_VARIANTS_VAR_0
  - TOOL_RESULT_SKILL_UNKNOWN_SCOPED_VARIANTS_VAR_1
  - TOOL_RESULT_SKILL_UNKNOWN_SCOPED_VARIANTS_VAR_2
-->
Unknown skill: ${TOOL_RESULT_SKILL_UNKNOWN_SCOPED_VARIANTS_VAR_0}. Directory-scoped variants exist: ${TOOL_RESULT_SKILL_UNKNOWN_SCOPED_VARIANTS_VAR_1.map((TOOL_RESULT_SKILL_UNKNOWN_SCOPED_VARIANTS_VAR_2)=>TOOL_RESULT_SKILL_UNKNOWN_SCOPED_VARIANTS_VAR_2.name).join(", ")} — invoke the variant whose directory contains the files you are working on.
