<!--
name: 'Tool Result: Artifact Type Reference Pages Follow'
description: >-
  Preamble attaching the type's first-read reference pages to a create-from-type
  tool_result and telling the model not to fetch them again.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_TYPE_REFERENCE_PAGES_FOLLOW_VAR_0
  - TOOL_RESULT_ARTIFACT_TYPE_REFERENCE_PAGES_FOLLOW_VAR_1
  - TOOL_RESULT_ARTIFACT_TYPE_REFERENCE_PAGES_FOLLOW_VAR_2
  - TOOL_RESULT_ARTIFACT_TYPE_REFERENCE_PAGES_FOLLOW_VAR_3
-->


The type's reference pages that its instructions above say to read first follow — ${TOOL_RESULT_ARTIFACT_TYPE_REFERENCE_PAGES_FOLLOW_VAR_0.map((TOOL_RESULT_ARTIFACT_TYPE_REFERENCE_PAGES_FOLLOW_VAR_1)=>TOOL_RESULT_ARTIFACT_TYPE_REFERENCE_PAGES_FOLLOW_VAR_1.path).join(", ")}, the same files a read of this Artifact returns; do not fetch them again${TOOL_RESULT_ARTIFACT_TYPE_REFERENCE_PAGES_FOLLOW_VAR_2?" unless you need a clipped remainder":""}.${TOOL_RESULT_ARTIFACT_TYPE_REFERENCE_PAGES_FOLLOW_VAR_3.length>0?` Not attached: ${TOOL_RESULT_ARTIFACT_TYPE_REFERENCE_PAGES_FOLLOW_VAR_3.join("; ")}.`:""}

