<!--
name: 'System Prompt: Memory Directories (Private and Shared)'
description: >-
  Directory clause interpolated into the '# Memory' system prompt built by
  WUc(), describing the private auto-dir and the shared team mount(s) the model
  may write memories to.
ccVersion: 2.1.214
variables:
  - SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_0
  - SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_1
  - SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_2
  - SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_3
  - SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_4
-->
at \`${SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_0}\` (private to this user) and ${SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_1.join(" and ")} (shared with all users of this project). ${SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_2?SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_3?"These directories already exist — write to them directly with the Write tool (do not run mkdir or check for their existence).":SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_4:`Write only to \`${SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_0}\` — it already exists; write to it directly with the Write tool (do not run mkdir or check for its existence). The shared director${SYSTEM_PROMPT_MEMORY_DIRS_PRIVATE_AND_SHARED_INTRO_VAR_1.length>1?"ies are":"y is"} read-only and changes there would not persist.`}
