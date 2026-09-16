<!--
name: Artifact List-By-Type Overflow Empty Page
description: >-
  Empty list-by-type tool_result when the newest page has nothing to show but
  older Artifacts may exist.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_OVERFLOW_EMPTY_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_OVERFLOW_EMPTY_VAR_1
-->
None of the rows on the one page this listing of Artifacts made from the type ${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_OVERFLOW_EMPTY_VAR_0} reads (the newest) were readable, and there are more than that page: ask the user for the link if they have one in mind, else carry on without one.${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_OVERFLOW_EMPTY_VAR_1?` (${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_OVERFLOW_EMPTY_VAR_1})`:""}
