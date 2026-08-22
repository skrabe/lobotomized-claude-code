<!--
name: ListAgents Self - Main Session Token
description: >-
  ListAgents tool result line naming this process's main session token for other
  sessions, shown when the caller is a subagent.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_LISTAGENTS_SELF_MAIN_SESSION_TOKEN_VAR_0
  - TOOL_RESULT_LISTAGENTS_SELF_MAIN_SESSION_TOKEN_VAR_1
-->
This process's main session is ${TOOL_RESULT_LISTAGENTS_SELF_MAIN_SESSION_TOKEN_VAR_0.token} — the name OTHER sessions use to message it (it is not listed below; from inside this process, address the main conversation as "${TOOL_RESULT_LISTAGENTS_SELF_MAIN_SESSION_TOKEN_VAR_1}").
