<!--
name: 'MCP authenticate: remote-session suffix'
description: >-
  Suffix on the MCP authenticate tool result explaining the remote-session
  paste-callback-URL flow.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_MCP_AUTHENTICATE_REMOTE_SUFFIX_VAR_0
  - TOOL_RESULT_MCP_AUTHENTICATE_REMOTE_SUFFIX_VAR_1
-->


This session is remote, so after authorizing the browser will try to load \`${TOOL_RESULT_MCP_AUTHENTICATE_REMOTE_SUFFIX_VAR_0}?code=...\` and show a connection error — that's expected. Ask the user to copy the full URL from the browser's address bar and paste it into chat, then call \`${TOOL_RESULT_MCP_AUTHENTICATE_REMOTE_SUFFIX_VAR_1}\` with that URL as \`callback_url\`.
