<!--
name: 'Tool Result: Artifact list more may exist'
description: Note that more artifacts may exist when the listing was truncated
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_ARTIFACT_LIST_MORE_MAY_EXIST_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_MORE_MAY_EXIST_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_MORE_MAY_EXIST_VAR_2
-->

(More may exist: ${TOOL_RESULT_ARTIFACT_LIST_MORE_MAY_EXIST_VAR_0?`a higher \`limit\` (up to ${TOOL_RESULT_ARTIFACT_LIST_MORE_MAY_EXIST_VAR_1}) may list more, and `:""}${TOOL_RESULT_ARTIFACT_LIST_MORE_MAY_EXIST_VAR_2})
