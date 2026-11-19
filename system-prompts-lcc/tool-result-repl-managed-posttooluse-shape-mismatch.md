<!--
name: 'Tool Result: REPL managed PostToolUse shape mismatch'
description: >-
  REPL inner call error when a managed PostToolUse hook rewrote a result that
  doesn't match the output schema
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_REPL_MANAGED_POSTTOOLUSE_SHAPE_MISMATCH_VAR_0
  - TOOL_RESULT_REPL_MANAGED_POSTTOOLUSE_SHAPE_MISMATCH_VAR_1
-->
a managed PostToolUse hook rewrote ${TOOL_RESULT_REPL_MANAGED_POSTTOOLUSE_SHAPE_MISMATCH_VAR_0.name} with a result that does not match its output shape: ${TOOL_RESULT_REPL_MANAGED_POSTTOOLUSE_SHAPE_MISMATCH_VAR_1.error.message}
