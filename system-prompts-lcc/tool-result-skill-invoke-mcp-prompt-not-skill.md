<!--
name: 'Skill invoke: MCP prompt not a skill'
description: >-
  Skill-tool error returned to the model when the named target is an MCP prompt
  rather than a skill.
ccVersion: 2.1.210
variables:
  - TOOL_RESULT_SKILL_INVOKE_MCP_PROMPT_NOT_SKILL_VAR_0
  - TOOL_RESULT_SKILL_INVOKE_MCP_PROMPT_NOT_SKILL_VAR_1
-->
${TOOL_RESULT_SKILL_INVOKE_MCP_PROMPT_NOT_SKILL_VAR_0} is an MCP prompt, not a skill. ${TOOL_RESULT_SKILL_INVOKE_MCP_PROMPT_NOT_SKILL_VAR_1(TOOL_RESULT_SKILL_INVOKE_MCP_PROMPT_NOT_SKILL_VAR_0)}
