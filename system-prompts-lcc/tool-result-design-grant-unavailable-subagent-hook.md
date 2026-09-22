<!--
name: 'Tool Result: Design Project Grant Unavailable (Subagent/Hook)'
description: >-
  ClaudeDesign permission-deny message returned to the model when a tokenless
  write needs a one-time project approval unavailable in subagent or
  PermissionRequest-hook sessions.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_DESIGN_GRANT_UNAVAILABLE_SUBAGENT_HOOK_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_GRANT_UNAVAILABLE_SUBAGENT_HOOK_VAR_0.operation}: writing without a plan_token requires a one-time project approval, which is not available in subagent or PermissionRequest-hook sessions — use finalize_plan with writes (and deletes if needed), then pass the returned plan_token.
