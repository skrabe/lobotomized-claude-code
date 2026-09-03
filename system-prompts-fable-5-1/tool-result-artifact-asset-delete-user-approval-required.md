<!--
name: Asset delete approval reason
description: >-
  safetyCheck decisionReason on the delete_asset ask stating approval must come
  from the user, not the auto-permission classifier.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_DELETE_USER_APPROVAL_REQUIRED_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_DELETE_USER_APPROVAL_REQUIRED_VAR_1
-->
Claude wants to ${TOOL_RESULT_ARTIFACT_ASSET_DELETE_USER_APPROVAL_REQUIRED_VAR_0} — approval must come from the user, not the auto-permission classifier${TOOL_RESULT_ARTIFACT_ASSET_DELETE_USER_APPROVAL_REQUIRED_VAR_1===""?"":`.${TOOL_RESULT_ARTIFACT_ASSET_DELETE_USER_APPROVAL_REQUIRED_VAR_1}`}
