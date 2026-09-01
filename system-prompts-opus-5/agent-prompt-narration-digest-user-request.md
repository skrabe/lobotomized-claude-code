<!--
name: 'Agent Prompt: Narration Digest User Request'
description: >-
  Digest heading and truncated user-turn text assembled by RXe into the
  narration model's user message.
ccVersion: 2.1.257
variables:
  - AGENT_PROMPT_NARRATION_DIGEST_USER_REQUEST_VAR_0
  - AGENT_PROMPT_NARRATION_DIGEST_USER_REQUEST_VAR_1
-->
USER'S REQUEST (this turn):
${AGENT_PROMPT_NARRATION_DIGEST_USER_REQUEST_VAR_0(AGENT_PROMPT_NARRATION_DIGEST_USER_REQUEST_VAR_1,2000)||"(not in view)"}
