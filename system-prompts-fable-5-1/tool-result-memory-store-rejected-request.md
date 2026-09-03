<!--
name: 'Tool Result: Memory store rejected the request'
description: >-
  Failure wrapper returned to the model when the memory backend refuses the
  request, with the reason phrase appended.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_STORE_REJECTED_REQUEST_VAR_0
  - TOOL_RESULT_MEMORY_STORE_REJECTED_REQUEST_VAR_1
-->
The memory store rejected the request: ${TOOL_RESULT_MEMORY_STORE_REJECTED_REQUEST_VAR_0(TOOL_RESULT_MEMORY_STORE_REJECTED_REQUEST_VAR_1.reason)}
