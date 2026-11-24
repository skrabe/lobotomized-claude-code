<!--
name: 'Tool Result: SendMessage cloud session not by name'
description: >-
  Refusal when a cloud/Remote Control session is addressed by name instead of
  id.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSION_NOT_BY_NAME_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSION_NOT_BY_NAME_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSION_NOT_BY_NAME_VAR_2
-->
Not sent: '${TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSION_NOT_BY_NAME_VAR_0.displayName}' is a cloud or Remote Control session, which is addressed from here by its session id, not its name. ${TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSION_NOT_BY_NAME_VAR_1(TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSION_NOT_BY_NAME_VAR_0.sessionId)===void 0?`${TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSION_NOT_BY_NAME_VAR_2} has the ids.`:`To reach it, set \`to\` to ${TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSION_NOT_BY_NAME_VAR_0.sessionId}.`}
