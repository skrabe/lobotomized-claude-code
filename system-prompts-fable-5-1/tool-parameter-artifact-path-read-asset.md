<!--
name: 'Tool Parameter: Artifact Path Read Asset'
description: >-
  path schema description for reading (and deleting) an uploaded asset by 32-hex
  id.
ccVersion: 2.1.269
variables:
  - TOOL_PARAMETER_ARTIFACT_PATH_READ_ASSET_VAR_0
-->
${TOOL_PARAMETER_ARTIFACT_PATH_READ_ASSET_VAR_0.multiFileOn?"It can instead be an":"read: an"} uploaded asset's id (32 hex characters, from an 'assets' listing or an upload result), and that asset is saved to a local file. delete: the id of the one asset to remove.
