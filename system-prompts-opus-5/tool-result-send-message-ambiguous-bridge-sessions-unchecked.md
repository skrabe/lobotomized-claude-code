<!--
name: SendMessage Ambiguous Bridge Sessions Unchecked
description: >-
  Note appended to an ambiguous SendMessage result when sessions on other
  machines could not be checked, asking the model to retry or list sessions.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_BRIDGE_SESSIONS_UNCHECKED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_BRIDGE_SESSIONS_UNCHECKED_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_BRIDGE_SESSIONS_UNCHECKED_VAR_2
-->

${TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_BRIDGE_SESSIONS_UNCHECKED_VAR_0} sessions on other machines could not be checked just now, so this list may be missing one; if you meant a session on another machine, retry${TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_BRIDGE_SESSIONS_UNCHECKED_VAR_1?` (or run ${TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_BRIDGE_SESSIONS_UNCHECKED_VAR_2} first)`:""}.
