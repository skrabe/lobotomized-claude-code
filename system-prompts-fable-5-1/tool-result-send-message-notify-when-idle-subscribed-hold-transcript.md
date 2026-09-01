<!--
name: 'Tool Result: SendMessage Notify When Idle Subscribed Hold Transcript'
description: SendMessage tool result when an idle subscription is armed but all inbound peer traffic is held and shown to the user in the transcript, not delivered to the model.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_SUBSCRIBED_HOLD_TRANSCRIPT_VAR_0
-->
Subscribed — "${TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_SUBSCRIBED_HOLD_TRANSCRIPT_VAR_0}" will send one notice when it is next idle (or exits); this session holds ALL inbound peer traffic (crossSessionInbound: hold), so it will be shown to your user in the transcript, not delivered to you.
