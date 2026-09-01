<!--
name: 'System Prompt: Subagent id usage footer'
description: >-
  Tool_result footer giving the agentId (with SendMessage continue hint plus a
  summary recap) and a usage block of token/tool/duration stats
ccVersion: 2.1.187
variables:
  - SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_0
  - SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_1
-->
agentId: ${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_0.agentId} (use SendMessage with to: '${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_0.agentId}', summary: '<5-10 word recap>' to continue this agent)${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_1}
<usage>subagent_tokens: ${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_0.totalTokens}
tool_uses: ${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_0.totalToolUseCount}
duration_ms: ${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_0.totalDurationMs}</usage>
