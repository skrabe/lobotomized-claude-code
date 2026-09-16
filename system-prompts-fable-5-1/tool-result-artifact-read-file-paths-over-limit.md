<!--
name: 'Tool Result: Artifact read_file Paths Over Limit'
description: read_file denial when paths names more files than one call may read.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_READ_FILE_PATHS_OVER_LIMIT_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_FILE_PATHS_OVER_LIMIT_VAR_1
-->
\`paths\` names ${TOOL_RESULT_ARTIFACT_READ_FILE_PATHS_OVER_LIMIT_VAR_0.length} paths; at most ${TOOL_RESULT_ARTIFACT_READ_FILE_PATHS_OVER_LIMIT_VAR_1} can be read in one call
