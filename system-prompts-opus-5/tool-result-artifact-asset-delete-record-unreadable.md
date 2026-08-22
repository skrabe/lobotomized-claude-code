<!--
name: Artifact Asset Delete Record Unreadable
description: >-
  asset_delete tool result when the deletion record cannot be read, so whether
  the asset was deleted is unknown.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_DELETE_RECORD_UNREADABLE_VAR_0
-->
This record of an asset deletion is unreadable — whether ${TOOL_RESULT_ARTIFACT_ASSET_DELETE_RECORD_UNREADABLE_VAR_0===""?"the asset":`_blob/${TOOL_RESULT_ARTIFACT_ASSET_DELETE_RECORD_UNREADABLE_VAR_0}`} was deleted is unknown; action "list_assets" shows what the artifact still holds.
