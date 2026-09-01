<!--
name: tool-result-pdf-file-read
description: >-
  Read tool_result content block announcing a PDF file was read, with its path
  and original size.
ccVersion: 2.1.191
variables:
  - TOOL_RESULT_PDF_FILE_READ_VAR_0
  - TOOL_RESULT_PDF_FILE_READ_VAR_1
-->
PDF file read: ${TOOL_RESULT_PDF_FILE_READ_VAR_0.file.filePath} (${TOOL_RESULT_PDF_FILE_READ_VAR_1(TOOL_RESULT_PDF_FILE_READ_VAR_0.file.originalSize)})
