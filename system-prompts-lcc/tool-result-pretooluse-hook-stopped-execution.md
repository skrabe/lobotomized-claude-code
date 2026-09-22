<!--
name: PreToolUse Hook Stopped Execution Result
description: >-
  Model-facing error tool_result content emitted when a PreToolUse hook blocks a
  tool call (is_error:true); gated on the hook returning a stop decision.
ccVersion: 2.1.191
variables:
  - TOOL_RESULT_PRETOOLUSE_HOOK_STOPPED_EXECUTION_VAR_0
-->
Execution stopped by PreToolUse hook${TOOL_RESULT_PRETOOLUSE_HOOK_STOPPED_EXECUTION_VAR_0?`: ${TOOL_RESULT_PRETOOLUSE_HOOK_STOPPED_EXECUTION_VAR_0}`:""}
