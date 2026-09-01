<!--
name: 'System Prompt: Team Memory Index File Reference'
description: >-
  Reference to the index file in the team memory directory, used in the
  write-a-memory instructions to point at where the per-memory pointer line
  goes.
ccVersion: 2.1.218
variables:
  - SYSTEM_PROMPT_MEMORY_TEAM_INDEX_FILE_REF_VAR_0
  - SYSTEM_PROMPT_MEMORY_TEAM_INDEX_FILE_REF_VAR_1
  - SYSTEM_PROMPT_MEMORY_TEAM_INDEX_FILE_REF_VAR_2
-->
the index file in that same directory (${SYSTEM_PROMPT_MEMORY_TEAM_INDEX_FILE_REF_VAR_0.map((SYSTEM_PROMPT_MEMORY_TEAM_INDEX_FILE_REF_VAR_1)=>`\`${SYSTEM_PROMPT_MEMORY_TEAM_INDEX_FILE_REF_VAR_2(SYSTEM_PROMPT_MEMORY_TEAM_INDEX_FILE_REF_VAR_1)}\``).join(", ")})
