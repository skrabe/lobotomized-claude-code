<!--
name: 'Tool Result: PDF Page Image Failed'
description: Reports that a specific extracted PDF page could not be processed as an image.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_PDF_PAGE_IMAGE_FAILED_VAR_0
  - TOOL_RESULT_PDF_PAGE_IMAGE_FAILED_VAR_1
  - TOOL_RESULT_PDF_PAGE_IMAGE_FAILED_VAR_2
-->
[Page ${TOOL_RESULT_PDF_PAGE_IMAGE_FAILED_VAR_0+TOOL_RESULT_PDF_PAGE_IMAGE_FAILED_VAR_1} could not be processed as an image${TOOL_RESULT_PDF_PAGE_IMAGE_FAILED_VAR_2.error?`: ${TOOL_RESULT_PDF_PAGE_IMAGE_FAILED_VAR_2.error}`:""}]
