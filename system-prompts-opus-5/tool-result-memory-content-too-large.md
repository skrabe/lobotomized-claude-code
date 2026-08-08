<!--
name: 'Tool Result: Memory document over size cap'
description: >-
  Refusal returned on memory_write when the content exceeds the per-document
  byte cap, telling the model to split it up.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_CONTENT_TOO_LARGE_VAR_0
  - TOOL_RESULT_MEMORY_CONTENT_TOO_LARGE_VAR_1
-->
Content is ${TOOL_RESULT_MEMORY_CONTENT_TOO_LARGE_VAR_0} bytes; a memory document is capped at ${TOOL_RESULT_MEMORY_CONTENT_TOO_LARGE_VAR_1} bytes. Split it into smaller documents.
