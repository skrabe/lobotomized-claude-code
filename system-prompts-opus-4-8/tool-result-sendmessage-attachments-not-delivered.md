<!--
name: 'Tool Result: SendMessage attachments not delivered'
description: >-
  Header of the SendMessage error tool_result telling the model the message
  reached the user but N attachments failed to upload.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SENDMESSAGE_ATTACHMENTS_NOT_DELIVERED_VAR_0
  - TOOL_RESULT_SENDMESSAGE_ATTACHMENTS_NOT_DELIVERED_VAR_1
  - TOOL_RESULT_SENDMESSAGE_ATTACHMENTS_NOT_DELIVERED_VAR_2
-->
Message delivered to user.${TOOL_RESULT_SENDMESSAGE_ATTACHMENTS_NOT_DELIVERED_VAR_0}
${TOOL_RESULT_SENDMESSAGE_ATTACHMENTS_NOT_DELIVERED_VAR_1.length} ${TOOL_RESULT_SENDMESSAGE_ATTACHMENTS_NOT_DELIVERED_VAR_2(TOOL_RESULT_SENDMESSAGE_ATTACHMENTS_NOT_DELIVERED_VAR_1.length,"attachment")} could not be delivered:
