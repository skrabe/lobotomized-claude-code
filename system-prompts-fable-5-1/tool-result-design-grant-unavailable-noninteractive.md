<!--
name: 'Tool Result: Design Project Grant Unavailable (Non-Interactive)'
description: >-
  ClaudeDesign permission-deny message returned to the model when a tokenless
  write needs a one-time interactive project approval that cannot be shown in a
  non-interactive session.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_DESIGN_GRANT_UNAVAILABLE_NONINTERACTIVE_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_GRANT_UNAVAILABLE_NONINTERACTIVE_VAR_0.operation}: writing without a plan_token requires a one-time interactive project approval, which is not available in non-interactive sessions — use finalize_plan with writes (and deletes if needed), then pass the returned plan_token.
