<!--
name: 'System Prompt: Agent Memory Entrypoint Not Loaded (Read-Only)'
description: >-
  Agent-memory section line when the memory entrypoint file was refused (a link,
  special file, or outside the working copy): treat this agent memory as
  read-only and do not write files in its folder.
ccVersion: 2.1.277
variables:
  - SYSTEM_PROMPT_AGENT_MEMORY_ENTRYPOINT_NOT_LOADED_READ_ONLY_VAR_0
-->
Your ${SYSTEM_PROMPT_AGENT_MEMORY_ENTRYPOINT_NOT_LOADED_READ_ONLY_VAR_0} was not loaded: it or its folder is a link or a special file, or could not be verified to be inside this working copy. Treat this agent memory as read-only in this session: do not create or write ${SYSTEM_PROMPT_AGENT_MEMORY_ENTRYPOINT_NOT_LOADED_READ_ONLY_VAR_0} or other files in its folder.
