<!--
name: 'Tool Result: Remote Host Unknown — Respell'
description: >-
  unknown_host tool_result when an attached machine matches ignoring case or an
  (offline) suffix, telling the model the exact lower-case name to use.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_UNKNOWN_RESPELL_VAR_0
  - TOOL_RESULT_REMOTE_HOST_UNKNOWN_RESPELL_VAR_1
  - TOOL_RESULT_REMOTE_HOST_UNKNOWN_RESPELL_VAR_2
  - TOOL_RESULT_REMOTE_HOST_UNKNOWN_RESPELL_VAR_3
-->
No machine named "${TOOL_RESULT_REMOTE_HOST_UNKNOWN_RESPELL_VAR_0}" is attached to this session — machine names are exact and lower-case: use "${TOOL_RESULT_REMOTE_HOST_UNKNOWN_RESPELL_VAR_1}"${TOOL_RESULT_REMOTE_HOST_UNKNOWN_RESPELL_VAR_2?' without the "(offline)" note':""}${TOOL_RESULT_REMOTE_HOST_UNKNOWN_RESPELL_VAR_3!==TOOL_RESULT_REMOTE_HOST_UNKNOWN_RESPELL_VAR_1?" — though it is not reachable right now, so a retry will fail until it reconnects":""}.
