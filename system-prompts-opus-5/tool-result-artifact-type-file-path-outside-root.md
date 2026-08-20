<!--
name: 'Tool Result: Artifact Type File Path Outside Root'
description: >-
  jPv validation error returned to the model when a typed-artifact data file
  does not live under `root` or the working directory.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_0
-->
file_path: a data file is served at its path relative to ${TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_0?"`root`":"the working directory"}, so it must live inside it — move it there${TOOL_RESULT_ARTIFACT_TYPE_FILE_PATH_OUTSIDE_ROOT_VAR_0?"":", or pass `files` with a `root` that contains it"}
