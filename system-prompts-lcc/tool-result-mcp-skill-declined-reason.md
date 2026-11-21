<!--
name: 'Tool result: MCP skill changed into declined kind'
description: Error when the server changed a skill into a kind Claude Code does not load.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_SKILL_DECLINED_REASON_VAR_0
  - TOOL_RESULT_MCP_SKILL_DECLINED_REASON_VAR_1
  - TOOL_RESULT_MCP_SKILL_DECLINED_REASON_VAR_3
  - TOOL_RESULT_MCP_SKILL_DECLINED_REASON_VAR_2
-->
${TOOL_RESULT_MCP_SKILL_DECLINED_REASON_VAR_0}, because the server has changed it into a skill ${TOOL_RESULT_MCP_SKILL_DECLINED_REASON_VAR_1[TOOL_RESULT_MCP_SKILL_DECLINED_REASON_VAR_3.reason]}, which Claude Code does not load.${TOOL_RESULT_MCP_SKILL_DECLINED_REASON_VAR_2(TOOL_RESULT_MCP_SKILL_DECLINED_REASON_VAR_3.reason)}
