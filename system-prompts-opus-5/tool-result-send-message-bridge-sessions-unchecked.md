<!--
name: 'Tool Result: Bridge Sessions Could Not Be Checked'
description: >-
  Note appended to SendMessage's not-reachable result when the cloud/bridge
  session list could not be fetched, explaining those sessions are reply-only
  from here.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_2
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_3
-->

${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_0} sessions on other machines could not be checked just now, so they were not searched. If '${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_1.to}' is one, retry${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_2?` (or run ${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_3} first)`:""} — do not fall back to the send_message connector; it cannot reach these sessions.
