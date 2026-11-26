<!--
name: 'Tool result: MCP skill slash line not loaded'
description: >-
  Refusal when a slash line not typed by the session owner names an MCP server's
  skill; points to typing it or using the Skill tool.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_MCP_SKILL_SLASH_LINE_NOT_LOADED_VAR_0
  - TOOL_RESULT_MCP_SKILL_SLASH_LINE_NOT_LOADED_VAR_1
  - TOOL_RESULT_MCP_SKILL_SLASH_LINE_NOT_LOADED_VAR_2
-->
The skill "/${TOOL_RESULT_MCP_SKILL_SLASH_LINE_NOT_LOADED_VAR_0(TOOL_RESULT_MCP_SKILL_SLASH_LINE_NOT_LOADED_VAR_1.name)}" comes from an MCP server, and this line did not load it. Type it at the session's own prompt, or ask Claude to use the skill. The ${TOOL_RESULT_MCP_SKILL_SLASH_LINE_NOT_LOADED_VAR_2} tool then asks for approval first, unless the permission mode or, outside plan mode, a rule already allows the skill.
