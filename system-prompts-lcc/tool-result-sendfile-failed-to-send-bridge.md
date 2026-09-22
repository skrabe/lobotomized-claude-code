<!--
name: SendFile failed-to-send (bridge)
description: >-
  SendFile tool result reporting a send failure over the bridge transport, with
  an error detail suffix.
ccVersion: 2.1.210
variables:
  - TOOL_RESULT_SENDFILE_FAILED_TO_SEND_BRIDGE_VAR_0
  - TOOL_RESULT_SENDFILE_FAILED_TO_SEND_BRIDGE_VAR_1
  - TOOL_RESULT_SENDFILE_FAILED_TO_SEND_BRIDGE_VAR_2
-->
Failed to send to ${TOOL_RESULT_SENDFILE_FAILED_TO_SEND_BRIDGE_VAR_0.label}: ${TOOL_RESULT_SENDFILE_FAILED_TO_SEND_BRIDGE_VAR_1.error??"unknown"}${TOOL_RESULT_SENDFILE_FAILED_TO_SEND_BRIDGE_VAR_2}
