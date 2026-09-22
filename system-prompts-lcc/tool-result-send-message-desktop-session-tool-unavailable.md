<!--
name: 'Tool Result: Send message desktop session tool unavailable'
description: >-
  SendMessage tool result when the target looks like a Claude Desktop session id
  but that messaging tool is not available.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_SEND_MESSAGE_DESKTOP_SESSION_TOOL_UNAVAILABLE_VAR_0
-->
No agent named '${TOOL_RESULT_SEND_MESSAGE_DESKTOP_SESSION_TOOL_UNAVAILABLE_VAR_0.to}' is reachable. It has the shape of a Claude Desktop session id, but Claude Desktop's session messaging tool is not available in this session, so SendMessage cannot deliver to it.
