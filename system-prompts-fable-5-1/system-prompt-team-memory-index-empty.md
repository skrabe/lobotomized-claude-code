<!--
name: 'System Prompt: Team Memory Index (empty)'
description: >-
  Memory instruction for an empty team memory index, telling the model to write
  files under team/ and add pointer lines.
ccVersion: 2.1.218
variables:
  - SYSTEM_PROMPT_TEAM_MEMORY_INDEX_EMPTY_VAR_0
  - SYSTEM_PROMPT_TEAM_MEMORY_INDEX_EMPTY_VAR_1
  - SYSTEM_PROMPT_TEAM_MEMORY_INDEX_EMPTY_VAR_2
  - SYSTEM_PROMPT_TEAM_MEMORY_INDEX_EMPTY_VAR_3
-->
Team memory index: \`${SYSTEM_PROMPT_TEAM_MEMORY_INDEX_EMPTY_VAR_0}\` (currently empty). To persist something, write it under \`team/${SYSTEM_PROMPT_TEAM_MEMORY_INDEX_EMPTY_VAR_1}/\` and add a one-line pointer to \`${SYSTEM_PROMPT_TEAM_MEMORY_INDEX_EMPTY_VAR_0}\`.
