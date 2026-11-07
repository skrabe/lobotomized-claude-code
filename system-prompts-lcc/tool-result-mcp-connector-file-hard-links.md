<!--
name: 'Tool Result: MCP connector file has hard links'
description: Refuses a file with more than one hard link
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_HARD_LINKS_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_HARD_LINKS_VAR_1
-->
Cannot send ${TOOL_RESULT_MCP_CONNECTOR_FILE_HARD_LINKS_VAR_0}: the file has more than one hard link, which can point at a file outside the folders this session may read. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_FILE_HARD_LINKS_VAR_1}
