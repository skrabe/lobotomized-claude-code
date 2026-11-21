<!--
name: 'Tool result: artifact type header'
description: >-
  Header line of a describe-type result naming the type, its tier or third-party
  mark, and release.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_ARTIFACT_TYPE_VAR_0
  - TOOL_RESULT_ARTIFACT_TYPE_VAR_1
  - TOOL_RESULT_ARTIFACT_TYPE_VAR_2
  - TOOL_RESULT_ARTIFACT_TYPE_VAR_3
  - TOOL_RESULT_ARTIFACT_TYPE_VAR_4
  - TOOL_RESULT_ARTIFACT_TYPE_VAR_5
-->
Artifact type ${TOOL_RESULT_ARTIFACT_TYPE_VAR_0}${TOOL_RESULT_ARTIFACT_TYPE_VAR_1.third_party===!0?` ${TOOL_RESULT_ARTIFACT_TYPE_VAR_2}`:TOOL_RESULT_ARTIFACT_TYPE_VAR_3(TOOL_RESULT_ARTIFACT_TYPE_VAR_1.tier)?` [${TOOL_RESULT_ARTIFACT_TYPE_VAR_1.tier}]`:""}${typeof TOOL_RESULT_ARTIFACT_TYPE_VAR_1.release==="string"?`, release ${TOOL_RESULT_ARTIFACT_TYPE_VAR_4(TOOL_RESULT_ARTIFACT_TYPE_VAR_1.release)}`:""} (${TOOL_RESULT_ARTIFACT_TYPE_VAR_5}).
