<!--
name: 'Tool Result: Artifact PR Review Republish Provenance Policy Deny'
description: >-
  Tool-result error when republish provenance verification is denied by policy,
  usually a permanent 403.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_POLICY_DENY_VAR_0
-->
could not read the published page to verify decision provenance (read denied: ${TOOL_RESULT_ARTIFACT_PR_REVIEW_REPUBLISH_PROVENANCE_POLICY_DENY_VAR_0}). This is usually a permanent policy deny — retry at most once (a concurrent republish can cause a one-off stale-version 403); every republish verifies decision provenance against the published page.
