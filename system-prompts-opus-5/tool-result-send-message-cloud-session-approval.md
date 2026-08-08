<!--
name: 'SendMessage: Cloud Session Approval'
description: >-
  Permission-request text for messaging a Claude session running in the cloud;
  reaches the model as the tool_result on rejection.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSION_APPROVAL_VAR_0
-->
Send a message to cloud session '${TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSION_APPROVAL_VAR_0.displayName}'? It reaches the receiving Claude (running in the cloud) via Anthropic's servers as a cross-session message — marked as from another Claude session, not from its user.
