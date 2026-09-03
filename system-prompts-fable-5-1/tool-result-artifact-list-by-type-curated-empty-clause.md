<!--
name: Artifact List-By-Type Curated Empty Clause
description: >-
  Parenthetical on the empty list-by-type result when the organization lists
  none for new artifacts.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_CURATED_EMPTY_CLAUSE_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_CURATED_EMPTY_CLAUSE_VAR_1
-->
 (the organization lists none for new artifacts${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_CURATED_EMPTY_CLAUSE_VAR_0==="all"?" and the user has none of their own":""}${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_CURATED_EMPTY_CLAUSE_VAR_1?`; ${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_CURATED_EMPTY_CLAUSE_VAR_1}`:""})
