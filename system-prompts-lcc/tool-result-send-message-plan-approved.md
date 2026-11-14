<!--
name: 'Tool Result: SendMessage plan approved'
description: >-
  SendMessage result confirming a plan was approved for a teammate who can now
  proceed.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_SEND_MESSAGE_PLAN_APPROVED_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_PLAN_APPROVED_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_PLAN_APPROVED_VAR_2
  - TOOL_RESULT_SEND_MESSAGE_PLAN_APPROVED_VAR_3
-->
Plan approved for ${TOOL_RESULT_SEND_MESSAGE_PLAN_APPROVED_VAR_0}. They will receive the approval and can proceed with implementation.${TOOL_RESULT_SEND_MESSAGE_PLAN_APPROVED_VAR_1===void 0&&TOOL_RESULT_SEND_MESSAGE_PLAN_APPROVED_VAR_2?TOOL_RESULT_SEND_MESSAGE_PLAN_APPROVED_VAR_3:""}
