<!--
name: 'Tool Result: PR-review republish provenance read HTTP failure'
description: >-
  Artifact tool error returned to the model when the provenance read fails with
  a non-transient HTTP status, so retrying cannot help.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_HTTP_FAILURE_VAR_0
-->
could not read the published page to verify decision provenance (read denied: ${TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_HTTP_FAILURE_VAR_0.err}). An HTTP ${TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_HTTP_FAILURE_VAR_0.status} failure is not transient, so retrying cannot succeed — every republish verifies decision provenance against the published page.
