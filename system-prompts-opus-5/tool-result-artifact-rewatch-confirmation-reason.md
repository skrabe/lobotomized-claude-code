<!--
name: Artifact Rewatch Confirmation Reason
description: >-
  safetyCheck decisionReason for re-watching an artifact whose watch was
  deliberately stopped; declined, it is the tool_result the model reads.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_REWATCH_CONFIRMATION_REASON_VAR_0
  - TOOL_RESULT_ARTIFACT_REWATCH_CONFIRMATION_REASON_VAR_1
-->
Re-watching an artifact whose watch was deliberately stopped requires confirmation — it resumes the subscription and republish self-heal for the rest of the session${TOOL_RESULT_ARTIFACT_REWATCH_CONFIRMATION_REASON_VAR_0&&!TOOL_RESULT_ARTIFACT_REWATCH_CONFIRMATION_REASON_VAR_1.declined?" and, on an artifact the user can edit whose link the user gave, lets Claude answer comments sent to Claude unattended (auto-replies that were stopped stay stopped; ones only paused by an interrupt resume)":""}
