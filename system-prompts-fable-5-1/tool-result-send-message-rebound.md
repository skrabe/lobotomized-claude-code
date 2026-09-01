<!--
name: Recipient rebound
description: >-
  SendMessage pin-guard tool-error returned to the model when a name now
  resolves to a different agent.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_SEND_MESSAGE_REBOUND_VAR_0
-->
'${TOOL_RESULT_SEND_MESSAGE_REBOUND_VAR_0.name}' now resolves to a different agent than it did earlier in this conversation: earlier sends went to [${TOOL_RESULT_SEND_MESSAGE_REBOUND_VAR_0.previous.ref}], which this name no longer reaches. Nothing was sent.
