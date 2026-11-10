<!--
name: 'Tool Result: MCP OAuth redirect guard (too many redirects)'
description: >-
  Error thrown when an MCP OAuth request is redirected too many times; reaches
  the model inside the MCP authenticate tool's 'Failed to start OAuth flow'
  result.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_TOO_MANY_REDIRECTS_VAR_0
  - TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_TOO_MANY_REDIRECTS_VAR_1
  - TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_TOO_MANY_REDIRECTS_VAR_2
-->
Stopped an OAuth request: ${TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_TOO_MANY_REDIRECTS_VAR_0(TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_TOO_MANY_REDIRECTS_VAR_1)} redirected it more than ${TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_TOO_MANY_REDIRECTS_VAR_2} times. Ask the owner of ${TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_TOO_MANY_REDIRECTS_VAR_0(TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_TOO_MANY_REDIRECTS_VAR_1)} to fix those redirects.
