<!--
name: '/pause-memory: memory paused for this session'
description: >-
  Result text shown when memory is toggled off for the session, stating that
  memory will not be read or written and previously-loaded content should not be
  referenced, with a hint to run /pause-memory again to resume.
ccVersion: 2.1.285
variables:
  - SLASH_COMMAND_PAUSE_MEMORY_PAUSED_THIS_SESSION_VAR_0
-->
Memory paused for this session · this conversation will not write or read new memories, and previously-loaded memory content should not be referenced.${""}

${SLASH_COMMAND_PAUSE_MEMORY_PAUSED_THIS_SESSION_VAR_0()}
