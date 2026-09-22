<!--
name: 'Tool Result: Artifact Durable Wake Remote Skip Note'
description: >-
  Remote watch tool-result suffix explaining that durable wake was skipped and
  appending the reason.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_RAIL_SKIPPED_TAIL_VAR_0
  - TOOL_RESULT_ARTIFACT_DURABLE_WAKE_RAIL_SKIPPED_TAIL_VAR_1
-->
 This remote session's durable wake rail was skipped as well: ${TOOL_RESULT_ARTIFACT_DURABLE_WAKE_RAIL_SKIPPED_TAIL_VAR_0.durable_skip_reason==="no_wake_minter"?"no wake-webhook minter is available (the session's own MCP mount was not found)":TOOL_RESULT_ARTIFACT_DURABLE_WAKE_RAIL_SKIPPED_TAIL_VAR_0.durable_skip_reason==="stop_latched"?"watching this artifact was stopped earlier in this session (do not retry on your own)":TOOL_RESULT_ARTIFACT_DURABLE_WAKE_RAIL_SKIPPED_TAIL_VAR_1(TOOL_RESULT_ARTIFACT_DURABLE_WAKE_RAIL_SKIPPED_TAIL_VAR_0.durable_skip_reason)}.
