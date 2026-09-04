<!--
name: 'Tool Result: Artifact Publish Live Version Read Same Turn'
description: >-
  Stale-version guard refusal telling the model the live version arrived earlier
  this turn, so it must republish next turn on that content.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_LIVE_VERSION_READ_SAME_TURN_VAR_0
-->
This artifact's live version reached you earlier in this same turn${TOOL_RESULT_ARTIFACT_PUBLISH_LIVE_VERSION_READ_SAME_TURN_VAR_0}, so this publish could not have been built on it: nothing was published. Publish again in your next turn, built on that content — do not resend this content unchanged.
