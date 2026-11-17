<!--
name: 'MCP redial: user needs to sign in'
description: >-
  Tail appended to sign-in redial notes saying the user must sign in (naming the
  auth tool) and to continue without the server.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_REDIAL_USER_NEEDS_SIGN_IN_VAR_0
  - TOOL_RESULT_MCP_REDIAL_USER_NEEDS_SIGN_IN_VAR_1
-->
The user needs to sign in${TOOL_RESULT_MCP_REDIAL_USER_NEEDS_SIGN_IN_VAR_0?` (${TOOL_RESULT_MCP_REDIAL_USER_NEEDS_SIGN_IN_VAR_1(TOOL_RESULT_MCP_REDIAL_USER_NEEDS_SIGN_IN_VAR_0.name)} starts that)`:""}. Continue without this server, and tell them if the task depends on it.
