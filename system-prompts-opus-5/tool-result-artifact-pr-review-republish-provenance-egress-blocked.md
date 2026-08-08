<!--
name: 'Tool Result: PR-review republish provenance read egress-blocked'
description: >-
  Artifact tool error returned to the model when a PR-review republish cannot
  verify decision provenance because the environment's network allowlist blocks
  reading the published page.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_EGRESS_BLOCKED_VAR_0
-->
could not read the published page to verify decision provenance (${TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_EGRESS_BLOCKED_VAR_0.err}). This environment's network allowlist blocks the read, so republish cannot proceed from here — every republish verifies decision provenance against the published page.
