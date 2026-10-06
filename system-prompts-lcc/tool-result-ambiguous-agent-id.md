<!--
name: 'Tool result: ambiguous agent id'
description: >-
  Error when a name matches both a teammate and a background agent, asking for
  the full address or task ID.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_0
  - TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_1
  - TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_2
  - TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_3
  - TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_4
-->
"${TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_0(TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_1)}" matches both teammate ${TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_2.map((TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_3)=>TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_0(TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_3)).join(", ")} and background agent ${TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_0(TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_4)}. Use the full address (name@team) for the teammate or the task ID for the background agent.
