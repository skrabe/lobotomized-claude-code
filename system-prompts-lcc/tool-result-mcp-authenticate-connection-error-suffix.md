<!--
name: 'MCP authenticate: connection-error suffix'
description: >-
  Suffix on the MCP authenticate tool result explaining what to do if the
  redirect page errors.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_MCP_AUTHENTICATE_CONNECTION_ERROR_SUFFIX_VAR_0
-->


If the browser shows a connection error on the redirect page, ask the user to paste the full URL from the address bar and call \`${TOOL_RESULT_MCP_AUTHENTICATE_CONNECTION_ERROR_SUFFIX_VAR_0}\` with it.
