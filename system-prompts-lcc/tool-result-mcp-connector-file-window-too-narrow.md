<!--
name: 'Tool Result: MCP connector file window too narrow'
description: >-
  Refuses a file call because the conversation is too narrow to list the files
  in the approval prompt and asks the user to widen it
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_WINDOW_TOO_NARROW_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_WINDOW_TOO_NARROW_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_WINDOW_TOO_NARROW_VAR_2
-->
No file was sent: to list the files this call would send, Claude Code's approval prompt needs the conversation to be at least ${TOOL_RESULT_MCP_CONNECTOR_FILE_WINDOW_TOO_NARROW_VAR_0} columns wide, and it is ${TOOL_RESULT_MCP_CONNECTOR_FILE_WINDOW_TOO_NARROW_VAR_1}. Ask the user to widen the window, or to close a side panel if one is open, then make this call again. ${TOOL_RESULT_MCP_CONNECTOR_FILE_WINDOW_TOO_NARROW_VAR_2}
