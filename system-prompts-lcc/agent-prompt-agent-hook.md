<!--
name: 'Agent Prompt: Agent Hook'
description: Prompt for an 'agent hook'
ccVersion: 2.1.294
variables:
  - HOOK_EVALUATION_TASK_PROMPT
  - TRANSCRIPT_PATH
  - IS_REMOTE_HOOK_CALL
  - STRUCTURED_OUTPUT_TOOL_NAME
  - AGENT_PROMPT_AGENT_HOOK_VAR_4
-->
${HOOK_EVALUATION_TASK_PROMPT} ${TRANSCRIPT_PATH!==void 0?`The conversation transcript is available at: ${TRANSCRIPT_PATH}`:IS_REMOTE_HOOK_CALL?"This call is being served for another machine's session; there is no local conversation transcript to read.":"There is no conversation transcript file to read here; ignore transcript_path in the hook input."}

Use the available tools to inspect the codebase and verify the condition.

When done, return your result using the ${STRUCTURED_OUTPUT_TOOL_NAME} tool, always with a reason.

${AGENT_PROMPT_AGENT_HOOK_VAR_4}
