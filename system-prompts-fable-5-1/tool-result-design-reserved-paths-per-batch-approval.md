<!--
name: 'Tool Result: Design Batch Includes Reserved Paths'
description: >-
  ClaudeDesign permission-deny message returned to the model when a batch
  touches paths that always require per-batch approval, directing it to
  finalize_plan with writes/deletes.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_DESIGN_RESERVED_PATHS_PER_BATCH_APPROVAL_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_RESERVED_PATHS_PER_BATCH_APPROVAL_VAR_0.operation}: this batch includes paths that always require per-batch approval — use finalize_plan with writes/deletes and pass the returned plan_token.
