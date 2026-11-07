<!--
name: 'Skill: Claude API never handle credentials in chat'
description: >-
  Claude API skill bullet forbidding taking codes, keys or tokens through chat
  or printing stored credentials, with safe token usage
ccVersion: 2.1.319
-->
- **Never** take a login code, a key or a token through this chat. Never open, print or copy anything in the sign-in store's `credentials/` folder, or run `ant auth print-credentials` with no flag (that prints the refresh token); use `--access-token` or `--env` only inside `$(...)` in the command that needs it, never into a file. `ant auth status` already gives the account, expiry and scopes.
