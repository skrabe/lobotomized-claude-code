<!--
name: Artifact Permission Ask Unanswered Deny
description: >-
  checkPermissions deny message when an artifact ask has no one in the session
  who can answer it; the model reads it as the tool_result.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_ARTIFACT_PERMISSION_ASK_UNANSWERED_DENY_VAR_0
  - TOOL_RESULT_ARTIFACT_PERMISSION_ASK_UNANSWERED_DENY_VAR_1
-->
Nothing was done. This needs a yes to: ${TOOL_RESULT_ARTIFACT_PERMISSION_ASK_UNANSWERED_DENY_VAR_0.map((TOOL_RESULT_ARTIFACT_PERMISSION_ASK_UNANSWERED_DENY_VAR_1)=>TOOL_RESULT_ARTIFACT_PERMISSION_ASK_UNANSWERED_DENY_VAR_1.question).join(" ")} No one can answer in this session.
