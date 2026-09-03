<!--
name: 'Tool Result: Cloud Session Local Changes Too Large'
description: >-
  Cloud-session create-fail message when local changes are too large to upload
  and the working tree cannot be bundled instead.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_TOO_LARGE_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_TOO_LARGE_VAR_1
  - TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_TOO_LARGE_VAR_2
-->
No cloud session was started: ${TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_TOO_LARGE_VAR_0[n]}, and ${TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_TOO_LARGE_VAR_1.repository_too_large}, so the working tree cannot be uploaded instead. To start one, ${TOOL_RESULT_CLOUD_SESSION_LOCAL_CHANGES_TOO_LARGE_VAR_2}
