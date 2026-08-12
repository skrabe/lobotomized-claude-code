<!--
name: Cloud session send success
description: SendMessage success result returned to the model.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SUCCESS_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SUCCESS_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SUCCESS_VAR_2
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SUCCESS_VAR_3
-->
“${TOOL_RESULT_SEND_MESSAGE_CLOUD_SUCCESS_VAR_0}” → ${TOOL_RESULT_SEND_MESSAGE_CLOUD_SUCCESS_VAR_1.displayName} (${TOOL_RESULT_SEND_MESSAGE_CLOUD_SUCCESS_VAR_1.via==="cloud"?"a Claude session running in the cloud":"a Claude session on another machine, over Remote Control"}${TOOL_RESULT_SEND_MESSAGE_CLOUD_SUCCESS_VAR_2?"; one-way: Remote Control is not connected, so the receiver cannot address a reply to this session":""})${TOOL_RESULT_SEND_MESSAGE_CLOUD_SUCCESS_VAR_3}
