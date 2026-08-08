<!--
name: 'Tool Result: PR-review republish provenance read policy deny'
description: >-
  Artifact tool error returned to the model when the provenance read is denied
  with 403, advising at most one retry for the concurrent-republish race.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_POLICY_DENY_VAR_0
-->
could not read the published page to verify decision provenance (read denied: ${TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_POLICY_DENY_VAR_0.err}). This is usually a permanent policy deny — retry at most once (a concurrent republish can cause a one-off stale-version 403); every republish verifies decision provenance against the published page.
