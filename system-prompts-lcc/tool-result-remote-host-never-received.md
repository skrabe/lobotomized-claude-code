<!--
name: 'Tool Result: Remote Host Never Received'
description: >-
  not_received tool_result when the host reports it never got the call, so it
  did not run and a retry is safe.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_0
  - TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_1
  - TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_2
-->
${TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_0(TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_1,TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_2)}, and ${TOOL_RESULT_REMOTE_HOST_NEVER_RECEIVED_VAR_1} reports it never received it: it did not run. It is safe to retry.
