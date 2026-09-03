<!--
name: 'Tool Result: Artifact Type File Path Outside Root'
description: >-
  jPv validation error returned to the model when a typed-artifact data file
  does not live under `root` or the working directory.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_0
  - TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_1
  - TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_2
  - TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_3
  - TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_4
-->
file_path: a data file is served at its path relative to ${TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_0?"`root`":"the working directory"}, so it must live inside it — ${TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_1(TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_2)} is not inside ${TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_1(TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_3)}${TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_0?` (relative paths resolve against the working directory ${TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_1(TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_4)}); move it there or correct the paths`:"; move it there, or pass `files` with a `root` that contains it"}
