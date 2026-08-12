<!--
name: 'Tool Result: Artifact watches list header'
description: >-
  Header line of the watches tool result listing this session's artifact watches
  (session-local; none survive a restart).
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_1
-->
${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_0.watches.length} artifact ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_1(TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_0.watches.length,"watch","watches")} in this session (session-local; none survive a restart):
