<!--
name: 'Tool Result: MCP connector file under credential name'
description: >-
  Refuses a file whose name or folder is where credentials are kept and says to
  tell the user
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_CREDENTIAL_NAME_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_CREDENTIAL_NAME_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_CREDENTIAL_NAME_VAR_2
-->
Cannot send ${TOOL_RESULT_MCP_CONNECTOR_FILE_CREDENTIAL_NAME_VAR_0}: its name or folder is one that credentials are kept under, so it is not sent to a connector on Claude's word alone. Tell the user it was not sent${TOOL_RESULT_MCP_CONNECTOR_FILE_CREDENTIAL_NAME_VAR_1?"; if they want it sent, they can attach it to the chat themselves":""}. ${TOOL_RESULT_MCP_CONNECTOR_FILE_CREDENTIAL_NAME_VAR_2}
