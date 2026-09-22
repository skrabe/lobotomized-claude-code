<!--
name: 'Tool Result: SendMessage no exact name confirm ref'
description: >-
  Tells the model that the recipient name only matched by prefix and that it
  must re-send with the session ref to confirm the intended agent
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_SEND_MESSAGE_NO_EXACT_NAME_CONFIRM_REF_VAR_0
-->
No agent is named '${TOOL_RESULT_SEND_MESSAGE_NO_EXACT_NAME_CONFIRM_REF_VAR_0.to}' exactly. Re-send with the ref to confirm you mean:
