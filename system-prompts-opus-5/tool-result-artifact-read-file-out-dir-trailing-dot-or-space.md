<!--
name: Artifact read_file out_dir trailing dot or space
description: >-
  Rejection reason for an out_dir whose directory name ends in a dot or space on
  Windows.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_TRAILING_DOT_OR_SPACE_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_TRAILING_DOT_OR_SPACE_VAR_1
-->
${TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_TRAILING_DOT_OR_SPACE_VAR_0===void 0||TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_TRAILING_DOT_OR_SPACE_VAR_0===""?"the default save directory":`out_dir ${TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_TRAILING_DOT_OR_SPACE_VAR_1(TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_TRAILING_DOT_OR_SPACE_VAR_0)}`} has a name ending in a dot or space, which Windows would save under a different name
