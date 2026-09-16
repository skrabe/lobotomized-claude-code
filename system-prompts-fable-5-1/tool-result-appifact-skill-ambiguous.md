<!--
name: Appifact Skill Ambiguous
description: >-
  AppifactRepl error when a skill name matches more than one installed skill;
  use the qualified name.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_APPIFACT_SKILL_AMBIGUOUS_VAR_0
  - TOOL_RESULT_APPIFACT_SKILL_AMBIGUOUS_VAR_1
  - TOOL_RESULT_APPIFACT_SKILL_AMBIGUOUS_VAR_2
-->
the skill ${TOOL_RESULT_APPIFACT_SKILL_AMBIGUOUS_VAR_0(TOOL_RESULT_APPIFACT_SKILL_AMBIGUOUS_VAR_1)} names more than one installed skill (${TOOL_RESULT_APPIFACT_SKILL_AMBIGUOUS_VAR_2.ambiguous.join(", ")}); use the qualified name
