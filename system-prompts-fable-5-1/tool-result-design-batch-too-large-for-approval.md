<!--
name: 'Tool Result: Design Batch Too Large To Display For Approval'
description: >-
  ClaudeDesign permission-deny message returned to the model when a write batch
  is too large to render for per-batch approval, telling it to split the batch
  or use finalize_plan.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_DESIGN_BATCH_TOO_LARGE_FOR_APPROVAL_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_BATCH_TOO_LARGE_FOR_APPROVAL_VAR_0.operation}: this batch is too large to display fully for approval — split it into smaller batches, or use finalize_plan with writes (and deletes if needed), then pass the returned plan_token.
