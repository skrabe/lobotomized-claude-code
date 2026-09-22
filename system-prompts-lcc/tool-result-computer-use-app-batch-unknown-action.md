<!--
name: Computer-use App Batch Unknown Action
description: >-
  app_batch validation tool_result when actions[i].action is not one of the
  allowed kinds.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_APP_BATCH_UNKNOWN_ACTION_VAR_0
  - TOOL_RESULT_COMPUTER_USE_APP_BATCH_UNKNOWN_ACTION_VAR_1
-->
actions[${TOOL_RESULT_COMPUTER_USE_APP_BATCH_UNKNOWN_ACTION_VAR_0}].action must be one of: ${[...TOOL_RESULT_COMPUTER_USE_APP_BATCH_UNKNOWN_ACTION_VAR_1].join(", ")}.
