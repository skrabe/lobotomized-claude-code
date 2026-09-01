<!--
name: 'Tool Result: Artifact read_page_data Requires Schema'
description: >-
  validateInput rejection telling the model that the Artifact `read_page_data`
  action needs a registered interaction schema; wrapped in <tool_use_error>
  and returned to the model.
ccVersion: 2.1.219
variables:
  - TOOL_RESULT_ARTIFACT_READ_PAGE_DATA_REQUIRES_SCHEMA_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_PAGE_DATA_REQUIRES_SCHEMA_VAR_1
-->
action "read_page_data" requires \`schema\`${TOOL_RESULT_ARTIFACT_READ_PAGE_DATA_REQUIRES_SCHEMA_VAR_0?.TOOL_RESULT_ARTIFACT_READ_PAGE_DATA_REQUIRES_SCHEMA_VAR_1?` (e.g. "${[...TOOL_RESULT_ARTIFACT_READ_PAGE_DATA_REQUIRES_SCHEMA_VAR_0][0]}")`:""}.
