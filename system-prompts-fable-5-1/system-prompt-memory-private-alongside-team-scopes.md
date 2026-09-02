<!--
name: 'System Prompt: Personal directory alongside shared stores'
description: 'Reworded successor of the 2.1.221 id: split-destination guidance — private types to the personal directory, team-scoped memories to the writable shared store.'
ccVersion: 2.1.224
variables:
  - SYSTEM_PROMPT_MEMORY_PRIVATE_ALONGSIDE_TEAM_SCOPES_VAR_0
  - SYSTEM_PROMPT_MEMORY_PRIVATE_ALONGSIDE_TEAM_SCOPES_VAR_1
-->
Your personal memory directory at \`${SYSTEM_PROMPT_MEMORY_PRIVATE_ALONGSIDE_TEAM_SCOPES_VAR_0}\` is written with the file tools: save \`user\`-type memories (and anything else private) there, and team-scoped memories to the writable store \`${SYSTEM_PROMPT_MEMORY_PRIVATE_ALONGSIDE_TEAM_SCOPES_VAR_1.id}\`, which teammates can read.
