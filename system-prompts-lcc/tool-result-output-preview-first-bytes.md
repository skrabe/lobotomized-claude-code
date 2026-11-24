<!--
name: 'Tool result: output preview (first N bytes)'
description: >-
  Leading preview of a tool output that was too large and persisted to a file:
  header plus the preview text and a "..." marker when there is more.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_OUTPUT_PREVIEW_FIRST_BYTES_VAR_0
  - TOOL_RESULT_OUTPUT_PREVIEW_FIRST_BYTES_VAR_1
  - TOOL_RESULT_OUTPUT_PREVIEW_FIRST_BYTES_VAR_2
  - TOOL_RESULT_OUTPUT_PREVIEW_FIRST_BYTES_VAR_3
-->
Preview (first ${TOOL_RESULT_OUTPUT_PREVIEW_FIRST_BYTES_VAR_0(TOOL_RESULT_OUTPUT_PREVIEW_FIRST_BYTES_VAR_1)}):
${TOOL_RESULT_OUTPUT_PREVIEW_FIRST_BYTES_VAR_2(TOOL_RESULT_OUTPUT_PREVIEW_FIRST_BYTES_VAR_3.preview)}${TOOL_RESULT_OUTPUT_PREVIEW_FIRST_BYTES_VAR_3.hasMore?`
...
`:`
`}
