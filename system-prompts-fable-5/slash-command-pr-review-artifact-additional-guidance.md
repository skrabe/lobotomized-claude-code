<!--
name: 'PR Review Artifact Command: Additional User Guidance Section'
description: >-
  Appended to the PR-review-artifact skill prompt when the user supplies
  free-form text after the PR number, framing it as extra guidance; returned as
  [{type:"text",text:n}] into the model's context.
ccVersion: 2.1.221
variables:
  - SLASH_COMMAND_PR_REVIEW_ARTIFACT_ADDITIONAL_GUIDANCE_VAR_0
-->



## Additional guidance from the user

${SLASH_COMMAND_PR_REVIEW_ARTIFACT_ADDITIONAL_GUIDANCE_VAR_0}
