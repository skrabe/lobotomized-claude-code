<!--
name: Artifact Read-File Protected Paths Deny
description: >-
  checkPermissions deny from ap() when every path in a batched read_file would
  be saved at a protected dest, telling the model nothing was read and to retry
  with path.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_READ_FILE_PROTECTED_PATHS_DENY_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_FILE_PROTECTED_PATHS_DENY_VAR_1
-->
every path in this read (${TOOL_RESULT_ARTIFACT_READ_FILE_PROTECTED_PATHS_DENY_VAR_0.join(", ")}${TOOL_RESULT_ARTIFACT_READ_FILE_PROTECTED_PATHS_DENY_VAR_1.length>TOOL_RESULT_ARTIFACT_READ_FILE_PROTECTED_PATHS_DENY_VAR_0.length?", …":""}) would be saved at a path Claude Code protects (git, hook, tool, and agent settings, shell profiles and other sensitive files), under a suspicious spelling, or through a link leading out of the scratchpad — nothing was read; read them one at a time with \`path\`
