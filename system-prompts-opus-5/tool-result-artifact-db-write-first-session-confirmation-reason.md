<!--
name: 'Tool Result: Artifact DB Write First-Session Confirmation Reason'
description: >-
  Ask-path decisionReason that artifact database writes persist and are visible
  to everyone who can open the artifact.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_2
-->
${TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_0?"First artifact database write this session":"This artifact database write"} requires confirmation${TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_1} — writes persist and are visible to everyone who can open the artifact${TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_0?"; approval covers database writes to any artifact for the rest of the session":""}${TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_2}
