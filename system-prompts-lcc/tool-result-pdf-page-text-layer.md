<!--
name: 'Tool Result: PDF page text layer'
description: Text block giving the extracted text layer of a PDF page alongside its image
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_PDF_PAGE_TEXT_LAYER_VAR_0
  - TOOL_RESULT_PDF_PAGE_TEXT_LAYER_VAR_1
  - TOOL_RESULT_PDF_PAGE_TEXT_LAYER_VAR_2
  - TOOL_RESULT_PDF_PAGE_TEXT_LAYER_VAR_3
-->
Text layer of page ${TOOL_RESULT_PDF_PAGE_TEXT_LAYER_VAR_0+TOOL_RESULT_PDF_PAGE_TEXT_LAYER_VAR_1}:
${TOOL_RESULT_PDF_PAGE_TEXT_LAYER_VAR_2(TOOL_RESULT_PDF_PAGE_TEXT_LAYER_VAR_3.text)}
