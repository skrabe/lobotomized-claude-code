<!--
name: 'Tool result: MCP skill load deny rule'
description: >-
  Skill not loaded because a deny rule for the Skill tool or its MCP server
  applies.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_SKILL_LOAD_DENY_RULE_VAR_0
  - TOOL_RESULT_MCP_SKILL_LOAD_DENY_RULE_VAR_1
  - TOOL_RESULT_MCP_SKILL_LOAD_DENY_RULE_VAR_2
-->
The skill "/${TOOL_RESULT_MCP_SKILL_LOAD_DENY_RULE_VAR_0}" was not loaded, because a deny rule for ${TOOL_RESULT_MCP_SKILL_LOAD_DENY_RULE_VAR_1===void 0?`the ${TOOL_RESULT_MCP_SKILL_LOAD_DENY_RULE_VAR_2} tool`:"its MCP server"} applies to it. For a skill from an MCP server, a deny rule also stops a line that the owner of the session types.
