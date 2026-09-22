<!--
name: 'Workflow tool result: syntax error'
description: >-
  tool_result content (is_error) returned to the model when a workflow script
  has a syntax error and was not launched; model-facing.
ccVersion: 2.1.191
variables:
  - TOOL_RESULT_WORKFLOW_SYNTAX_ERROR_VAR_0
-->
Workflow script has a syntax error and was not launched:
${TOOL_RESULT_WORKFLOW_SYNTAX_ERROR_VAR_0.error}
