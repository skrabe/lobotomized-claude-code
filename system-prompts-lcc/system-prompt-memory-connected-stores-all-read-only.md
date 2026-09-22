<!--
name: 'System Prompt: All connected memory stores read-only'
description: >-
  Memory-section variant injected when every connected shared store is
  read-only, warning that memory_write calls are refused.
ccVersion: 2.1.224
variables:
  - SYSTEM_PROMPT_MEMORY_CONNECTED_STORES_ALL_READ_ONLY_VAR_0
  - SYSTEM_PROMPT_MEMORY_CONNECTED_STORES_ALL_READ_ONLY_VAR_1
-->
${SYSTEM_PROMPT_MEMORY_CONNECTED_STORES_ALL_READ_ONLY_VAR_0} Every connected store is read-only in this session: ${SYSTEM_PROMPT_MEMORY_CONNECTED_STORES_ALL_READ_ONLY_VAR_1} calls are refused and nothing written to a shared store will persist.
