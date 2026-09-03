<!--
name: Artifact Separate Tools Load Hint
description: >-
  Artifact tool-description **Separate tools** sentence telling the model to
  load a sibling tool when needed.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_HINT_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_HINT_VAR_1
-->
**Separate tools**: ${TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_HINT_VAR_0.join(", ")} — ${TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_HINT_VAR_0.length===1?"a separate tool":"separate tools"}; load one with ${TOOL_DESCRIPTION_ARTIFACT_SEPARATE_TOOLS_LOAD_HINT_VAR_1} when you need it.
