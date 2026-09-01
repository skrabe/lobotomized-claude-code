<!--
name: 'Tool Result: Design Call Names No Target Paths'
description: >-
  ClaudeDesign permission-deny message returned to the model when a write batch
  declares an empty targets list, asking it to list files to write or use
  finalize_plan.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_DESIGN_NO_TARGET_PATHS_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_NO_TARGET_PATHS_VAR_0.operation}: this call names no target paths — list the files to write, or use finalize_plan with writes (and deletes if needed), then pass the returned plan_token.
