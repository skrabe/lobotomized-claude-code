<!--
name: 'Tool Result: Auto mode unavailable agent stopped'
description: >-
  Message when auto mode's safety check is unavailable so a subagent was stopped
  before finishing, telling the model its result is partial and to finish
  without it and tell the user.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_AUTO_MODE_UNAVAILABLE_AGENT_STOPPED_VAR_0
  - TOOL_RESULT_AUTO_MODE_UNAVAILABLE_AGENT_STOPPED_VAR_1
-->
Auto mode is unavailable: ${TOOL_RESULT_AUTO_MODE_UNAVAILABLE_AGENT_STOPPED_VAR_0(TOOL_RESULT_AUTO_MODE_UNAVAILABLE_AGENT_STOPPED_VAR_1)}, so this agent was stopped before it finished. Nobody interrupted it; whatever it returned is partial. Starting it again ${TOOL_RESULT_AUTO_MODE_UNAVAILABLE_AGENT_STOPPED_VAR_1==="no_classifier_for_session"?"will":"may"} stop the same way. Finish what you can without it, then tell the user what is blocked.
