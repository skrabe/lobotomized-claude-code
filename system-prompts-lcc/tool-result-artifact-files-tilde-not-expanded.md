<!--
name: 'Tool result: Artifact file path tilde not expanded'
description: >-
  Error returned to the model when a `files` source path uses a leading ~ which
  is not expanded here.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_FILES_TILDE_NOT_EXPANDED_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_TILDE_NOT_EXPANDED_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_TILDE_NOT_EXPANDED_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_TILDE_NOT_EXPANDED_VAR_1)} — "~" is not expanded here; pass a base-relative or absolute path
