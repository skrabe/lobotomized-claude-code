<!--
name: 'Tool result: MCP connector upload storage not connected'
description: >-
  Connector upload error: the upload service could not complete a connection to
  the connector's storage; nothing sent.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_NOT_CONNECTED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_NOT_CONNECTED_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_NOT_CONNECTED_VAR_2
-->
Claude's upload service began to connect to the connector's storage to send ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_NOT_CONNECTED_VAR_0} there, but could not complete the connection. The service says it sent none of the file on. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_NOT_CONNECTED_VAR_1}${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_STORAGE_NOT_CONNECTED_VAR_2} If this keeps happening, the connector's storage may not be set up to receive files from Claude yet. The connector's maker can look into that.
