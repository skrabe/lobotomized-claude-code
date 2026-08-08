<!--
name: 'Tool Result: SendFile Bridge Sessions Unchecked'
description: >-
  Note appended to SendFile's no-peer-session-reachable refusal when the
  cloud/bridge session list could not be fetched.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SENDFILE_BRIDGE_SESSIONS_UNCHECKED_VAR_0
  - TOOL_RESULT_SENDFILE_BRIDGE_SESSIONS_UNCHECKED_VAR_1
  - TOOL_RESULT_SENDFILE_BRIDGE_SESSIONS_UNCHECKED_VAR_2
  - TOOL_RESULT_SENDFILE_BRIDGE_SESSIONS_UNCHECKED_VAR_3
-->

${TOOL_RESULT_SENDFILE_BRIDGE_SESSIONS_UNCHECKED_VAR_0} sessions on other machines could not be checked just now, so they were not searched. If '${TOOL_RESULT_SENDFILE_BRIDGE_SESSIONS_UNCHECKED_VAR_1}' is one, retry${TOOL_RESULT_SENDFILE_BRIDGE_SESSIONS_UNCHECKED_VAR_2?` (or run ${TOOL_RESULT_SENDFILE_BRIDGE_SESSIONS_UNCHECKED_VAR_3} first)`:""}.
