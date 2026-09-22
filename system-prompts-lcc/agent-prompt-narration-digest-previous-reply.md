<!--
name: 'Agent Prompt: Narration Digest Previous Reply'
description: >-
  Optional digest clause appending the end of the previous assistant reply into
  the narration user message.
ccVersion: 2.1.257
variables:
  - AGENT_PROMPT_NARRATION_DIGEST_PREVIOUS_REPLY_VAR_0
  - AGENT_PROMPT_NARRATION_DIGEST_PREVIOUS_REPLY_VAR_1
-->

End of your previous reply: ${AGENT_PROMPT_NARRATION_DIGEST_PREVIOUS_REPLY_VAR_0(AGENT_PROMPT_NARRATION_DIGEST_PREVIOUS_REPLY_VAR_1,700)}
