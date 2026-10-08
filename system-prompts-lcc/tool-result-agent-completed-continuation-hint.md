<!--
name: Completed Agent Continuation Hint
description: >-
  Adds the SendMessage target and summary format for continuing a completed
  agent.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_AGENT_COMPLETED_CONTINUATION_HINT_VAR_0
  - TOOL_RESULT_AGENT_COMPLETED_CONTINUATION_HINT_VAR_1
-->
 (use ${TOOL_RESULT_AGENT_COMPLETED_CONTINUATION_HINT_VAR_0} with to: '${TOOL_RESULT_AGENT_COMPLETED_CONTINUATION_HINT_VAR_1.agentId}', summary: '<5-10 word recap>' to continue this agent)
