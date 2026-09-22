<!--
name: Artifact Upload Asset Not Stored Header
description: >-
  Header above failed upload_asset lines telling the model not to reference
  those files.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_NOT_STORED_HEADER_VAR_0
-->

Not stored, or not known to be (each line says why; do not reference these):
${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_NOT_STORED_HEADER_VAR_0.join(`
`)}
