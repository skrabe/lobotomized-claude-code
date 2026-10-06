<!--
name: 'Tool result: tool not run because its placement changed after permission check'
description: >-
  Tool-call rejection returned as the tool_result when the machine/session a
  tool runs on changed between its permission check and the call; tells the
  model to send the call again.
ccVersion: 2.1.291
variables:
  - >-
    TOOL_RESULT_TOOL_WRAPPER_NOT_RUN_PLACEMENT_CHANGED_AFTER_PERMISSION_CHECK_VAR_0
-->
${TOOL_RESULT_TOOL_WRAPPER_NOT_RUN_PLACEMENT_CHANGED_AFTER_PERMISSION_CHECK_VAR_0.name} was not run: where it runs changed after its permission was checked. Send the call again.
