<!--
name: Artifact Publish Review Check Transient Read Denied
description: >-
  Refuses publishing when a transient content scan prevents checking whether the
  target is a review page.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_TRANSIENT_READ_DENIED_VAR_0
-->
publish refused: could not verify the target page is not a review page (read denied: ${TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_TRANSIENT_READ_DENIED_VAR_0}). Read the page (action: "read") to check its state, or publish a fresh artifact (omit \`url\` and use a new \`file_path\`).
