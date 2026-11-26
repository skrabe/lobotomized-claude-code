<!--
name: 'Hook deny: answer cannot be kept inside a batch'
description: >-
  Deny reason when a hook's answer for a tool cannot be applied inside a batch;
  asks to call the tool on its own.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_HOOK_ANSWER_NOT_KEPT_IN_BATCH_VAR_0
-->
A hook's answer for ${TOOL_RESULT_HOOK_ANSWER_NOT_KEPT_IN_BATCH_VAR_0.tool_name} cannot be kept inside a batch. No action ran. Call ${TOOL_RESULT_HOOK_ANSWER_NOT_KEPT_IN_BATCH_VAR_0.tool_name} on its own.
