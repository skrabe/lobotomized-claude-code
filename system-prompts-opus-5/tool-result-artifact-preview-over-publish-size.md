<!--
name: 'Artifact Preview: Over Publish Size Limit'
description: >-
  Static preview size issue when the composed page exceeds the publish megabyte
  cap including inlined runtimes.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_PREVIEW_OVER_PUBLISH_SIZE_VAR_0
  - TOOL_RESULT_ARTIFACT_PREVIEW_OVER_PUBLISH_SIZE_VAR_1
  - TOOL_RESULT_ARTIFACT_PREVIEW_OVER_PUBLISH_SIZE_VAR_2
-->
page is ${TOOL_RESULT_ARTIFACT_PREVIEW_OVER_PUBLISH_SIZE_VAR_0(TOOL_RESULT_ARTIFACT_PREVIEW_OVER_PUBLISH_SIZE_VAR_1)} as published, over the ${TOOL_RESULT_ARTIFACT_PREVIEW_OVER_PUBLISH_SIZE_VAR_2/1024/1024} MB publish limit (inline diagram and highlighting runtimes included)
