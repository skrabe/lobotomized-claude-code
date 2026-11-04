<!--
name: 'Tool Result: Artifact Live Subscription Arming'
description: >-
  Status line appended to the artifact-publish tool result telling the model the
  live republish watch is arming in the background.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_LIVE_SUBSCRIPTION_ARMING_VAR_0
-->

Live subscription: arming in the background — not connected yet, so this is not a watch until \`status\` shows it connected (you are told if it cannot connect, unless this turn is interrupted first). Once connected, this session keeps track of new versions of this artifact published elsewhere; a new version starts no turn and sends no notification${TOOL_RESULT_ARTIFACT_LIVE_SUBSCRIPTION_ARMING_VAR_0()}.
