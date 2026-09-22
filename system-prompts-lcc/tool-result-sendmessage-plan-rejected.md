<!--
name: 'Tool Result: Plan Rejected With Feedback'
description: >-
  Success message returned to the team lead's model after rejecting a teammate's
  plan via the SendMessage tool.
ccVersion: 2.1.214
variables:
  - TOOL_RESULT_SENDMESSAGE_PLAN_REJECTED_VAR_0
  - TOOL_RESULT_SENDMESSAGE_PLAN_REJECTED_VAR_1
  - TOOL_RESULT_SENDMESSAGE_PLAN_REJECTED_VAR_2
-->
Plan rejected for ${TOOL_RESULT_SENDMESSAGE_PLAN_REJECTED_VAR_0} with feedback: "${TOOL_RESULT_SENDMESSAGE_PLAN_REJECTED_VAR_1(TOOL_RESULT_SENDMESSAGE_PLAN_REJECTED_VAR_2,50)}"
