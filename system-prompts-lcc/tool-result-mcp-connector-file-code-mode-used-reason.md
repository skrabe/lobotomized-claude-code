<!--
name: 'Tool Result: MCP connector file refused after code mode'
description: >-
  Reason fragment saying files are not sent once a mode has been on since
  startup and the user must restart with it off
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_CODE_MODE_USED_REASON_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_CODE_MODE_USED_REASON_VAR_1
-->
Claude Code does not send a file to a connector once ${TOOL_RESULT_MCP_CONNECTOR_FILE_CODE_MODE_USED_REASON_VAR_0} has been on since Claude Code was started, as it has been here. To send a file, the user would at least have to quit Claude Code and start it again with ${TOOL_RESULT_MCP_CONNECTOR_FILE_CODE_MODE_USED_REASON_VAR_1} off
