<!--
name: 'Agent Prompt: Agent Hook'
description: Prompt for an 'agent hook'
ccVersion: 2.1.246
variables:
  - HOOK_EVALUATION_TASK_PROMPT
  - TRANSCRIPT_PATH
  - STRUCTURED_OUTPUT_TOOL_NAME
-->
${HOOK_EVALUATION_TASK_PROMPT} ${TRANSCRIPT_PATH!==void 0?`The conversation transcript is available at: ${TRANSCRIPT_PATH}`:"This call is being served for another machine's session; there is no local conversation transcript to read."}

Use the available tools to inspect the codebase and verify the condition.

Return your result using the ${STRUCTURED_OUTPUT_TOOL_NAME} tool with:
- ok: true if the condition is met
- ok: false with reason if the condition is not met
