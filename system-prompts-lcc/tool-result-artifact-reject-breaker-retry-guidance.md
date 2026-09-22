<!--
name: 'Tool Result: Artifact Reject Breaker Retry Guidance'
description: >-
  Reject-breaker tool-result telling the model not to repeat the same Artifact
  call and to either apply the stated fix or stop and explain the failure.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_REJECT_BREAKER_RETRY_GUIDANCE_VAR_0
-->
${TOOL_RESULT_ARTIFACT_REJECT_BREAKER_RETRY_GUIDANCE_VAR_0} Do not send the same call again: either make the specific change the error describes, or stop calling Artifact for this target and tell the user what is failing and why.
