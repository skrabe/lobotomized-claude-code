<!--
name: 'Tool result: artifact file outside working dir'
description: >-
  Artifact publish error: a file is outside the allowed folders; copy it in and
  use the copy's path.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_COPY_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_COPY_VAR_1
  - TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_COPY_VAR_2
  - TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_COPY_VAR_3
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_COPY_VAR_0(TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_COPY_VAR_1)} is outside ${TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_COPY_VAR_2}, so a publish cannot read it. Copy the file to ${TOOL_RESULT_ARTIFACT_FILES_OUTSIDE_WORKING_DIR_COPY_VAR_3} and use the copy's path.
