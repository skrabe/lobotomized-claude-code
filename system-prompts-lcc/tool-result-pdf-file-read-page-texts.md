<!--
name: 'Tool Result: PDF file read page texts'
description: Introduces the text of all pages of a read PDF
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_PDF_FILE_READ_PAGE_TEXTS_VAR_0
  - TOOL_RESULT_PDF_FILE_READ_PAGE_TEXTS_VAR_1
-->
PDF file read: ${TOOL_RESULT_PDF_FILE_READ_PAGE_TEXTS_VAR_0.path} (${TOOL_RESULT_PDF_FILE_READ_PAGE_TEXTS_VAR_1(TOOL_RESULT_PDF_FILE_READ_PAGE_TEXTS_VAR_0.data.originalSize)}). This is the text of ${TOOL_RESULT_PDF_FILE_READ_PAGE_TEXTS_VAR_0.pages===1?"its one page":`all ${TOOL_RESULT_PDF_FILE_READ_PAGE_TEXTS_VAR_0.pages} pages`}. It shows no pictures, charts or scanned pages: those are in the file alone.${TOOL_RESULT_PDF_FILE_READ_PAGE_TEXTS_VAR_0.data.picturePages===void 0?"":` ${TOOL_RESULT_PDF_FILE_READ_PAGE_TEXTS_VAR_0.data.picturePages}`}
