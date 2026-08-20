<!--
name: 'Tool Result: Artifact DB Write Plan-Mode User Approval Required'
description: >-
  safetyCheck decisionReason for the first artifact database write in plan mode:
  a durable shared-state change the auto-permission classifier must not approve.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_PLAN_MODE_USER_APPROVAL_REQUIRED_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_WRITE_PLAN_MODE_USER_APPROVAL_REQUIRED_VAR_1
-->
First artifact database write in plan mode is a durable shared-state change${TOOL_RESULT_ARTIFACT_DB_WRITE_PLAN_MODE_USER_APPROVAL_REQUIRED_VAR_0} — approval must come from the user, not the auto-permission classifier${TOOL_RESULT_ARTIFACT_DB_WRITE_PLAN_MODE_USER_APPROVAL_REQUIRED_VAR_1}
