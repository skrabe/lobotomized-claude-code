<!--
name: 'Agent Prompt: Narration Digest Just Now'
description: >-
  Digest of the latest assistant text and still-running tool calls sent to the
  narration model.
ccVersion: 2.1.257
variables:
  - AGENT_PROMPT_NARRATION_DIGEST_JUST_NOW_VAR_0
-->
JUST NOW (your latest message; these tool calls are still running):
${AGENT_PROMPT_NARRATION_DIGEST_JUST_NOW_VAR_0.join(`
`)||"(no tool calls)"}
