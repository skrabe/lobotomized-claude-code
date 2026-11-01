<!--
name: 'Tool result: output preview start and end'
description: >-
  Persisted-output preview showing the beginning and end of a large tool output
  with the omitted byte count between.
ccVersion: 2.1.316
variables:
  - TOOL_RESULT_OUTPUT_PREVIEW_START_AND_END_VAR_0
  - TOOL_RESULT_OUTPUT_PREVIEW_START_AND_END_VAR_1
  - TOOL_RESULT_OUTPUT_PREVIEW_START_AND_END_VAR_2
  - TOOL_RESULT_OUTPUT_PREVIEW_START_AND_END_VAR_3
-->
${TOOL_RESULT_OUTPUT_PREVIEW_START_AND_END_VAR_0}Preview (start and end):
${TOOL_RESULT_OUTPUT_PREVIEW_START_AND_END_VAR_1.preview}
[… ${TOOL_RESULT_OUTPUT_PREVIEW_START_AND_END_VAR_2(TOOL_RESULT_OUTPUT_PREVIEW_START_AND_END_VAR_3)} omitted …]
${TOOL_RESULT_OUTPUT_PREVIEW_START_AND_END_VAR_1.previewEnd}
