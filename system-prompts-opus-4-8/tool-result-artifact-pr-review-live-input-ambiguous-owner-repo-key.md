<!--
name: PR Review Live Input Ambiguous Owner/Repo Key
description: >-
  Nlp() validation failure naming a live.input key that matches both the owner
  and repository key families, which the stamped path refuses rather than
  guessing.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_LIVE_INPUT_AMBIGUOUS_OWNER_REPO_KEY_VAR_0
-->

live.input.${TOOL_RESULT_ARTIFACT_PR_REVIEW_LIVE_INPUT_AMBIGUOUS_OWNER_REPO_KEY_VAR_0} names both the owner and repository key families — with a stamp, refuse ambiguity rather than guess which family pins it
