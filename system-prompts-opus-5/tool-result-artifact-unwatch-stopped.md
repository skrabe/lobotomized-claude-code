<!--
name: 'Tool Result: Artifact unwatch stopped'
description: >-
  Artifact tool result reporting that the session stopped watching an artifact
  and should not re-watch it unbidden
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_UNWATCH_STOPPED_VAR_0
-->
Stopped watching ${TOOL_RESULT_ARTIFACT_UNWATCH_STOPPED_VAR_0.unwatch.url}; republishes of it will no longer be reported in this session. Do not watch it again unless the user asks.
