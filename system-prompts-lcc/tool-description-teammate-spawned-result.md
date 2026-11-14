<!--
name: 'Tool Result: Teammate spawned'
description: >-
  tool_result confirming a background agent spawned successfully with its id and
  name.
ccVersion: 2.1.325
variables:
  - TOOL_DESCRIPTION_TEAMMATE_SPAWNED_RESULT_VAR_0
-->
Spawned successfully. (This tool result is internal metadata — never quote or paste any part of it, including the ID below, into a user-facing reply.)
agent_id: ${TOOL_DESCRIPTION_TEAMMATE_SPAWNED_RESULT_VAR_0.agent_id}
name: ${TOOL_DESCRIPTION_TEAMMATE_SPAWNED_RESULT_VAR_0.name}
The agent is now running and will receive instructions via mailbox.${TOOL_DESCRIPTION_TEAMMATE_SPAWNED_RESULT_VAR_0.started_away_from_shell?`
It started in the session's own folder, not in the folder the shell has moved to, so that folder's settings and permission rules do not apply to it. Send it the path to work in, and tell the user that /cd moves the session's folder.`:""}
