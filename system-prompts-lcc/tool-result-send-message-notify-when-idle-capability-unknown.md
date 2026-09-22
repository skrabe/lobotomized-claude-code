<!--
name: 'Tool Result: SendMessage Notify When Idle Capability Unknown'
description: >-
  SendMessage tool result when an idle subscription was sent but the peer's
  idle-notice support could not be confirmed.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_CAPABILITY_UNKNOWN_VAR_0
-->
Subscription sent to "${TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_CAPABILITY_UNKNOWN_VAR_0}" — but whether it supports idle notices is unknown (no readable session-registry record vouches for it), so a notice may never come; you will be told if it lapses unheard. Do not rely on it.
