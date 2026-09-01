<!--
name: 'Tool Result: Artifact <title> Tag Overrides title Param'
description: >-
  Warning pushed into the Artifact tool's result `warnings` array, returned to
  the model when the document's <title> supersedes the title parameter.
ccVersion: 2.1.214
variables:
  - TOOL_RESULT_ARTIFACT_TITLE_TAG_WINS_VAR_0
  - TOOL_RESULT_ARTIFACT_TITLE_TAG_WINS_VAR_1
  - TOOL_RESULT_ARTIFACT_TITLE_TAG_WINS_VAR_2
-->
The document's own <title> ("${TOOL_RESULT_ARTIFACT_TITLE_TAG_WINS_VAR_0(TOOL_RESULT_ARTIFACT_TITLE_TAG_WINS_VAR_1)}") names this artifact; the \`title\` parameter ("${TOOL_RESULT_ARTIFACT_TITLE_TAG_WINS_VAR_0(TOOL_RESULT_ARTIFACT_TITLE_TAG_WINS_VAR_2)}") was not applied.
