<!--
name: 'Tool Result: Artifact root symlink chain unresolvable'
description: >-
  Validation error for the Artifact publish `root` base directory, returned to
  the model when root is a symlink whose chain can't be safely resolved (network
  target, '..' in link text, or too many links).
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_ROOT_SYMLINK_UNRESOLVABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOT_SYMLINK_UNRESOLVABLE_VAR_1
-->
root: ${TOOL_RESULT_ARTIFACT_ROOT_SYMLINK_UNRESOLVABLE_VAR_0.stringify(TOOL_RESULT_ARTIFACT_ROOT_SYMLINK_UNRESOLVABLE_VAR_1)} is a symlink whose chain cannot be safely resolved (network target, a \`..\` segment in link text, or too many links) — pass the target directory itself
