<!--
name: 'Tool result: SendMessage invalid fields (session_name route)'
description: >-
  Refusal under pgr() listing the accepted to/session_name/message forms and the
  only fields allowed.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_SEND_MESSAGE_INVALID_FIELDS_SESSION_NAME_ROUTE_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_INVALID_FIELDS_SESSION_NAME_ROUTE_VAR_1
-->
Not sent. Give a full session id or "${TOOL_RESULT_SEND_MESSAGE_INVALID_FIELDS_SESSION_NAME_ROUTE_VAR_0}" as \`to\`, or "${TOOL_RESULT_SEND_MESSAGE_INVALID_FIELDS_SESSION_NAME_ROUTE_VAR_1}" with a title as \`options.session_name\`, and plain text as \`message\`. Leave out \`notify_when_idle\` and every other field except a short \`summary\`, \`options.priority\` and an \`options.session_name\` that is not empty.
