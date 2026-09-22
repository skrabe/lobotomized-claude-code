<!--
name: SendFile failed-to-send (socket)
description: >-
  SendFile tool result reporting a send failure to a labeled recipient over the
  local socket, with an error detail suffix.
ccVersion: 2.1.210
variables:
  - TOOL_RESULT_SENDFILE_FAILED_TO_SEND_UDS_VAR_0
  - TOOL_RESULT_SENDFILE_FAILED_TO_SEND_UDS_VAR_1
  - TOOL_RESULT_SENDFILE_FAILED_TO_SEND_UDS_VAR_2
  - TOOL_RESULT_SENDFILE_FAILED_TO_SEND_UDS_VAR_3
-->
Failed to send to ${TOOL_RESULT_SENDFILE_FAILED_TO_SEND_UDS_VAR_0.label}: ${TOOL_RESULT_SENDFILE_FAILED_TO_SEND_UDS_VAR_1(TOOL_RESULT_SENDFILE_FAILED_TO_SEND_UDS_VAR_2)}${TOOL_RESULT_SENDFILE_FAILED_TO_SEND_UDS_VAR_3}
