<!--
name: 'Tool result: remote tool permission rule check failed'
description: >-
  Permission deny message returned when the attached machine could not finish
  checking its permission rules for a call, telling the model to report it as an
  error rather than a refusal.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_REMOTE_TOOL_PERMISSION_RULES_CHECK_FAILED_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_PERMISSION_RULES_CHECK_FAILED_VAR_1
-->
${TOOL_RESULT_REMOTE_TOOL_PERMISSION_RULES_CHECK_FAILED_VAR_0} could not finish checking its permission rules for this ${TOOL_RESULT_REMOTE_TOOL_PERMISSION_RULES_CHECK_FAILED_VAR_1} call, so the call was not run and nobody was asked. Sending the same call again is unlikely to help. Tell the user: this is an error on ${TOOL_RESULT_REMOTE_TOOL_PERMISSION_RULES_CHECK_FAILED_VAR_0}, not a refusal by one of its rules.
