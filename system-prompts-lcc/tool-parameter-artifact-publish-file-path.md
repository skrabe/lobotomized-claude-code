<!--
name: 'Tool Parameter: Artifact Publish File Path'
description: >-
  Artifact tool file_path parameter for the local page (or type data file /
  asset) to publish.
ccVersion: 2.1.269
variables:
  - TOOL_PARAMETER_ARTIFACT_PUBLISH_FILE_PATH_VAR_0
-->
publish: the local page Claude publishes (.html, or .md only when a skill says so).${TOOL_PARAMETER_ARTIFACT_PUBLISH_FILE_PATH_VAR_0.typesOn?" For an Artifact created from an Artifact type, it is one of that Artifact's data files.":""}${TOOL_PARAMETER_ARTIFACT_PUBLISH_FILE_PATH_VAR_0.assetsOn?" With `asset: true`, it is the local file Claude uploads.":""} A short, distinctive basename also serves as the title when nothing else gives one.
