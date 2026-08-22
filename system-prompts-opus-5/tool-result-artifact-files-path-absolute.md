<!--
name: 'Artifact files: published path is absolute'
description: >-
  Path-validation tool-error returned to the model when a published path starts
  with "/". CC 2.1.239 refactored these into a shared Gem(e,label) validator,
  hoisting the "files: published path" prefix into a call-site argument; id
  reused from 2.1.238.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_1
  - TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_2
-->
${TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_0} ${TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_1.stringify(TOOL_RESULT_ARTIFACT_FILES_PATH_ABSOLUTE_VAR_2)} is absolute — published paths are relative to the artifact root
