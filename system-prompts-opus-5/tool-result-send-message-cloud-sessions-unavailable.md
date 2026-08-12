<!--
name: 'Tool Result: Send message cloud sessions unavailable'
description: >-
  Tells Claude in a failed send-message result that remote sessions could not be
  searched and the connector cannot reach them.
ccVersion: 2.1.228
variables:
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSIONS_UNAVAILABLE_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSIONS_UNAVAILABLE_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSIONS_UNAVAILABLE_VAR_2
-->

Your account's other sessions (Remote Control and cloud) could not be checked just now, so they were not searched. If '${TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSIONS_UNAVAILABLE_VAR_0.to}' is one, retry${TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSIONS_UNAVAILABLE_VAR_1?` (or run ${TOOL_RESULT_SEND_MESSAGE_CLOUD_SESSIONS_UNAVAILABLE_VAR_2} first)`:""} — do not fall back to the send_message connector; it cannot reach these sessions.
