<!--
name: Artifact Durable Wake Relay Unavailable
description: >-
  Durable-wake failure reason when this session's gateway did not carry a wake
  subscription (relay_unavailable, optional HTTP status).
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_RELAY_UNAVAILABLE_VAR_0
-->
Durable wake subscription: not armed — this session's gateway did not carry a wake subscription earlier (relay_unavailable${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_RELAY_UNAVAILABLE_VAR_0!==void 0?`: HTTP ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_RELAY_UNAVAILABLE_VAR_0}`:""}), so nothing will wake this session about this artifact; only an explicit watch re-checks.
