<!--
name: 'Tool Result: Design Project Cannot Hold Durable Write Grant'
description: >-
  ClaudeDesign permission-deny message returned to the model when the target
  project_id is ineligible for a durable write grant (e.g. shared from another
  org), routing it to finalize_plan.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_DESIGN_PROJECT_GRANT_INELIGIBLE_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_PROJECT_GRANT_INELIGIBLE_VAR_0.operation}: this project cannot hold a durable write grant for this account (it may be shared from another organization) — use finalize_plan with writes (and deletes if needed), then pass the returned plan_token.
