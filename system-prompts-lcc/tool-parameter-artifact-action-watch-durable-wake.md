<!--
name: Artifact action watch (durable wake rail)
description: >-
  Action-enum description for watch/unwatch/status on the durable wake rail used
  by remote sessions.
ccVersion: 2.1.239
variables:
  - TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_DURABLE_WAKE_VAR_0
-->
 'watch' registers a durable wake subscription on the artifact at \`url\`: this remote session holds no live stream, so instead it is woken with a new turn when the artifact is republished elsewhere${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_DURABLE_WAKE_VAR_0?" or a comment on it is sent to Claude":""} (no live updates — on wake re-read the artifact${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_DURABLE_WAKE_VAR_0?" and, on a comment wake, its comments":""})${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_DURABLE_WAKE_VAR_0?"":"; reading and replying to artifact comments is not enabled in this session"}; 'unwatch' removes that subscription; 'status' lists this session's artifact watches (pass \`url\` to check one).${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_DURABLE_WAKE_VAR_0?" 'resume_replies' (re-enabling automatic comment replies the user stopped) is unavailable in this remote session — there is no live watch to re-arm, and comment wakes come through 'watch' — so say so rather than calling it.":""}
