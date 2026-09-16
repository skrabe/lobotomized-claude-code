<!--
name: 'Slash Command: Code Review Fallback Unix Socket Without OAuth'
description: >-
  Gun() clause that ANTHROPIC_UNIX_SOCKET is set without
  CLAUDE_CODE_OAUTH_TOKEN, interpolated into the catalogued /code-review ultra
  fallback notice the model reads.
ccVersion: 2.1.273
variables:
  - SLASH_COMMAND_CODE_REVIEW_FALLBACK_UNIX_SOCKET_WITHOUT_OAUTH_VAR_0
-->
${SLASH_COMMAND_CODE_REVIEW_FALLBACK_UNIX_SOCKET_WITHOUT_OAUTH_VAR_0} ANTHROPIC_UNIX_SOCKET is set without CLAUDE_CODE_OAUTH_TOKEN, so requests on the socket carry no claude.ai login (on a claude ssh remote: the local machine is API-key-authed).
