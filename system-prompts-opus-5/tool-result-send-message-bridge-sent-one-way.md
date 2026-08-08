<!--
name: 'Tool Result: Bridge Message Sent One-Way'
description: >-
  SendMessage success result for a bridge (Remote Control) send, noting the send
  was one-way because Remote Control is not connected locally.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_1
-->
“${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_0}” → ${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_1.to} (one-way: Remote Control is not connected, so the receiver cannot address a reply to this session)
