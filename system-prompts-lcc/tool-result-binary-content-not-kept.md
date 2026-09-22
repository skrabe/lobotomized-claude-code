<!--
name: 'Tool Result: Binary Content Not Kept'
description: >-
  Placeholder tool_result text when binary MCP resource bytes could not be
  persisted and are omitted.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_BINARY_CONTENT_NOT_KEPT_VAR_0
  - TOOL_RESULT_BINARY_CONTENT_NOT_KEPT_VAR_1
  - TOOL_RESULT_BINARY_CONTENT_NOT_KEPT_VAR_2
-->
[Binary content (${TOOL_RESULT_BINARY_CONTENT_NOT_KEPT_VAR_0.length<=100&&/^[\w.+-]+\/[\w.+-]+$/.test(TOOL_RESULT_BINARY_CONTENT_NOT_KEPT_VAR_0)?TOOL_RESULT_BINARY_CONTENT_NOT_KEPT_VAR_0:"application/octet-stream"}, ${TOOL_RESULT_BINARY_CONTENT_NOT_KEPT_VAR_1(TOOL_RESULT_BINARY_CONTENT_NOT_KEPT_VAR_2)}) was not kept: it could not be saved.]
