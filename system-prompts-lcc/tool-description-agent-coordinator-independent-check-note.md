<!--
name: 'Agent tool (coordinator): give the problem, not your conclusion'
description: >-
  Agent tool prompt variant for coordinator mode (f$e gate) that appends a
  warning that an agent handed your hypothesis tends to confirm it.
ccVersion: 2.1.328
variables:
  - TOOL_DESCRIPTION_AGENT_COORDINATOR_INDEPENDENT_CHECK_NOTE_VAR_0
  - TOOL_DESCRIPTION_AGENT_COORDINATOR_INDEPENDENT_CHECK_NOTE_VAR_1
-->
${TOOL_DESCRIPTION_AGENT_COORDINATOR_INDEPENDENT_CHECK_NOTE_VAR_0}${TOOL_DESCRIPTION_AGENT_COORDINATOR_INDEPENDENT_CHECK_NOTE_VAR_1}

An agent handed your hypothesis tends to return it confirmed. For an independent check, give it the problem, not your conclusion.
