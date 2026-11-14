<!--
name: 'Data: API error claude.ai login expired, fallback has no credit'
description: >-
  Authentication API-error message saying the claude.ai login expired and the
  fallback credential lacks credit, with sign-in and add-funds remedies.
ccVersion: 2.1.325
variables:
  - DATA_API_ERROR_CLAUDE_AI_LOGIN_EXPIRED_FALLBACK_NO_CREDIT_VAR_0
  - DATA_API_ERROR_CLAUDE_AI_LOGIN_EXPIRED_FALLBACK_NO_CREDIT_VAR_1
-->
Failed to authenticate: your claude.ai login expired. Claude Code tried ${DATA_API_ERROR_CLAUDE_AI_LOGIN_EXPIRED_FALLBACK_NO_CREDIT_VAR_0} instead, but it doesn't have enough credit. Run \`claude auth login\` to sign in again, or add funds: ${DATA_API_ERROR_CLAUDE_AI_LOGIN_EXPIRED_FALLBACK_NO_CREDIT_VAR_1}
