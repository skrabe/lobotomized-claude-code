<!--
name: 'System Prompt: Team-Only Memory Write Location'
description: >-
  Memory-directory location clause for a team-only session (no private dir): the
  team dirs shared with all project users, and whether to write directly or that
  team memory is read-only.
ccVersion: 2.1.218
variables:
  - SYSTEM_PROMPT_MEMORY_TEAM_ONLY_WRITE_LOCATION_VAR_0
  - SYSTEM_PROMPT_MEMORY_TEAM_ONLY_WRITE_LOCATION_VAR_1
  - SYSTEM_PROMPT_MEMORY_TEAM_ONLY_WRITE_LOCATION_VAR_2
-->
at ${SYSTEM_PROMPT_MEMORY_TEAM_ONLY_WRITE_LOCATION_VAR_0.join(" and ")} (shared with all users of this project). ${SYSTEM_PROMPT_MEMORY_TEAM_ONLY_WRITE_LOCATION_VAR_1?SYSTEM_PROMPT_MEMORY_TEAM_ONLY_WRITE_LOCATION_VAR_0.length>1?"These directories already exist — write to them directly with the Write tool (do not run mkdir or check for their existence).":SYSTEM_PROMPT_MEMORY_TEAM_ONLY_WRITE_LOCATION_VAR_2:"Team memory is read-only this session — you cannot persist new memories."}
