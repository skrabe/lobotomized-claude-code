<!--
name: 'Tool Result: Artifact publish review-page check transient failure'
description: >-
  Error returned to the model when the Artifact publish review-page precheck
  fails transiently and the publish should be retried.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_TRANSIENT_VAR_0
-->
publish refused: could not verify the target page is not a review page (transient read failure: ${TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_TRANSIENT_VAR_0}). Retry the publish; if it persists, read the page (action: "read") to confirm it is reachable.
