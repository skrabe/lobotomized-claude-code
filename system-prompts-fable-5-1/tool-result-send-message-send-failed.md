<!--
name: Send failed
description: SendMessage tool-error returned to the model.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_SEND_MESSAGE_SEND_FAILED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_SEND_FAILED_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_SEND_FAILED_VAR_2
-->
Failed to send to ${TOOL_RESULT_SEND_MESSAGE_SEND_FAILED_VAR_0.displayName}: ${TOOL_RESULT_SEND_MESSAGE_SEND_FAILED_VAR_1.error??"unknown"}${TOOL_RESULT_SEND_MESSAGE_SEND_FAILED_VAR_2}
