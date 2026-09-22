<!--
name: 'Memory: index truncation warning'
description: >-
  Memory system prompt bullet warning the index is loaded into context and
  truncated after a limit.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_MEMORY_INDEX_TRUNCATION_VAR_0
  - SYSTEM_PROMPT_MEMORY_INDEX_TRUNCATION_VAR_1
-->
- \`${SYSTEM_PROMPT_MEMORY_INDEX_TRUNCATION_VAR_0}\` is loaded into your conversation context — lines after ${SYSTEM_PROMPT_MEMORY_INDEX_TRUNCATION_VAR_1} will be truncated, so keep the index concise
