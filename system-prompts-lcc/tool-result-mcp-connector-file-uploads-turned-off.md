<!--
name: 'Tool Result: MCP connector file sending turned off'
description: >-
  Refuses a file call because connector file sending was turned off during the
  session
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_UPLOADS_TURNED_OFF_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_UPLOADS_TURNED_OFF_VAR_1
-->
No file was sent: sending files to connectors was turned off during this session. ${TOOL_RESULT_MCP_CONNECTOR_FILE_UPLOADS_TURNED_OFF_VAR_0(TOOL_RESULT_MCP_CONNECTOR_FILE_UPLOADS_TURNED_OFF_VAR_1)} Tell the user, and do not retry with a file. Calls that name no file still work.
