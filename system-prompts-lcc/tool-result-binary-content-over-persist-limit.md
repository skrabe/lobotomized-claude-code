<!--
name: 'Tool Result: Binary Content Over Persist Limit'
description: >-
  Error returned by persistBinaryContent() and interpolated verbatim into
  model-facing tool-result text such as 'Binary content could not be saved to
  disk: ${error}' for MCP resources and MCP task results.
ccVersion: 2.1.214
variables:
  - TOOL_RESULT_BINARY_CONTENT_OVER_PERSIST_LIMIT_VAR_0
  - TOOL_RESULT_BINARY_CONTENT_OVER_PERSIST_LIMIT_VAR_1
-->
content is ${TOOL_RESULT_BINARY_CONTENT_OVER_PERSIST_LIMIT_VAR_0.length} bytes, over the ${TOOL_RESULT_BINARY_CONTENT_OVER_PERSIST_LIMIT_VAR_1} byte persist limit
