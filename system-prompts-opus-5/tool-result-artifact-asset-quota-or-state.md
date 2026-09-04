<!--
name: Asset call failed — quota or state
description: >-
  Artifact asset error arm for a quota_or_state code, selecting the upload or
  non-upload explanation of why the Artifact has no usable asset store.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_QUOTA_OR_STATE_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_QUOTA_OR_STATE_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSET_QUOTA_OR_STATE_VAR_2
-->
${TOOL_RESULT_ARTIFACT_ASSET_QUOTA_OR_STATE_VAR_0}: ${TOOL_RESULT_ARTIFACT_ASSET_QUOTA_OR_STATE_VAR_1??(TOOL_RESULT_ARTIFACT_ASSET_QUOTA_OR_STATE_VAR_2==="upload"||TOOL_RESULT_ARTIFACT_ASSET_QUOTA_OR_STATE_VAR_2==="copy"?"the Artifact cannot take uploads right now — it is a live document, unpublished, retired, being deleted, or over its asset storage quota":"the Artifact has no asset store right now — it is a live document, unpublished, retired, or being deleted")}
