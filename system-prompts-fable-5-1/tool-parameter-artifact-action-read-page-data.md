<!--
name: 'Tool Parameter: Artifact action — read_page_data'
description: >-
  Fragment appended to the Artifact tool's `action` parameter description
  explaining what read_page_data does; part of the tool schema the model reads.
ccVersion: 2.1.219
variables:
  - TOOL_PARAMETER_ARTIFACT_ACTION_READ_PAGE_DATA_VAR_0
  - TOOL_PARAMETER_ARTIFACT_ACTION_READ_PAGE_DATA_VAR_1
-->
 'read_page_data' reads the declared data island from the published artifact at \`url\`, validates it against the interaction schema named by \`schema\` (available: ${TOOL_PARAMETER_ARTIFACT_ACTION_READ_PAGE_DATA_VAR_0.map((TOOL_PARAMETER_ARTIFACT_ACTION_READ_PAGE_DATA_VAR_1)=>`'${TOOL_PARAMETER_ARTIFACT_ACTION_READ_PAGE_DATA_VAR_1}'`).join(", ")}), and returns its validated typed entries only — never page content; it refuses when the island is out of contract.
