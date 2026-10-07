<!--
name: 'Tool Result: Artifact policy unverifiable 403 instructions'
description: >-
  Tells the model the organization policy request was refused with HTTP 403 in a
  cloud session, not to retry, and what to tell the user
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_ARTIFACT_POLICY_UNVERIFIABLE_403_INSTRUCTIONS_VAR_0
-->
Claude Code reads the organization's policy from ${TOOL_RESULT_ARTIFACT_POLICY_UNVERIFIABLE_403_INSTRUCTIONS_VAR_0}. Do not retry this call now. Tell the user that artifacts are unavailable because Anthropic couldn't confirm their organization's settings for this cloud session, and that it isn't a problem with their network.
