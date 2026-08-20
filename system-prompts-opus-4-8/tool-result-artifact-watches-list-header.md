<!--
name: 'Tool Result: Artifact watches list header'
description: >-
  Header line of the watches tool result listing this session's artifact watches
  (session-local; none survive a restart).
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_1
-->
${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_0} artifact ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_1(TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_0,"watch","watches")} in this session${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_2?"":` (session-local; ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_3})`}${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_4>0?`, plus ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_4} ${TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_1(TOOL_RESULT_ARTIFACT_WATCHES_LIST_HEADER_VAR_4,"artifact")} with auto-replies stopped and no connection`:""}:
