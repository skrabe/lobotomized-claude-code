<!--
name: 'Tool result: Artifact file symlink cannot be safely resolved'
description: >-
  Error returned to the model when a `files` source is a symlink whose chain
  cannot be safely resolved (network target, `..` in link text, or too many
  links).
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_FILES_UNSAFE_SYMLINK_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_UNSAFE_SYMLINK_VAR_1
-->
files: ${TOOL_RESULT_ARTIFACT_FILES_UNSAFE_SYMLINK_VAR_0.stringify(TOOL_RESULT_ARTIFACT_FILES_UNSAFE_SYMLINK_VAR_1)} is a symlink whose chain cannot be safely resolved (network target, a \`..\` segment in link text, or too many links) — list the link's target path instead
