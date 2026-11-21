<!--
name: 'Tool Result: REPL spawnContext refused'
description: Error when spawnContext is refused or the Agent tool returns no agent id
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_REPL_SPAWN_CONTEXT_REFUSED_VAR_0
  - TOOL_RESULT_REPL_SPAWN_CONTEXT_REFUSED_VAR_1
-->
spawnContext '${TOOL_RESULT_REPL_SPAWN_CONTEXT_REFUSED_VAR_0}' refused — ${TOOL_RESULT_REPL_SPAWN_CONTEXT_REFUSED_VAR_1??"the Agent tool returned no agent id"}
