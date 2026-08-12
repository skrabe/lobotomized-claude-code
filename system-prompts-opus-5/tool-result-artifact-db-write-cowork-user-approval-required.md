<!--
name: 'Tool Result: Artifact DB Write Requires User Approval'
description: >-
  Provides the Cowork safety reason used when an artifact database write must be
  approved directly by the user.
ccVersion: 2.1.228
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_COWORK_USER_APPROVAL_REQUIRED_VAR_0
-->
Artifact database writes from a Cowork session are durable shared-state changes — approval must come from the user, not the auto-permission classifier${TOOL_RESULT_ARTIFACT_DB_WRITE_COWORK_USER_APPROVAL_REQUIRED_VAR_0}
