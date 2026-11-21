<!--
name: 'Tool result: MCP resource read, skill declined'
description: >-
  MCP resource read error noting the server changed the skill into a kind Claude
  Code does not load.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_0
  - TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_1
  - TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_2
  - TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_4
  - TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_3
-->
${TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_0} The server has changed the skill "${TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_1}" into a skill ${TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_2[TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_4.reason]}, which Claude Code does not load. For this reason, loading the skill again will not help.${TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_3(TOOL_RESULT_MCP_RESOURCE_SKILL_DECLINED_VAR_4.reason)}
