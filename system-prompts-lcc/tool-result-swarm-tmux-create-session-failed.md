<!--
name: 'Tool result: swarm tmux session creation failed'
description: Error when tmux fails to create the external swarm session.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_SWARM_TMUX_CREATE_SESSION_FAILED_VAR_0
-->
Failed to create swarm session: ${TOOL_RESULT_SWARM_TMUX_CREATE_SESSION_FAILED_VAR_0.stderr||"Unknown error"}
