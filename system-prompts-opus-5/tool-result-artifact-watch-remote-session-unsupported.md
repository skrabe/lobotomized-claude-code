<!--
name: Artifact Watch Unsupported In Remote Sessions
description: >-
  Tool result explaining that watching an artifact is not supported from a
  remote session and how the user can watch it locally.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_2
  - TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_3
-->
${TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_0}Not watching ${TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_1(TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_2.url)} — watching an artifact for new versions${TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_3?" and comments":""} isn't supported yet from remote sessions, so nothing will notify this session. ${TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_3?"Publishing, reading comments, and replying still work here.":"Publishing still works here."} To watch it, the user can run \`claude --watch-artifact ${TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_1(TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_2.url)}\` in Claude Code on their own machine.
