<!--
name: Artifact Read-File Set-Aside Reason
description: >-
  Per-file set-aside tool_result from av() explaining why a batched read_file
  dest was skipped and telling the model to read it with path.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_1
  - TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_2
  - TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_3
  - TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_4
  - TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_5
  - TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_6
-->
set aside: ${TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_0(TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_1)&&!TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_2([TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_3])?TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_4(TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_1)?"a link where it would be saved leads out of the scratchpad":"its name is one the file-edit safety rules screen even in the scratchpad (git, hook, tool, and agent settings)":TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_5().decisionReason?.TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_6==="safetyCheck"?"it would be saved at a path Claude Code protects (settings, hooks, .git, shell profiles and other sensitive files) or under a suspicious spelling":TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_5().decisionReason?.TOOL_RESULT_ARTIFACT_READ_FILE_SET_ASIDE_VAR_6==="rule"?"an Edit ask rule of the user’s asks before this file is written":"the approval set it aside"} — read it by itself with \`path\`
