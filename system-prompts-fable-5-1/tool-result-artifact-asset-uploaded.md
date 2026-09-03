<!--
name: 'Tool result: Artifact asset uploaded'
description: >-
  Confirms an asset upload with its name, size, type and hash, and tells the
  model that every artifact viewer can load it and that it persists until
  delete_asset
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_2
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_3
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_4
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_5
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_6
-->
Asset uploaded: ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_0(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.file_name,128)} (${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_2(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.size_bytes)} bytes, ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_3(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.content_type,TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_4,"unrecognized content type")}${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_5}) ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_6} Everyone who can open the artifact can load this file; the upload is durable until deleted with action "delete_asset".
