<!--
name: Artifact Publish Review Check Proxy Read Denied
description: >-
  Refuses publishing when a proxy denial blocks checking the target's review
  state.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_PROXY_READ_DENIED_VAR_0
-->
publish refused: could not verify the target page is not a review page (read denied: ${TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_PROXY_READ_DENIED_VAR_0}). Publish a fresh artifact instead (omit \`url\` and use a new \`file_path\`).
