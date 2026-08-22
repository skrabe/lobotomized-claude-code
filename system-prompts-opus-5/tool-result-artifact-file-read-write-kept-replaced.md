<!--
name: 'Artifact File Read - Replaced Copy Removed, Bytes Kept'
description: >-
  read_file error when the earlier copy was removed but the fetched file could
  not be moved into its place; the bytes stay at the .partial path.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_REPLACED_VAR_0
  - TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_REPLACED_VAR_1
  - TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_REPLACED_VAR_2
  - TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_REPLACED_VAR_3
-->
the earlier copy at ${TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_REPLACED_VAR_0.basename(TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_REPLACED_VAR_1)} was removed but the fetched file could not be moved into its place (${TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_REPLACED_VAR_2}) — the bytes are kept at ${TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_KEPT_REPLACED_VAR_3.partial}; move or delete that file
