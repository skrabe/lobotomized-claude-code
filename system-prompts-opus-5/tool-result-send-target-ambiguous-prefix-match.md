<!--
name: 'Tool Result: Send target ambiguous by prefix'
description: >-
  SendMessage refusal headline telling the model that the recipient name
  prefix-matched several agents and it must resend with a specific ref.
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PREFIX_MATCH_VAR_0
  - TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PREFIX_MATCH_VAR_1
-->
'${TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PREFIX_MATCH_VAR_0.to}' matches ${TOOL_RESULT_SEND_TARGET_AMBIGUOUS_PREFIX_MATCH_VAR_1.total} agents by prefix. Re-send with the ref of the one you mean:
