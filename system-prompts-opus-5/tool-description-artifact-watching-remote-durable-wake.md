<!--
name: 'Tool Description: Artifact Watching Remote Durable Wake'
description: >-
  Remote-session Artifact prompt section: watches are durable wake
  subscriptions, not a live connection.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_REMOTE_DURABLE_WAKE_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_REMOTE_DURABLE_WAKE_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_REMOTE_DURABLE_WAKE_VAR_2
-->
**Watching for republishes**: in this remote session a watch is a durable wake subscription held by the artifact service, not a live connection: this session is woken with a new turn when the watched artifact is republished elsewhere${TOOL_DESCRIPTION_ARTIFACT_WATCHING_REMOTE_DURABLE_WAKE_VAR_0?", or when a comment on it is sent to Claude":""}; nothing streams in between, so on a wake re-read the artifact before editing. Publishing an artifact starts registering its watch in the background, and the result line says whether that began, was skipped, or was already registered. ${TOOL_DESCRIPTION_ARTIFACT_WATCHING_REMOTE_DURABLE_WAKE_VAR_1} Do not claim you are watching an artifact unless a watch result or a publish result's "already registered" line says so — its "arming" line is not yet a watch.${TOOL_DESCRIPTION_ARTIFACT_WATCHING_REMOTE_DURABLE_WAKE_VAR_2}
