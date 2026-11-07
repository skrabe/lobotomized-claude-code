<!--
name: 'Tool Result: MCP connector raw call refused (conversation unreadable)'
description: >-
  Refuses a raw connector call when the conversation could not be read and
  blames Claude Code or its host if it persists
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_CONVERSATION_UNREAD_VAR_0
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_CONVERSATION_UNREAD_VAR_0} was not called: Claude Code could not read this conversation, so it could not tell whether this call would send a path as plain text. Calling again may or may not work. If it keeps happening, the fault is in Claude Code or in the program that runs it.
