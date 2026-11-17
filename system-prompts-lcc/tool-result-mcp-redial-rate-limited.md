<!--
name: 'MCP redial: rate limited'
description: >-
  Redial note that the server answered 429; continue without it and tell the
  user if the task depends on it.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_REDIAL_RATE_LIMITED_VAR_0
-->
Claude Code tried to connect to ${TOOL_RESULT_MCP_REDIAL_RATE_LIMITED_VAR_0} again, and it answered that it gets too many requests (429). A call or search does not try it again. Continue without this server, and tell the user if the task depends on it.
