<!--
name: 'Tool Result: ClaudeDesign Project Identity Unverified Deny'
description: >-
  Denial message returned when a durable project write grant cannot be offered
  because the project identity could not be verified, instructing the model to
  read the project first or fall back to the finalize_plan/plan_token flow;
  delivered to the model as an is_error tool_result.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_CLAUDEDESIGN_PROJECT_IDENTITY_UNVERIFIED_DENY_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_CLAUDEDESIGN_PROJECT_IDENTITY_UNVERIFIED_DENY_VAR_0.operation}: a durable project write grant is only offered when the approval dialog can name its target, and the project identity (name, sharing, URL) could not be verified or rendered faithfully. If this is a fresh connection, read the project first (e.g. get_project — approve the Claude Design connection if prompted) and retry once; otherwise use finalize_plan with writes/deletes and pass the returned plan_token (the per-batch flow), which is always supported.
