<!--
name: Send target ambiguous — multiple peers
description: >-
  Refused-target SendFile result when a recipient name matches multiple peer
  sessions, asking the model to re-send with a specific ref.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PEER_SESSIONS_VAR_0
  - TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PEER_SESSIONS_VAR_1
  - TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PEER_SESSIONS_VAR_2
-->
'${TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PEER_SESSIONS_VAR_0}' matches ${TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PEER_SESSIONS_VAR_1.length} peer session(s). Re-send with the ref:
${TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PEER_SESSIONS_VAR_2}${TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PEER_SESSIONS_VAR_3}
