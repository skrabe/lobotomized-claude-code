<!--
name: 'Tool result: SendMessage session_name requires session id'
description: >-
  Validation refusal when options.session_name is used with a `to` that is not a
  session id or the session/title sentinels.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_SEND_MESSAGE_SESSION_NAME_REQUIRES_SESSION_ID_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_SESSION_NAME_REQUIRES_SESSION_ID_VAR_1
-->
Not sent: \`session_name\` works only with a session id, "${TOOL_RESULT_SEND_MESSAGE_SESSION_NAME_REQUIRES_SESSION_ID_VAR_0}" or "${TOOL_RESULT_SEND_MESSAGE_SESSION_NAME_REQUIRES_SESSION_ID_VAR_1}" as \`to\`. To find a session by its title, set \`to\` to "${TOOL_RESULT_SEND_MESSAGE_SESSION_NAME_REQUIRES_SESSION_ID_VAR_1}". To message an agent here, send it again without \`options\`.
