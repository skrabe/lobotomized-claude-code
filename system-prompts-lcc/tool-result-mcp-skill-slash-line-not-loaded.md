<!--
name: 'Tool result: MCP skill slash line not loaded'
description: >-
  An MCP skill line not typed at the session prompt is not loaded; explains how
  it can be loaded with approval.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_SKILL_SLASH_LINE_NOT_LOADED_VAR_0
  - TOOL_RESULT_MCP_SKILL_SLASH_LINE_NOT_LOADED_VAR_1
-->
The skill "/${TOOL_RESULT_MCP_SKILL_SLASH_LINE_NOT_LOADED_VAR_0}" comes from an MCP server, and this line did not load it. Type it at the session's own prompt, or ask Claude to use the skill. The ${TOOL_RESULT_MCP_SKILL_SLASH_LINE_NOT_LOADED_VAR_1} tool then asks for approval first, unless the permission mode or, outside plan mode, a rule already allows the skill.
