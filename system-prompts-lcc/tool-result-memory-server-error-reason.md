<!--
name: 'Tool Result: Memory server error reason'
description: >-
  Reason fragment interpolated into the 'memory store rejected the request'
  tool_result for an http_NNN failure code.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_SERVER_ERROR_REASON_VAR_0
-->
the server returned an error (${TOOL_RESULT_MEMORY_SERVER_ERROR_REASON_VAR_0.slice(5)})
