<!--
name: 'Tool result: SendMessage priority requires session id'
description: >-
  Validation refusal when options.priority is set but `to` is not a session id
  or the session sentinel.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_SEND_MESSAGE_PRIORITY_REQUIRES_SESSION_ID_VAR_0
-->
Not sent: a priority works only with a session id or "${TOOL_RESULT_SEND_MESSAGE_PRIORITY_REQUIRES_SESSION_ID_VAR_0}". Send it again without \`options\`.
