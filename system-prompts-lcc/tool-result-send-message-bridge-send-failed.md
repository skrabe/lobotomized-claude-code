<!--
name: 'Tool Result: Bridge Send Failed'
description: >-
  SendMessage failure result when postInterClaudeMessage rejects a bridge send,
  with an optional stale-bridge-ID hint appended.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SEND_FAILED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SEND_FAILED_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SEND_FAILED_VAR_2
-->
Failed to send to ${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SEND_FAILED_VAR_0.to}: ${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SEND_FAILED_VAR_1.error??"unknown"}${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SEND_FAILED_VAR_2}
