<!--
name: Artifact Type Instructions Unreadable
description: >-
  Artifact-read note when the type ships an instructions file that could not be
  read, asking the model to ask the user before writing data if the expected
  content is unclear.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_TYPE_INSTRUCTIONS_UNREADABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_TYPE_INSTRUCTIONS_UNREADABLE_VAR_1
-->


[This Artifact's type ships an instructions file (${TOOL_RESULT_ARTIFACT_TYPE_INSTRUCTIONS_UNREADABLE_VAR_0}) describing the content its page expects, but it could not be read here: ${TOOL_RESULT_ARTIFACT_TYPE_INSTRUCTIONS_UNREADABLE_VAR_1.why}. If what it expects isn't clear from the file names, ask the user before writing data to it.]
