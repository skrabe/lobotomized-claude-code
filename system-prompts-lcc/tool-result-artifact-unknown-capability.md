<!--
name: Artifact unknown capability error
description: >-
  Publish error returned to the model listing capabilities the pinned contract
  does not support, told to fix or drop them.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_0
  - TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_1
  - TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_2
  - TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_3
  - TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_4
  - TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_5
-->
unknown ${TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_0(TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_1.length,"capability","capabilities")}: ${TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_2} — contract ${TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_3.version} supports: ${TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_4||"(none)"}.${TOOL_RESULT_ARTIFACT_UNKNOWN_CAPABILITY_VAR_5} Fix or drop the declaration; the control plane would reject it anyway.
