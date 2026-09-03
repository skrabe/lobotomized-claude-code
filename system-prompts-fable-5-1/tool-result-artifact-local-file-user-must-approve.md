<!--
name: 'Tool Result: Artifact Local File User Must Approve'
description: >-
  Permission-ask suffix for a single local file whose path or link requires a
  human approval.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_LOCAL_FILE_USER_MUST_APPROVE_VAR_0
  - TOOL_RESULT_ARTIFACT_LOCAL_FILE_USER_MUST_APPROVE_VAR_1
  - TOOL_RESULT_ARTIFACT_LOCAL_FILE_USER_MUST_APPROVE_VAR_2
-->
 The local file "${TOOL_RESULT_ARTIFACT_LOCAL_FILE_USER_MUST_APPROVE_VAR_0(TOOL_RESULT_ARTIFACT_LOCAL_FILE_USER_MUST_APPROVE_VAR_1.askPath,256)}" ${TOOL_RESULT_ARTIFACT_LOCAL_FILE_USER_MUST_APPROVE_VAR_2.join(" and ")}, so only you can approve this.
