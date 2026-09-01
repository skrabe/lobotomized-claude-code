<!--
name: Agent stopped by user (resume)
description: >-
  Resume tool-error returned to the model that the agent was user-stopped and
  must be treated as cancelled.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_AGENT_STOPPED_BY_USER_VAR_0
-->
Agent ${TOOL_RESULT_AGENT_STOPPED_BY_USER_VAR_0} was stopped by the user and won't be resumed. Treat its work as cancelled; only launch a new agent if the user explicitly asks.
