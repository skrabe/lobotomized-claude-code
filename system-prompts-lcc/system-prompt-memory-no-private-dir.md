<!--
name: 'Memory: no private directory this session'
description: >-
  Memory system prompt line for the team-only variant noting there is no private
  directory.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_MEMORY_NO_PRIVATE_DIR_VAR_0
  - SYSTEM_PROMPT_MEMORY_NO_PRIVATE_DIR_VAR_1
-->
There is no separate private memory directory in this session. Save every memory type to ${SYSTEM_PROMPT_MEMORY_NO_PRIVATE_DIR_VAR_0?`\`${SYSTEM_PROMPT_MEMORY_NO_PRIVATE_DIR_VAR_1}\``:"one of the team directories listed above"}, bearing in mind it is shared with teammates.
