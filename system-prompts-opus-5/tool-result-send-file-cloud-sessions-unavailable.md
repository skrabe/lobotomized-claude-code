<!--
name: 'Tool Result: SendFile cloud sessions unavailable'
description: >-
  Tells Claude in a refused SendFile result that Remote Control and cloud
  sessions could not be searched and the operation should be retried.
ccVersion: 2.1.228
variables:
  - TOOL_RESULT_SEND_FILE_CLOUD_SESSIONS_UNAVAILABLE_VAR_0
  - TOOL_RESULT_SEND_FILE_CLOUD_SESSIONS_UNAVAILABLE_VAR_1
  - TOOL_RESULT_SEND_FILE_CLOUD_SESSIONS_UNAVAILABLE_VAR_2
-->

Your account's other sessions (Remote Control and cloud) could not be checked just now, so they were not searched. If '${TOOL_RESULT_SEND_FILE_CLOUD_SESSIONS_UNAVAILABLE_VAR_0}' is one, retry${TOOL_RESULT_SEND_FILE_CLOUD_SESSIONS_UNAVAILABLE_VAR_1?` (or run ${TOOL_RESULT_SEND_FILE_CLOUD_SESSIONS_UNAVAILABLE_VAR_2} first)`:""}.
