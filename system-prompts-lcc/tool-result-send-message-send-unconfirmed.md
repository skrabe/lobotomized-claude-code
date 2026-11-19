<!--
name: 'Tool Result: SendMessage send unconfirmed'
description: >-
  SendMessage result when delivery to a peer session was not confirmed: the
  message may have arrived, so do not resend blindly
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_SEND_MESSAGE_SEND_UNCONFIRMED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_SEND_UNCONFIRMED_VAR_1
-->
Sending to ${TOOL_RESULT_SEND_MESSAGE_SEND_UNCONFIRMED_VAR_0} was not confirmed (${TOOL_RESULT_SEND_MESSAGE_SEND_UNCONFIRMED_VAR_1}), so the message may have arrived. Do not send it again unless you learn that it did not arrive, or that session may get it twice. Tell your user, or check with that session later.
