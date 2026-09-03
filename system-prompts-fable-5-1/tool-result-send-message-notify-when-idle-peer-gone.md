<!--
name: 'Tool Result: Notify When Idle Peer Gone'
description: >-
  SendMessage tool-result when no session is listening at the target address,
  voiding any earlier idle subscription.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_PEER_GONE_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_PEER_GONE_VAR_1
-->
notify_when_idle: no session is listening at that address any more; nothing was subscribed, and any earlier idle subscription to it is void${TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_PEER_GONE_VAR_0(TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_PEER_GONE_VAR_1)}
