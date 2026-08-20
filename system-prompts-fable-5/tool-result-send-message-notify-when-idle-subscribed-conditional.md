<!--
name: 'Tool Result: SendMessage Notify When Idle Subscribed Conditional'
description: SendMessage tool result for an idle subscription that is delivered to the model only if the peer shares this session's permission class.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_SUBSCRIBED_CONDITIONAL_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_SUBSCRIBED_CONDITIONAL_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_SUBSCRIBED_CONDITIONAL_VAR_2
-->
Subscribed — "${TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_SUBSCRIBED_CONDITIONAL_VAR_0}" will send one notice when it is next idle (or exits). It is delivered to you if ${TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_SUBSCRIBED_CONDITIONAL_VAR_1}; otherwise it is ${TOOL_RESULT_SEND_MESSAGE_NOTIFY_WHEN_IDLE_SUBSCRIBED_CONDITIONAL_VAR_2?"only logged here":"shown to your user in the transcript"} (this session holds other inbound peer traffic).
