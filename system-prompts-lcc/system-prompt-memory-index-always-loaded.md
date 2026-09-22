<!--
name: 'Memory: index always loaded'
description: >-
  Memory system prompt bullet noting the index is always loaded into context and
  truncated after a limit.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_MEMORY_INDEX_ALWAYS_LOADED_VAR_0
  - SYSTEM_PROMPT_MEMORY_INDEX_ALWAYS_LOADED_VAR_1
-->
- \`${SYSTEM_PROMPT_MEMORY_INDEX_ALWAYS_LOADED_VAR_0}\` is always loaded into your conversation context — lines after ${SYSTEM_PROMPT_MEMORY_INDEX_ALWAYS_LOADED_VAR_1} will be truncated, so keep the index concise
