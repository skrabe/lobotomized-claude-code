<!--
name: 'System Prompt: Browser extension not connected (account mismatch)'
description: >-
  Tool_result returned on browser disconnect explaining the OAuth token belongs
  to a different claude.ai account, with remediation steps
ccVersion: 2.1.178
variables:
  - SYSTEM_PROMPT_BROWSER_EXTENSION_NOT_CONNECTED_ACCOUNT_MISMATCH_VAR_0
-->
Browser extension is not connected: the OAuth token Claude Code is using belongs to a different claude.ai account than the one Claude Code is logged in as. If CLAUDE_CODE_OAUTH_TOKEN is set in your shell or CI profile, unset it (or re-mint it for this account), then run /logout and /login in Claude Code and make sure the browser extension is signed into the same claude.ai account. If you continue to experience issues, please report a bug: ${SYSTEM_PROMPT_BROWSER_EXTENSION_NOT_CONNECTED_ACCOUNT_MISMATCH_VAR_0}
