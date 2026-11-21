<!--
name: 'Tool result: artifact root outside working dir'
description: >-
  Artifact publish error: root is outside the allowed folders, so copy the files
  into an allowed folder and pass it as root.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKING_DIR_COPY_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKING_DIR_COPY_VAR_1
  - TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKING_DIR_COPY_VAR_2
  - TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKING_DIR_COPY_VAR_3
-->
root: ${TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKING_DIR_COPY_VAR_0(TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKING_DIR_COPY_VAR_1)} is outside ${TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKING_DIR_COPY_VAR_2}, so a publish cannot read from it. Copy the files to a folder ${TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKING_DIR_COPY_VAR_3} and pass that folder as \`root\`.
