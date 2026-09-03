<!--
name: 'Slash Command: /mcp — Disable Did Not Persist'
description: >-
  Sanitized /mcp disable result when another session re-enabled the server so
  this disable did not stick; the next launch will reconnect it.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_MCP_DISABLE_DID_NOT_PERSIST_VAR_0
-->
"${SLASH_COMMAND_MCP_DISABLE_DID_NOT_PERSIST_VAR_0}" was re-enabled in another session, so this disable didn't persist. Left alone, it connects on the next launch.
