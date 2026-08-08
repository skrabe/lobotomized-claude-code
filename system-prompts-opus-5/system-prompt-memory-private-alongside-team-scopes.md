<!--
name: 'System Prompt: Private Memory Alongside Writable Team Memory'
description: >-
  Memory system prompt clause splitting memory types between the private
  directory and writable team directories.
ccVersion: 2.1.224
variables:
  - SYSTEM_PROMPT_MEMORY_PRIVATE_ALONGSIDE_TEAM_SCOPES_VAR_0
  - SYSTEM_PROMPT_MEMORY_PRIVATE_ALONGSIDE_TEAM_SCOPES_VAR_1
-->
Your personal memory directory at \`${SYSTEM_PROMPT_MEMORY_PRIVATE_ALONGSIDE_TEAM_SCOPES_VAR_0}\` persists alongside the shared stores and is written with the file tools: save \`user\`-type memories (and anything else private) there, and team-scoped memories to the writable store \`${SYSTEM_PROMPT_MEMORY_PRIVATE_ALONGSIDE_TEAM_SCOPES_VAR_1.id}\`, bearing in mind it is shared with teammates. ${"Your personal memory directory already exists — write to it directly with the Write tool (do not run mkdir or check for its existence)."}
