<!--
name: 'Tool Result: Not An Artifact URL'
description: >-
  validateInput rejection when url is not a parseable artifact link, telling the
  model how to update versus publish.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_VAR_0
  - TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_VAR_1
  - TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_VAR_2
-->
not an artifact URL: ${TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_VAR_0(TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_VAR_1)} — to update an existing artifact pass its ${TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_VAR_2()} link (action: "list" shows them); to publish a new one, omit \`url\`.
