<!--
name: 'Tool Result: Agent resume id from other process'
description: >-
  Resume-agent tool_result when the id was never in this session (e.g. a lead's
  subagent seen from a teammate pane) and must be addressed via SendMessage
  instead.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_AGENT_RESUME_ID_FROM_OTHER_PROCESS_VAR_0
  - TOOL_RESULT_AGENT_RESUME_ID_FROM_OTHER_PROCESS_VAR_1
  - TOOL_RESULT_AGENT_RESUME_ID_FROM_OTHER_PROCESS_VAR_2
  - TOOL_RESULT_AGENT_RESUME_ID_FROM_OTHER_PROCESS_VAR_3
-->
Agent "${TOOL_RESULT_AGENT_RESUME_ID_FROM_OTHER_PROCESS_VAR_0.agentName}" could not be resumed: ${TOOL_RESULT_AGENT_RESUME_ID_FROM_OTHER_PROCESS_VAR_1(TOOL_RESULT_AGENT_RESUME_ID_FROM_OTHER_PROCESS_VAR_2)}. If you read this id in a message from another Claude Code process (e.g. the lead's subagent, seen from a teammate pane), it never ran in this session — reply through "${TOOL_RESULT_AGENT_RESUME_ID_FROM_OTHER_PROCESS_VAR_3}" or the session that sent it instead of the raw id.
