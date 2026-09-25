<!--
name: 'Tool Result: Skill Permission — Rule Covers Only Prefixed Names'
description: >-
  ue() boundary case for a reserved prefix: the Skill() rule only covers names
  starting with "<prefix>:", with advice to add Skill(<name>).
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_ONLY_PREFIXED_NAMES_VAR_0
  - TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_ONLY_PREFIXED_NAMES_VAR_1
  - TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_ONLY_PREFIXED_NAMES_VAR_2
-->
Skill(${TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_ONLY_PREFIXED_NAMES_VAR_0}) only covers names starting with "${TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_ONLY_PREFIXED_NAMES_VAR_1}:". Add Skill(${TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_ONLY_PREFIXED_NAMES_VAR_2}) to allow ${TOOL_RESULT_SKILL_PERMISSION_RULE_COVERS_ONLY_PREFIXED_NAMES_VAR_2} without asking.
