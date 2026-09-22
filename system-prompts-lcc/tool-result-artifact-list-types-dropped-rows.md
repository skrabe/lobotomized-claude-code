<!--
name: 'Tool Result: Artifact List Types Dropped Rows'
description: >-
  list_types note that some type rows could not be read and are missing from the
  listing.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_LIST_TYPES_DROPPED_ROWS_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_TYPES_DROPPED_ROWS_VAR_1
-->
${TOOL_RESULT_ARTIFACT_LIST_TYPES_DROPPED_ROWS_VAR_0.dropped} ${TOOL_RESULT_ARTIFACT_LIST_TYPES_DROPPED_ROWS_VAR_1(TOOL_RESULT_ARTIFACT_LIST_TYPES_DROPPED_ROWS_VAR_0.dropped,"row")} could not be read and ${TOOL_RESULT_ARTIFACT_LIST_TYPES_DROPPED_ROWS_VAR_0.dropped===1?"is":"are"} missing from this listing.
