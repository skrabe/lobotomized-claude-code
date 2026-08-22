<!--
name: 'Tool Result: Design Project Approval Blocked By Permission Mode'
description: >-
  ClaudeDesign permission-deny message returned to the model when a tokenless
  write to an ungranted project needs an interactive approval the current
  permission mode cannot show.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_DESIGN_GRANT_NOT_SHOWN_PERMISSION_MODE_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_GRANT_NOT_SHOWN_PERMISSION_MODE_VAR_0.operation}: writing without a plan_token to a project without a write grant requires a one-time interactive approval, which cannot be shown in this permission mode — use finalize_plan with writes (and deletes if needed), then pass the returned plan_token.
