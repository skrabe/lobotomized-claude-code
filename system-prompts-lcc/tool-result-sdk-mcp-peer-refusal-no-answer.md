<!--
name: 'Tool Result: SDK MCP peer refusal with no other answer'
description: >-
  Error for an SDK MCP server call that a client refused while no other attached
  client answered within the grace period, so the call was cancelled
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_SDK_MCP_PEER_REFUSAL_NO_ANSWER_VAR_0
  - TOOL_RESULT_SDK_MCP_PEER_REFUSAL_NO_ANSWER_VAR_1
-->
${TOOL_RESULT_SDK_MCP_PEER_REFUSAL_NO_ANSWER_VAR_0} (and no other answer came within ${(TOOL_RESULT_SDK_MCP_PEER_REFUSAL_NO_ANSWER_VAR_1.peerRefusalGraceMs??0)/1000} s, so the call was cancelled)
