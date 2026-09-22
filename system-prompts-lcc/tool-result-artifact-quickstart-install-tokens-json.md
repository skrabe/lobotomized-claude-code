<!--
name: Artifact Quickstart Install Tokens Json
description: >-
  Tells the model how to attach a saved design-system tokens.json (and unpin
  slides) when creating an artifact.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_0
  - TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_1
  - TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_2
  - TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_3
-->
  To install the design system, send its saved tokens.json as it is: in the call that sends the ${TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_0.whole}, files gets "project/ds/<folder>/tokens.json": {"from": ${TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_1(TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_2)}, "contentType": "application/json"}${TOOL_RESULT_ARTIFACT_QUICKSTART_INSTALL_TOKENS_JSON_VAR_3.typeKey==="slides"?', and its designSystems record gets "unpinned": true':""}.
