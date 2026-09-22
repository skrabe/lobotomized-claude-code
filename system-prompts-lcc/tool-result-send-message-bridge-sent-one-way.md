<!--
name: Bridge message sent one-way
description: >-
  SendMessage success result for a bridge (Remote Control) address send, noting
  the send was one-way so the receiver cannot address a reply to this session.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_2
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_3
-->
“${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_0}” → ${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_1.to} (one-way: ${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_2(TOOL_RESULT_SEND_MESSAGE_BRIDGE_SENT_ONE_WAY_VAR_3)}, so the receiver cannot address a reply to this session)
