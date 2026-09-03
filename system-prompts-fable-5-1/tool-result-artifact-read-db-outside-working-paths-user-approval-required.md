<!--
name: 'Tool Result: Artifact read_db Outside Working Paths Requires User Approval'
description: >-
  safetyCheck decisionReason when read_db would write database documents outside
  the allowed working paths, so the auto-permission classifier must not approve
  it.
ccVersion: 2.1.237
variables:
  - >-
    TOOL_RESULT_ARTIFACT_READ_DB_OUTSIDE_WORKING_PATHS_USER_APPROVAL_REQUIRED_VAR_0
-->
Saving artifact database documents as ${TOOL_RESULT_ARTIFACT_READ_DB_OUTSIDE_WORKING_PATHS_USER_APPROVAL_REQUIRED_VAR_0} writes web content outside the allowed working paths — approval must come from the user, not the auto-permission classifier
