<!--
name: Artifact read_file path invalid on Windows
description: >-
  Rejection reason for a read_file path that cannot be a Windows file name
  (reserved device name, trailing dot/space, or forbidden character).
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_READ_FILE_PATH_INVALID_ON_WINDOWS_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_FILE_PATH_INVALID_ON_WINDOWS_VAR_1
-->
path ${TOOL_RESULT_ARTIFACT_READ_FILE_PATH_INVALID_ON_WINDOWS_VAR_0(TOOL_RESULT_ARTIFACT_READ_FILE_PATH_INVALID_ON_WINDOWS_VAR_1)} cannot be a file name on Windows (reserved device name, trailing dot or space, or one of < > " | *)
