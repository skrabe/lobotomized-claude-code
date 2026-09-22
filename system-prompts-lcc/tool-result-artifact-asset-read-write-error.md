<!--
name: Artifact asset read — save failed
description: >-
  Artifact asset_read error reporting that the asset was fetched but could not
  be written to disk, with the underlying errno.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_ERROR_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_ERROR_VAR_1
-->
the asset was fetched but could not be saved (${TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_ERROR_VAR_0(TOOL_RESULT_ARTIFACT_ASSET_READ_WRITE_ERROR_VAR_1)??"unexpected error"})
