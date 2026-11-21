<!--
name: 'Tool result: skill permission check MCP mismatch'
description: >-
  Skill not run because the permission check was for an MCP skill and the name
  now finds none; retry the Skill tool.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_SKILL_PERMISSION_CHECK_MCP_DISPATCH_MISMATCH_VAR_0
  - TOOL_RESULT_SKILL_PERMISSION_CHECK_MCP_DISPATCH_MISMATCH_VAR_1
-->
Skill "${TOOL_RESULT_SKILL_PERMISSION_CHECK_MCP_DISPATCH_MISMATCH_VAR_0}" was not run, because the permission check was for a skill from an MCP server, and this name now finds no skill from an MCP server. Use the ${TOOL_RESULT_SKILL_PERMISSION_CHECK_MCP_DISPATCH_MISMATCH_VAR_1} tool once more.
