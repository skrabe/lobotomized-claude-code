<!--
name: 'Tool Result: MCP skill declined for a reason'
description: >-
  Skill tool error when the server serves the addressed skill in a form Claude
  Code declines, naming the reason.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_SKILL_DECLINED_BY_REASON_VAR_0
  - TOOL_RESULT_MCP_SKILL_DECLINED_BY_REASON_VAR_1
  - TOOL_RESULT_MCP_SKILL_DECLINED_BY_REASON_VAR_3
  - TOOL_RESULT_MCP_SKILL_DECLINED_BY_REASON_VAR_2
-->
${TOOL_RESULT_MCP_SKILL_DECLINED_BY_REASON_VAR_0}: the server serves it as a skill ${TOOL_RESULT_MCP_SKILL_DECLINED_BY_REASON_VAR_1[TOOL_RESULT_MCP_SKILL_DECLINED_BY_REASON_VAR_3.reason]}, which Claude Code does not load.${TOOL_RESULT_MCP_SKILL_DECLINED_BY_REASON_VAR_2(TOOL_RESULT_MCP_SKILL_DECLINED_BY_REASON_VAR_3.reason)}
