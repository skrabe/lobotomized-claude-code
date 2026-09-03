<!--
name: 'Tool Result: Artifact Live Subscription Publish Adopted'
description: >-
  Live-subscription status line when this agent holds no watch and the launching
  session takes over republish notifications.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_ARTIFACT_LIVE_SUBSCRIPTION_PUBLISH_ADOPTED_VAR_0
-->
Live subscription: this agent holds no watch; the session that launched it takes over live updates for this artifact when this agent finishes normally — that session is then notified when this artifact is republished elsewhere${TOOL_RESULT_ARTIFACT_LIVE_SUBSCRIPTION_PUBLISH_ADOPTED_VAR_0()}.
