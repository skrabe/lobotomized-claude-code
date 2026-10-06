<!--
name: 'Tool Result: workflow token budget exceeded'
description: >-
  Error thrown into a workflow script when its output-token budget is exhausted,
  stopping further agent() calls while in-flight agents finish.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WORKFLOW_TOKEN_BUDGET_EXCEEDED_VAR_0
  - TOOL_RESULT_WORKFLOW_TOKEN_BUDGET_EXCEEDED_VAR_1
-->
Workflow token budget exceeded (${TOOL_RESULT_WORKFLOW_TOKEN_BUDGET_EXCEEDED_VAR_0.toLocaleString()} / ${TOOL_RESULT_WORKFLOW_TOKEN_BUDGET_EXCEEDED_VAR_1.toLocaleString()} output tokens). Stopping further agent() calls. In-flight agents will complete; their results are preserved.
