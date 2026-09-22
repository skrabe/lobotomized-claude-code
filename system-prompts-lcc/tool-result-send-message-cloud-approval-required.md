<!--
name: Cross-machine send needs approval — isolatePeerMachines
description: >-
  Result returned to Claude when a cross-session send was denied at the
  permission phase under isolatePeerMachines, stating nothing was sent; now
  shared by SendMessage and SendFile.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_APPROVAL_REQUIRED_VAR_0
-->
isolatePeerMachines is enabled: sending to ${TOOL_RESULT_SEND_MESSAGE_CLOUD_APPROVAL_REQUIRED_VAR_0} needs your approval — nothing was sent.
