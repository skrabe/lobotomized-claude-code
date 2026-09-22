<!--
name: Computer-use batch action-not-allowed
description: Validation tool-result listing allowed batch actions.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_COMPUTER_USE_BATCH_ACTION_NOT_ALLOWED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_BATCH_ACTION_NOT_ALLOWED_VAR_1
  - TOOL_RESULT_COMPUTER_USE_BATCH_ACTION_NOT_ALLOWED_VAR_2
-->
actions[${TOOL_RESULT_COMPUTER_USE_BATCH_ACTION_NOT_ALLOWED_VAR_0}].action="${TOOL_RESULT_COMPUTER_USE_BATCH_ACTION_NOT_ALLOWED_VAR_1}" is not allowed in a batch. Allowed: ${[...TOOL_RESULT_COMPUTER_USE_BATCH_ACTION_NOT_ALLOWED_VAR_2].join(", ")}.
