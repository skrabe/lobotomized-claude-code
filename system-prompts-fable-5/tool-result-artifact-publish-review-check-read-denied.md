<!--
name: 'Tool Result: Artifact publish review-page check read denied'
description: >-
  Error returned to the model when an Artifact publish cannot read the target
  page to prove it is not a certified review page and the HTTP status is
  non-transient.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_READ_DENIED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_READ_DENIED_VAR_1
-->
publish refused: could not verify the target page is not a review page (read denied: ${TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_READ_DENIED_VAR_0}). An HTTP ${TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_READ_DENIED_VAR_1.status} failure is not transient, so retrying this publish cannot succeed — read the page (action: "read") to check its state, or publish a fresh artifact (omit \`url\` and use a new \`file_path\`).
