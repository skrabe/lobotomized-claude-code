<!--
name: PDF page out-of-range error
description: >-
  Read-tool error result returned to the model when the requested PDF page range
  is outside the document.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_0
  - TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_1
  - TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_2
  - TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_3
  - TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_4
  - TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_5
-->
Requested ${TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_0(TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_1)} is outside the document (PDF has ${TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_2} ${TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_3(TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_2,"page")}). Use a range within 1-${TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_2}, maximum ${TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_4} pages per request (e.g. pages: "1-${TOOL_RESULT_PDF_PAGE_OUT_OF_RANGE_VAR_5}").
