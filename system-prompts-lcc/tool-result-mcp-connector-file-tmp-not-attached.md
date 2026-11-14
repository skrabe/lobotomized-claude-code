<!--
name: 'Tool Result: MCP connector file /tmp not attached'
description: >-
  Refuses attaching a file under /tmp and tells Claude to copy it into the given
  folder and call again
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TMP_NOT_ATTACHED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TMP_NOT_ATTACHED_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TMP_NOT_ATTACHED_VAR_2
-->
Cannot attach "${TOOL_RESULT_MCP_CONNECTOR_FILE_TMP_NOT_ATTACHED_VAR_0}": files under /tmp are not attached. If you made this file, copy it into ${TOOL_RESULT_MCP_CONNECTOR_FILE_TMP_NOT_ATTACHED_VAR_1} and make the call again with the copy's path. ${TOOL_RESULT_MCP_CONNECTOR_FILE_TMP_NOT_ATTACHED_VAR_2}
