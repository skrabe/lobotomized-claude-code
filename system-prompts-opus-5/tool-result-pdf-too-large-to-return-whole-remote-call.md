<!--
name: PDF Too Large To Return Whole Remote Call
description: >-
  Remote Read refusal when a whole-PDF payload exceeds the transport size
  budget.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_PDF_TOO_LARGE_TO_RETURN_WHOLE_REMOTE_CALL_VAR_0
  - TOOL_RESULT_PDF_TOO_LARGE_TO_RETURN_WHOLE_REMOTE_CALL_VAR_1
  - TOOL_RESULT_PDF_TOO_LARGE_TO_RETURN_WHOLE_REMOTE_CALL_VAR_2
-->
This PDF (${TOOL_RESULT_PDF_TOO_LARGE_TO_RETURN_WHOLE_REMOTE_CALL_VAR_0(TOOL_RESULT_PDF_TOO_LARGE_TO_RETURN_WHOLE_REMOTE_CALL_VAR_1.size)}) is larger than can be returned whole from this machine to the calling session (at most ${TOOL_RESULT_PDF_TOO_LARGE_TO_RETURN_WHOLE_REMOTE_CALL_VAR_0(TOOL_RESULT_PDF_TOO_LARGE_TO_RETURN_WHOLE_REMOTE_CALL_VAR_2.wholePdfMaxRawBytes)}). Use the pages parameter with at most ${TOOL_RESULT_PDF_TOO_LARGE_TO_RETURN_WHOLE_REMOTE_CALL_VAR_2.pdfMaxPagesPerRead} pages per call (for example pages: 1-3, which come back as images), or read the file where the session runs.
