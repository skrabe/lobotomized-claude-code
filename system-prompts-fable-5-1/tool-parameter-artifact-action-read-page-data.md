<!--
name: 'Tool Parameter: Artifact action read_page_data'
description: >-
  Describes the artifact tool's 'read_page_data' action: read the declared data
  island and validate it against a named interaction schema.
ccVersion: 2.1.269
variables:
  - TOOL_PARAMETER_ARTIFACT_ACTION_READ_PAGE_DATA_VAR_0
  - TOOL_PARAMETER_ARTIFACT_ACTION_READ_PAGE_DATA_VAR_1
-->
 'read_page_data' reads the declared data island from the published artifact at \`url\`, validates it against the interaction schema named by \`schema\` (available: ${TOOL_PARAMETER_ARTIFACT_ACTION_READ_PAGE_DATA_VAR_0.map((TOOL_PARAMETER_ARTIFACT_ACTION_READ_PAGE_DATA_VAR_1)=>`'${TOOL_PARAMETER_ARTIFACT_ACTION_READ_PAGE_DATA_VAR_1}'`).join(", ")}), and returns its validated typed entries only — never page content; it refuses when the island is out of contract.
