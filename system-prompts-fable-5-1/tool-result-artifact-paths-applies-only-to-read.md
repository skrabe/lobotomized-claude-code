<!--
name: Artifact Paths Applies Only To Read
description: >-
  validateInput rejection when paths is passed on a non-read action; supporting
  files belong in files.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_PATHS_APPLIES_ONLY_TO_READ_VAR_0
-->
\`paths\` applies only to ${TOOL_RESULT_ARTIFACT_PATHS_APPLIES_ONLY_TO_READ_VAR_0('action "read_file"',()=>'action "read"')} — to publish supporting files, list them in \`files\`
