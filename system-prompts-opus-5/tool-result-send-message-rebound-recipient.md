<!--
name: Earlier Recipient Description
description: >-
  SendMessage rebound-error fragment explaining that the earlier recipient was
  another Claude session but the name now belongs to an in-session agent.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_2
  - TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_3
-->
The earlier recipient is ${TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_0(TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_1)!==TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_1?"a Claude session on another machine (cloud or Remote Control)":"another Claude session on this machine"}; this name now belongs to an agent in this session.${TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_2?` Use ${TOOL_RESULT_SEND_MESSAGE_REBOUND_RECIPIENT_VAR_3} if you still need that session.`:""}
