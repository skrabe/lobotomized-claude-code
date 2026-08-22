<!--
name: Artifact asset delete - nothing deleted
description: >-
  asset_delete tool result for an id that matched no asset in the artifact's
  store.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_DELETE_NOT_FOUND_VAR_0
-->
Nothing deleted: the artifact's asset store has no asset with ${TOOL_RESULT_ARTIFACT_ASSET_DELETE_NOT_FOUND_VAR_0===""?"that id":`id ${TOOL_RESULT_ARTIFACT_ASSET_DELETE_NOT_FOUND_VAR_0}`} (already deleted, or never there).
