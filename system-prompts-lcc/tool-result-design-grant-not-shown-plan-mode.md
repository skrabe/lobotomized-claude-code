<!--
name: 'Tool Result: Design Project Approval Not Shown In Plan Mode'
description: >-
  ClaudeDesign permission-deny message returned to the model when a tokenless
  write needs a one-time project approval that plan mode will not display.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_DESIGN_GRANT_NOT_SHOWN_PLAN_MODE_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_GRANT_NOT_SHOWN_PLAN_MODE_VAR_0.operation}: writing without a plan_token requires a one-time project approval, which is not shown in plan mode — use finalize_plan with writes (and deletes if needed), then pass the returned plan_token.
