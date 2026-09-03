<!--
name: 'Tool Result: Remote Host Request Too Large'
description: >-
  request_too_large refuse/error tool_result when the call's input exceeds the
  per-host MiB cap and was not sent.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_REQUEST_TOO_LARGE_VAR_0
  - TOOL_RESULT_REMOTE_HOST_REQUEST_TOO_LARGE_VAR_1
  - TOOL_RESULT_REMOTE_HOST_REQUEST_TOO_LARGE_VAR_2
  - TOOL_RESULT_REMOTE_HOST_REQUEST_TOO_LARGE_VAR_3
-->
This call's input is ${TOOL_RESULT_REMOTE_HOST_REQUEST_TOO_LARGE_VAR_0(TOOL_RESULT_REMOTE_HOST_REQUEST_TOO_LARGE_VAR_1)} MiB, over the ${TOOL_RESULT_REMOTE_HOST_REQUEST_TOO_LARGE_VAR_0(TOOL_RESULT_REMOTE_HOST_REQUEST_TOO_LARGE_VAR_2)} MiB limit for calls to ${TOOL_RESULT_REMOTE_HOST_REQUEST_TOO_LARGE_VAR_3}; it was not sent.
