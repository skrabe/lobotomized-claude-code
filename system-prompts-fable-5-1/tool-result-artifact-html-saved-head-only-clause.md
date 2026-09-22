<!--
name: 'Tool Result: Artifact Saved HTML Head-Only Clause'
description: >-
  Tool-result clause telling the model the inlined head is not the whole
  artifact and any republish must be built from the saved file.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_HTML_SAVED_HEAD_ONLY_CLAUSE_VAR_0
  - TOOL_RESULT_ARTIFACT_HTML_SAVED_HEAD_ONLY_CLAUSE_VAR_1
  - TOOL_RESULT_ARTIFACT_HTML_SAVED_HEAD_ONLY_CLAUSE_VAR_2
-->
 — the head below is NOT the whole artifact: build any republish from that file${TOOL_RESULT_ARTIFACT_HTML_SAVED_HEAD_ONLY_CLAUSE_VAR_0}${TOOL_RESULT_ARTIFACT_HTML_SAVED_HEAD_ONLY_CLAUSE_VAR_1(TOOL_RESULT_ARTIFACT_HTML_SAVED_HEAD_ONLY_CLAUSE_VAR_2.html)?"; it is the page as served — the wrapper around your markup and the <!-- frame-runtime --> block in it come off again when you republish it, so leave them as they are":""}
