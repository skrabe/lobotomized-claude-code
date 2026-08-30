<!--
name: Artifact action watch unavailable (no rail)
description: >-
  Action-enum description fragment stating watch/unwatch/status subscriptions
  are not available in this session.
ccVersion: 2.1.239
variables:
  - TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_UNAVAILABLE_VAR_0
  - TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_UNAVAILABLE_VAR_1
-->
 'watch', 'unwatch', and 'status' manage live-update subscriptions that notify a session when an artifact is republished elsewhere, and those aren't available in this session: 'watch' only reports that${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_UNAVAILABLE_VAR_0()} — no republish${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_UNAVAILABLE_VAR_1?" or comment":""} notification reaches this session — and 'status' lists this session's artifact watches (pass \`url\` to check one).${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_UNAVAILABLE_VAR_1?" 'resume_replies' (re-enabling automatic comment replies the user stopped) isn't available here either — automatic replies ride a live watch — so say so rather than calling it.":""}
