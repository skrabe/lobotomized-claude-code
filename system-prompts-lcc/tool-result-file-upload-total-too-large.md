<!--
name: 'Tool result: File upload total too large'
description: >-
  Error when the files in one upload call exceed the total size limit, so
  nothing was uploaded
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_0
  - TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_1
  - TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_2
-->
Cannot upload "${TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_0}": the files in one call can total at most ${TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_1>=1e6?`${(TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_2.floor(TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_1/1e5)/10).toFixed(1)} MB`:TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_1>=1000?`${TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_2.floor(TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_1/1000)} KB`:`${TOOL_RESULT_FILE_UPLOAD_TOTAL_TOO_LARGE_VAR_1} bytes`}, and nothing in this call was uploaded. Upload a smaller file, or one file per call if the page takes them one at a time. Otherwise ask the user to choose the file in their browser themselves.
