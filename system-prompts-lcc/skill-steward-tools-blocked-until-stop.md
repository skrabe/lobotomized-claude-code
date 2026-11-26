<!--
name: 'Skill: steward tools blocked until stop'
description: >-
  Until the user sends the stop command or /clear, Claude can't run tools in
  this session
ccVersion: 2.1.332
variables:
  - SKILL_STEWARD_TOOLS_BLOCKED_UNTIL_STOP_VAR_0
  - SKILL_STEWARD_TOOLS_BLOCKED_UNTIL_STOP_VAR_1
  - SKILL_STEWARD_TOOLS_BLOCKED_UNTIL_STOP_VAR_2
-->
 Until you send ${SKILL_STEWARD_TOOLS_BLOCKED_UNTIL_STOP_VAR_0()?"/steward stop":SKILL_STEWARD_TOOLS_BLOCKED_UNTIL_STOP_VAR_1(SKILL_STEWARD_TOOLS_BLOCKED_UNTIL_STOP_VAR_2.binding)} or /clear, Claude can't run tools in this session.
