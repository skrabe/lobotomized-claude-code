<!--
name: 'Tool Result: SendMessage limited to plain text to own agents'
description: >-
  Refusal telling the model messaging in this session carries only plain text to
  agents of this session and how to set the to field
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_SEND_MESSAGE_PLAIN_TEXT_OWN_AGENTS_ONLY_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_PLAIN_TEXT_OWN_AGENTS_ONLY_VAR_1
-->
Not sent. In this session ${TOOL_RESULT_SEND_MESSAGE_PLAIN_TEXT_OWN_AGENTS_ONLY_VAR_0} carries only plain text, and only to agents of this session: an agent launched in it with the ${TOOL_RESULT_SEND_MESSAGE_PLAIN_TEXT_OWN_AGENTS_ONLY_VAR_1} tool or, from a subagent, "main". Set \`to\` to such an agent's name, to the agentId from its spawn result, or to "main".
