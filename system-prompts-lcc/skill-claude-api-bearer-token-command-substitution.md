<!--
name: 'Skill: Claude API bearer token via command substitution'
description: >-
  Claude API skill line sending the ant access token inline via $(...) or
  ANTHROPIC_AUTH_TOKEN as the Authorization bearer
ccVersion: 2.1.319
-->
send `Authorization: Bearer $(ant auth print-credentials --access-token)` (short-lived, and never printed this way; if the active row is `ANTHROPIC_AUTH_TOKEN`, send `$ANTHROPIC_AUTH_TOKEN`) **plus**
