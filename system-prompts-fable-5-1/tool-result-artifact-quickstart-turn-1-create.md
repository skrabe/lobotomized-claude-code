<!--
name: Artifact Quickstart Turn 1 Create
description: >-
  Turn 1 create-mode instruction, now with optional auto_open and a dynamic file
  list instead of Bash.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_QUICKSTART_TURN_1_CREATE_VAR_0
  - TOOL_RESULT_ARTIFACT_QUICKSTART_TURN_1_CREATE_VAR_1
-->
Turn 1: create the artifact with Artifact({ type_url, title${TOOL_RESULT_ARTIFACT_QUICKSTART_TURN_1_CREATE_VAR_0?"":', auto_open: "after_first_write"'} }) and read ${TOOL_RESULT_ARTIFACT_QUICKSTART_TURN_1_CREATE_VAR_1}.
