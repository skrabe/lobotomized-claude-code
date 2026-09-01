<!--
name: 'Tool Result: Artifact root outside working directory'
description: >-
  Validation error for the Artifact publish `root` base directory, returned to
  the model when an absolute root lies outside the working directory.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKDIR_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKDIR_VAR_1
-->
root: ${TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKDIR_VAR_0.stringify(TOOL_RESULT_ARTIFACT_ROOT_OUTSIDE_WORKDIR_VAR_1)} is outside the working directory — pass a working-directory-relative path
