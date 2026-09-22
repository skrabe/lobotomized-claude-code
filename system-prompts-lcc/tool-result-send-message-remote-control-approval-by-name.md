<!--
name: 'SendMessage: Remote Control Approval (by name)'
description: >-
  Permission-request text for messaging a Remote Control session addressed by
  raw name; reaches the model as the tool_result on rejection.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_REMOTE_CONTROL_APPROVAL_BY_NAME_VAR_0
-->
Send a message to Remote Control session ${TOOL_RESULT_SEND_MESSAGE_REMOTE_CONTROL_APPROVAL_BY_NAME_VAR_0.to}? It reaches the receiving Claude (possibly another machine) via Anthropic's servers as a cross-session message — marked as from another Claude session, not from its user.
