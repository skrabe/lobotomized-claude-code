<!--
name: Asset upload default decision reason
description: >-
  Fallback type:"other" decisionReason for an asset upload, stating the file
  becomes loadable by every artifact viewer.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_LOADABLE_BY_VIEWERS_REASON_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_LOADABLE_BY_VIEWERS_REASON_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_LOADABLE_BY_VIEWERS_REASON_VAR_2
-->
Uploading ${TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_LOADABLE_BY_VIEWERS_REASON_VAR_0} makes it loadable by everyone who can open the artifact${TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_LOADABLE_BY_VIEWERS_REASON_VAR_1?"; approval covers further uploads to this artifact for the rest of the session":""}${TOOL_RESULT_ARTIFACT_ASSET_UPLOAD_LOADABLE_BY_VIEWERS_REASON_VAR_2}
