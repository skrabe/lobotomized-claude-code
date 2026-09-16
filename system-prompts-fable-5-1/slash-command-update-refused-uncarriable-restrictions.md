<!--
name: 'Slash command: Update refused uncarriable restrictions'
description: >-
  Refuses an in-session version switch because the session carries restrictions
  a restart cannot preserve
ccVersion: 2.1.273
variables:
  - SLASH_COMMAND_UPDATE_REFUSED_UNCARRIABLE_RESTRICTIONS_VAR_0
  - SLASH_COMMAND_UPDATE_REFUSED_UNCARRIABLE_RESTRICTIONS_VAR_1
-->
Can't switch to the new version from inside this session — it has restrictions a restart can't carry over (${SLASH_COMMAND_UPDATE_REFUSED_UNCARRIABLE_RESTRICTIONS_VAR_0.join("; ")}). Nothing was changed; exit and start claude again for the new version${SLASH_COMMAND_UPDATE_REFUSED_UNCARRIABLE_RESTRICTIONS_VAR_1}.
