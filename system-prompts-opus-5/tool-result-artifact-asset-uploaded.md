<!--
name: 'Tool result: Artifact asset uploaded'
description: >-
  Confirms an asset upload and tells the model how to reference the stored file
  from the page and database
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1
-->
Asset uploaded: ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_0(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.file_name)} (${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.size_bytes} bytes, ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_0(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.content_type)}${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.sha256!==void 0?`, sha256 ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.sha256}`:""}) is now stored in the artifact as ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_0(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.url)} (id ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_0(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.id)}). Reference it from the page by that relative url — e.g. <img src=${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_0(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_VAR_1.url)}> — which resolves in every view of the artifact; store the id in the artifact's database if rows need to point at it. Everyone who can open the artifact can load this file; the upload is durable until deleted with action "delete_asset".
