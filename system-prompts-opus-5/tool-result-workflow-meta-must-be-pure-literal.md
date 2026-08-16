<!--
name: 'Tool Result: Workflow meta must be a pure literal'
description: >-
  Tells the model the exported meta object may not contain computed expressions,
  which is the constraint it has to satisfy on the next attempt.
ccVersion: 2.1.233
variables:
  - TOOL_RESULT_WORKFLOW_META_MUST_BE_PURE_LITERAL_VAR_0
  - TOOL_RESULT_WORKFLOW_META_MUST_BE_PURE_LITERAL_VAR_1
  - TOOL_RESULT_WORKFLOW_META_MUST_BE_PURE_LITERAL_VAR_2
-->
meta must be a pure literal: ${TOOL_RESULT_WORKFLOW_META_MUST_BE_PURE_LITERAL_VAR_0 instanceof TOOL_RESULT_WORKFLOW_META_MUST_BE_PURE_LITERAL_VAR_1?TOOL_RESULT_WORKFLOW_META_MUST_BE_PURE_LITERAL_VAR_0.message:TOOL_RESULT_WORKFLOW_META_MUST_BE_PURE_LITERAL_VAR_2(TOOL_RESULT_WORKFLOW_META_MUST_BE_PURE_LITERAL_VAR_0)}
