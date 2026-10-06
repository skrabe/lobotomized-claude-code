<!--
name: 'Agent resume refused: agent still stopping'
description: >-
  Resume error returned to the model when the target agent's previous run was
  stopped but has not exited, telling it to re-run TaskStop or wait.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_AGENT_STILL_STOPPING_VAR_0
  - TOOL_RESULT_AGENT_STILL_STOPPING_VAR_1
-->
Agent ${TOOL_RESULT_AGENT_STILL_STOPPING_VAR_0} is still stopping — its previous run was stopped but has not exited. Re-run ${TOOL_RESULT_AGENT_STILL_STOPPING_VAR_1} on it or wait for it to exit before resuming.
