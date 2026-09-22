<!--
name: Artifact Action Watch Unavailable
description: >-
  Action-parameter description that watch/unwatch/status live subscriptions are
  unavailable in this session.
ccVersion: 2.1.274
variables:
  - TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_UNAVAILABLE_VAR_0
  - TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_UNAVAILABLE_VAR_1
-->
 'watch', 'unwatch', and 'status' manage live-update subscriptions through which a session keeps track of new versions of an artifact published elsewhere, and those aren't available in this session: 'watch' only reports that${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_UNAVAILABLE_VAR_0()} — this session does not keep track of new versions${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_UNAVAILABLE_VAR_1?", and no comment notification reaches it":""} — and 'status' lists this session's artifact watches (pass \`url\` to check one).${TOOL_PARAMETER_ARTIFACT_ACTION_WATCH_UNAVAILABLE_VAR_1?" 'resume_replies' (re-enabling automatic comment replies the user stopped) isn't available here either — automatic replies ride a live watch — so say so rather than calling it.":""}
