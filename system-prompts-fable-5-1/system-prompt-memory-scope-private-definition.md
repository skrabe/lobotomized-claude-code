<!--
name: 'System Prompt: Memory Scope Private Definition'
description: >-
  Memory-scope fragment defining private memories (persist per-user, stored at
  the root path).
ccVersion: 2.1.178
variables:
  - SYSTEM_PROMPT_MEMORY_SCOPE_PRIVATE_DEFINITION_VAR_0
-->
- private: memories shared only between you and the current user, persisting across conversations with this user, stored at the root \`${SYSTEM_PROMPT_MEMORY_SCOPE_PRIVATE_DEFINITION_VAR_0}\`.
