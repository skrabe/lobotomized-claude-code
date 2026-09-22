<!--
name: Artifact listing count header
description: >-
  Count/scope header line of the ArtifactTool listing tool_result (e.g. "N
  artifacts shared with you (most recent first):"), returned to the model.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_2
-->
${TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_0.length} ${TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_1.scope==="shared"?TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_2(TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_0.length,"artifact shared with you","artifacts shared with you"):TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_2(TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_0.length,TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_1.scope==="all"?"artifact":"published artifact")}${TOOL_RESULT_ARTIFACT_LIST_COUNT_HEADER_VAR_1.scope==="all"?", published by you or shared with you":""} (most recent first):
