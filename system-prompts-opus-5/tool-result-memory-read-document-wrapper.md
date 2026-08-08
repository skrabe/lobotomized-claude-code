<!--
name: 'Tool Result: memory_read document wrapper'
description: >-
  Wrapper the memory_read tool result uses around a fetched memory document —
  shared-store reference-data header, updated/version line, and the document
  body.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_READ_DOCUMENT_WRAPPER_VAR_0
  - TOOL_RESULT_MEMORY_READ_DOCUMENT_WRAPPER_VAR_1
  - TOOL_RESULT_MEMORY_READ_DOCUMENT_WRAPPER_VAR_2
  - TOOL_RESULT_MEMORY_READ_DOCUMENT_WRAPPER_VAR_3
-->
${TOOL_RESULT_MEMORY_READ_DOCUMENT_WRAPPER_VAR_0}
[updated: ${TOOL_RESULT_MEMORY_READ_DOCUMENT_WRAPPER_VAR_1.updatedAt?.TOOL_RESULT_MEMORY_READ_DOCUMENT_WRAPPER_VAR_2(/^\d{4}-\d{2}-\d{2}/)?.[0]??"unknown"}] [version: ${TOOL_RESULT_MEMORY_READ_DOCUMENT_WRAPPER_VAR_1.version??""}]${TOOL_RESULT_MEMORY_READ_DOCUMENT_WRAPPER_VAR_3}
${TOOL_RESULT_MEMORY_READ_DOCUMENT_WRAPPER_VAR_1.content??""}
