<!--
name: 'Tool Result: Artifact watches list header'
description: >-
  Header of the Artifact watches tool result reporting the number of
  session-local watches and noting that none survive a restart.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_1
-->
${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_0.watches.length} artifact ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_1(TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_0.watches.length,"watch","watches")} in this session (session-local; none survive a restart):
