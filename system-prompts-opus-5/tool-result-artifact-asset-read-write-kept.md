<!--
name: 'Tool Result: Asset read — staged bytes kept after failed move'
description: >-
  read_asset error when the fetched asset could not be moved to its destination;
  the bytes remain at the .partial path for the user to move or delete.
ccVersion: 2.1.235
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_VAR_1
  - TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_VAR_2
  - TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_VAR_3
-->
the fetched asset could not be moved to ${TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_VAR_0.basename(TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_VAR_1)} (${TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_VAR_2}) — the bytes are kept at ${TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_KEPT_VAR_3.partial}; move or delete that file
