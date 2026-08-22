<!--
name: Artifact File Read - Bytes Kept After Failed Move
description: >-
  read_file error when the fetched file could not be moved to its destination;
  the bytes stay at the .partial path.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_VAR_0
  - TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_VAR_1
  - TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_VAR_2
  - TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_VAR_3
-->
the fetched file could not be moved to ${TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_VAR_0.basename(TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_VAR_1)} (${TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_VAR_2}) — the bytes are kept at ${TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_VAR_3.partial}; move or delete that file
