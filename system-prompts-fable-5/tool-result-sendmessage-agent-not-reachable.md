<!--
name: 'SendMessage Result: No Such Agent'
description: >-
  `{data:{success:false,message:…}}` returned from SendMessage's `call` for the
  not-found resolution kind; its mapToolResultToToolResultBlockParam serializes
  data into a `{type:"text"}` tool_result block for the model, with spelling
  hints and near-miss suggestions.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SENDMESSAGE_AGENT_NOT_REACHABLE_VAR_0
  - TOOL_RESULT_SENDMESSAGE_AGENT_NOT_REACHABLE_VAR_1
  - TOOL_RESULT_SENDMESSAGE_AGENT_NOT_REACHABLE_VAR_2
  - TOOL_RESULT_SENDMESSAGE_AGENT_NOT_REACHABLE_VAR_3
-->

No agent named '${TOOL_RESULT_SENDMESSAGE_AGENT_NOT_REACHABLE_VAR_0.to}' is reachable.${TOOL_RESULT_SENDMESSAGE_AGENT_NOT_REACHABLE_VAR_1}${TOOL_RESULT_SENDMESSAGE_AGENT_NOT_REACHABLE_VAR_2}
${TOOL_RESULT_SENDMESSAGE_AGENT_NOT_REACHABLE_VAR_3}
