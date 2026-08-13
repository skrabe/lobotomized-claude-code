<!--
name: 'Tool Result: Artifact Durable Wake Remote Skip Note'
description: >-
  Remote watch tool-result suffix explaining that durable wake was skipped and
  appending the reason.
ccVersion: 2.1.231
variables:
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_REMOTE_SKIP_NOTE_VAR_0
-->
 This remote session's durable wake rail was skipped as well: ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_REMOTE_SKIP_NOTE_VAR_0.durable_skip_reason==="flag_off"?"durable wake subscriptions are not enabled for this session":TOOL_RESULT_ARTIFACT_DURABLE_WAKE_REMOTE_SKIP_NOTE_VAR_0.durable_skip_reason==="no_wake_minter"?"no wake-webhook minter is available (the session's own MCP mount was not found)":TOOL_RESULT_ARTIFACT_DURABLE_WAKE_REMOTE_SKIP_NOTE_VAR_0.durable_skip_reason}.
