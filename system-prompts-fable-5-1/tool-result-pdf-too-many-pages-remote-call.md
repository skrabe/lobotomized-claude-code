<!--
name: PDF Too Many Pages Remote Call
description: >-
  Read-tool validateInput error when a served/cloud call would return a whole
  PDF or too many pages from this machine.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_PDF_TOO_MANY_PAGES_REMOTE_CALL_VAR_0
  - TOOL_RESULT_PDF_TOO_MANY_PAGES_REMOTE_CALL_VAR_1
-->
${TOOL_RESULT_PDF_TOO_MANY_PAGES_REMOTE_CALL_VAR_0?"A whole PDF cannot be returned from this machine to the calling session":`${TOOL_RESULT_PDF_TOO_MANY_PAGES_REMOTE_CALL_VAR_1} is too many pages to return from this machine in one call`}. Use the pages parameter with at most ${TOOL_RESULT_PDF_TOO_MANY_PAGES_REMOTE_CALL_VAR_2.pdfMaxPagesPerRead} pages per call (for example pages: 1-3, which come back as images), or read the file where the session runs.
