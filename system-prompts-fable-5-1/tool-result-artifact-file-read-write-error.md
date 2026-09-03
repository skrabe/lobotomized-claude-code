<!--
name: Artifact File Read - Save Failed
description: >-
  read_file error reporting that the file was fetched but could not be written
  to disk, with the underlying errno.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_ERROR_VAR_1
-->
the file was fetched but could not be saved (${TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_ERROR_VAR_0(TOOL_RESULT_ARTIFACT_FILE_READ_WRITE_ERROR_VAR_1)??"unexpected error"})
