<!--
name: 'Tool Result: PR-review republish provenance page unreachable'
description: >-
  Artifact tool error returned to the model when the published page simply could
  not be reached for the provenance check, so a retry is worthwhile.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_UNREACHABLE_VAR_0
-->
could not read the published page to verify decision provenance: ${TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_UNREACHABLE_VAR_0.err}. Retry when the page is reachable — every republish verifies decision provenance against the published page.
