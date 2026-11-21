<!--
name: 'System Prompt: Subagent id usage footer'
description: >-
  tool_result footer giving the agentId (with a SendMessage continue hint that
  now carries a summary recap) plus a usage block of token/tool/duration stats
ccVersion: 2.1.330
variables:
  - SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_0
  - SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_1
  - SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_2
  - SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_3
-->
${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_0}agentId: ${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_1.agentId}${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_2}${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_3}
<usage>subagent_tokens: ${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_1.totalTokens}
tool_uses: ${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_1.totalToolUseCount}
duration_ms: ${SYSTEM_PROMPT_SUBAGENT_ID_USAGE_FOOTER_VAR_1.totalDurationMs}</usage>
