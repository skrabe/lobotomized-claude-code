<!--
name: Artifact read approval-scope clause
description: >-
  Clause appended to the read/list consent ask stating that approving covers
  reads of this artifact's published files or assets for the rest of the
  conversation, with an optional server-side-copies interpolation.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_1
  - TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_2
-->
; approving covers reads of this artifact's ${TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_0?"published files":"assets"}${TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_1}${TOOL_RESULT_ARTIFACT_READ_APPROVAL_SCOPE_CLAUSE_VAR_2()?" (and server-side copies of them into other artifacts)":""} for the rest of the conversation
