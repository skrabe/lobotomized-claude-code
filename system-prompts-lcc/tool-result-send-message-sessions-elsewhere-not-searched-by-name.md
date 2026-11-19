<!--
name: 'Tool Result: SendMessage sessions elsewhere not searched by name'
description: >-
  Note in a SendMessage/send-file result that the user's sessions off this
  machine are not looked up by name, with an optional pointer to the tool that
  can message one by session id
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_SEND_MESSAGE_SESSIONS_ELSEWHERE_NOT_SEARCHED_BY_NAME_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_SESSIONS_ELSEWHERE_NOT_SEARCHED_BY_NAME_VAR_1
-->

Your user's sessions outside this machine are not searched by name here. If '${TOOL_RESULT_SEND_MESSAGE_SESSIONS_ELSEWHERE_NOT_SEARCHED_BY_NAME_VAR_0}' is one of them, nothing was sent to it.${TOOL_RESULT_SEND_MESSAGE_SESSIONS_ELSEWHERE_NOT_SEARCHED_BY_NAME_VAR_1===void 0?"":` ${TOOL_RESULT_SEND_MESSAGE_SESSIONS_ELSEWHERE_NOT_SEARCHED_BY_NAME_VAR_1} can message one by its session id.`}
