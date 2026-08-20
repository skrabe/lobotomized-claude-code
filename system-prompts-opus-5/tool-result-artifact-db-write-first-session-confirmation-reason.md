<!--
name: 'Tool Result: Artifact DB Write First-Session Confirmation Reason'
description: >-
  Default decisionReason for the first artifact database write this session:
  writes persist and are visible to everyone who can open the artifact.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_2
-->
First artifact database write this session requires confirmation${TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_0} — writes persist and are visible to everyone who can open the artifact${TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_1?"; approval covers database writes to any artifact for the rest of the session":""}${TOOL_RESULT_ARTIFACT_DB_WRITE_FIRST_SESSION_CONFIRMATION_REASON_VAR_2}
