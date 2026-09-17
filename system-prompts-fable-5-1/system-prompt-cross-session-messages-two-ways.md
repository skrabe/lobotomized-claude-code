<!--
name: 'System Prompt: Cross-Session Messages Two Ways'
description: >-
  System-prompt clause describing two paths owner/member messages reach the
  agent when in-thread send is off.
ccVersion: 2.1.274
variables:
  - SYSTEM_PROMPT_CROSS_SESSION_MESSAGES_TWO_WAYS_VAR_0
  - SYSTEM_PROMPT_CROSS_SESSION_MESSAGES_TWO_WAYS_VAR_1
  - SYSTEM_PROMPT_CROSS_SESSION_MESSAGES_TWO_WAYS_VAR_2
-->
 Their messages reach the agent in two ways: the server attaches them to a coordinator session's relay, and the server returns them from \`${SYSTEM_PROMPT_CROSS_SESSION_MESSAGES_TWO_WAYS_VAR_0}\`, \`${SYSTEM_PROMPT_CROSS_SESSION_MESSAGES_TWO_WAYS_VAR_1}\` and \`${SYSTEM_PROMPT_CROSS_SESSION_MESSAGES_TWO_WAYS_VAR_2}\`.
