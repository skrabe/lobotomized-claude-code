<!--
name: 'Tool Result: MCP Authenticate Sign-In Already In Progress'
description: >-
  MCP authenticate tool result lead when an earlier sign-in is still in
  progress, so the link shown is that sign-in's; if the user saw an error page,
  ask them to sign in via /mcp instead.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_MCP_AUTHENTICATE_SIGN_IN_ALREADY_IN_PROGRESS_VAR_0
  - TOOL_RESULT_MCP_AUTHENTICATE_SIGN_IN_ALREADY_IN_PROGRESS_VAR_1
-->
A sign-in for ${TOOL_RESULT_MCP_AUTHENTICATE_SIGN_IN_ALREADY_IN_PROGRESS_VAR_0(TOOL_RESULT_MCP_AUTHENTICATE_SIGN_IN_ALREADY_IN_PROGRESS_VAR_1)} that started earlier is still in progress, so the link below is that sign-in's link, not a new one. If the user says the sign-in page showed an error before they could approve access, ask them to run /mcp and sign in there instead.

