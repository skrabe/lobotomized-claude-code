<!--
name: 'Tool Result: Skill Permission — Rule Covers Old Skill Name'
description: >-
  ue() renamed case: the Skill() rule covers the skill's former name; tells the
  user to add the new name to allow it without asking.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_OLD_NAME_VAR_0
  - TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_OLD_NAME_VAR_1
  - TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_OLD_NAME_VAR_2
-->
Skill(${TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_OLD_NAME_VAR_0}) covers this skill's old name, ${TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_OLD_NAME_VAR_1.formerName}. It is now ${TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_OLD_NAME_VAR_2}; add Skill(${TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_OLD_NAME_VAR_2}) to allow it without asking.
