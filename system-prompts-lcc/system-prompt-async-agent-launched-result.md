<!--
name: 'System Prompt: Async agent launched result'
description: >-
  Tool_result confirming an async agent launched in the background, giving the
  internal agentId and SendMessage continuation hint
ccVersion: 2.1.331
variables:
  - SYSTEM_PROMPT_ASYNC_AGENT_LAUNCHED_RESULT_VAR_0
  - SYSTEM_PROMPT_ASYNC_AGENT_LAUNCHED_RESULT_VAR_1
  - SYSTEM_PROMPT_ASYNC_AGENT_LAUNCHED_RESULT_VAR_2
-->
Async agent launched successfully. (This tool result is internal metadata — never quote or paste any part of it, including the agentId below, into a user-facing reply.)
agentId: ${SYSTEM_PROMPT_ASYNC_AGENT_LAUNCHED_RESULT_VAR_0.agentId} (internal ID - do not mention to user.${SYSTEM_PROMPT_ASYNC_AGENT_LAUNCHED_RESULT_VAR_0.canContinueAgent===!1?"":` Use ${SYSTEM_PROMPT_ASYNC_AGENT_LAUNCHED_RESULT_VAR_1} with to: '${SYSTEM_PROMPT_ASYNC_AGENT_LAUNCHED_RESULT_VAR_0.agentId}', summary: '<5-10 word recap>' to continue this agent.`})
${SYSTEM_PROMPT_ASYNC_AGENT_LAUNCHED_RESULT_VAR_2}
