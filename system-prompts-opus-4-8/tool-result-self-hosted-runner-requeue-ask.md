<!--
name: 'Tool Result: Requeue runner session ask message'
description: >-
  The requeue tool's ask-permission message; the TUI dialog never renders
  permissionResult.message (it renders the tool description and decisionReason),
  so this text only ever reaches the model as the tool_result when the ask goes
  unresolved.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SELF_HOSTED_RUNNER_REQUEUE_ASK_VAR_0
-->
Requeue session ${TOOL_RESULT_SELF_HOSTED_RUNNER_REQUEUE_ASK_VAR_0.session_id} off runner ${TOOL_RESULT_SELF_HOSTED_RUNNER_REQUEUE_ASK_VAR_0.runner_id}?
