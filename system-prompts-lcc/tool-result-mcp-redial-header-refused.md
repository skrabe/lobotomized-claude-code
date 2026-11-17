<!--
name: 'MCP redial: configured credential rejected'
description: >-
  Redial note that the server rejected its configured header/headersHelper
  credential; continue without it and tell the user if needed.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_REDIAL_HEADER_REFUSED_VAR_0
-->
Claude Code connected to ${TOOL_RESULT_MCP_REDIAL_HEADER_REFUSED_VAR_0} again, and it rejected the credential in its configuration (a header or headersHelper). The user needs to update it. Continue without this server, and tell them if the task depends on it.
