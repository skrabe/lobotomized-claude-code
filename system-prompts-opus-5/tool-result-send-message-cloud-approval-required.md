<!--
name: 'Tool Result: Cloud Send Needs Approval'
description: >-
  SendMessage failure result when isolatePeerMachines is on and the user did not
  approve the cross-machine send to a cloud session.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_APPROVAL_REQUIRED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_APPROVAL_REQUIRED_VAR_1
-->
isolatePeerMachines is enabled: sending to ${TOOL_RESULT_SEND_MESSAGE_CLOUD_APPROVAL_REQUIRED_VAR_0} '${TOOL_RESULT_SEND_MESSAGE_CLOUD_APPROVAL_REQUIRED_VAR_1.displayName}' needs your approval — nothing was sent.
