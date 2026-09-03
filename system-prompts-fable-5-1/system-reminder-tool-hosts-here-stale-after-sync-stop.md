<!--
name: Tool Hosts Here Stale After Sync Stop
description: >-
  Here-machine bullet when file sync stopped but the directory could not be
  emptied, so the copy is stale and must not be read, run, or edited.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HERE_STALE_AFTER_SYNC_STOP_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HERE_STALE_AFTER_SYNC_STOP_VAR_1
-->
- ${SYSTEM_REMINDER_TOOL_HOSTS_HERE_STALE_AFTER_SYNC_STOP_VAR_0()}: ${SYSTEM_REMINDER_TOOL_HOSTS_HERE_STALE_AFTER_SYNC_STOP_VAR_1} — STALE since file sync stopped for this session (it could not be emptied): do not read, run or edit the project there; only scratch work that needs none of the project's files belongs here.
