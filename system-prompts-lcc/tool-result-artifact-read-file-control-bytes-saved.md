<!--
name: 'Tool Result: Artifact read file — control bytes, saved to disk'
description: >-
  Artifact read file result when the file contains raw terminal control bytes:
  nothing is inlined, the full file is saved to a path, and the model is told to
  Read it.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_ARTIFACT_READ_FILE_CONTROL_BYTES_SAVED_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_FILE_CONTROL_BYTES_SAVED_VAR_1
  - TOOL_RESULT_ARTIFACT_READ_FILE_CONTROL_BYTES_SAVED_VAR_2
-->
${TOOL_RESULT_ARTIFACT_READ_FILE_CONTROL_BYTES_SAVED_VAR_0}; it contains raw terminal control bytes, so nothing is inlined; full file saved to ${TOOL_RESULT_ARTIFACT_READ_FILE_CONTROL_BYTES_SAVED_VAR_1.filepath}${TOOL_RESULT_ARTIFACT_READ_FILE_CONTROL_BYTES_SAVED_VAR_2||"; Read that file for the content"}]
