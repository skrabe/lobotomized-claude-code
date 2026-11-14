<!--
name: 'Tool Result: Artifact watch remote session unsupported'
description: >-
  Watch result saying watching is unsupported from remote sessions and how the
  user can watch locally.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_2
-->
Not watching ${TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_0(TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_1.url)} — watching an artifact for new versions${TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_2?" and comments":""} isn't supported yet from remote sessions, so nothing will notify this session. ${TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_2?"Publishing, reading comments, and replying still work here.":"Publishing still works here."} To watch it, the user can run \`claude --watch-artifact ${TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_0(TOOL_RESULT_ARTIFACT_WATCH_REMOTE_SESSION_UNSUPPORTED_VAR_1.url)}\` in Claude Code on their own machine.
