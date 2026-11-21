<!--
name: 'Tool result: agent not resumed, not main conversation'
description: >-
  Refusal: a user-stopped agent can be resumed only by Claude's message from the
  main conversation.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_AGENT_NOT_RESUMED_NOT_MAIN_CONVERSATION_VAR_0
-->
Agent ${TOOL_RESULT_AGENT_NOT_RESUMED_NOT_MAIN_CONVERSATION_VAR_0} ended when the user pressed Stop, and was not resumed. Only Claude's own message from the main conversation can resume it. Its work stays undone unless the sender does it or the main conversation resumes the agent.
