<!--
name: 'SendMessage: Unverified Peer Approval'
description: >-
  Permission-request text when the peer-session list could not be checked and
  isolatePeerMachines is on, so the recipient may be on another machine.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_UNVERIFIED_PEER_APPROVAL_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_UNVERIFIED_PEER_APPROVAL_VAR_1
-->
Send a message to '${TOOL_RESULT_SEND_MESSAGE_UNVERIFIED_PEER_APPROVAL_VAR_0.to}'? Just now ${TOOL_RESULT_SEND_MESSAGE_UNVERIFIED_PEER_APPROVAL_VAR_1}, so it is unknown whether this name is a Claude session on another machine (isolatePeerMachines is enabled).
