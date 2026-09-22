<!--
name: 'Tool Result: Send Message Peer Session Cannot Receive'
description: >-
  SendMessage denial/tool result when the target session is configured not to
  accept cross-session messages.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_SEND_MESSAGE_PEER_SESSION_CANNOT_RECEIVE_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_PEER_SESSION_CANNOT_RECEIVE_VAR_1
-->
Not sent: '${TOOL_RESULT_SEND_MESSAGE_PEER_SESSION_CANNOT_RECEIVE_VAR_0}' ${TOOL_RESULT_SEND_MESSAGE_PEER_SESSION_CANNOT_RECEIVE_VAR_1} — its Claude would never see the message. That session is set not to accept cross-session messages (the feature is off on its platform, or a setting or policy there refuses them); reach that machine another way, or ask its user to enable it (listings refresh within a few minutes — re-run ListAgents after they do).
