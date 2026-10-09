<!--
name: Artifact Delete Permission Ask
description: >-
  Approval question for permanently deleting an Artifact; asked of the user and,
  when no one can answer, returned to the model inside the deny that lists the
  unanswered questions.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_ARTIFACT_DELETE_PERMISSION_ASK_VAR_0
  - TOOL_RESULT_ARTIFACT_DELETE_PERMISSION_ASK_VAR_1
  - TOOL_RESULT_ARTIFACT_DELETE_PERMISSION_ASK_VAR_2
-->
Permanently delete ${TOOL_RESULT_ARTIFACT_DELETE_PERMISSION_ASK_VAR_0||TOOL_RESULT_ARTIFACT_DELETE_PERMISSION_ASK_VAR_1===void 0?TOOL_RESULT_ARTIFACT_DELETE_PERMISSION_ASK_VAR_2:TOOL_RESULT_ARTIFACT_DELETE_PERMISSION_ASK_VAR_1}?
