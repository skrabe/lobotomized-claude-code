<!--
name: 'Tool Result: Artifact DB Relay Did Not Carry Request'
description: >-
  ArtifactData error returned when this cloud session's artifact connection did
  not carry the db request, so nothing ran. It adds that Claude Code on the
  user's own machine can still read and edit the artifact.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_3
  - TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_4
-->
db ${TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_0} failed (${TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_1("store_unavailable")}): ${TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_2?"resolving 'me' failed — ":""}this cloud session's artifact connection did not carry the request${TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_3.status?` (HTTP ${TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_3.status})`:""}, so nothing ran; this says nothing about the artifact or its data, and if the user has access, Claude Code on their own machine can still read and edit it${TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_0==="write"?TOOL_RESULT_ARTIFACT_DB_RELAY_NOT_CARRIED_VAR_4:""}
