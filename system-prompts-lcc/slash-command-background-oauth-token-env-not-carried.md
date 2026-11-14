<!--
name: 'Slash command: /background OAuth token env not carried'
description: >-
  Error returned when CLAUDE_CODE_OAUTH_TOKEN would not reach a background
  session, so the handoff is refused.
ccVersion: 2.1.325
-->
CLAUDE_CODE_OAUTH_TOKEN wouldn't reach a background session, which would use another sign-in, such as your saved login. Keep working in this terminal, or start Claude Code without that variable: it then uses the profile that ANTHROPIC_PROFILE names, or your saved login if you unset that too
