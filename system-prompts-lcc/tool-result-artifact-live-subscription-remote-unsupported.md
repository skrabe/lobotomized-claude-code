<!--
name: 'Tool Result: Artifact Live Subscription Not Supported (Remote)'
description: >-
  Publish/watch status line saying live subscriptions are not supported yet from
  remote sessions and the artifact (and comments) must be re-read on request.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_LIVE_SUBSCRIPTION_REMOTE_UNSUPPORTED_VAR_0
-->
Live subscription: not supported yet from remote sessions — nothing notifies this session of new versions${TOOL_RESULT_ARTIFACT_LIVE_SUBSCRIPTION_REMOTE_UNSUPPORTED_VAR_0?" or of comments sent to Claude":""}; re-read the artifact${TOOL_RESULT_ARTIFACT_LIVE_SUBSCRIPTION_REMOTE_UNSUPPORTED_VAR_0?" (and its comments)":""} when the user asks.
