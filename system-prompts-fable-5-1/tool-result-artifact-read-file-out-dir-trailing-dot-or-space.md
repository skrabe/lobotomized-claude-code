<!--
name: Artifact read_file out_dir trailing dot or space
description: >-
  Rejection reason for an out_dir whose directory name ends in a dot or space on
  Windows.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_TRAILING_DOT_OR_SPACE_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_TRAILING_DOT_OR_SPACE_VAR_1
-->
out_dir ${TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_TRAILING_DOT_OR_SPACE_VAR_0.stringify(TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_TRAILING_DOT_OR_SPACE_VAR_1)} has a name ending in a dot or space, which Windows would save under a different name
