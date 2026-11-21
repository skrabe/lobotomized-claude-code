<!--
name: 'Tool Result: Skill load approval request'
description: >-
  Opens the Skill tool approval ask by naming the skill, warning it can direct
  Claude to run code, and giving its version
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_SKILL_LOAD_APPROVAL_REQUEST_VAR_0
  - TOOL_RESULT_SKILL_LOAD_APPROVAL_REQUEST_VAR_1
  - TOOL_RESULT_SKILL_LOAD_APPROVAL_REQUEST_VAR_2
  - TOOL_RESULT_SKILL_LOAD_APPROVAL_REQUEST_VAR_3
-->
${TOOL_RESULT_SKILL_LOAD_APPROVAL_REQUEST_VAR_0(TOOL_RESULT_SKILL_LOAD_APPROVAL_REQUEST_VAR_1.isChanged)}Load skill "${TOOL_RESULT_SKILL_LOAD_APPROVAL_REQUEST_VAR_2}". It can direct Claude to run code. ${TOOL_RESULT_SKILL_LOAD_APPROVAL_REQUEST_VAR_3(TOOL_RESULT_SKILL_LOAD_APPROVAL_REQUEST_VAR_1)}
