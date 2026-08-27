<!--
name: Artifact Delete — Consent Ask
description: >-
  The permanent-delete confirmation prompt, used both as the ask message and as
  its safetyCheck decisionReason.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_DELETE_CONSENT_ASK_VAR_0
  - TOOL_RESULT_ARTIFACT_DELETE_CONSENT_ASK_VAR_1
  - TOOL_RESULT_ARTIFACT_DELETE_CONSENT_ASK_VAR_2
  - TOOL_RESULT_ARTIFACT_DELETE_CONSENT_ASK_VAR_3
-->
Claude wants to permanently delete ${TOOL_RESULT_ARTIFACT_DELETE_CONSENT_ASK_VAR_0?`the artifact "${TOOL_RESULT_ARTIFACT_DELETE_CONSENT_ASK_VAR_0}"`:`the artifact at ${TOOL_RESULT_ARTIFACT_DELETE_CONSENT_ASK_VAR_1}`} (${TOOL_RESULT_ARTIFACT_DELETE_CONSENT_ASK_VAR_2}). Its link will stop working for everyone, its comments and version history are deleted too, and this can't be undone.${TOOL_RESULT_ARTIFACT_DELETE_CONSENT_ASK_VAR_3}
