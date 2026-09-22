<!--
name: 'Tool Result: PDF Page Count Unknown'
description: >-
  Read-tool error when pdfinfo cannot determine page count, directing the model
  to pass an explicit pages range.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_PDF_PAGE_COUNT_UNKNOWN_VAR_0
  - TOOL_RESULT_PDF_PAGE_COUNT_UNKNOWN_VAR_1
  - TOOL_RESULT_PDF_PAGE_COUNT_UNKNOWN_VAR_2
  - TOOL_RESULT_PDF_PAGE_COUNT_UNKNOWN_VAR_3
  - TOOL_RESULT_PDF_PAGE_COUNT_UNKNOWN_VAR_4
-->
This PDF's page count is unknown (${TOOL_RESULT_PDF_PAGE_COUNT_UNKNOWN_VAR_0(TOOL_RESULT_PDF_PAGE_COUNT_UNKNOWN_VAR_1.pdfinfoFailure)}). At ${TOOL_RESULT_PDF_PAGE_COUNT_UNKNOWN_VAR_2(TOOL_RESULT_PDF_PAGE_COUNT_UNKNOWN_VAR_3.size)} it may be too long to read whole. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum ${TOOL_RESULT_PDF_PAGE_COUNT_UNKNOWN_VAR_4} pages per request.
