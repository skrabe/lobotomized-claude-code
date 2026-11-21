<!--
name: 'Tool Result: Read line range too large'
description: >-
  Read tool error when the requested line range holds more text than one read
  can return, telling the model to use a smaller limit or search.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_READ_LINE_RANGE_TOO_LARGE_VAR_0
  - TOOL_RESULT_READ_LINE_RANGE_TOO_LARGE_VAR_1
  - TOOL_RESULT_READ_LINE_RANGE_TOO_LARGE_VAR_2
  - TOOL_RESULT_READ_LINE_RANGE_TOO_LARGE_VAR_3
-->
${TOOL_RESULT_READ_LINE_RANGE_TOO_LARGE_VAR_0} ${TOOL_RESULT_READ_LINE_RANGE_TOO_LARGE_VAR_1(TOOL_RESULT_READ_LINE_RANGE_TOO_LARGE_VAR_2)} of text, more than a read can return. Use a smaller limit — or, if a single line is this large, no limit will fit it: search for specific content instead.${TOOL_RESULT_READ_LINE_RANGE_TOO_LARGE_VAR_3}
