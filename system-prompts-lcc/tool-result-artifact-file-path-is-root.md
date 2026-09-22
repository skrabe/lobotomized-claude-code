<!--
name: 'Tool Result: Artifact File Path Is Root'
description: >-
  Type-instance file_path error when the path is `root` or the working directory
  itself rather than a data file inside it.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_FILE_PATH_IS_ROOT_VAR_0
  - TOOL_RESULT_ARTIFACT_FILE_PATH_IS_ROOT_VAR_1
  - TOOL_RESULT_ARTIFACT_FILE_PATH_IS_ROOT_VAR_2
-->
file_path: ${TOOL_RESULT_ARTIFACT_FILE_PATH_IS_ROOT_VAR_0(TOOL_RESULT_ARTIFACT_FILE_PATH_IS_ROOT_VAR_1)} is ${TOOL_RESULT_ARTIFACT_FILE_PATH_IS_ROOT_VAR_2?"`root`":"the working directory"} itself — name a data file inside it
