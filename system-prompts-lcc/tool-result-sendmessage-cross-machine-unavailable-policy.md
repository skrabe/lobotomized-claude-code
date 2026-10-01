<!--
name: 'Tool Result: Cross-machine messaging blocked by policy'
description: >-
  SendMessage tool result when an organization policy blocks reaching a
  bridge/cloud-session recipient, with the policy reason.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_SENDMESSAGE_CROSS_MACHINE_UNAVAILABLE_POLICY_VAR_0
-->
Cross-machine messaging is unavailable: ${TOOL_RESULT_SENDMESSAGE_CROSS_MACHINE_UNAVAILABLE_POLICY_VAR_0.reason} Messages to sessions on this machine still work.
