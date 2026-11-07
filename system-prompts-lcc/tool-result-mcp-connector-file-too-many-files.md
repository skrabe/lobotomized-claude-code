<!--
name: 'Tool Result: MCP connector too many files for approval prompt'
description: >-
  Refuses a call naming more files than fit in the approval prompt's file list
  and asks to split them across calls
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_3
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_4
-->
No file was sent: this call names ${TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_0} files, and Claude Code sends only files whose full paths fit whole in the ${TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_1}-line list of files of its approval prompt (a long path takes several lines${TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_2?`, and one of these files' paths has characters that may imitate others, so a line that says so takes one of the ${TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_1}`:""}). Send the files in several calls with fewer files each. ${TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_3(TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_FILES_VAR_4)}
