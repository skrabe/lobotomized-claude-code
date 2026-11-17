<!--
name: 'Tool Result: $.agent.call tool not loaded in agent'
description: >-
  Error when a $.agent.call names a tool the target agent has not loaded, with
  how that agent's model loads it
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_AGENT_CALL_TOOL_NOT_LOADED_VAR_0
  - TOOL_RESULT_AGENT_CALL_TOOL_NOT_LOADED_VAR_1
-->
${TOOL_RESULT_AGENT_CALL_TOOL_NOT_LOADED_VAR_0} did not run: the agent it was called as has not loaded it. That agent's model loads it with ${TOOL_RESULT_AGENT_CALL_TOOL_NOT_LOADED_VAR_1} (query "select:${TOOL_RESULT_AGENT_CALL_TOOL_NOT_LOADED_VAR_0}"). A $.agent.call made from that model's next reply on can run it; a script already running must be started again.
