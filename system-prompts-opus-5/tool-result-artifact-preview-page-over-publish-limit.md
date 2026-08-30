<!--
name: 'Artifact Preview: Over Publish Size Limit'
description: >-
  Static preview size issue when the composed page exceeds the publish megabyte
  cap including inlined runtimes.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_PREVIEW_PAGE_OVER_PUBLISH_LIMIT_VAR_0
  - TOOL_RESULT_ARTIFACT_PREVIEW_PAGE_OVER_PUBLISH_LIMIT_VAR_1
  - TOOL_RESULT_ARTIFACT_PREVIEW_PAGE_OVER_PUBLISH_LIMIT_VAR_2
-->
page is ${TOOL_RESULT_ARTIFACT_PREVIEW_PAGE_OVER_PUBLISH_LIMIT_VAR_0(TOOL_RESULT_ARTIFACT_PREVIEW_PAGE_OVER_PUBLISH_LIMIT_VAR_1)} as published, over the ${TOOL_RESULT_ARTIFACT_PREVIEW_PAGE_OVER_PUBLISH_LIMIT_VAR_2/1024/1024} MB publish limit (the inline highlighting runtime included)
