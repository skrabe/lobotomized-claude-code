<!--
name: 'Tool Result: Send target ambiguous, same name'
description: >-
  SendMessage refusal headline telling the model that several agents share the
  given name exactly and it must resend with a specific ref.
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_SEND_TARGET_AMBIGUOUS_SAME_NAME_VAR_0
  - TOOL_RESULT_SEND_TARGET_AMBIGUOUS_SAME_NAME_VAR_1
-->
${TOOL_RESULT_SEND_TARGET_AMBIGUOUS_SAME_NAME_VAR_0.total} agents are named '${TOOL_RESULT_SEND_TARGET_AMBIGUOUS_SAME_NAME_VAR_1.to}'. Re-send with the ref of the one you mean:
