<!--
name: PDF too many pages error
description: >-
  Read-tool error result returned to the model when a PDF has too many pages to
  read at once.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_PDF_TOO_MANY_PAGES_VAR_0
  - TOOL_RESULT_PDF_TOO_MANY_PAGES_VAR_1
-->
This PDF has ${TOOL_RESULT_PDF_TOO_MANY_PAGES_VAR_0} pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum ${TOOL_RESULT_PDF_TOO_MANY_PAGES_VAR_1} pages per request.
