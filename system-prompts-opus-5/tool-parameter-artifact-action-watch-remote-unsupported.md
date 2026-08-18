<!--
name: 'Tool parameter: Artifact action — watch/unwatch/status (remote unsupported)'
description: >-
  Remote-session branch of the action-parameter addendum describing that
  watch/unwatch/status subscriptions are not supported from a remote session.
ccVersion: 2.1.234
variables:
  - TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_REMOTE_UNSUPPORTED_VAR_0
-->
 'watch', 'unwatch', and 'status' manage live-update subscriptions that notify a session when another session republishes an artifact, and those aren't supported yet from this remote session: 'watch' only reports that — no republish${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_REMOTE_UNSUPPORTED_VAR_0?" or comment":""} notification reaches this session — and 'status' lists this session's artifact watches (pass \`url\` to check one).${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_REMOTE_UNSUPPORTED_VAR_0?" 'resume_replies' (re-enabling automatic comment replies the user stopped) isn't supported from this remote session either — automatic replies run only in a live session, so say so rather than calling it.":""}
