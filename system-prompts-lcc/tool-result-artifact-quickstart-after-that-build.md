<!--
name: Artifact Quickstart After That Build
description: >-
  After the read/create turn, tells the model to build from the create-or-read
  result using the files it read.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_QUICKSTART_AFTER_THAT_BUILD_VAR_0
  - TOOL_RESULT_ARTIFACT_QUICKSTART_AFTER_THAT_BUILD_VAR_1
-->
After that: build the ${TOOL_RESULT_ARTIFACT_QUICKSTART_AFTER_THAT_BUILD_VAR_0.whole} as the ${TOOL_RESULT_ARTIFACT_QUICKSTART_AFTER_THAT_BUILD_VAR_1?"create":"read"} result's instructions say, using the files you read.
