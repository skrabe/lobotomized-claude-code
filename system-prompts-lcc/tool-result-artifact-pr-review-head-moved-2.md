<!--
name: 'Tool Result: Artifact PR-Review Head Moved (Remediation)'
description: >-
  Second concatenated fragment of the pr_review head-moved error, telling the
  model to re-gather the PR and re-author the payload against the current head;
  delivered in the Artifact tool_result.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_HEAD_MOVED_2_VAR_0
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_HEAD_MOVED_2_VAR_1
-->
${TOOL_RESULT_ARTIFACT_PR_REVIEW_HEAD_MOVED_2_VAR_0.owner}/${TOOL_RESULT_ARTIFACT_PR_REVIEW_HEAD_MOVED_2_VAR_0.repo}#${TOOL_RESULT_ARTIFACT_PR_REVIEW_HEAD_MOVED_2_VAR_0.number} is now at ${TOOL_RESULT_ARTIFACT_PR_REVIEW_HEAD_MOVED_2_VAR_1.headSha.slice(0,12)}… — re-gather the PR (step 1) and re-author the payload against the current head
