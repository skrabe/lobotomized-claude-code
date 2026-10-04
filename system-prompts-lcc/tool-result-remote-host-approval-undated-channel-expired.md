<!--
name: 'Tool Result: Remote host approval answer too old'
description: >-
  Tells the model a permission approval reached the target too long after the
  request was raised (dated or over a channel with no delivery time) to be
  honoured, so the request was withdrawn and nothing ran.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_UNDATED_CHANNEL_EXPIRED_VAR_0
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_UNDATED_CHANNEL_EXPIRED_VAR_1
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_UNDATED_CHANNEL_EXPIRED_VAR_2
  - TOOL_RESULT_REMOTE_HOST_APPROVAL_UNDATED_CHANNEL_EXPIRED_VAR_3
-->
This approval reached ${TOOL_RESULT_REMOTE_HOST_APPROVAL_UNDATED_CHANNEL_EXPIRED_VAR_0} ${TOOL_RESULT_REMOTE_HOST_APPROVAL_UNDATED_CHANNEL_EXPIRED_VAR_1} is honoured for (${TOOL_RESULT_REMOTE_HOST_APPROVAL_UNDATED_CHANNEL_EXPIRED_VAR_2} ${TOOL_RESULT_REMOTE_HOST_APPROVAL_UNDATED_CHANNEL_EXPIRED_VAR_3(TOOL_RESULT_REMOTE_HOST_APPROVAL_UNDATED_CHANNEL_EXPIRED_VAR_2,"hour")}) — so the request was withdrawn and nothing ran. Send the call again if it is still wanted.
