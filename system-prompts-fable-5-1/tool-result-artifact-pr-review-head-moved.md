<!--
name: 'Tool Result: Artifact PR-Review Head Moved'
description: >-
  First fragment of the pr_review identity-mismatch reason, thrown as an
  ArtifactInputError and returned to the model as the Artifact tool's error
  result when the reviewed PR head SHA no longer matches.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_HEAD_MOVED_VAR_0
-->
the PR moved since the review: the payload reviewed ${TOOL_RESULT_ARTIFACT_PR_REVIEW_HEAD_MOVED_VAR_0.reviewed_head_sha.slice(0,12)}… but 
