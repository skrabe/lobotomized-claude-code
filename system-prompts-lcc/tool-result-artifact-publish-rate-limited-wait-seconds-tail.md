<!--
name: 'Tool Result: Artifact Publish Rate-Limited Wait Tail'
description: >-
  Artifact rate-limit result tail after the retry delay: publishing limits are
  shared so the wait may be longer, and nothing else about the call should
  change
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_RATE_LIMITED_WAIT_SECONDS_TAIL_VAR_0
-->
 seconds — publishing limits are shared, so the wait can be longer while others publish; change nothing${TOOL_RESULT_ARTIFACT_PUBLISH_RATE_LIMITED_WAIT_SECONDS_TAIL_VAR_0?" else":""} about the call to get past this.
