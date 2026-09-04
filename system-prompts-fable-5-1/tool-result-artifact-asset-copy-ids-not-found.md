<!--
name: Artifact Asset Copy Ids Not Found
description: >-
  Artifact copy_from error when the source holds no asset with one of the given
  ids; nothing was copied.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_COPY_IDS_NOT_FOUND_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_COPY_IDS_NOT_FOUND_VAR_1
-->
${TOOL_RESULT_ARTIFACT_ASSET_COPY_IDS_NOT_FOUND_VAR_0}: ${TOOL_RESULT_ARTIFACT_ASSET_COPY_IDS_NOT_FOUND_VAR_1??"the source Artifact holds no asset with one of the given ids"} — run action "list_assets" on from_url for its current ids; nothing was copied
