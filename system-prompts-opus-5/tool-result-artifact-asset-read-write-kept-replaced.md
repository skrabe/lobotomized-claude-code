<!--
name: 'Tool Result: Asset read — replaced copy removed, staged bytes kept'
description: >-
  read_asset error when the earlier copy at the destination was removed but the
  fetched asset could not be moved into its place; the bytes remain at the
  .partial path for the user to move or delete.
ccVersion: 2.1.235
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_REPLACED_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_REPLACED_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_REPLACED_VAR_2
  - TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_REPLACED_VAR_3
-->
the earlier copy at ${TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_REPLACED_VAR_0.basename(TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_REPLACED_VAR_1)} was removed but the fetched asset could not be moved into its place (${TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_REPLACED_VAR_2}) — the bytes are kept at ${TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_REPLACED_VAR_3.partial}; move or delete that file
