<!--
name: Design write op unvalidatable
description: >-
  ClaudeDesign tool-error returned to the model when a write-capable op lacks a
  client schema.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_DESIGN_OP_WRITE_UNVALIDATABLE_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_OP_WRITE_UNVALIDATABLE_VAR_0}: the server reports this operation as write-capable, and this client version can't validate its arguments (it needs a WRITE_OP_SCHEMAS entry). Update Claude Code to use it.
