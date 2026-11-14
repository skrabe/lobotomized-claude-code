<!--
name: 'Tool Result: MCP connector file restricted folders only'
description: >-
  Under --restricted or deny/ask rules only files in the start folder and added
  folders can be sent; suggests /add-dir
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_RESTRICTED_FOLDERS_ONLY_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_RESTRICTED_FOLDERS_ONLY_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_RESTRICTED_FOLDERS_ONLY_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_FILE_RESTRICTED_FOLDERS_ONLY_VAR_3
  - TOOL_RESULT_MCP_CONNECTOR_FILE_RESTRICTED_FOLDERS_ONLY_VAR_4
-->
${TOOL_RESULT_MCP_CONNECTOR_FILE_RESTRICTED_FOLDERS_ONLY_VAR_0}: ${TOOL_RESULT_MCP_CONNECTOR_FILE_RESTRICTED_FOLDERS_ONLY_VAR_1.restricted?"under --restricted":`where this session has ${TOOL_RESULT_MCP_CONNECTOR_FILE_RESTRICTED_FOLDERS_ONLY_VAR_2} deny or ask rules`}, only files in the folder Claude Code started in and in folders added for this session can be sent. The user can add a folder with /add-dir ("Yes, for this session") or start Claude Code there.${TOOL_RESULT_MCP_CONNECTOR_FILE_RESTRICTED_FOLDERS_ONLY_VAR_3} ${TOOL_RESULT_MCP_CONNECTOR_FILE_RESTRICTED_FOLDERS_ONLY_VAR_4}
