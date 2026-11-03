<!--
name: 'Tool Result: ExitPlanMode Doc plan takes no argument'
description: >-
  Validation error when ExitPlanMode is called with arguments while the
  session's plan is a Claude Doc: edit the Doc, then call with no argument
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EXITPLANMODE_DOC_PLAN_CALL_WITHOUT_ARGUMENT_VAR_0
  - TOOL_RESULT_EXITPLANMODE_DOC_PLAN_CALL_WITHOUT_ARGUMENT_VAR_1
-->
This session's plan is ${TOOL_RESULT_EXITPLANMODE_DOC_PLAN_CALL_WITHOUT_ARGUMENT_VAR_0(TOOL_RESULT_EXITPLANMODE_DOC_PLAN_CALL_WITHOUT_ARGUMENT_VAR_1)}, and the user approves the Doc as it stands. Put any change into the Doc, then call this tool with no argument.
