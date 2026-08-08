<!--
name: 'System Prompt: Save team-scoped memories in writable store'
description: >-
  Memory-section line of the system prompt instructing Claude to save new
  team-scoped memories in the writable store and keep its index current.
ccVersion: 2.1.224
variables:
  - SYSTEM_PROMPT_MEMORY_SAVE_TEAM_SCOPED_WRITABLE_STORE_VAR_0
  - SYSTEM_PROMPT_MEMORY_SAVE_TEAM_SCOPED_WRITABLE_STORE_VAR_1
-->
Save new team-scoped memories in the writable store \`${SYSTEM_PROMPT_MEMORY_SAVE_TEAM_SCOPED_WRITABLE_STORE_VAR_0.id}\` under \`${SYSTEM_PROMPT_MEMORY_SAVE_TEAM_SCOPED_WRITABLE_STORE_VAR_0.projectDir}\`, and keep its index \`${SYSTEM_PROMPT_MEMORY_SAVE_TEAM_SCOPED_WRITABLE_STORE_VAR_0.indexPath}\` current — the ${SYSTEM_PROMPT_MEMORY_SAVE_TEAM_SCOPED_WRITABLE_STORE_VAR_1} tool prompt describes the index format.
