<!--
name: tool-result-pdf-pages-extracted
description: >-
  Read tool_result content block reporting how many PDF pages were extracted
  from a file and its original size.
ccVersion: 2.1.191
variables:
  - TOOL_RESULT_PDF_PAGES_EXTRACTED_VAR_0
  - TOOL_RESULT_PDF_PAGES_EXTRACTED_VAR_1
-->
PDF pages extracted: ${TOOL_RESULT_PDF_PAGES_EXTRACTED_VAR_0.file.count} page(s) from ${TOOL_RESULT_PDF_PAGES_EXTRACTED_VAR_0.file.filePath} (${TOOL_RESULT_PDF_PAGES_EXTRACTED_VAR_1(TOOL_RESULT_PDF_PAGES_EXTRACTED_VAR_0.file.originalSize)})
