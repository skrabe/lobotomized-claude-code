<!--
name: 'Memory: appropriate team directory reference'
description: >-
  Memory system prompt fragment naming the appropriate team directory to write
  to.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_MEMORY_TEAM_DIRECTORY_REF_VAR_0
  - SYSTEM_PROMPT_MEMORY_TEAM_DIRECTORY_REF_VAR_1
-->
the appropriate team directory (${SYSTEM_PROMPT_MEMORY_TEAM_DIRECTORY_REF_VAR_0.map((SYSTEM_PROMPT_MEMORY_TEAM_DIRECTORY_REF_VAR_1)=>`\`${SYSTEM_PROMPT_MEMORY_TEAM_DIRECTORY_REF_VAR_1}\``).join(" or ")})
