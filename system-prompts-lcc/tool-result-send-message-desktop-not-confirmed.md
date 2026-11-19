<!--
name: 'Tool Result: SendMessage Desktop delivery not confirmed'
description: >-
  Says a Claude Desktop session has not confirmed starting on the message and
  warns against resending
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_SEND_MESSAGE_DESKTOP_NOT_CONFIRMED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_DESKTOP_NOT_CONFIRMED_VAR_1
-->
Not confirmed: Claude Desktop session ${TOOL_RESULT_SEND_MESSAGE_DESKTOP_NOT_CONFIRMED_VAR_0.to} has given no sign of starting on the message, and it still may. Do not send it again unless you learn that it did not arrive, or that session may get it twice. Desktop said: ${TOOL_RESULT_SEND_MESSAGE_DESKTOP_NOT_CONFIRMED_VAR_1.message}
