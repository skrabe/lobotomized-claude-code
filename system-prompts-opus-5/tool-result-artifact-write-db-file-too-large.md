<!--
name: 'Tool Result: write_db File Too Large'
description: >-
  validateInput tooLarge callback for write_db when file_path exceeds the JSON
  byte limit; the failure message is returned to the model as a tool error.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WRITE_DB_FILE_TOO_LARGE_VAR_0
  - TOOL_RESULT_ARTIFACT_WRITE_DB_FILE_TOO_LARGE_VAR_1
  - TOOL_RESULT_ARTIFACT_WRITE_DB_FILE_TOO_LARGE_VAR_2
-->
file_path is ${TOOL_RESULT_ARTIFACT_WRITE_DB_FILE_TOO_LARGE_VAR_0} bytes — write_db reads at most ${TOOL_RESULT_ARTIFACT_WRITE_DB_FILE_TOO_LARGE_VAR_1} bytes of JSON, and the document it holds must serialize to ${TOOL_RESULT_ARTIFACT_WRITE_DB_FILE_TOO_LARGE_VAR_2} bytes or fewer
