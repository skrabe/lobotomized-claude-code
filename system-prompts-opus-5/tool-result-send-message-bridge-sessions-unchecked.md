<!--
name: 'Tool Result: Bridge Sessions Could Not Be Checked'
description: >-
  Note appended to SendMessage's not-reachable result when the cloud/bridge
  session list could not be fetched, explaining those sessions are reply-only
  from here.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_2
-->

${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_0} sessions could not be checked just now. If '${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_1.to}' is a ${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_0} session on this account, note those are reply-only from here — messageable ${TOOL_RESULT_SEND_MESSAGE_BRIDGE_SESSIONS_UNCHECKED_VAR_2} — and the send_message connector cannot reach them either.
