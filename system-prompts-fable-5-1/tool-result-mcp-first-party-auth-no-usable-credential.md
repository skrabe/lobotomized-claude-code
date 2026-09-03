<!--
name: 'Tool Result: MCP first-party auth no usable credential'
description: >-
  Failed MCP client .error when first-party auth has no usable claude.ai
  credential and /login or /design-login is required.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_MCP_FIRST_PARTY_AUTH_NO_USABLE_CREDENTIAL_VAR_0
  - TOOL_RESULT_MCP_FIRST_PARTY_AUTH_NO_USABLE_CREDENTIAL_VAR_1
  - TOOL_RESULT_MCP_FIRST_PARTY_AUTH_NO_USABLE_CREDENTIAL_VAR_2
-->
${TOOL_RESULT_MCP_FIRST_PARTY_AUTH_NO_USABLE_CREDENTIAL_VAR_0} needs a claude.ai sign-in and Claude Code had no usable credential to send (${TOOL_RESULT_MCP_FIRST_PARTY_AUTH_NO_USABLE_CREDENTIAL_VAR_1}). Run ${TOOL_RESULT_MCP_FIRST_PARTY_AUTH_NO_USABLE_CREDENTIAL_VAR_2?"/design-login":"/login"} and retry.
