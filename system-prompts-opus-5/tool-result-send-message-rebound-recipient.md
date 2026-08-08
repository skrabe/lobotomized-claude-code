<!--
name: Earlier recipient description
description: SendMessage rebound tool-error fragment returned to the model.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_2
  - TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_3
-->
The earlier recipient is ${TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_0(TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_1)!==TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_1?"a Claude session running in the cloud":"another Claude session on this machine"}; this name now belongs to an agent in this session.${TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_2?` Use ${TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_3} if you still need that session.`:""}
