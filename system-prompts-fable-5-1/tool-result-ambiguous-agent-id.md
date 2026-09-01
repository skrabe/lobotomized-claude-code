<!--
name: Ambiguous agent ID
description: >-
  Tool error returned to the model when an agent reference matches both a
  teammate and a background agent.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_0
  - TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_1
  - TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_2
-->
"${TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_0(TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_1)}" matches both teammate ${TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_2.map((TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_3)=>TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_0(TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_3)).join(", ")} and background agent ${TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_0(TOOL_RESULT_AMBIGUOUS_AGENT_ID_VAR_4)}. Use the full agent ID (name@team) for the teammate or the task ID for the background agent.
