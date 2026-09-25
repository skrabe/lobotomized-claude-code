<!--
name: 'Tool Result: Artifact Quickstart — Install Design System tokens.json'
description: >-
  Artifact quickstart instruction to install the design system by sending its
  saved tokens.json in the first call that publishes the deliverable, plus the
  slides designSystems unpinned note.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_0
  - TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_1
  - TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_2
  - TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_3
-->
  To install the design system, send its saved tokens.json as it is: in the first call that publishes the ${TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_0.whole}, files gets "project/ds/<folder>/tokens.json": {"from": ${TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_1(TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_2)}, "contentType": "application/json"}${TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_3.typeKey==="slides"?', and its designSystems record gets "unpinned": true':""}.
