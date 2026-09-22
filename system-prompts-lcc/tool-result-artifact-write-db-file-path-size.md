<!--
name: 'Tool Result: Artifact write_db File Path Size'
description: >-
  cPv.size error thrown to the model when write_db's file_path is empty or
  larger than the JSON byte cap.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WRITE_DB_FILE_PATH_SIZE_VAR_0
  - TOOL_RESULT_ARTIFACT_WRITE_DB_FILE_PATH_SIZE_VAR_1
-->
file_path is empty or larger than ${TOOL_RESULT_ARTIFACT_WRITE_DB_FILE_PATH_SIZE_VAR_0} bytes — write_db reads at most that much JSON, and the document must serialize to ${TOOL_RESULT_ARTIFACT_WRITE_DB_FILE_PATH_SIZE_VAR_1} bytes or fewer
