<!--
name: Artifact read approval-scope clause
description: >-
  Clause (Kr) appended to the read/list consent ask stating that approving
  covers reads of this artifact's published files and assets for the rest of the
  conversation.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_1
-->
; approving covers reads of this artifact's ${TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_0?"published files":"assets"}${TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_1}${TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_2()?" (and server-side copies of them into other artifacts)":""} for the rest of the conversation
