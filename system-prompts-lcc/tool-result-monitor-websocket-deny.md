<!--
name: Monitor WebSocket deny
description: >-
  Permission deny message returned to the model when Monitor is refused a
  WebSocket to a private host.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_MONITOR_WEBSOCKET_DENY_VAR_0
-->
Monitor cannot open a WebSocket to ${TOOL_RESULT_MONITOR_WEBSOCKET_DENY_VAR_0.host}: ${TOOL_RESULT_MONITOR_WEBSOCKET_DENY_VAR_0.detail}.
