<!--
name: 'System reminder: steward loader entry watch over'
description: >-
  A file has a loader entry that could load foreign code; the watch is over:
  stop gh/git, arm no wake-up, tell the user to rerun /steward
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_STEWARD_LOADER_ENTRY_WATCH_OVER_VAR_0
-->
${SYSTEM_REMINDER_STEWARD_LOADER_ENTRY_WATCH_OVER_VAR_0} has an entry that could load somebody else's code or files, and no watch runs with it in this session. The watch is over: run no more gh or git, arm no wake-up, and tell the user that /steward, typed again, says which entry and what to do
