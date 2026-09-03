<!--
name: 'Tool Result: Artifact PR Review Republish Provenance Egress Blocked'
description: >-
  Tool-result error when republish cannot verify decision provenance because the
  environment network allowlist blocked the published-page read.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_EGRESS_BLOCKED_VAR_0
-->
could not read the published page to verify decision provenance (${TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_EGRESS_BLOCKED_VAR_0}). This environment's network allowlist blocks the read, so republish cannot proceed from here — every republish verifies decision provenance against the published page.
