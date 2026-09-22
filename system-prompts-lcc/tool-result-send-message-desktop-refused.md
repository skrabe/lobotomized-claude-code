<!--
name: SendMessage Desktop Delivery Refused
description: >-
  SendMessage tool_result when Claude Desktop refused delivery, quoting the
  desktop session id and reason.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_SEND_MESSAGE_DESKTOP_REFUSED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_DESKTOP_REFUSED_VAR_1
-->
Not delivered to Claude Desktop session ${TOOL_RESULT_SEND_MESSAGE_DESKTOP_REFUSED_VAR_0.to}: ${TOOL_RESULT_SEND_MESSAGE_DESKTOP_REFUSED_VAR_1.message}
