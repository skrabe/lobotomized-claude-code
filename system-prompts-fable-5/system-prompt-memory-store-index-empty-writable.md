<!--
name: 'System Prompt: Empty writable memory-store index'
description: >-
  Memory system-prompt line injected when a connected writable memory store has
  an empty prompt index, telling Claude to create the index with memory_write.
ccVersion: 2.1.224
variables:
  - SYSTEM_PROMPT_MEMORY_STORE_INDEX_EMPTY_WRITABLE_VAR_0
  - SYSTEM_PROMPT_MEMORY_STORE_INDEX_EMPTY_WRITABLE_VAR_1
-->
You have a memory index \`/${SYSTEM_PROMPT_MEMORY_STORE_INDEX_EMPTY_WRITABLE_VAR_0}\` in ${SYSTEM_PROMPT_MEMORY_STORE_INDEX_EMPTY_WRITABLE_VAR_1} (currently empty).
