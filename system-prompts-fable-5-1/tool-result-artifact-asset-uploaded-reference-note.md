<!--
name: 'Artifact asset uploaded: how to reference it'
description: >-
  Fragment of the asset-upload tool result telling the model the stored relative
  url and how to reference the asset from the page.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_2
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_3
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_4
-->
is now stored in the artifact as ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_0(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_1)} (id ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_2(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_3.id,TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_4,"unreadable")}). Reference it from the page by that url verbatim — e.g. <img src=${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_0(TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_REFERENCE_NOTE_VAR_1)}> — which resolves in every view of the artifact; store the id in the artifact's database if rows need to point at it.
