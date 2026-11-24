<!--
name: 'Tool result: SendMessage invalid fields (other session)'
description: >-
  Refusal telling Claude to give a full session id or the sentinel as to, plain
  text message, and only summary and options.priority.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_SEND_MESSAGE_INVALID_FIELDS_OTHER_SESSION_VAR_0
-->
Not sent. To message another session, give its full session id or "${TOOL_RESULT_SEND_MESSAGE_INVALID_FIELDS_OTHER_SESSION_VAR_0}" as \`to\` and plain text as \`message\`. Leave out \`notify_when_idle\` and every other field except a short \`summary\` and \`options\` with only \`priority\`.
