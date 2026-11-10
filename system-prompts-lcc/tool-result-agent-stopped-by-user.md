<!--
name: 'Tool Result: Agent stopped by user'
description: >-
  Tells the model a stopped agent won't be resumed and to treat its work as
  cancelled
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_AGENT_STOPPED_BY_USER_VAR_0
-->
Agent ${TOOL_RESULT_AGENT_STOPPED_BY_USER_VAR_0} was stopped and won't be resumed. Treat its work as cancelled; only launch a new agent if the user explicitly asks.
