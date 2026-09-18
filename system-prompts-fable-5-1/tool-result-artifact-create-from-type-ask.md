<!--
name: 'Tool Result: Artifact create from type ask'
description: >-
  Permission ask message when Claude wants to create a new private claude.ai
  artifact from an Artifact type, naming the type and title and noting the page
  was written by the type's publisher
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_0
  - TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_1
  - TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_2
  - TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_3
  - TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_4
-->
Claude wants to create a new private artifact on claude.ai from ${TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_0!==""?`the artifact type "${TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_0}"`:"an artifact type"}${TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_1?`, titled "${TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_1}"`:""}. Its page was written by that type's publisher; no local file is uploaded.${TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_2}

type: ${TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_3(TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_ASK_VAR_4)}
