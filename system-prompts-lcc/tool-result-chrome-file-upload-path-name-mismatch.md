<!--
name: 'Tool Result: Chrome file_upload path does not end in file name'
description: >-
  Refuses a Chrome file_upload whose path does not end in the chosen file's name
  and asks to call again with the file's own path
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_CHROME_FILE_UPLOAD_PATH_NAME_MISMATCH_VAR_0
  - TOOL_RESULT_CHROME_FILE_UPLOAD_PATH_NAME_MISMATCH_VAR_1
  - TOOL_RESULT_CHROME_FILE_UPLOAD_PATH_NAME_MISMATCH_VAR_2
  - TOOL_RESULT_CHROME_FILE_UPLOAD_PATH_NAME_MISMATCH_VAR_3
-->
Nothing was uploaded: the path "${TOOL_RESULT_CHROME_FILE_UPLOAD_PATH_NAME_MISMATCH_VAR_0(TOOL_RESULT_CHROME_FILE_UPLOAD_PATH_NAME_MISMATCH_VAR_1(TOOL_RESULT_CHROME_FILE_UPLOAD_PATH_NAME_MISMATCH_VAR_2))}" does not end in the file's name, "${TOOL_RESULT_CHROME_FILE_UPLOAD_PATH_NAME_MISMATCH_VAR_0(TOOL_RESULT_CHROME_FILE_UPLOAD_PATH_NAME_MISMATCH_VAR_3.name)}". Call file_upload again with a path to the file itself, ending in its name.
