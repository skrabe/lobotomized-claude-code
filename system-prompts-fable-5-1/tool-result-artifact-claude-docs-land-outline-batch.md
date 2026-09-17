<!--
name: Artifact Claude Docs Land Outline Batch
description: >-
  Instructs a single Claude Docs batch update to the prose root, then fill
  section by section.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_LAND_OUTLINE_BATCH_VAR_0
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_LAND_OUTLINE_BATCH_VAR_1
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_LAND_OUTLINE_BATCH_VAR_2
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_LAND_OUTLINE_BATCH_VAR_3
-->
Land the outline with ONE call to the Claude Docs connector's \`batch\` tool addressed to ${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_LAND_OUTLINE_BATCH_VAR_0(TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_LAND_OUTLINE_BATCH_VAR_1.projectId)} whose members update node ${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_LAND_OUTLINE_BATCH_VAR_2(TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_LAND_OUTLINE_BATCH_VAR_1.nodeId)} (the tab's prose root), then fill it section by section${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_LAND_OUTLINE_BATCH_VAR_3}.
