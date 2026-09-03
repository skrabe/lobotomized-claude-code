<!--
name: 'SendMessage: Remote Control Session Approval'
description: >-
  Permission-request text for messaging a Claude session on another machine over
  Remote Control; reaches the model as the tool_result on rejection.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_REMOTE_CONTROL_SESSION_APPROVAL_VAR_0
-->
Send a message to Remote Control session '${TOOL_RESULT_SEND_MESSAGE_REMOTE_CONTROL_SESSION_APPROVAL_VAR_0.displayName}'? It reaches the receiving Claude (on another machine) via Anthropic's servers as a cross-session message — marked as from another Claude session, not from its user.
