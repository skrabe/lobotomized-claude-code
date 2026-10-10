<!--
name: 'Tool Result: Read long lines footer'
description: >-
  Footer on Read results for files with very long lines explaining character
  truncation and paging by offset
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_0
  - TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_1
  - TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_2
  - TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_3
  - TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_4
  - TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_5
  - TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_6
  - TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_7
-->
${TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_0}: showing the first ${TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_1.length} of ${TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_2.length} characters (${TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_3.tokenCount} tokens, ${TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_4}); this file has very long lines and cannot be paginated by line. Use ${TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_5} to find a specific section, or ${TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_6} with offset/limit to page through it.${TOOL_RESULT_READ_LONG_LINES_FOOTER_VAR_7} Do NOT answer from this excerpt alone if the answer may be elsewhere in the file.]
