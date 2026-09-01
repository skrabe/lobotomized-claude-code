<!--
name: 'Tool Result: Artifact List Made From Type'
description: >-
  list tool_result header for Artifacts made from a type, with mine/shared rows
  and default marking.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_2
  - TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_3
  - TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_4
  - TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_5
-->
${TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_0.rows.length} ${TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_1(TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_0.rows.length,"Artifact")} made from the type ${TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_2} ${TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_3}${TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_4}. Each row leads with (mine) or (shared); a default, when there is one, is always the first row and is marked there, before its title, as the user's or the organization's default (${TOOL_RESULT_ARTIFACT_LIST_MADE_FROM_TYPE_VAR_5}):
