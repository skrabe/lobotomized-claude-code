<!--
name: 'Tool Result: Artifact PR-Review Payload Invalid'
description: >-
  Error returned by the Artifact tool when a composed pr_review payload fails
  schema validation on publish.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_PAYLOAD_INVALID_VAR_0
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_PAYLOAD_INVALID_VAR_1
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_PAYLOAD_INVALID_VAR_2
-->

the pr_review payload failed validation: ${TOOL_RESULT_ARTIFACT_PR_REVIEW_PAYLOAD_INVALID_VAR_0 instanceof TOOL_RESULT_ARTIFACT_PR_REVIEW_PAYLOAD_INVALID_VAR_1?TOOL_RESULT_ARTIFACT_PR_REVIEW_PAYLOAD_INVALID_VAR_0.message:TOOL_RESULT_ARTIFACT_PR_REVIEW_PAYLOAD_INVALID_VAR_2(TOOL_RESULT_ARTIFACT_PR_REVIEW_PAYLOAD_INVALID_VAR_0)}. Fix the payload JSON and retry.
