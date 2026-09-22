<!--
name: Artifact read confirmation reason
description: >-
  decisionReason stating the artifact read requires confirmation because its
  content enters the conversation.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_READ_CONFIRMATION_REASON_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_CONFIRMATION_REASON_VAR_1
-->
Reading ${TOOL_RESULT_ARTIFACT_READ_CONFIRMATION_REASON_VAR_0} requires confirmation — its content enters the conversation${TOOL_RESULT_ARTIFACT_READ_CONFIRMATION_REASON_VAR_1?"; approval covers re-reads of this artifact for the rest of the conversation":""}
