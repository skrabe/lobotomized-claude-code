<!--
name: 'Tool Result: Artifact PR Review Republish Provenance HTTP Failure'
description: >-
  Tool-result error when republish provenance verification fails on a
  non-transient HTTP status.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_HTTP_FAILURE_VAR_0
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_HTTP_FAILURE_VAR_1
-->
could not read the published page to verify decision provenance (read denied: ${TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_HTTP_FAILURE_VAR_0}). An HTTP ${TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_HTTP_FAILURE_VAR_1.status} failure is not transient, so retrying cannot succeed — every republish verifies decision provenance against the published page.
