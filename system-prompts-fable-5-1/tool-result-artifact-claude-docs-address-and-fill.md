<!--
name: Artifact Claude Docs Address And Fill
description: >-
  Instructs addressing the Claude Docs project, reading tab/root ids, then
  filling the document.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_ADDRESS_AND_FILL_VAR_0
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_ADDRESS_AND_FILL_VAR_1
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_ADDRESS_AND_FILL_VAR_2
-->
With the Claude Docs connector, address it as ${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_ADDRESS_AND_FILL_VAR_0(TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_ADDRESS_AND_FILL_VAR_1.projectId)} and read it once for its tab and root ids before writing, then fill it${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_ADDRESS_AND_FILL_VAR_2}.
