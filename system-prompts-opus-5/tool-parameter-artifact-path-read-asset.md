<!--
name: 'Tool Parameter: Artifact Path Read Asset'
description: >-
  path schema description for reading (and optionally deleting) an uploaded
  asset by 32-hex id.
ccVersion: 2.1.267
variables:
  - TOOL_PARAMETER_ARTIFACT_PATH_READ_ASSET_VAR_0
-->
${TOOL_PARAMETER_ARTIFACT_PATH_READ_ASSET_VAR_0.multiFileOn?"Or an":"read: an"} uploaded asset's id (32 hex characters, from an 'assets' listing or an upload result) — that asset is saved to a local file; delete: the id of the one asset to remove.
