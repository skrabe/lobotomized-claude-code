<!--
name: 'Tool Result: Notify When Idle Cap'
description: >-
  SendMessage tool-result when this session already holds the maximum pending
  idle subscriptions.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_CAP_VAR_0
-->
notify_when_idle: this session already holds ${TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_CAP_VAR_0} pending idle subscriptions — wait for some to fire or expire.
