<!--
name: 'Tool Result: Artifact PR-Review Template Mismatch'
description: >-
  Artifact publish-time validation failure telling the model its
  artifact-pr-review page violated the template contract and how to fix it;
  delivered to the model inside a <tool_use_error> tool_result.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_TEMPLATE_MISMATCH_VAR_0
-->
This page carries the artifact-pr-review machinery but failed publish-time validation: ${TOOL_RESULT_ARTIFACT_PR_REVIEW_TEMPLATE_MISMATCH_VAR_0.reason}. Carry the template blocks byte-for-byte and keep the rest of the page within the skill's contract — no script fragments or event handlers, no elements or attributes that fetch or navigate, no CSS network functions, and no src/href other than the PR's canonical GitHub URL — then retry.
