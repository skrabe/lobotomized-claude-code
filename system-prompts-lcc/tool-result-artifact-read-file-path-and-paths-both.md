<!--
name: Artifact Read File Path And Paths Both
description: validateInput rejection when read_file is passed both path and paths.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_READ_FILE_PATH_AND_PATHS_BOTH_VAR_0
-->
action "${TOOL_RESULT_ARTIFACT_READ_FILE_PATH_AND_PATHS_BOTH_VAR_0("read_file",()=>"read")}" takes \`path\` (one file) or \`paths\` (several), not both — remove one.
