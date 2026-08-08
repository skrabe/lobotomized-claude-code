<!--
name: 'System Prompt: Memory store index pointer instructions'
description: >-
  Step-2 of the "How to save memories" section used when memories live in a
  memory-service store: tells the model to add a one-line pointer to the store's
  index document via memory_write.
ccVersion: 2.1.224
variables:
  - SYSTEM_PROMPT_MEMORY_STORE_INDEX_POINTER_INSTRUCTIONS_VAR_0
  - SYSTEM_PROMPT_MEMORY_STORE_INDEX_POINTER_INSTRUCTIONS_VAR_1
  - SYSTEM_PROMPT_MEMORY_STORE_INDEX_POINTER_INSTRUCTIONS_VAR_2
-->
**Step 2** — add a pointer to that document in the store's index document with ${SYSTEM_PROMPT_MEMORY_STORE_INDEX_POINTER_INSTRUCTIONS_VAR_0}. Each entry should be one line, under ~150 characters: \`- [Title](file.md) — one-line hook\`. The index has no frontmatter. Never write memory content directly into the index.
