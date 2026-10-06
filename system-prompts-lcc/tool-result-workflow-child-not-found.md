<!--
name: 'Tool Result: workflow() child name not found'
description: >-
  Error thrown into a workflow script when workflow('<name>') names no known
  workflow, listing the available ones; reaches the model as the workflow's
  failure report.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WORKFLOW_CHILD_NOT_FOUND_VAR_0
  - TOOL_RESULT_WORKFLOW_CHILD_NOT_FOUND_VAR_1
-->
workflow('${TOOL_RESULT_WORKFLOW_CHILD_NOT_FOUND_VAR_0}'): no workflow with that name. Available: ${TOOL_RESULT_WORKFLOW_CHILD_NOT_FOUND_VAR_1||"(none)"}
