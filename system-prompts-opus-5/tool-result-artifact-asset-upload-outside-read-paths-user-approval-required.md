<!--
name: Asset upload outside-read-paths approval reason
description: >-
  safetyCheck decisionReason when the uploaded file lies outside the session's
  allowed read paths.
ccVersion: 2.1.234
variables:
  - >-
    TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_OUTSIDE_READ_PATHS_USER_APPROVAL_REQUIRED_VAR_0
  - >-
    TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_OUTSIDE_READ_PATHS_USER_APPROVAL_REQUIRED_VAR_1
-->
Uploading ${TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_OUTSIDE_READ_PATHS_USER_APPROVAL_REQUIRED_VAR_0} sends a file from outside the allowed read paths to a web-reachable page — approval must come from the user, not the auto-permission classifier${TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_OUTSIDE_READ_PATHS_USER_APPROVAL_REQUIRED_VAR_1}
