<!--
name: 'Tool Result: Artifact DB Write Cowork User Approval Required'
description: >-
  safetyCheck decisionReason that Cowork-session artifact database writes are
  durable shared-state changes requiring the user, not the auto-permission
  classifier.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_COWORK_USER_APPROVAL_REQUIRED_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_WRITE_COWORK_USER_APPROVAL_REQUIRED_VAR_1
-->
Artifact database writes from a Cowork session are durable shared-state changes${TOOL_RESULT_ARTIFACT_DB_WRITE_COWORK_USER_APPROVAL_REQUIRED_VAR_0} — approval must come from the user, not the auto-permission classifier${TOOL_RESULT_ARTIFACT_DB_WRITE_COWORK_USER_APPROVAL_REQUIRED_VAR_1}
