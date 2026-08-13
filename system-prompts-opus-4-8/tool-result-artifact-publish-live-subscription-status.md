<!--
name: 'Tool Result: Artifact Publish Live-Subscription Status'
description: >-
  Dynamic live-subscription status suffix appended to the Artifact publish tool
  result, including durable-wake arming status.
ccVersion: 2.1.231
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_LIVE_SUBSCRIPTION_STATUS_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_LIVE_SUBSCRIPTION_STATUS_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_LIVE_SUBSCRIPTION_STATUS_VAR_2
-->


${TOOL_RESULT_ARTIFACT_PUBLISH_LIVE_SUBSCRIPTION_STATUS_VAR_0&&TOOL_RESULT_ARTIFACT_PUBLISH_LIVE_SUBSCRIPTION_STATUS_VAR_1.liveSubscription==="durable_arming"?"Durable wake subscription: arming in the background — once armed, this session is woken by a new turn when another session republishes this artifact, or when anyone sends a comment on it to Claude.":TOOL_RESULT_ARTIFACT_PUBLISH_LIVE_SUBSCRIPTION_STATUS_VAR_2(TOOL_RESULT_ARTIFACT_PUBLISH_LIVE_SUBSCRIPTION_STATUS_VAR_1.liveSubscription)}
