<!--
name: 'Send to Project: MCP tool calls by server intro'
description: >-
  Intro line of the MCP tool-calls section in the /send-to-project folder facts,
  saying what was counted and explaining connectors versus local servers.
ccVersion: 2.1.314
variables:
  - DATA_SEND_TO_PROJECT_MCP_TOOL_CALLS_HEADER_VAR_0
  - DATA_SEND_TO_PROJECT_MCP_TOOL_CALLS_HEADER_VAR_1
-->
MCP tool calls by server, counted in ${[DATA_SEND_TO_PROJECT_MCP_TOOL_CALLS_HEADER_VAR_0.sessionsScanned>0?`the ${DATA_SEND_TO_PROJECT_MCP_TOOL_CALLS_HEADER_VAR_0.sessionsScanned===1?"most recent session transcript":`${DATA_SEND_TO_PROJECT_MCP_TOOL_CALLS_HEADER_VAR_0.sessionsScanned} most recent session transcripts`} (read whole, not just the condensed text below)`:null,DATA_SEND_TO_PROJECT_MCP_TOOL_CALLS_HEADER_VAR_0.includesCurrentConversation?"the conversation above":null].filter((DATA_SEND_TO_PROJECT_MCP_TOOL_CALLS_HEADER_VAR_1)=>DATA_SEND_TO_PROJECT_MCP_TOOL_CALLS_HEADER_VAR_1!==null).join(" and ")}. A claude.ai connector lives in the cloud; a local server is configured on this computer only and does not carry over to the project.
