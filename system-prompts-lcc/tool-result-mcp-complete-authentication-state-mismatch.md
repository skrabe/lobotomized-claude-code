<!--
name: 'MCP complete_authentication: state mismatch'
description: >-
  Tool-result error from MCP complete_authentication when the callback URL
  belongs to another OAuth attempt or has no authorization code.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_MCP_COMPLETE_AUTHENTICATION_STATE_MISMATCH_VAR_0
  - TOOL_RESULT_MCP_COMPLETE_AUTHENTICATION_STATE_MISMATCH_VAR_1
-->
That callback URL belongs to a different sign-in attempt for ${TOOL_RESULT_MCP_COMPLETE_AUTHENTICATION_STATE_MISMATCH_VAR_0(TOOL_RESULT_MCP_COMPLETE_AUTHENTICATION_STATE_MISMATCH_VAR_1)} (its state does not match the flow in progress), or carries no authorization code. The current flow is still waiting: ask the user for the URL from the page this sign-in opened, then retry.
