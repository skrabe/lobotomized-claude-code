<!--
name: 'Tool Result: MCP first-party auth rejected design-scoped login 403'
description: >-
  Failed MCP client .error when a design-scoped /login that already includes
  Claude Design is still HTTP 403, implicating account/project access.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_MCP_FIRST_PARTY_AUTH_REJECTED_DESIGN_SCOPED_LOGIN_403_VAR_0
-->
${TOOL_RESULT_MCP_FIRST_PARTY_AUTH_REJECTED_DESIGN_SCOPED_LOGIN_403_VAR_0} rejected your claude.ai login for Claude Design (HTTP 403) even though that login already includes Claude Design permissions, so this is most likely an account or project access problem. Check that your account has access to Claude Design; if it does, run /design-login and retry.
