<!--
name: 'Tool Result: Workflow Script Determinism Error'
description: >-
  Validation error returned to the model: workflow scripts must be deterministic
  (no Date.now/Math.random/new Date); stamp results after return or pass
  timestamps via args.
ccVersion: 2.1.251
-->
Workflow scripts must be deterministic: Date.now()/Math.random()/new Date() are unavailable (breaks resume). Stamp results after the workflow returns, or pass timestamps via args.${TOOL_RESULT_WORKFLOW_SCRIPT_DETERMINISM_ERROR_VAR_0(TOOL_RESULT_WORKFLOW_SCRIPT_DETERMINISM_ERROR_VAR_1,TOOL_RESULT_WORKFLOW_SCRIPT_DETERMINISM_ERROR_VAR_2.options.tools)}
