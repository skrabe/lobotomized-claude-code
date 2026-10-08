<!--
name: Artifact Publish Review Check HTTP 403 Retry Once
description: Limits retries when an HTTP 403 prevents checking the target's review state.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_403_RETRY_ONCE_VAR_0
-->
publish refused: could not verify the target page is not a review page (read denied: ${TOOL_RESULT_ARTIFACT_PUBLISH_REVIEW_CHECK_403_RETRY_ONCE_VAR_0}). This is usually a permanent policy deny — retry at most once (a concurrent republish can cause a one-off stale-version 403); if it repeats, read the page (action: "read") to check its state, or publish a fresh artifact (omit \`url\` and use a new \`file_path\`).
