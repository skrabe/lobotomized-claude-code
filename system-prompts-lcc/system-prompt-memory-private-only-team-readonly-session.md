<!--
name: 'System Prompt: Private Memory Only (Team Read-Only)'
description: >-
  Memory system prompt clause used when team memory is read-only, directing
  every memory type to the private directory for this session.
ccVersion: 2.1.224
variables:
  - SYSTEM_PROMPT_MEMORY_PRIVATE_ONLY_TEAM_READONLY_SESSION_VAR_0
-->
Save every memory type in your personal memory directory at \`${SYSTEM_PROMPT_MEMORY_PRIVATE_ONLY_TEAM_READONLY_SESSION_VAR_0}\` with the file tools this session — the shared stores are read-only, so team-scoped memories also belong there for now. ${"Your personal memory directory already exists — write to it directly with the Write tool (do not run mkdir or check for its existence)."}
