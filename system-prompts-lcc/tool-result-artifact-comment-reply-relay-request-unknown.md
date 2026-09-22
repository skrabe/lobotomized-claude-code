<!--
name: Comment Reply Outcome Unknown — Relay Request Or Network
description: >-
  First-attempt catch when the relay request fails or the network times out, so
  the reply may already have posted.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_COMMENT_REPLY_RELAY_REQUEST_UNKNOWN_VAR_0
-->
comment reply outcome unknown (${TOOL_RESULT_ARTIFACT_COMMENT_REPLY_RELAY_REQUEST_UNKNOWN_VAR_0?"relay request failed":"no answer: network error or timeout"}) — it may have posted; re-read the comments before retrying
