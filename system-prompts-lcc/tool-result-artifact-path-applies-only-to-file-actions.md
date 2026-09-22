<!--
name: Artifact Path Applies Only To File Actions
description: >-
  validateInput rejection when path is passed on a publish instead of listing
  supporting files in files.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_PATH_APPLIES_ONLY_TO_FILE_ACTIONS_VAR_0
-->
\`path\` applies only to ${TOOL_RESULT_ARTIFACT_PATH_APPLIES_ONLY_TO_FILE_ACTIONS_VAR_0()?'actions "read_file", "watch" and "sync"':'action "read_file"'} — to publish supporting files, list them in \`files\`
