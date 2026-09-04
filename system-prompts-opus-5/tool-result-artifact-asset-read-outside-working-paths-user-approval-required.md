<!--
name: Artifact file/asset save outside working paths requires user approval
description: >-
  safetyCheck decisionReason when saving an artifact file or asset writes web
  content outside the allowed working paths.
ccVersion: 2.1.261
variables:
  - >-
    TOOL_RESULT_ARTIFACT_ASSET_READ_OUTSIDE_WORKING_PATHS_USER_APPROVAL_REQUIRED_VAR_0
  - >-
    TOOL_RESULT_ARTIFACT_ASSET_READ_OUTSIDE_WORKING_PATHS_USER_APPROVAL_REQUIRED_VAR_1
-->
Saving an artifact ${TOOL_RESULT_ARTIFACT_ASSET_READ_OUTSIDE_WORKING_PATHS_USER_APPROVAL_REQUIRED_VAR_0?"file":"asset"} as ${TOOL_RESULT_ARTIFACT_ASSET_READ_OUTSIDE_WORKING_PATHS_USER_APPROVAL_REQUIRED_VAR_1} writes web content outside the allowed working paths — approval must come from the user, not the auto-permission classifier${TOOL_RESULT_ARTIFACT_ASSET_READ_OUTSIDE_WORKING_PATHS_USER_APPROVAL_REQUIRED_VAR_2}
