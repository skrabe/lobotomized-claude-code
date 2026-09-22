<!--
name: 'Tool Result: Cross-Session Inbox Rate Limit'
description: >-
  Tells the sending agent too many messages hit one session's inbox rate limit,
  so this send was dropped and it should batch or wait.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_SEND_MESSAGE_INBOX_RATE_LIMIT_VAR_0
-->
Too many messages to this session just now: ${TOOL_RESULT_SEND_MESSAGE_INBOX_RATE_LIMIT_VAR_0} were sent recently and more would be dropped by its rate limit, so this one was not sent. Batch what remains into one message, or wait a little before sending more.
