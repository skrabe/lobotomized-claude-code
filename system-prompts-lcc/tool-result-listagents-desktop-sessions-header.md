<!--
name: 'Tool result: ListAgents Claude Desktop sessions header'
description: Header for Claude Desktop sessions explaining the bracketed ids.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_LISTAGENTS_DESKTOP_SESSIONS_HEADER_VAR_0
  - TOOL_RESULT_LISTAGENTS_DESKTOP_SESSIONS_HEADER_VAR_1
  - TOOL_RESULT_LISTAGENTS_DESKTOP_SESSIONS_HEADER_VAR_2
  - TOOL_RESULT_LISTAGENTS_DESKTOP_SESSIONS_HEADER_VAR_3
-->
The brackets after each name below hold that session's id.${TOOL_RESULT_LISTAGENTS_DESKTOP_SESSIONS_HEADER_VAR_0?` To message a Claude Desktop session, give ${TOOL_RESULT_LISTAGENTS_DESKTOP_SESSIONS_HEADER_VAR_1} its name and brackets as printed: the name alone can belong to another session. A message wakes a stopped session.`:""}${TOOL_RESULT_LISTAGENTS_DESKTOP_SESSIONS_HEADER_VAR_2.some((TOOL_RESULT_LISTAGENTS_DESKTOP_SESSIONS_HEADER_VAR_3)=>TOOL_RESULT_LISTAGENTS_DESKTOP_SESSIONS_HEADER_VAR_3.cloud)?" A cloud session below may still be running, and its work cannot be seen from here, so do not redo it unless the user asks.":""}
