<!--
name: registerTool name invalid
description: >-
  REPL registerTool error surfaced to the model when a tool name fails the
  allowed pattern.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_REGISTERTOOL_NAME_INVALID_VAR_0
  - TOOL_RESULT_REGISTERTOOL_NAME_INVALID_VAR_1
-->
registerTool: name must match ^[a-zA-Z0-9_-]{1,111}$ (wire name is prefixed with 'eval_registered__'), got ${typeof TOOL_RESULT_REGISTERTOOL_NAME_INVALID_VAR_0}: ${TOOL_RESULT_REGISTERTOOL_NAME_INVALID_VAR_1.toStr(TOOL_RESULT_REGISTERTOOL_NAME_INVALID_VAR_0).slice(0,50)}
