<!--
name: 'REPL: Hook Result Shape Mismatch'
description: >-
  Refusal when a managed PostToolUse hook or tool.call step produced a result
  that does not match the tool's output schema.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_HOOK_RESULT_SHAPE_MISMATCH_VAR_0
  - TOOL_RESULT_REPL_HOOK_RESULT_SHAPE_MISMATCH_VAR_1
  - TOOL_RESULT_REPL_HOOK_RESULT_SHAPE_MISMATCH_VAR_2
-->
${TOOL_RESULT_REPL_HOOK_RESULT_SHAPE_MISMATCH_VAR_0.rewritten?"a managed PostToolUse hook rewrote":"tool.call step resolved"} ${TOOL_RESULT_REPL_HOOK_RESULT_SHAPE_MISMATCH_VAR_1.name} with a result that does not match its output shape: ${TOOL_RESULT_REPL_HOOK_RESULT_SHAPE_MISMATCH_VAR_2.error.message}
