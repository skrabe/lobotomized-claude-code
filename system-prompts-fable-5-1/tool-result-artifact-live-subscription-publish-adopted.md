<!--
name: 'Tool Result: Artifact Live Subscription Publish Adopted'
description: >-
  Live-subscription status line when this agent holds no watch and the launching
  session takes over republish notifications.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_LIVE_SUBSCRIPTION_PUBLISH_ADOPTED_VAR_0
-->
Live subscription: this agent holds no watch; the session that launched it takes over live updates for this artifact when this agent finishes normally — that session then keeps track of new versions of this artifact published elsewhere; a new version starts no turn and sends no notification${TOOL_RESULT_ARTIFACT_LIVE_SUBSCRIPTION_PUBLISH_ADOPTED_VAR_0()}.
