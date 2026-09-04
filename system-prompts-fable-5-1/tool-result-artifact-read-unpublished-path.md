<!--
name: Artifact Read Unpublished Path
description: >-
  Artifact-read tool result when a requested file is not published on the served
  version.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_READ_UNPUBLISHED_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_UNPUBLISHED_PATH_VAR_1
  - TOOL_RESULT_ARTIFACT_READ_UNPUBLISHED_PATH_VAR_2
  - TOOL_RESULT_ARTIFACT_READ_UNPUBLISHED_PATH_VAR_3
-->
Artifact ${TOOL_RESULT_ARTIFACT_READ_UNPUBLISHED_PATH_VAR_0.slug}: no file is published at ${TOOL_RESULT_ARTIFACT_READ_UNPUBLISHED_PATH_VAR_1} in the served version (a single-page artifact has only its page).${TOOL_RESULT_ARTIFACT_READ_UNPUBLISHED_PATH_VAR_2?` The ${TOOL_RESULT_ARTIFACT_READ_UNPUBLISHED_PATH_VAR_3} tool's list_files action, with this artifact's URL, shows the published paths.`:""}
