<!--
name: 'Tool Result: PDF too large, read by pages'
description: >-
  Text block substituted for a PDF too large to show whole in a tool result,
  telling Claude to read it again with the pages parameter
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_PDF_TOO_LARGE_READ_BY_PAGES_VAR_0
  - TOOL_RESULT_PDF_TOO_LARGE_READ_BY_PAGES_VAR_1
  - TOOL_RESULT_PDF_TOO_LARGE_READ_BY_PAGES_VAR_2
-->
[This PDF (${TOOL_RESULT_PDF_TOO_LARGE_READ_BY_PAGES_VAR_0(TOOL_RESULT_PDF_TOO_LARGE_READ_BY_PAGES_VAR_1)}) cannot be shown whole in this session. Read it again with the pages parameter, for example pages: "1-5", at most ${TOOL_RESULT_PDF_TOO_LARGE_READ_BY_PAGES_VAR_2} pages per call.]
