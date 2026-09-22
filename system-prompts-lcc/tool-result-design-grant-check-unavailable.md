<!--
name: 'Tool Result: Design Write-Grant Check Unavailable'
description: >-
  ClaudeDesign permission-deny message returned to the model when the server
  cannot be probed for a durable project write grant, telling it to use
  finalize_plan instead.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_DESIGN_GRANT_CHECK_UNAVAILABLE_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_GRANT_CHECK_UNAVAILABLE_VAR_0.operation}: could not check for a project write grant (this server may not support durable grants) — use finalize_plan with writes (and deletes if needed), then pass the returned plan_token.
