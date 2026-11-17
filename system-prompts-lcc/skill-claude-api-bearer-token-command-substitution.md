<!--
name: 'Skill: Claude API bearer token command substitution'
description: >-
  Tells raw curl/HTTP calls to send a Bearer token via ant auth
  print-credentials command substitution, or $ANTHROPIC_AUTH_TOKEN
ccVersion: 2.1.326
-->
**Raw `curl` / HTTP (`Profile` or `ANTHROPIC_AUTH_TOKEN` row):** send `Authorization: Bearer $(ant auth print-credentials --access-token)` (short-lived, and never printed this way; on an `ANTHROPIC_AUTH_TOKEN` row, send `$ANTHROPIC_AUTH_TOKEN`) **plus**
