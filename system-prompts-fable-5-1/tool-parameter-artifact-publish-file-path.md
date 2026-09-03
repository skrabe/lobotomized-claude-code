<!--
name: 'Tool Parameter: Artifact Publish File Path'
description: >-
  Artifact tool file_path parameter for the local page (or type data file /
  asset) to publish.
ccVersion: 2.1.257
variables:
  - TOOL_PARAMETER_ARTIFACT_PUBLISH_FILE_PATH_VAR_0
-->
publish: the local page to publish (.html; .md only when a skill says so)${TOOL_PARAMETER_ARTIFACT_PUBLISH_FILE_PATH_VAR_0.typesOn?" — or, for an Artifact created from an Artifact type, one of its data files":""}${TOOL_PARAMETER_ARTIFACT_PUBLISH_FILE_PATH_VAR_0.assetsOn?"; with `asset: true`, the local file to upload":""}. A short, distinctive basename doubles as the last-resort title.
