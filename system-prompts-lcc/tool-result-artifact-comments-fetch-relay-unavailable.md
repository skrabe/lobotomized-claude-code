<!--
name: Comments Fetch Failed — Relay Did Not Carry The Read
description: >-
  Artifact comments-read `{err}` when this session's comment connection
  (relay-unavailable) carried no read, telling the model to retry once then tell
  the user.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_COMMENTS_FETCH_RELAY_UNAVAILABLE_VAR_0
-->
comments fetch failed (this session's comment connection did not carry the read${TOOL_RESULT_ARTIFACT_COMMENTS_FETCH_RELAY_UNAVAILABLE_VAR_0!==0?`, HTTP ${TOOL_RESULT_ARTIFACT_COMMENTS_FETCH_RELAY_UNAVAILABLE_VAR_0}`:""}; nothing was read) — retry once; if it fails again, tell the user comments cannot be read from this session right now
