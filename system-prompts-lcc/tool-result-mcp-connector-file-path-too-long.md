<!--
name: 'Tool Result: MCP connector file path too long for approval prompt'
description: >-
  Refuses a file whose path cannot be shown whole in the approval prompt and
  suggests widening or a shorter copy
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_3
  - TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_4
  - TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_5
  - TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_6
  - TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_7
  - TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_8
-->
Cannot send ${TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_0(TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_1(TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_2.path))}: the file's full path, or the path it lies at, is too long for Claude Code to show whole in its approval prompt, whose list of files has ${TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_3} lines${TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_4([TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_2])?`; one of those two paths has characters that may imitate others, so a line that says so takes one of the ${TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_3}`:""}. ${TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_5([TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_2],TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_6)?`The path would fit in a conversation at least ${TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_7} columns wide, so the user can widen the window, or close a side panel if one is open. `:""}A copy at a shorter path in the folder Claude Code started in can be sent. ${TOOL_RESULT_MCP_CONNECTOR_FILE_PATH_TOO_LONG_VAR_8}
