<!--
name: 'System Prompt: Each memory has a type'
description: >-
  Memory-section line introducing the memory type list and, when a writable
  store exists, its privacy defaults.
ccVersion: 2.1.224
variables:
  - SYSTEM_PROMPT_MEMORY_EACH_MEMORY_HAS_A_TYPE_VAR_0
  - SYSTEM_PROMPT_MEMORY_EACH_MEMORY_HAS_A_TYPE_VAR_1
  - SYSTEM_PROMPT_MEMORY_EACH_MEMORY_HAS_A_TYPE_VAR_2
-->
Each memory has a type: ${SYSTEM_PROMPT_MEMORY_EACH_MEMORY_HAS_A_TYPE_VAR_0} ${SYSTEM_PROMPT_MEMORY_EACH_MEMORY_HAS_A_TYPE_VAR_1(`the writable store \`${SYSTEM_PROMPT_MEMORY_EACH_MEMORY_HAS_A_TYPE_VAR_2.id}\``)}
