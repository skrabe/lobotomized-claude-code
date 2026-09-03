<!--
name: 'Tool Description: Artifact Watching Live Subscribe Compact'
description: Compact live-watch Artifact prompt arm for sessions that subscribe on publish.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_COMPACT_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_COMPACT_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_COMPACT_VAR_2
-->
**Watching for republishes**: publishing an artifact starts subscribing this session to its live changes in the background, and the result line says whether that began, was skipped, or was already connected; you are told if it cannot connect, and watches reconnect on their own if the connection drops. A later republish from elsewhere — another session, or someone saving from a page that can publish new versions of itself — arrives as a notification telling you to re-read it before editing.${TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_COMPACT_VAR_0?" A comment on a watched artifact that is sent to Claude also wakes this session while that artifact's auto-replies are armed (when comment auto-replies are on for this session, a publish arms them).":""} ${TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_COMPACT_VAR_1} Watches are session-local, and the user can see and stop them in /tasks. Do not claim you are watching an artifact unless a watch result or a publish result's "already connected" line says so — its "arming" line is not yet a watch. Only an interactive or SDK main-loop session holds a watch (not a subagent, teammate, background, or print session).${TOOL_DESCRIPTION_ARTIFACT_WATCHING_LIVE_SUBSCRIBE_COMPACT_VAR_2}
