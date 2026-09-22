<!--
name: Artifact asset deleted
description: >-
  Tool result confirming an asset was deleted and warning that references to it
  will now fail to load.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_DELETED_VAR_0
-->
Asset deleted: ${TOOL_RESULT_ARTIFACT_ASSET_DELETED_VAR_0===""?"it":`_blob/${TOOL_RESULT_ARTIFACT_ASSET_DELETED_VAR_0}`} is gone from the artifact's asset store.
